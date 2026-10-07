import React from 'react';
import { Check, ArrowRight, Plus, X } from 'lucide-react';

export default function SkillBadge({
  id,
  skill,
  type = 'default', // 'existing' | 'improve' | 'recommended' | 'default'
  onRemove,
  onClick,
  size = 'md',
}) {
  const types = {
    existing: {
      bg: 'bg-[#EDF7F1] text-[#246343] border-[#65A98A]/30',
      icon: Check,
    },
    improve: {
      bg: 'bg-[#FFF7E8] text-[#8C6212] border-[#D9A441]/30',
      icon: ArrowRight,
    },
    recommended: {
      bg: 'bg-[#F3F0FF] text-[#6C56CE] border-[#9B8AFB]/30',
      icon: Plus,
    },
    default: {
      bg: 'bg-[#EEF1FF] text-[#4255A8] border-[#6B7FD7]/20',
      icon: null,
    },
  };

  const current = types[type] || types.default;
  const Icon = current.icon;

  const sizes = {
    sm: 'text-xs px-2.5 py-1 gap-1',
    md: 'text-sm px-3 py-1.5 gap-1.5',
    lg: 'text-sm px-3.5 py-2 gap-2',
  };

  return (
    <span
      id={id}
      onClick={onClick}
      className={`inline-flex items-center rounded-lg font-medium border transition-colors select-none whitespace-nowrap ${current.bg} ${sizes[size] || sizes.md} ${onClick ? 'cursor-pointer hover:opacity-85' : ''}`}
    >
      {Icon && <Icon className="w-3.5 h-3.5 shrink-0 opacity-80" />}
      <span>{skill}</span>
      {onRemove && (
        <button
          type="button"
          onClick={(e) => {
            e.stopPropagation();
            onRemove(skill);
          }}
          className="ml-1 hover:bg-black/10 rounded-full p-0.5 transition-colors cursor-pointer"
          title={`Remove ${skill}`}
        >
          <X className="w-3 h-3" />
        </button>
      )}
    </span>
  );
}
