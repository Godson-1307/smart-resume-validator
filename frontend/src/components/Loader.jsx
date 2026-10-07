import React from 'react';
import { Loader2 } from 'lucide-react';

export default function Loader({
  size = 'md',
  text = 'Processing...',
  subtext = '',
  className = '',
}) {
  const sizes = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12',
  };

  return (
    <div className={`flex flex-col items-center justify-center p-6 text-center ${className}`}>
      <Loader2 className={`${sizes[size] || sizes.md} text-[#6B7FD7] animate-spin mb-3`} />
      <h3 className="font-semibold text-[#263247] text-base">{text}</h3>
      {subtext && <p className="text-sm text-[#667085] mt-1 max-w-sm">{subtext}</p>}
    </div>
  );
}
