import React from 'react';
import { IndianRupee, TrendingUp, Info } from 'lucide-react';

export default function SalaryInput({ value, onChange }) {
  const numValue = Number(value) || 12;

  const handleSliderChange = (e) => {
    onChange(Number(e.target.value));
  };

  const handleInputChange = (e) => {
    const val = e.target.value;
    onChange(val === '' ? '' : Number(val));
  };

  return (
    <div id="career-salary-input" className="space-y-6">
      <div className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-2xl p-6 text-center space-y-4">
        <span className="text-xs uppercase font-bold tracking-wider text-[#64748B]">
          Expected Target Package (Annual)
        </span>

        <div className="flex items-center justify-center gap-2">
          <span className="text-3xl font-extrabold text-[#6B7FD7]">₹</span>
          <input
            type="number"
            min="1"
            max="120"
            value={value}
            onChange={handleInputChange}
            className="w-24 text-3xl font-black text-[#263247] text-center bg-white border border-[#CBD5E1] rounded-xl py-1 focus:ring-2 focus:ring-[#6B7FD7]/30 focus:outline-hidden"
          />
          <span className="text-2xl font-bold text-[#64748B]">LPA</span>
        </div>

        <p className="text-xs text-[#94A3B8]">
          (Lakhs Per Annum • Indian Rupees ₹)
        </p>

        {/* Range Slider for fast selection */}
        <div className="pt-4 max-w-md mx-auto">
          <input
            type="range"
            min="3"
            max="60"
            step="1"
            value={numValue}
            onChange={handleSliderChange}
            className="w-full h-2 bg-[#E2E8F0] rounded-lg appearance-none cursor-pointer accent-[#6B7FD7]"
          />
          <div className="flex justify-between text-[11px] text-[#94A3B8] mt-1.5 font-medium">
            <span>₹3 LPA</span>
            <span>₹12 LPA (Typical target)</span>
            <span>₹30 LPA</span>
            <span>₹60+ LPA</span>
          </div>
        </div>
      </div>

      <div className="p-4 rounded-xl bg-[#EEF1FF]/60 border border-[#6B7FD7]/20 flex items-start gap-2.5 text-xs text-[#4F62BD]">
        <Info className="w-4 h-4 shrink-0 text-[#6B7FD7] mt-0.5" />
        <p>
          The system will compare this figure against prevailing market bands to identify experience depth and technical leadership requirements.
        </p>
      </div>
    </div>
  );
}
