import React from 'react';
import { useCareerAnalysis } from '../hooks/useCareerAnalysis.js';
import GoalForm from '../career/GoalForm.jsx';
import { Compass, Sparkles } from 'lucide-react';

export default function CareerGoals() {
  const { submitCareerGoals, isCareerAnalyzing, navigateTo } = useCareerAnalysis();

  const handleSubmit = async (answers) => {
    await submitCareerGoals(answers);
  };

  return (
    <div id="page-career-goals" className="max-w-3xl mx-auto px-4 py-8 sm:py-12 space-y-8">
      
      {/* Top Header matching Section 17 */}
      <div className="text-center space-y-2">
        <span className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-3 py-1 rounded-full">
          <Compass className="w-3.5 h-3.5" /> Stage 2 • Goal Mapping
        </span>
        <h1 className="text-3xl sm:text-4xl font-black text-[#263247] tracking-tight">
          Now Let's Understand Your Career Goal
        </h1>
        <p className="text-sm sm:text-base text-[#667085] max-w-lg mx-auto">
          Tell us where you want to go, and we'll compare your current profile with your target.
        </p>
      </div>

      {/* Guided Questionnaire Form */}
      <GoalForm onSubmit={handleSubmit} isSubmitting={isCareerAnalyzing} />

    </div>
  );
}
