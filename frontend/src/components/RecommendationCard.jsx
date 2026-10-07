import React from 'react';
import { AlertCircle, AlertTriangle, Info, ArrowUpRight } from 'lucide-react';

export default function RecommendationCard({
  id,
  recommendation,
}) {
  const { priority, problem, current, recommended, suggestion, reason } = recommendation;

  const priorityMeta = {
    'HIGH PRIORITY': {
      badge: 'bg-[#FEF0F0] text-[#D97878] border-[#D97878]/30',
      borderLeft: 'border-l-4 border-l-[#D97878]',
      icon: AlertCircle,
    },
    'MEDIUM PRIORITY': {
      badge: 'bg-[#FFF7E8] text-[#D9A441] border-[#D9A441]/30',
      borderLeft: 'border-l-4 border-l-[#D9A441]',
      icon: AlertTriangle,
    },
    'LOW PRIORITY': {
      badge: 'bg-[#EEF1FF] text-[#6B7FD7] border-[#6B7FD7]/30',
      borderLeft: 'border-l-4 border-l-[#6B7FD7]',
      icon: Info,
    },
  };

  const meta = priorityMeta[priority] || priorityMeta['MEDIUM PRIORITY'];
  const PriorityIcon = meta.icon;

  return (
    <div
      id={id}
      className={`bg-white border border-[#E6EAF0] rounded-2xl p-5 shadow-xs transition-all hover:shadow-md hover:border-[#CBD5E1] ${meta.borderLeft}`}
    >
      {/* Top row: Priority Badge & Problem Title */}
      <div className="flex items-start justify-between gap-3 mb-3">
        <div>
          <span
            className={`inline-flex items-center gap-1 text-[11px] font-bold uppercase tracking-wider px-2.5 py-0.5 rounded-md border ${meta.badge}`}
          >
            <PriorityIcon className="w-3 h-3" />
            {priority}
          </span>
          <h4 className="text-base font-semibold text-[#263247] mt-1.5">{problem}</h4>
        </div>
      </div>

      {/* Comparison: Current vs Recommended (if present) */}
      {(current || recommended) && (
        <div className="my-3 space-y-2 text-xs">
          {current && (
            <div className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl p-3">
              <span className="font-semibold text-[#64748B] uppercase text-[10px] tracking-wider block mb-1">
                Current text:
              </span>
              <p className="text-[#475569] italic font-mono bg-white p-2 rounded-lg border border-[#EDF2F7]">
                "{current}"
              </p>
            </div>
          )}

          {recommended && (
            <div className="bg-[#EDF7F1]/60 border border-[#65A98A]/30 rounded-xl p-3">
              <span className="font-semibold text-[#2F6F50] uppercase text-[10px] tracking-wider block mb-1">
                Recommended rewrite:
              </span>
              <p className="text-[#1E4A35] font-mono bg-white p-2 rounded-lg border border-[#C6E7D5]">
                "{recommended}"
              </p>
            </div>
          )}
        </div>
      )}

      {/* Suggestion & Reason */}
      <div className="mt-3 pt-3 border-t border-[#F1F5F9] space-y-1.5 text-xs text-[#667085]">
        {suggestion && (
          <p>
            <span className="font-semibold text-[#263247]">Action:</span> {suggestion}
          </p>
        )}
        {reason && (
          <p className="text-[#64748B]">
            <span className="font-semibold text-[#263247]">Why:</span> {reason}
          </p>
        )}
      </div>
    </div>
  );
}
