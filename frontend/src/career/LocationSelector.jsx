import React from 'react';
import { INDUSTRIES, WORK_MODES } from '../utils/constants.js';
import { Building2, MapPin, Laptop } from 'lucide-react';

export default function LocationSelector({
  industry,
  onIndustryChange,
  country,
  onCountryChange,
  city,
  onCityChange,
  workType,
  onWorkTypeChange,
}) {
  return (
    <div id="career-location-selector" className="space-y-6">
      
      {/* Target Industry */}
      <div>
        <label className="block text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2 flex items-center gap-1.5">
          <Building2 className="w-3.5 h-3.5 text-[#6B7FD7]" /> Target Industry
        </label>
        <select
          value={industry}
          onChange={(e) => onIndustryChange(e.target.value)}
          className="w-full px-4 py-2.5 text-sm bg-white border border-[#E2E8F0] rounded-xl text-[#263247] focus:ring-2 focus:ring-[#6B7FD7]/20 focus:outline-hidden"
        >
          {INDUSTRIES.map((ind) => (
            <option key={ind} value={ind}>
              {ind}
            </option>
          ))}
        </select>
      </div>

      {/* Target City & Country */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label className="block text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2 flex items-center gap-1.5">
            <MapPin className="w-3.5 h-3.5 text-[#6B7FD7]" /> Target Country
          </label>
          <input
            type="text"
            value={country}
            onChange={(e) => onCountryChange(e.target.value)}
            placeholder="e.g. India, United States"
            className="w-full px-4 py-2.5 text-sm bg-white border border-[#E2E8F0] rounded-xl text-[#263247] focus:ring-2 focus:ring-[#6B7FD7]/20 focus:outline-hidden"
          />
        </div>

        <div>
          <label className="block text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2 flex items-center gap-1.5">
            <MapPin className="w-3.5 h-3.5 text-[#6B7FD7]" /> Preferred City
          </label>
          <input
            type="text"
            value={city}
            onChange={(e) => onCityChange(e.target.value)}
            placeholder="e.g. Mumbai, Bengaluru, Remote"
            className="w-full px-4 py-2.5 text-sm bg-white border border-[#E2E8F0] rounded-xl text-[#263247] focus:ring-2 focus:ring-[#6B7FD7]/20 focus:outline-hidden"
          />
        </div>
      </div>

      {/* Work Arrangement Mode */}
      <div>
        <label className="block text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2 flex items-center gap-1.5">
          <Laptop className="w-3.5 h-3.5 text-[#6B7FD7]" /> Work Preference
        </label>
        <div className="grid grid-cols-3 gap-3">
          {WORK_MODES.map((mode) => {
            const isSelected = workType === mode.id;
            return (
              <button
                key={mode.id}
                type="button"
                onClick={() => onWorkTypeChange(mode.id)}
                className={`p-3 rounded-xl border text-center transition-all cursor-pointer ${
                  isSelected
                    ? 'border-[#6B7FD7] bg-[#EEF1FF] text-[#263247] shadow-xs font-bold'
                    : 'border-[#E2E8F0] bg-white text-[#64748B] hover:border-[#CBD5E1]'
                }`}
              >
                <span className="text-xs sm:text-sm block">{mode.label}</span>
                <span className="text-[10px] text-[#94A3B8] hidden sm:block mt-0.5">{mode.desc}</span>
              </button>
            );
          })}
        </div>
      </div>

    </div>
  );
}
