"""Tests for tools/literature.py — literature search and download."""
import json
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from literature import (
    search_arxiv,
    search_scholar,
    fetch_arxiv_pdf,
    fetch_doi,
    list_papers,
)

SAMPLE_ARXIV_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2310.15138v1</id>
    <title>De novo protein design with RFdiffusion</title>
    <summary>We describe RFdiffusion, a method for de novo protein design.</summary>
    <published>2023-10-23T00:00:00Z</published>
    <author><name>Watson JL</name></author>
    <author><name>Juergens D</name></author>
    <link title="pdf" href="https://arxiv.org/pdf/2310.15138v1" rel="related" type="application/pdf"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2411.00123v1</id>
    <title>All-atom protein generation</title>
    <summary>A newer method for all-atom generation.</summary>
    <published>2024-11-01T00:00:00Z</published>
    <author><name>Smith A</name></author>
    <link title="pdf" href="https://arxiv.org/pdf/2411.00123v1" rel="related" type="application/pdf"/>
  </entry>
</feed>"""

SAMPLE_S2_JSON = json.dumps({
    "data": [
        {
            "title": "RFdiffusion paper",
            "authors": [{"name": "Watson JL"}, {"name": "Juergens D"}],
            "year": 2023,
            "abstract": "A method for de novo protein design using diffusion.",
            "externalIds": {"ArXiv": "2310.15138", "DOI": "10.1038/s41586-023-06415-8"},
            "url": "https://www.semanticscholar.org/paper/abc123",
        }
    ]
})


class TestSearchArxiv:
    def test_parses_results(self):
        mock_resp = MagicMock()
        mock_resp.read.return_value = SAMPLE_ARXIV_XML.encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            results = search_arxiv("protein design", max_results=10)
        assert len(results) == 2
        assert results[0]["arxiv_id"] == "2310.15138v1"
        assert "RFdiffusion" in results[0]["title"]
        assert results[0]["pdf_url"] is not None

    def test_returns_empty_on_error(self):
        with patch("literature.urllib.request.urlopen", side_effect=Exception("network")):
            results = search_arxiv("test query")
        assert results == []

    def test_extracts_authors(self):
        mock_resp = MagicMock()
        mock_resp.read.return_value = SAMPLE_ARXIV_XML.encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            results = search_arxiv("test")
        assert "Watson JL" in results[0]["authors"]

    def test_extracts_date(self):
        mock_resp = MagicMock()
        mock_resp.read.return_value = SAMPLE_ARXIV_XML.encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            results = search_arxiv("test")
        assert results[0]["published"] == "2023-10-23"


class TestSearchScholar:
    def test_parses_results(self):
        mock_resp = MagicMock()
        mock_resp.read.return_value = SAMPLE_S2_JSON.encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            results = search_scholar("RFdiffusion")
        assert len(results) == 1
        assert results[0]["arxiv_id"] == "2310.15138"
        assert results[0]["doi"] == "10.1038/s41586-023-06415-8"

    def test_returns_empty_on_error(self):
        with patch("literature.urllib.request.urlopen", side_effect=Exception("rate limit")):
            results = search_scholar("test")
        assert results == []


class TestFetchArxiv:
    def test_downloads_pdf(self, tmp_path):
        mock_resp = MagicMock()
        mock_resp.read.return_value = b"%PDF-1.4 fake content"
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            path = fetch_arxiv_pdf("2310.15138", out_dir=tmp_path)
        assert path is not None
        assert path.exists()
        assert path.suffix == ".pdf"
        assert path.read_bytes() == b"%PDF-1.4 fake content"

    def test_skips_existing(self, tmp_path):
        existing = tmp_path / "2310.15138.pdf"
        existing.write_text("already here")
        path = fetch_arxiv_pdf("2310.15138", out_dir=tmp_path)
        assert path == existing

    def test_returns_none_on_error(self, tmp_path):
        with patch("literature.urllib.request.urlopen", side_effect=Exception("404")):
            path = fetch_arxiv_pdf("9999.99999", out_dir=tmp_path)
        assert path is None

    def test_cleans_arxiv_id(self, tmp_path):
        mock_resp = MagicMock()
        mock_resp.read.return_value = b"%PDF"
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            path = fetch_arxiv_pdf("arXiv:2310.15138", out_dir=tmp_path)
        assert path is not None
        assert "arXiv" not in path.name


class TestFetchDoi:
    def test_downloads_open_access(self, tmp_path):
        unpaywall_resp = MagicMock()
        unpaywall_resp.read.return_value = json.dumps({
            "best_oa_location": {"url_for_pdf": "https://example.com/paper.pdf"}
        }).encode()
        unpaywall_resp.__enter__ = lambda s: s
        unpaywall_resp.__exit__ = MagicMock(return_value=False)
        pdf_resp = MagicMock()
        pdf_resp.read.return_value = b"%PDF-1.4 content"
        pdf_resp.__enter__ = lambda s: s
        pdf_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", side_effect=[unpaywall_resp, pdf_resp]):
            path = fetch_doi("10.1038/s41586-023-06415-8", out_dir=tmp_path)
        assert path is not None
        assert path.exists()

    def test_returns_none_when_no_oa(self, tmp_path):
        mock_resp = MagicMock()
        mock_resp.read.return_value = json.dumps({"best_oa_location": None}).encode()
        mock_resp.__enter__ = lambda s: s
        mock_resp.__exit__ = MagicMock(return_value=False)
        with patch("literature.urllib.request.urlopen", return_value=mock_resp):
            path = fetch_doi("10.xxxx/closed-access", out_dir=tmp_path)
        assert path is None


class TestListPapers:
    def test_lists_pdfs(self, tmp_path, capsys):
        (tmp_path / "paper1.pdf").write_bytes(b"x" * 1024)
        (tmp_path / "paper2.pdf").write_bytes(b"x" * 2048)
        with patch("literature.RAW_DIR", tmp_path):
            list_papers()
        out = capsys.readouterr().out
        assert "paper1.pdf" in out
        assert "paper2.pdf" in out
