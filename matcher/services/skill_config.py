# Maps each skill to a tier. "must_have" carries more scoring weight.
# Keys are the canonical skill name used for matching (lowercase).

SKILL_TIERS = {
    # Languages
    "python": "must_have",
    "javascript": "must_have",
    "java": "nice_to_have",
    "c++": "nice_to_have",
    "typescript": "nice_to_have",
    "sql": "must_have",
    "go": "nice_to_have",
    "php": "nice_to_have",

    # Web / backend frameworks
    "django": "must_have",
    "django rest framework": "must_have",
    "drf": "must_have",
    "flask": "nice_to_have",
    "fastapi": "nice_to_have",
    "node.js": "nice_to_have",
    "express": "nice_to_have",
    "spring boot": "nice_to_have",

    # Frontend
    "react": "nice_to_have",
    "vue": "nice_to_have",
    "angular": "nice_to_have",
    "html": "nice_to_have",
    "css": "nice_to_have",
    "bootstrap": "nice_to_have",
    "tailwind": "nice_to_have",

    # APIs / auth
    "rest api": "must_have",
    "rest apis": "must_have",
    "graphql": "nice_to_have",
    "jwt": "nice_to_have",
    "jwt authentication": "nice_to_have",
    "oauth": "nice_to_have",
    "rbac": "nice_to_have",

    # Databases
    "postgresql": "nice_to_have",
    "mysql": "nice_to_have",
    "sqlite": "nice_to_have",
    "mongodb": "nice_to_have",
    "nosql": "nice_to_have",
    "redis": "nice_to_have",
    "supabase": "nice_to_have",
    "database optimization": "nice_to_have",

    # DevOps / infra
    "docker": "nice_to_have",
    "kubernetes": "nice_to_have",
    "aws": "nice_to_have",
    "gcp": "nice_to_have",
    "azure": "nice_to_have",
    "linux": "nice_to_have",
    "ci/cd": "nice_to_have",
    "nginx": "nice_to_have",

    # Tools
    "git": "must_have",
    "github": "must_have",
    "postman": "nice_to_have",
    "pytest": "nice_to_have",
    "celery": "nice_to_have",

    # Data / ML
    "machine learning": "nice_to_have",
    "nlp": "nice_to_have",
    "spacy": "nice_to_have",
    "pandas": "nice_to_have",
    "numpy": "nice_to_have",
    "data analytics": "nice_to_have",

    # General concepts
    "object-oriented programming": "must_have",
    "oop": "must_have",
    "crud": "nice_to_have",
    "unit testing": "nice_to_have",
    "agile": "nice_to_have",
    "problem solving": "nice_to_have",
}

# Synonym map — alternate phrasings that should resolve to the same canonical skill.
# Key: variant text as it might appear in a resume/JD. Value: canonical skill name in SKILL_TIERS.
SKILL_SYNONYMS = {
    "js": "javascript",
    "reactjs": "react",
    "react.js": "react",
    "nodejs": "node.js",
    "node": "node.js",
    "postgres": "postgresql",
    "oop concepts": "object-oriented programming",
    "object oriented programming": "object-oriented programming",
    "github & git": "github",
    "git/github": "github",
    "git & github": "github",
    "rest apis": "rest api",
    "restful apis": "rest api",
    "restful api": "rest api",
    "jwt auth": "jwt",
    "jwt-based": "jwt",
    "role-based access control": "rbac",
}


def get_tier(skill: str) -> str:
    return SKILL_TIERS.get(skill, "nice_to_have")