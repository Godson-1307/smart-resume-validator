import React from 'react';
import { CheckCircle2, ThumbsUp } from 'lucide-react';

export default function ResumeStrengths({ strengths = [] }) {
  const defaultStrengths = [
    'Strong technical skill section',
    'Relevant academic projects',
    'Good education information',
    'Clear contact information',
    'Relevant programming languages',
  ];

  const items = strengths.length > 0 ? strengths : defaultStrengths;

  return (
    <div id="resume-strengths-section" className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
      <div className="flex items-center gap-2 mb-4 pb-3 border-b border-[#F1F5F9]">
        <div className="w-8 h-8 rounded-lg bg-[#EDF7F1] text-[#65A98A] flex items-center justify-center">
          <ThumbsUp className="w-4 h-4" />
        </div>
        <div>
          <h3 className="text-base font-bold text-[#263247]">Resume Strengths</h3>
          <p className="text-xs text-[#667085]">Validated positive signals that stand out to ATS filters</p>
        </div>
      </div>

      <div className="space-y-2.5">
        {items.map((strength, idx) => (
          <div
            key={idx}
            className="flex items-start gap-3 p-3 rounded-xl bg-[#EDF7F1]/50 border border-[#65A98A]/20 transition-all hover:bg-[#EDF7F1]/80"
          >
            <CheckCircle2 className="w-4 h-4 text-[#65A98A] shrink-0 mt-0.5" />
            <p className="text-xs sm:text-sm font-medium text-[#263247]">{strength}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
