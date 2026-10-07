import React, { useState } from 'react';
import { POPULAR_ROLES } from '../utils/constants.js';
import { Briefcase, Plus, Check } from 'lucide-react';

export default function RoleSelector({ value, onChange }) {
  const [isCustom, setIsCustom] = useState(!POPULAR_ROLES.includes(value) && Boolean(value));
  const [customValue, setCustomValue] = useState(isCustom ? value : '');

  const handleSelect = (role) => {
    if (role === 'Other') {
      setIsCustom(true);
      if (customValue) onChange(customValue);
    } else {
      setIsCustom(false);
      onChange(role);
    }
  };

  const handleCustomChange = (e) => {
    const newVal = e.target.value;
    setCustomValue(newVal);
    onChange(newVal);
  };

  return (
    <div id="career-role-selector" className="space-y-4">
      <div className="flex items-center gap-2 text-xs font-semibold text-[#667085] uppercase tracking-wider">
        <Briefcase className="w-4 h-4 text-[#6B7FD7]" /> Select Target Role
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        {POPULAR_ROLES.map((role) => {
          const isSelected = !isCustom && value === role;
          return (
            <button
              key={role}
              type="button"
              onClick={() => handleSelect(role)}
              className={`flex items-center justify-between p-3.5 rounded-xl border text-xs sm:text-sm font-medium transition-all text-left cursor-pointer ${
                isSelected
                  ? 'border-[#6B7FD7] bg-[#EEF1FF] text-[#263247] shadow-xs'
                  : 'border-[#E2E8F0] bg-white hover:border-[#CBD5E1] text-[#475569]'
              }`}
            >
              <span>{role}</span>
              {isSelected && <Check className="w-4 h-4 text-[#6B7FD7] shrink-0" />}
            </button>
          );
        })}
      </div>

      {/* Custom Role Input */}
      {isCustom && (
        <div className="pt-2 animate-fadeIn">
          <label className="block text-xs font-semibold text-[#263247] mb-1.5">
            Specify Custom Role
          </label>
          <div className="relative">
            <input
              type="text"
              value={customValue}
              onChange={handleCustomChange}
              placeholder="e.g. Lead Robotics Perception Engineer"
              className="w-full px-4 py-2.5 text-sm bg-white border border-[#6B7FD7] rounded-xl focus:ring-2 focus:ring-[#6B7FD7]/20 focus:outline-hidden"
              autoFocus
            />
          </div>
        </div>
      )}
    </div>
  );
}
