"""Retrieve relevant wiki pages for proof context."""
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class WikiPage:
    slug: str
    title: str
    tags: list[str]
    content: str
    path: Path


class WikiRetriever:
    """Simple keyword-based wiki retrieval. No embeddings needed for small wikis."""

    def __init__(self, wiki_root: Path):
        self.wiki_root = wiki_root
        self._pages: list[WikiPage] = []
        self._load_pages()

    def _load_pages(self):
        for subdir in ["concepts", "entities", "syntheses", "summaries", "comparisons"]:
            d = self.wiki_root / subdir
            if not d.exists():
                continue
            for f in d.glob("*.md"):
                content = f.read_text()
                title = self._extract_field(content, "title") or f.stem
                tags = self._extract_tags(content)
                self._pages.append(WikiPage(
                    slug=f.stem, title=title, tags=tags,
                    content=content, path=f,
                ))

    def _extract_field(self, content: str, field: str) -> str:
        m = re.search(rf'^{field}:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    def _extract_tags(self, content: str) -> list[str]:
        m = re.search(r'^tags:\s*\[(.*?)\]', content, re.MULTILINE)
        if not m:
            return []
        return [t.strip().strip('"').strip("'") for t in m.group(1).split(",") if t.strip()]

    def retrieve(self, query: str, top_k: int = 3) -> list[WikiPage]:
        """Retrieve pages most relevant to query via keyword overlap."""
        query_terms = set(re.findall(r'\w+', query.lower()))
        scored = []
        for page in self._pages:
            page_terms = set(re.findall(r'\w+', (page.content + " ".join(page.tags)).lower()))
            overlap = len(query_terms & page_terms)
            if overlap > 0:
                scored.append((overlap, page))
        scored.sort(key=lambda x: -x[0])
        return [p for _, p in scored[:top_k]]

    def retrieve_failures(self, topic: str) -> list[WikiPage]:
        """Retrieve synthesis pages that document failed strategies for a topic."""
        results = []
        topic_lower = topic.lower()
        for page in self._pages:
            if page.path.parent.name != "syntheses":
                continue
            if topic_lower in page.content.lower() or topic_lower in " ".join(page.tags).lower():
                results.append(page)
        return results
