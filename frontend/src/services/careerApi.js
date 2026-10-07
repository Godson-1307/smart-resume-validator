import { request } from './api.js';

export async function analyzeCareer(careerPayload) {
  const { resume_id, ...goal } = careerPayload;

  if (!resume_id) {
    throw new Error('Resume ID is required for career analysis.');
  }

  const backendPayload = {
    target_role: goal.target_role,
    expected_package: goal.expected_package ?? null,
    industry: goal.industry ?? null,
    experience_level: goal.experience_level ?? null,
    country: goal.country ?? null,
    city: goal.city ?? null,
    work_type: goal.work_type ?? null,
  };

  const data = await request(
    `/api/resume/${resume_id}/career-analysis`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(backendPayload),
    }
  );

  if (!data.is_resume) {
    throw new Error(
      data.message || 'Please upload a proper resume.'
    );
  }

  const analysis = data.career_analysis || {};

  const packageValue = Number(
    analysis.expected_package ?? goal.expected_package ?? 0
  );

  const requiredSkills = analysis.required_skills || [];
  const missingSkills = analysis.missing_skills || [];
  const currentSkills = analysis.current_skills || [];
  const coverage = analysis.coverage_percentage ?? 0;

  const recommendations = (
    analysis.recommendations || []
  ).map((item) => {
    if (typeof item === 'string') return item;
    return item.message || item.suggestion || String(item);
  });

  const roleMatch = {
    role: analysis.matched_role || analysis.target_role,
    match_percentage: coverage,
    required_skills: requiredSkills,
    missing_skills: missingSkills,
  };

  const location = [
    goal.city,
    goal.country,
  ].filter(Boolean).join(', ');

  return {
    target_role: analysis.target_role || goal.target_role,
    industry: analysis.industry || goal.industry || 'Technology',
    location: location || 'Not specified',
    work_type: goal.work_type || 'Not specified',
    expected_package: packageValue,
    experience_level:
      analysis.experience_level || goal.experience_level || 'Not specified',
    existing_skills: currentSkills,
    skills_to_improve: missingSkills,
    recommended_skills: missingSkills,
    recommendations,
    roadmap: [],
    package_analysis: {
      target_role: analysis.target_role || goal.target_role,
      expected_package: packageValue,
      currency: 'INR',
      unit: 'LPA',
      market_average: 'Not provided by current backend',
      profile_gap_summary:
        'Compare the listed missing skills with the target-role baseline.',
      target_assessment:
        analysis.note ||
        'The current version does not use live salary-market data.',
    },
    matched_roles: roleMatch.role
      ? [roleMatch]
      : [],
    coverage_percentage: coverage,
    matching_skills: analysis.matching_skills || [],
    missing_skills: missingSkills,
    required_skills: requiredSkills,
  };
}
