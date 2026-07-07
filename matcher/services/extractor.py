import re
import pdfplumber
from .skill_config import SKILL_TIERS, SKILL_SYNONYMS

# Build the full list of terms to search for: canonical skills + synonym variants
ALL_TERMS = list(SKILL_TIERS.keys()) + list(SKILL_SYNONYMS.keys())


def _to_canonical(term: str) -> str:
    return SKILL_SYNONYMS.get(term, term)


def extract_skills(text: str) -> list[str]:
    """
    Extract skills from text using word-boundary regex matching
    (prevents false merges like 'git' + 'python' -> 'gitpython',
    and false substrings like 'java' matching inside 'javascript').
    Resolves synonyms to their canonical skill name.
    """
    if not text:
        return []

    text_lower = text.lower()
    found = set()

    for term in ALL_TERMS:
        # Escape regex special chars (e.g. "c++", "ci/cd") and require word boundaries.
        pattern = r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"
        if re.search(pattern, text_lower):
            found.add(_to_canonical(term))

    return sorted(found)


def extract_entities(text: str) -> dict:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = {"ORG": [], "PERSON": [], "GPE": []}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)
    return entities


def extract_text_from_pdf(file) -> str:
    text_parts = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)