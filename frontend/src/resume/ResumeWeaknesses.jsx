import React from 'react';
import { AlertTriangle } from 'lucide-react';

export default function ResumeWeaknesses({ weaknesses = [] }) {
  const defaultWeaknesses = [
    'Work experience lacks measurable achievements',
    'Project descriptions are too short',
    'Missing important keywords',
    'Summary section could be stronger',
    'Skills section could be better organized',
  ];

  const items = weaknesses.length > 0 ? weaknesses : defaultWeaknesses;

  return (
    <div id="resume-weaknesses-section" className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
      <div className="flex items-center gap-2 mb-4 pb-3 border-b border-[#F1F5F9]">
        <div className="w-8 h-8 rounded-lg bg-[#FFF7E8] text-[#D9A441] flex items-center justify-center">
          <AlertTriangle className="w-4 h-4" />
        </div>
        <div>
          <h3 className="text-base font-bold text-[#263247]">Areas To Improve</h3>
          <p className="text-xs text-[#667085]">Critical gaps reducing interview shortlisting rates</p>
        </div>
      </div>

      <div className="space-y-2.5">
        {items.map((weakness, idx) => (
          <div
            key={idx}
            className="flex items-start gap-3 p-3 rounded-xl bg-[#FFF7E8]/50 border border-[#D9A441]/20 transition-all hover:bg-[#FFF7E8]/80"
          >
            <AlertTriangle className="w-4 h-4 text-[#D9A441] shrink-0 mt-0.5" />
            <p className="text-xs sm:text-sm font-medium text-[#263247]">{weakness}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
