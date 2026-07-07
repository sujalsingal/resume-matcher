from .skill_config import get_tier

MUST_HAVE_WEIGHT = 2
NICE_TO_HAVE_WEIGHT = 1


def compute_match(resume_skills: list[str], jd_skills: list[str]) -> dict:
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    must_have_jd = {s for s in jd_set if get_tier(s) == "must_have"}
    nice_to_have_jd = {s for s in jd_set if get_tier(s) == "nice_to_have"}

    must_matched = sorted(must_have_jd & resume_set)
    must_missing = sorted(must_have_jd - resume_set)
    nice_matched = sorted(nice_to_have_jd & resume_set)
    nice_missing = sorted(nice_to_have_jd - resume_set)

    total_possible = (len(must_have_jd) * MUST_HAVE_WEIGHT) + (len(nice_to_have_jd) * NICE_TO_HAVE_WEIGHT)
    total_achieved = (len(must_matched) * MUST_HAVE_WEIGHT) + (len(nice_matched) * NICE_TO_HAVE_WEIGHT)

    score = round((total_achieved / total_possible) * 100) if total_possible > 0 else 0

    return {
        "score": score,
        "must_have_skills": {"matched": must_matched, "missing": must_missing},
        "nice_to_have_skills": {"matched": nice_matched, "missing": nice_missing},
    }


def generate_explanation(match_data: dict) -> dict:
    score = match_data["score"]
    must_missing = match_data["must_have_skills"]["missing"]
    nice_missing = match_data["nice_to_have_skills"]["missing"]

    if score >= 80:
        summary = "Strong match — the resume covers most of the key skills required for this role."
    elif score >= 50:
        summary = "Moderate match — some important skills are present, but notable gaps remain."
    else:
        summary = "Weak match — the resume is missing several core skills needed for this role."

    suggestions = []
    if must_missing:
        suggestions.append(
            f"Add or highlight experience with: {', '.join(must_missing)} — these are core requirements."
        )
    if nice_missing:
        suggestions.append(
            f"Consider mentioning: {', '.join(nice_missing)} to strengthen the application further."
        )
    if not suggestions:
        suggestions.append("The resume covers all identified skills well.")

    return {"summary": summary, "suggestions": suggestions}