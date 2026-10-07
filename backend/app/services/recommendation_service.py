def add_recommendation(
    recommendations: list,
    priority: str,
    area: str,
    message: str
):
    """
    Add a recommendation in a structured format.
    """

    recommendations.append({
        "priority": priority,
        "area": area,
        "message": message
    })


def generate_recommendations(score_result: dict) -> list:
    """
    Generate prioritized and actionable recommendations
    from the resume score breakdown.
    """

    recommendations = []

    breakdown = score_result.get("breakdown", {})

    # -------------------------------------------------
    # 1. CONTACT & HEADER
    # -------------------------------------------------

    contact = breakdown.get("contact_header", {})
    contact_score = contact.get("score", 0)

    if contact_score < 10:
        add_recommendation(
            recommendations,
            "High",
            "Contact & Header",
            "Complete your header with your full name, "
            "professional email address, and phone number."
        )

    # -------------------------------------------------
    # 2. SUMMARY
    # -------------------------------------------------

    summary = breakdown.get("summary", {})
    summary_score = summary.get("score", 0)

    if summary_score < 5:
        add_recommendation(
            recommendations,
            "High",
            "Summary",
            "Add a professional summary describing your "
            "background, strongest skills, and career direction."
        )

    elif summary_score < 10:
        add_recommendation(
            recommendations,
            "Medium",
            "Summary",
            "Strengthen your summary by mentioning your "
            "specialization, relevant skills, and target career direction."
        )

    # -------------------------------------------------
    # 3. EDUCATION
    # -------------------------------------------------

    education = breakdown.get("education", {})
    education_score = education.get("score", 0)

    if education_score < 6:
        add_recommendation(
            recommendations,
            "High",
            "Education",
            "Clearly include your degree, institution, "
            "and relevant education dates."
        )

    elif education_score < 10:
        add_recommendation(
            recommendations,
            "Low",
            "Education",
            "Review your education section and make sure "
            "your qualification, institution, and dates are clearly presented."
        )

    # -------------------------------------------------
    # 4. SKILLS
    # -------------------------------------------------

    skills = breakdown.get("skills", {})
    skills_score = skills.get("score", 0)

    detected_skills = skills.get(
        "skills_detected",
        []
    )

    if skills_score < 6:
        add_recommendation(
            recommendations,
            "High",
            "Skills",
            "Create a focused skills section containing "
            "specific technical and professional skills."
        )

    elif skills_score < 12:
        add_recommendation(
            recommendations,
            "High",
            "Skills",
            "Expand your skill set with relevant technologies "
            "and prioritize skills related to the roles you want."
        )

    else:
        if len(detected_skills) > 0:
            add_recommendation(
                recommendations,
                "Low",
                "Skills",
                "Keep your skills section focused and remove "
                "skills that are outdated or not relevant to your target roles."
            )

    # -------------------------------------------------
    # 5. EXPERIENCE
    # -------------------------------------------------

    experience = breakdown.get("experience", {})
    experience_score = experience.get("score", 0)

    if experience_score == 0:
        add_recommendation(
            recommendations,
            "Medium",
            "Experience",
            "Add internships, work experience, freelance work, "
            "or other relevant professional exposure when available."
        )

    elif experience_score < 10:
        add_recommendation(
            recommendations,
            "High",
            "Experience",
            "Rewrite experience entries using action verbs and "
            "explain what you contributed rather than only listing duties."
        )

        add_recommendation(
            recommendations,
            "Medium",
            "Experience",
            "Add measurable results where possible, such as "
            "performance improvements, users reached, time saved, or project scale."
        )

    # -------------------------------------------------
    # 6. PROJECTS
    # -------------------------------------------------

    projects = breakdown.get("projects", {})
    projects_score = projects.get("score", 0)

    if projects_score == 0:
        add_recommendation(
            recommendations,
            "High",
            "Projects",
            "Add relevant academic or personal projects "
            "to demonstrate practical application of your skills."
        )

    elif projects_score < 10:
        add_recommendation(
            recommendations,
            "High",
            "Projects",
            "For each project, describe the problem, your solution, "
            "the technologies used, and the final outcome."
        )

        add_recommendation(
            recommendations,
            "Medium",
            "Projects",
            "Highlight your personal contribution instead of "
            "only describing what the project does."
        )

    # -------------------------------------------------
    # 7. CERTIFICATIONS & ACHIEVEMENTS
    # -------------------------------------------------

    certifications = breakdown.get(
        "certifications_achievements",
        {}
    )

    certification_score = certifications.get(
        "score",
        0
    )

    if certification_score == 0:
        add_recommendation(
            recommendations,
            "Low",
            "Certifications & Achievements",
            "Add relevant certifications, awards, competitions, "
            "or other achievements when available."
        )

    elif certification_score < 6:
        add_recommendation(
            recommendations,
            "Low",
            "Certifications & Achievements",
            "Add more specific details about your certifications "
            "or achievements and explain their relevance where useful."
        )

    # -------------------------------------------------
    # 8. STRUCTURE & READABILITY
    # -------------------------------------------------

    structure = breakdown.get(
        "structure_readability",
        {}
    )

    structure_score = structure.get(
        "score",
        0
    )

    if structure_score < 8:
        add_recommendation(
            recommendations,
            "High",
            "Structure",
            "Improve organization with clear headings, "
            "consistent spacing, and concise bullet points."
        )

    elif structure_score < 12:
        add_recommendation(
            recommendations,
            "Medium",
            "Structure",
            "Improve readability by shortening long descriptions "
            "and keeping formatting consistent across sections."
        )

    # -------------------------------------------------
    # 9. OVERALL SCORE
    # -------------------------------------------------

    overall_score = score_result.get(
        "score",
        0
    )

    if overall_score < 50:

        add_recommendation(
            recommendations,
            "High",
            "Overall",
            "Strengthen the major resume sections before using "
            "this resume for job applications."
        )

    elif overall_score < 75:

        add_recommendation(
            recommendations,
            "Medium",
            "Overall",
            "Your resume has a solid foundation. Focus first on "
            "the lowest-scoring sections to improve the overall profile."
        )

    else:

        add_recommendation(
            recommendations,
            "Low",
            "Overall",
            "Maintain the current structure and tailor the resume "
            "to each target role rather than using one identical version everywhere."
        )

    return recommendations