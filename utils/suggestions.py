def generate_suggestions(missing_skills):

    suggestions = []

    if "Flask" in missing_skills:
        suggestions.append(
            "Build a Flask project to strengthen your backend development skills."
        )

    if "Git" in missing_skills:
        suggestions.append(
            "Learn Git and upload your projects to GitHub."
        )

    if "SQL" in missing_skills:
        suggestions.append(
            "Practice SQL queries and database design."
        )

    if "HTML" in missing_skills:
        suggestions.append(
            "Improve your HTML skills to build better web applications."
        )

    if "CSS" in missing_skills:
        suggestions.append(
            "Practice CSS layouts like Flexbox and Grid."
        )

    if "Machine Learning" in missing_skills:
        suggestions.append(
            "Complete one Machine Learning project using Python."
        )

    return suggestions