import React from 'react';
import SkillBadge from '../components/SkillBadge.jsx';
import { CheckCircle2, ArrowRightCircle, PlusCircle, Target, UserCheck } from 'lucide-react';

export default function CareerGap({
  targetRole = 'Machine Learning Engineer',
  alreadyHave = [],
  needToImprove = [],
  missingRecommended = [],
  packageAnalysis = null,
}) {
  return (
    <div id="career-gap-section" className="space-y-6">
      
      {/* Profile vs Target Role Header */}
      <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pb-4 border-b border-[#F1F5F9]">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center">
              <Target className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] uppercase font-bold tracking-wider text-[#98A2B3]">
                Benchmark Comparison
              </span>
              <h3 className="text-lg font-bold text-[#263247]">Current Profile vs. Target Role</h3>
            </div>
          </div>

          <div className="text-right">
            <span className="text-xs text-[#64748B]">Target Role:</span>
            <p className="text-sm font-extrabold text-[#6B7FD7]">{targetRole}</p>
          </div>
        </div>

        {packageAnalysis && (
          <div className="mt-4 p-4 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0] flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 text-xs">
            <div>
              <span className="font-semibold text-[#263247]">Market Package Expectation:</span>
              <span className="ml-1.5 font-bold text-[#6B7FD7]">
                ₹{packageAnalysis.expected_package} LPA
              </span>
              <span className="ml-2 text-[#94A3B8]">(Market Band: {packageAnalysis.market_average})</span>
            </div>
            <p className="text-[#64748B] italic">{packageAnalysis.profile_gap_summary}</p>
          </div>
        )}
      </div>

      {/* 3 Skill Gap Categories */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        
        {/* Category 1: Already Have */}
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-5 shadow-xs flex flex-col">
          <div className="flex items-center gap-2 mb-3 pb-3 border-b border-[#EDF7F1]">
            <div className="w-7 h-7 rounded-lg bg-[#EDF7F1] text-[#65A98A] flex items-center justify-center">
              <CheckCircle2 className="w-4 h-4" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-[#263247]">Already Have</h4>
              <span className="text-[11px] text-[#65A98A] font-medium">
                {alreadyHave.length} Verified Skills
              </span>
            </div>
          </div>
          <div className="flex flex-wrap gap-2 flex-1 items-start content-start">
            {alreadyHave.map((sk, idx) => (
              <SkillBadge key={idx} skill={sk} type="existing" size="sm" />
            ))}
          </div>
        </div>

        {/* Category 2: Need To Improve */}
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-5 shadow-xs flex flex-col">
          <div className="flex items-center gap-2 mb-3 pb-3 border-b border-[#FFF7E8]">
            <div className="w-7 h-7 rounded-lg bg-[#FFF7E8] text-[#D9A441] flex items-center justify-center">
              <ArrowRightCircle className="w-4 h-4" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-[#263247]">Need To Improve</h4>
              <span className="text-[11px] text-[#D9A441] font-medium">
                {needToImprove.length} Skills in Progress
              </span>
            </div>
          </div>
          <div className="flex flex-wrap gap-2 flex-1 items-start content-start">
            {needToImprove.map((sk, idx) => (
              <SkillBadge key={idx} skill={sk} type="improve" size="sm" />
            ))}
          </div>
        </div>

        {/* Category 3: Missing / Recommended */}
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-5 shadow-xs flex flex-col">
          <div className="flex items-center gap-2 mb-3 pb-3 border-b border-[#F3F0FF]">
            <div className="w-7 h-7 rounded-lg bg-[#F3F0FF] text-[#9B8AFB] flex items-center justify-center">
              <PlusCircle className="w-4 h-4" />
            </div>
            <div>
              <h4 className="text-sm font-bold text-[#263247]">Missing / Recommended</h4>
              <span className="text-[11px] text-[#9B8AFB] font-medium">
                {missingRecommended.length} High-Impact Additions
              </span>
            </div>
          </div>
          <div className="flex flex-wrap gap-2 flex-1 items-start content-start">
            {missingRecommended.map((sk, idx) => (
              <SkillBadge key={idx} skill={sk} type="recommended" size="sm" />
            ))}
          </div>
        </div>

      </div>

    </div>
  );
}
