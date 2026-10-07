import React, { useState } from 'react';
import RecommendationCard from '../components/RecommendationCard.jsx';
import { Sparkles, Filter } from 'lucide-react';

export default function ImprovementList({ recommendations = [] }) {
  const [filter, setFilter] = useState('ALL');

  const filtered = recommendations.filter((rec) => {
    if (filter === 'ALL') return true;
    return rec.priority === filter;
  });

  return (
    <div id="improvement-suggestions-section" className="space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white p-5 rounded-2xl border border-[#E6EAF0] shadow-xs">
        <div>
          <span className="text-[10px] uppercase font-bold tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-2 py-0.5 rounded-md">
            Actionable Enhancements
          </span>
          <h3 className="text-lg font-bold text-[#263247] mt-1">
            Improvement Suggestions
          </h3>
          <p className="text-xs text-[#667085]">
            Specific, high-impact edits to transform your resume into an interview magnet
          </p>
        </div>

        {/* Priority Filter */}
        <div className="flex items-center gap-1.5 bg-[#F8FAFC] p-1 rounded-xl border border-[#E2E8F0] text-xs">
          <Filter className="w-3.5 h-3.5 text-[#94A3B8] ml-2" />
          {['ALL', 'HIGH PRIORITY', 'MEDIUM PRIORITY', 'LOW PRIORITY'].map((p) => (
            <button
              key={p}
              type="button"
              onClick={() => setFilter(p)}
              className={`px-2.5 py-1 rounded-lg font-medium transition-colors cursor-pointer ${
                filter === p
                  ? 'bg-white text-[#263247] shadow-xs font-semibold'
                  : 'text-[#64748B] hover:text-[#263247]'
              }`}
            >
              {p === 'ALL' ? 'All' : p.replace(' PRIORITY', '')}
            </button>
          ))}
        </div>
      </div>

      {/* Cards List */}
      <div className="space-y-3.5">
        {filtered.length > 0 ? (
          filtered.map((rec, idx) => (
            <RecommendationCard
              key={rec.id || idx}
              id={`recommendation-card-${idx}`}
              recommendation={rec}
            />
          ))
        ) : (
          <div className="bg-white border border-[#E6EAF0] rounded-2xl p-8 text-center text-xs text-[#667085]">
            No recommendations match the selected filter.
          </div>
        )}
      </div>
    </div>
  );
}
