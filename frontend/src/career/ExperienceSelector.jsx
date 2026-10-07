import React from 'react';
import { EXPERIENCE_LEVELS } from '../utils/constants.js';
import { Check, Clock } from 'lucide-react';

export default function ExperienceSelector({ value, onChange }) {
  return (
    <div id="career-experience-selector" className="space-y-4">
      <div className="flex items-center gap-2 text-xs font-semibold text-[#667085] uppercase tracking-wider">
        <Clock className="w-4 h-4 text-[#6B7FD7]" /> Select Target Experience Level
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {EXPERIENCE_LEVELS.map((level) => {
          const isSelected = value === level || (level.startsWith(value) && value !== '');
          return (
            <button
              key={level}
              type="button"
              onClick={() => onChange(level)}
              className={`flex items-center justify-between p-4 rounded-xl border text-left transition-all cursor-pointer ${
                isSelected
                  ? 'border-[#6B7FD7] bg-[#EEF1FF] text-[#263247] shadow-xs font-semibold'
                  : 'border-[#E2E8F0] bg-white hover:border-[#CBD5E1] text-[#475569]'
              }`}
            >
              <span className="text-xs sm:text-sm">{level}</span>
              {isSelected && <Check className="w-4 h-4 text-[#6B7FD7] shrink-0" />}
            </button>
          );
        })}
      </div>
    </div>
  );
}
