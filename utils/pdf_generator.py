from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    filename,
    score,
    job_match,
    skills,
    missing_skills,
    ai_feedback
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Resume Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"Resume Score: {score}/100", styles["BodyText"]))

    story.append(Paragraph(f"Job Match: {job_match}%", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Detected Skills</b>", styles["Heading2"]))

    for skill in skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>AI Feedback</b>", styles["Heading2"]))

    story.append(Paragraph(ai_feedback.replace("\n", "<br/>"), styles["BodyText"]))

    doc.build(story)