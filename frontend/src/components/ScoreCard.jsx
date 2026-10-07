import React from 'react';
import { getScoreAssessment } from '../utils/formatScore.js';

export default function ScoreCard({
  id,
  score = 78,
  title = 'Overall Resume Score',
  subtitle = '',
  size = 'lg',
}) {
  const assessment = getScoreAssessment(score);
  const radius = size === 'lg' ? 48 : 36;
  const strokeWidth = size === 'lg' ? 8 : 6;
  const normalizedRadius = radius - strokeWidth / 2;
  const circumference = normalizedRadius * 2 * Math.PI;
  const strokeDashoffset = circumference - (score / 100) * circumference;

  return (
    <div
      id={id}
      className="bg-white border border-[#E6EAF0] rounded-2xl p-6 sm:p-8 flex flex-col items-center text-center shadow-xs"
    >
      <h3 className="text-xs font-semibold uppercase tracking-wider text-[#667085] mb-4">
        {title}
      </h3>

      {/* Circular Progress Ring */}
      <div className="relative flex items-center justify-center my-2">
        <svg
          height={radius * 2}
          width={radius * 2}
          className="transform -rotate-90"
        >
          {/* Background circle */}
          <circle
            stroke="#EEF1FF"
            fill="transparent"
            strokeWidth={strokeWidth}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
          />
          {/* Progress circle */}
          <circle
            stroke={assessment.color}
            fill="transparent"
            strokeWidth={strokeWidth}
            strokeDasharray={`${circumference} ${circumference}`}
            style={{ strokeDashoffset }}
            strokeLinecap="round"
            className="transition-all duration-1000 ease-out"
            r={normalizedRadius}
            cx={radius}
            cy={radius}
          />
        </svg>

        {/* Center score readout */}
        <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
          <span className="text-3xl sm:text-4xl font-extrabold text-[#263247] tracking-tight">
            {score}
          </span>
          <span className="text-xs font-medium text-[#98A2B3]">/ 100</span>
        </div>
      </div>

      {/* Assessment Label */}
      <div className="mt-4 flex flex-col items-center">
        <span
          className={`inline-block px-3 py-1 text-xs font-semibold rounded-full border ${assessment.badgeClass} mb-2`}
        >
          {assessment.label}
        </span>
        <p className="text-xs text-[#667085] max-w-xs leading-relaxed">
          {subtitle || assessment.desc}
        </p>
      </div>
    </div>
  );
}
