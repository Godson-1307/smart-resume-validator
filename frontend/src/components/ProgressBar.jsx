import React from 'react';

export default function ProgressBar({
  id,
  value = 0,
  max = 100,
  height = 'h-2.5',
  color = '#6B7FD7',
  showLabel = false,
  label = '',
  className = '',
}) {
  const percentage = Math.min(100, Math.max(0, Math.round((value / max) * 100)));

  return (
    <div id={id} className={`w-full ${className}`}>
      {(showLabel || label) && (
        <div className="flex justify-between items-center text-xs font-medium text-[#667085] mb-1.5">
          <span>{label}</span>
          <span>{percentage}%</span>
        </div>
      )}
      <div className={`w-full bg-[#E6EAF0] rounded-full overflow-hidden ${height}`}>
        <div
          className="h-full rounded-full transition-all duration-700 ease-out"
          style={{
            width: `${percentage}%`,
            backgroundColor: color,
          }}
        />
      </div>
    </div>
  );
}
