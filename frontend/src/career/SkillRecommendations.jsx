import React from 'react';
import { Lightbulb, Target, CheckCircle2, ChevronRight, Briefcase } from 'lucide-react';
import SkillBadge from '../components/SkillBadge.jsx';

export default function SkillRecommendations({
  targetRole = 'Machine Learning Engineer',
  recommendations = [],
  matchedRoles = [],
}) {
  return (
    <div id="skill-recommendations-section" className="space-y-6">
      
      {/* Personalized Recommendations Box */}
      <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
        <div className="flex items-center gap-3 mb-4 pb-3 border-b border-[#F1F5F9]">
          <div className="w-8 h-8 rounded-lg bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center">
            <Lightbulb className="w-4 h-4" />
          </div>
          <div>
            <span className="text-[10px] uppercase font-bold tracking-wider text-[#6B7FD7]">
              Context-Aware Strategy
            </span>
            <h3 className="text-base font-bold text-[#263247]">
              Personalized Recommendations for {targetRole}
            </h3>
          </div>
        </div>

        <p className="text-xs text-[#667085] mb-4">
          Synthesized by factoring your current skills, target role, expected compensation, and experience level:
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          {recommendations.map((recText, idx) => (
            <div
              key={idx}
              className="flex items-start gap-3 p-3.5 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0] hover:border-[#CBD5E1] transition-colors"
            >
              <span className="w-6 h-6 rounded-full bg-[#EEF1FF] text-[#6B7FD7] text-xs font-bold flex items-center justify-center shrink-0 mt-0.5">
                {idx + 1}
              </span>
              <p className="text-xs sm:text-sm font-medium text-[#263247] leading-relaxed">
                {recText}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Alternative Matched Roles (Section 30) */}
      {matchedRoles.length > 0 && (
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
          <div className="flex items-center gap-3 mb-4 pb-3 border-b border-[#F1F5F9]">
            <div className="w-8 h-8 rounded-lg bg-[#F3F0FF] text-[#9B8AFB] flex items-center justify-center">
              <Briefcase className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-base font-bold text-[#263247]">Roles Matching Your Current Profile</h3>
              <p className="text-xs text-[#667085]">Adjacent opportunities where your existing skillset confers an immediate advantage</p>
            </div>
          </div>

          <div className="space-y-3">
            {matchedRoles.map((roleItem, idx) => (
              <div
                key={idx}
                className="p-4 rounded-xl border border-[#E2E8F0] bg-[#F8FAFC]/50 hover:bg-white hover:border-[#CBD5E1] transition-all flex flex-col md:flex-row md:items-center justify-between gap-4"
              >
                <div className="space-y-1.5">
                  <div className="flex items-center gap-3">
                    <h4 className="font-bold text-sm text-[#263247]">{roleItem.role}</h4>
                    <span className="text-xs font-bold text-[#2F6F50] bg-[#EDF7F1] px-2 py-0.5 rounded-md border border-[#65A98A]/30">
                      {roleItem.match_percentage}% Match
                    </span>
                  </div>

                  {/* Skills tags */}
                  <div className="flex flex-wrap items-center gap-1.5 text-xs">
                    <span className="text-[10px] text-[#94A3B8] font-semibold uppercase">Missing:</span>
                    {roleItem.missing_skills.map((sk, sIdx) => (
                      <span
                        key={sIdx}
                        className="text-[11px] px-2 py-0.5 rounded bg-[#FEF0F0] text-[#D97878] border border-[#D97878]/30 font-medium"
                      >
                        + {sk}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="text-xs text-[#667085] flex items-center gap-2 self-end md:self-auto">
                  <span className="hidden sm:inline">Requires {roleItem.required_skills.length} core proficiencies</span>
                  <ChevronRight className="w-4 h-4 text-[#94A3B8]" />
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
