from app.services.qwen_service import extract_resume_information


resume_text = """
Godson Nadar
Email: godson.nadar@gmail.com
Phone: 9876543210

SUMMARY
Third-year Artificial Intelligence and Machine Learning
engineering student interested in machine learning,
natural language processing and software development.

EDUCATION
Bachelor of Engineering in Artificial Intelligence and
Machine Learning, St. Francis Institute of Technology,
2024 - 2028

SKILLS
Python, SQL, Machine Learning, Deep Learning, NLP,
FastAPI, HTML, CSS, JavaScript, Git, PyTorch

EXPERIENCE
AI/ML Intern at ABC Technologies.
Worked on machine learning models and data preprocessing.
Developed Python-based solutions for internal projects.

PROJECTS
Smart Resume Validator
Developed a resume analysis system using Python and FastAPI.

OCR Extraction System
Built an OCR document extraction project using Qwen2-VL.

CERTIFICATIONS
Python Programming Certification
Machine Learning Fundamentals Certification
"""


print("=" * 60)
print("QWEN SERVICE TEST")
print("=" * 60)

try:

    result = extract_resume_information(
        resume_text
    )

    print("\nQwen extraction successful.\n")

    print("Name:")
    print(result["name"])

    print("\nEmail:")
    print(result["email"])

    print("\nPhone:")
    print(result["phone"])

    print("\nSkills:")
    print(result["skills"])

    print("\nEducation:")
    print(result["education"])

    print("\nExperience:")
    print(result["experience"])

    print("\nProjects:")
    print(result["projects"])

    print("\nCertifications:")
    print(result["certifications"])

    print("\n" + "=" * 60)
    print("TEST PASSED")
    print("=" * 60)

except Exception as error:

    print("\nTEST FAILED")
    print(type(error).__name__)
    print(error)