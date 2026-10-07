# Smart Resume Validator

A modern web application built according to the Frontend Development Specification that does more than calculate an ATS score.

## Features

- **Document Classification & Anti-False Scoring Guard**: Automatically validates whether an uploaded document is genuinely a resume. Unrelated files (e.g. `college_notes.pdf`, receipts, homework) are rejected with a clear message:
  > *"This document does not appear to be a valid resume. Please upload a proper resume."*
- **Multidimensional ATS Diagnostics**: 8-metric rubric evaluating ATS Compatibility, Skills, Experience, Education, Projects, Formatting, Keyword Match, and Achievements.
- **Detailed Resume Analysis**: Extracted personal information, education, experience, validated strengths, and prioritized areas to improve.
- **Improvement Suggestions**: Actionable rewrites with Before vs. After examples, rationale, and priority tags (`HIGH`, `MEDIUM`, `LOW`).
- **Guided Career Goal Questionnaire**: 5-step guided flow capturing Target Role, Industry, Location, Expected Package (₹ LPA), and Experience Level.
- **Career Gap Analysis**: Real-time comparison of verified skills against target market requirements (Already Have, Need To Improve, Missing / Recommended).
- **Personalized 6-Month Action Roadmap**: Chronological progression with monthly deliverables to bridge skill gaps and land target job offers.
- **Matched Job Role Suggestions**: Discovers adjacent opportunities where existing candidate skills offer immediate leverage.

## Frontend Folder Structure

```
smart-resume-validator/
│
├── public/
│   ├── favicon.ico
│   └── assets/
│
├── src/
│   ├── assets/
│   │   ├── logo.svg
│   │   ├── illustrations/
│   │   └── icons/
│   │
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── Footer.jsx
│   │   ├── Button.jsx
│   │   ├── Loader.jsx
│   │   ├── ProgressBar.jsx
│   │   ├── ScoreCard.jsx
│   │   ├── SkillBadge.jsx
│   │   ├── RecommendationCard.jsx
│   │   ├── ErrorMessage.jsx
│   │   └── FileUpload.jsx
│   │
│   ├── resume/
│   │   ├── ResumeUploader.jsx
│   │   ├── ResumePreview.jsx
│   │   ├── ValidationStatus.jsx
│   │   ├── ResumeScore.jsx
│   │   ├── ScoreBreakdown.jsx
│   │   ├── ResumeStrengths.jsx
│   │   ├── ResumeWeaknesses.jsx
│   │   ├── ImprovementList.jsx
│   │   └── ResumeInformation.jsx
│   │
│   ├── career/
│   │   ├── GoalForm.jsx
│   │   ├── RoleSelector.jsx
│   │   ├── SalaryInput.jsx
│   │   ├── LocationSelector.jsx
│   │   ├── ExperienceSelector.jsx
│   │   ├── SkillSelector.jsx
│   │   ├── CareerGap.jsx
│   │   ├── SkillRecommendations.jsx
│   │   └── CareerRoadmap.jsx
│   │
│   ├── pages/
│   │   ├── Home.jsx
│   │   ├── UploadResume.jsx
│   │   ├── Validation.jsx
│   │   ├── Analysis.jsx
│   │   ├── Dashboard.jsx
│   │   ├── CareerGoals.jsx
│   │   ├── CareerAnalysis.jsx
│   │   └── NotFound.jsx
│   │
│   ├── services/
│   │   ├── api.js
│   │   ├── resumeApi.js
│   │   └── careerApi.js
│   │
│   ├── hooks/
│   │   ├── useResume.js
│   │   └── useCareerAnalysis.js
│   │
│   ├── context/
│   │   └── ResumeContext.jsx
│   │
│   ├── utils/
│   │   ├── validation.js
│   │   ├── formatScore.js
│   │   └── constants.js
│   │
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── package.json
└── README.md
```

## API Contract

The frontend connects directly to the local FastAPI backend. Set `VITE_API_BASE_URL` in `.env` to the backend origin, for example `http://127.0.0.1:8000`.

- `POST /api/resume/upload`: Uploads the selected document and returns a `resume_id`.
- `GET /api/resume/{resume_id}/validate`: Validates whether the document is a resume.
- `GET /api/resume/{resume_id}/full-analysis`: Returns score, breakdown, recommendations, Qwen extraction, and semantic analysis.
- `POST /api/resume/{resume_id}/career-analysis`: Compares the resume against the submitted career goal.
- `GET /api/resume/{resume_id}/history`: Retrieves the persisted analysis for one resume.
- `GET /api/resume/history/all`: Retrieves resume history.

The frontend no longer uses mock analysis fallbacks when the backend is unavailable.

## Design System

Strictly adheres to the specification's light, subtle & chill aesthetic:
- Background: `#F7F9FC`
- Cards: `#FFFFFF` with `#E6EAF0` borders
- Primary Accent: `#6B7FD7` (Soft Blue)
- Secondary Accent: `#9B8AFB` (Soft Lavender)
- Status Colors: Success (`#65A98A`), Warning (`#D9A441`), Error (`#D97878`)
- Typography: Manrope / Inter with generous negative space
