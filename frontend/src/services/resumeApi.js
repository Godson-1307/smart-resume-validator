import { request } from './api.js';

function scoreTo100(value, maxScore) {
  if (typeof value !== 'number' || !maxScore) return 0;
  return Math.round((value / maxScore) * 100);
}

function mapRecommendation(rec, index) {
  if (typeof rec === 'string') {
    return {
      id: `rec-${index + 1}`,
      priority: 'MEDIUM PRIORITY',
      problem: 'Resume improvement',
      suggestion: rec,
      reason: 'This recommendation is based on the resume analysis.',
    };
  }

  const priorityMap = {
    High: 'HIGH PRIORITY',
    Medium: 'MEDIUM PRIORITY',
    Low: 'LOW PRIORITY',
  };

  return {
    id: rec.id || `rec-${index + 1}`,
    priority: priorityMap[rec.priority] || rec.priority || 'MEDIUM PRIORITY',
    problem: rec.area || 'Resume improvement',
    current: rec.current || '',
    recommended: rec.recommended || '',
    suggestion: rec.message || rec.suggestion || '',
    reason: rec.reason || '',
  };
}

function mapAnalysisResponse(data) {
  const breakdown = data.breakdown || {};
  const ai = data.ai_extraction || {};
  const semantic = data.ai_semantic_analysis || {};

  const educationBlock = breakdown.education || {};
  const experienceBlock = breakdown.experience || {};
  const projectsBlock = breakdown.projects || {};
  const skillsBlock = breakdown.skills || {};
  const certificationsBlock = breakdown.certifications_achievements || {};
  const structureBlock = breakdown.structure_readability || {};

  const categories = {
    ats_compatibility: scoreTo100(
      structureBlock.score,
      structureBlock.max_score
    ),
    skills: scoreTo100(
      skillsBlock.score,
      skillsBlock.max_score
    ),
    experience: scoreTo100(
      experienceBlock.score,
      experienceBlock.max_score
    ),
    education: scoreTo100(
      educationBlock.score,
      educationBlock.max_score
    ),
    projects: scoreTo100(
      projectsBlock.score,
      projectsBlock.max_score
    ),
    formatting: scoreTo100(
      structureBlock.score,
      structureBlock.max_score
    ),
    keyword_match: scoreTo100(
      skillsBlock.score,
      skillsBlock.max_score
    ),
    achievements: scoreTo100(
      certificationsBlock.score,
      certificationsBlock.max_score
    ),
  };

  const education = (ai.education || []).map((item) => ({
    degree: item,
    institution: '',
    year: '',
  }));

  const experience = (ai.experience || []).map((item) => ({
    company: '',
    role: item,
    duration: '',
    description: item,
  }));

  let recommendations = (data.recommendations || []).map(
    mapRecommendation
  );

  if (recommendations.length === 0) {
    recommendations = (data.rule_based_improvements || []).map(
      mapRecommendation
    );
  }

  return {
    resume_id: data.resume_id,
    overall_score: data.score ?? 0,
    candidate: {
      name: ai.name || '',
      email: ai.email || '',
      phone: ai.phone || '',
      location: '',
    },
    education,
    experience,
    skills: ai.skills || [],
    categories,
    strengths: semantic.success
      ? semantic.strengths || []
      : [],
    weaknesses: semantic.success
      ? semantic.weaknesses || []
      : [],
    recommendations,
    projects: ai.projects || [],
    certifications: ai.certifications || [],
    ai_extraction: ai,
    ai_semantic_analysis: semantic,
  };
}

export async function uploadResume(file) {
  const formData = new FormData();
  formData.append('file', file);

  return request('/api/resume/upload', {
    method: 'POST',
    body: formData,
  });
}

export async function validateResume(resumeId) {
  const data = await request(
    `/api/resume/${resumeId}/validate`
  );

  // Backend stores confidence as 0-100; the existing UI
  // expects a 0-1 value before multiplying by 100.
  return {
    ...data,
    confidence:
      typeof data.confidence === 'number'
        ? data.confidence / 100
        : 0,
  };
}

export async function analyzeResume(resumeId) {
  const data = await request(
    `/api/resume/${resumeId}/full-analysis`
  );

  return mapAnalysisResponse(data);
}
