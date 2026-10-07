import { useState } from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import { analyzeCareer } from '../services/careerApi.js';

export function useCareerAnalysis() {
  const context = useResumeContext();
  const [careerStepIndex, setCareerStepIndex] = useState(0);

  const submitCareerGoals = async (overrideAnswers = null) => {
    const payload = overrideAnswers || context.careerAnswers;

    try {
      context.setIsCareerAnalyzing(true);
      context.navigateTo('career-analysis');

      const result = await analyzeCareer({
        resume_id: context.resumeId,
        ...payload,
      });

      context.setCareerAnalysis(result);
      context.setIsCareerAnalyzing(false);
      return result;
    } catch (err) {
      context.setIsCareerAnalyzing(false);
      context.setError(err.message || 'Unable to complete career goal analysis.');
      return null;
    }
  };

  return {
    ...context,
    careerStepIndex,
    setCareerStepIndex,
    submitCareerGoals,
  };
}
