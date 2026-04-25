#!/usr/bin/env python3
"""Literature search and download tools for AutoLab.

Usage:
    # Search arXiv
    python tools/literature.py search "protein diffusion design"

    # Search with filters
    python tools/literature.py search "MPNN sequence design" --max-results 5 --sort relevance

    # Download a paper by arXiv ID
    python tools/literature.py fetch 2310.15138

    # Download by DOI
    python tools/literature.py fetch-doi 10.1038/s41586-023-06415-8

    # Search and download top result
    python tools/literature.py search "RFdiffusion all-atom" --download

    # Search Semantic Scholar
    python tools/literature.py scholar "protein binder design RFdiffusion"

    # List downloaded papers
    python tools/literature.py list
"""
import argparse
import json
import re
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

RAW_DIR = Path("raw/papers")
RAW_DIR.mkdir(parents=True, exist_ok=True)

ARXIV_API = "http://export.arxiv.org/api/query"
S2_API = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_arxiv(query, max_results=10, sort_by="relevance"):
    """Search arXiv and return list of papers."""
    sort_map = {"relevance": "relevance", "date": "submittedDate", "updated": "lastUpdatedDate"}
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_map.get(sort_by, "relevance"),
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            data = resp.read()
    except Exception as e:
        print(f"Error searching arXiv: {e}", file=sys.stderr)
        return []

    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(data)
    papers = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")[:200]
        arxiv_id = entry.find("atom:id", ns).text.strip().split("/abs/")[-1]
        published = entry.find("atom:published", ns).text[:10]
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]
        pdf_link = None
        for link in entry.findall("atom:link", ns):
            if link.get("title") == "pdf":
                pdf_link = link.get("href")
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors[:3],
            "published": published,
            "summary": summary,
            "pdf_url": pdf_link,
        })
    return papers


def search_scholar(query, max_results=10):
    """Search Semantic Scholar and return list of papers."""
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,year,abstract,externalIds,url",
    }
    url = f"{S2_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "AutoLab/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(f"Error searching Semantic Scholar: {e}", file=sys.stderr)
        return []

    papers = []
    for p in data.get("data", []):
        arxiv_id = (p.get("externalIds") or {}).get("ArXiv", "")
        doi = (p.get("externalIds") or {}).get("DOI", "")
        papers.append({
            "title": p.get("title", ""),
            "authors": [a["name"] for a in (p.get("authors") or [])[:3]],
            "year": p.get("year"),
            "abstract": (p.get("abstract") or "")[:200],
            "arxiv_id": arxiv_id,
            "doi": doi,
            "url": p.get("url", ""),
        })
    return papers


def fetch_arxiv_pdf(arxiv_id, out_dir=None):
    """Download PDF from arXiv by ID."""
    out_dir = Path(out_dir or RAW_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    clean_id = arxiv_id.replace("arxiv:", "").replace("arXiv:", "").strip()
    pdf_url = f"https://arxiv.org/pdf/{clean_id}.pdf"
    slug = re.sub(r"[^\w.-]", "_", clean_id)
    out_path = out_dir / f"{slug}.pdf"
    if out_path.exists():
        print(f"Already downloaded: {out_path}")
        return out_path
    print(f"Downloading {pdf_url} ...")
    try:
        req = urllib.request.Request(pdf_url, headers={"User-Agent": "AutoLab/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            out_path.write_bytes(resp.read())
        print(f"Saved: {out_path}")
        return out_path
    except Exception as e:
        print(f"Error downloading: {e}", file=sys.stderr)
        return None


def fetch_doi(doi, out_dir=None):
    """Try to fetch open-access PDF via DOI using Unpaywall."""
    out_dir = Path(out_dir or RAW_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    unpaywall_url = f"https://api.unpaywall.org/v2/{doi}?email=autolab@example.com"
    try:
        req = urllib.request.Request(unpaywall_url, headers={"User-Agent": "AutoLab/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        oa = data.get("best_oa_location") or {}
        pdf_url = oa.get("url_for_pdf") or oa.get("url")
        if not pdf_url:
            print(f"No open-access PDF found for DOI {doi}")
            return None
        slug = re.sub(r"[^\w.-]", "_", doi)
        out_path = out_dir / f"{slug}.pdf"
        if out_path.exists():
            print(f"Already downloaded: {out_path}")
            return out_path
        print(f"Downloading {pdf_url} ...")
        req2 = urllib.request.Request(pdf_url, headers={"User-Agent": "AutoLab/1.0"})
        with urllib.request.urlopen(req2, timeout=60) as resp:
            out_path.write_bytes(resp.read())
        print(f"Saved: {out_path}")
        return out_path
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None


def list_papers():
    """List all downloaded papers."""
    for f in sorted(RAW_DIR.glob("*.pdf")):
        size = f.stat().st_size / 1024
        print(f"  {f.name} ({size:.0f} KB)")
    articles = Path("raw/articles")
    if articles.exists():
        for f in sorted(articles.glob("*.md")):
            print(f"  {f.name} (article)")


def main():
    parser = argparse.ArgumentParser(description="Literature search and download")
    sub = parser.add_subparsers(dest="cmd")

    p_search = sub.add_parser("search", help="Search arXiv")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--max-results", type=int, default=10)
    p_search.add_argument("--sort", choices=["relevance", "date", "updated"], default="relevance")
    p_search.add_argument("--download", action="store_true", help="Download top result")

    p_scholar = sub.add_parser("scholar", help="Search Semantic Scholar")
    p_scholar.add_argument("query")
    p_scholar.add_argument("--max-results", type=int, default=10)

    p_fetch = sub.add_parser("fetch", help="Download arXiv paper by ID")
    p_fetch.add_argument("arxiv_id", help="e.g., 2310.15138")

    p_doi = sub.add_parser("fetch-doi", help="Download paper by DOI")
    p_doi.add_argument("doi", help="e.g., 10.1038/s41586-023-06415-8")

    sub.add_parser("list", help="List downloaded papers")

    args = parser.parse_args()

    if args.cmd == "search":
        papers = search_arxiv(args.query, args.max_results, args.sort)
        for i, p in enumerate(papers):
            print(f"\n[{i+1}] {p['title']}")
            print(f"    {', '.join(p['authors'])} ({p['published']})")
            print(f"    arXiv:{p['arxiv_id']}")
            print(f"    {p['summary']}...")
        if args.download and papers:
            fetch_arxiv_pdf(papers[0]["arxiv_id"])

    elif args.cmd == "scholar":
        papers = search_scholar(args.query, args.max_results)
        for i, p in enumerate(papers):
            print(f"\n[{i+1}] {p['title']}")
            print(f"    {', '.join(p['authors'])} ({p.get('year', '?')})")
            if p.get("arxiv_id"):
                print(f"    arXiv:{p['arxiv_id']}")
            if p.get("doi"):
                print(f"    DOI:{p['doi']}")
            print(f"    {p['abstract']}...")

    elif args.cmd == "fetch":
        fetch_arxiv_pdf(args.arxiv_id)

    elif args.cmd == "fetch-doi":
        fetch_doi(args.doi)

    elif args.cmd == "list":
        list_papers()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
