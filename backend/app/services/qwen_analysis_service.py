import re

from app.services.qwen_service import (
    get_qwen_model,
    generate_qwen_response
)


# =========================================================
# TAG PARSER
# =========================================================

def extract_xml_tag(
    text: str,
    tag: str
) -> str:
    """
    Extract an XML-style tag.

    Example:
    <SUMMARY>some text</SUMMARY>
    """

    pattern = rf"<{tag}>(.*?)</{tag}>"

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


# =========================================================
# LABEL PARSER
# =========================================================

def extract_label_section(
    text: str,
    labels: list
) -> str:
    """
    Extract a section when Qwen returns:

    SUMMARY: text
    STRENGTH: text
    WEAKNESS: text

    rather than XML tags.
    """

    label_pattern = "|".join(
        re.escape(label)
        for label in labels
    )

    pattern = (
        rf"(?im)^\s*(?:{label_pattern})\s*:\s*"
        rf"(.*?)(?=^\s*[A-Z][A-Z_ ]{{2,}}\s*:|\Z)"
    )

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


# =========================================================
# LIST CLEANING
# =========================================================

def clean_analysis_items(
    text: str
) -> list:
    """
    Convert semantic analysis text into a clean list.
    """

    if not text:
        return []

    # Remove bullets
    text = re.sub(
        r"(?m)^\s*[-•*]\s*",
        "",
        text
    )

    # Remove repeated whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    if not text:
        return []

    # Prefer || separators when present
    if "||" in text:

        parts = text.split("||")

    # Otherwise split numbered/bulleted-style sentences
    else:

        parts = re.split(
            r"\s*(?:\d+\.\s+|;\s+)\s*",
            text
        )

    items = []

    for item in parts:

        item = item.strip()

        if item and item not in items:
            items.append(item)

    return items


# =========================================================
# SEMANTIC RESPONSE PARSER
# =========================================================

def parse_semantic_response(
    response: str
) -> dict:
    """
    Parse semantic analysis from either:

    <SUMMARY>...</SUMMARY>

    OR

    SUMMARY: ...
    """

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    summary = extract_xml_tag(
        response,
        "SUMMARY"
    )

    if not summary:

        summary = extract_label_section(
            response,
            [
                "SUMMARY"
            ]
        )

    # -----------------------------------------------------
    # STRENGTHS
    # -----------------------------------------------------

    strengths_text = extract_xml_tag(
        response,
        "STRENGTHS"
    )

    if not strengths_text:

        strengths_text = extract_xml_tag(
            response,
            "STRENGTH"
        )

    if not strengths_text:

        strengths_text = extract_label_section(
            response,
            [
                "STRENGTHS",
                "STRENGTH"
            ]
        )

    strengths = clean_analysis_items(
        strengths_text
    )

    # -----------------------------------------------------
    # WEAKNESSES
    # -----------------------------------------------------

    weaknesses_text = extract_xml_tag(
        response,
        "WEAKNESSES"
    )

    if not weaknesses_text:

        weaknesses_text = extract_xml_tag(
            response,
            "WEAKNESS"
        )

    if not weaknesses_text:

        weaknesses_text = extract_label_section(
            response,
            [
                "WEAKNESSES",
                "WEAKNESS"
            ]
        )

    weaknesses = clean_analysis_items(
        weaknesses_text
    )

    # -----------------------------------------------------
    # PROJECTS
    # -----------------------------------------------------

    projects = extract_xml_tag(
        response,
        "PROJECTS"
    )

    if not projects:

        projects = extract_label_section(
            response,
            [
                "PROJECTS",
                "PROJECT"
            ]
        )

    # -----------------------------------------------------
    # IMPROVEMENTS
    # -----------------------------------------------------

    improvements_text = extract_xml_tag(
        response,
        "IMPROVEMENTS"
    )

    if not improvements_text:

        improvements_text = extract_xml_tag(
            response,
            "IMPROVEMENT"
        )

    if not improvements_text:

        improvements_text = extract_label_section(
            response,
            [
                "IMPROVEMENTS",
                "IMPROVEMENT",
                "IMPROVEMEN"
            ]
        )

    improvements = clean_analysis_items(
        improvements_text
    )

    # -----------------------------------------------------
    # OVERALL
    # -----------------------------------------------------

    overall = extract_xml_tag(
        response,
        "OVERALL"
    )

    if not overall:

        overall = extract_label_section(
            response,
            [
                "OVERALL"
            ]
        )

    return {
        "summary_assessment": summary,
        "strengths": strengths[:3],
        "weaknesses": weaknesses[:3],
        "project_assessment": projects,
        "improvements": improvements[:3],
        "overall_observation": overall
    }


# =========================================================
# SEMANTIC ANALYSIS
# =========================================================

def analyze_resume_semantically(
    resume_text: str
) -> dict:
    """
    Use Qwen to semantically analyze resume content.
    """

    if not resume_text or not resume_text.strip():

        raise ValueError(
            "No resume text was provided."
        )

    model, processor = get_qwen_model()

    # -----------------------------------------------------
    # PROMPT
    # -----------------------------------------------------

    prompt = f"""
Analyze the resume below.

Return ONLY these six lines.

SUMMARY: one short assessment
STRENGTHS: strength 1 || strength 2 || strength 3
WEAKNESSES: weakness 1 || weakness 2 || weakness 3
PROJECTS: one short project assessment
IMPROVEMENTS: improvement 1 || improvement 2 || improvement 3
OVERALL: one short overall observation

Rules:
- Do not repeat the resume.
- Do not use JSON.
- Do not use markdown.
- Do not invent facts.
- Only use information present in the resume.
- Keep responses concise.
- Maximum 3 strengths.
- Maximum 3 weaknesses.
- Maximum 3 improvements.
- Stop after the OVERALL line.

Resume:

{resume_text}
"""

    # -----------------------------------------------------
    # GENERATE
    # -----------------------------------------------------

    raw_output = generate_qwen_response(
        model,
        processor,
        prompt,
        max_new_tokens=350
    )

    print("\n" + "=" * 60)
    print("QWEN SEMANTIC ANALYSIS")
    print("=" * 60)
    print(raw_output)
    print("=" * 60)

    # -----------------------------------------------------
    # PARSE
    # -----------------------------------------------------

    result = parse_semantic_response(
        raw_output
    )

    # -----------------------------------------------------
    # CHECK RESULT
    # -----------------------------------------------------

    has_analysis = (
        bool(result["summary_assessment"])
        or bool(result["strengths"])
        or bool(result["weaknesses"])
        or bool(result["project_assessment"])
        or bool(result["improvements"])
        or bool(result["overall_observation"])
    )

    if not has_analysis:

        return {
            "success": False,
            "message": (
                "Qwen did not return recognizable "
                "semantic analysis."
            ),
            "raw_analysis": raw_output
        }

    return {
        "success": True,
        "summary_assessment": (
            result["summary_assessment"]
        ),
        "strengths": result["strengths"],
        "weaknesses": result["weaknesses"],
        "project_assessment": (
            result["project_assessment"]
        ),
        "improvements": result["improvements"],
        "overall_observation": (
            result["overall_observation"]
        )
    }