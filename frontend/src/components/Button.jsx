import React from 'react';

export default function Button({
  id,
  children,
  variant = 'primary',
  size = 'md',
  onClick,
  disabled = false,
  className = '',
  type = 'button',
  icon: Icon,
  iconPosition = 'left',
}) {
  const baseStyles =
    'inline-flex items-center justify-center font-medium rounded-xl transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed select-none focus:outline-hidden focus:ring-2 focus:ring-[#6B7FD7]/30';

  const variants = {
    primary:
      'bg-[#6B7FD7] text-white hover:bg-[#5C70C8] active:scale-[0.98] shadow-xs hover:shadow-md hover:shadow-[#6B7FD7]/20',
    secondary:
      'bg-[#EEF1FF] text-[#4F62BD] hover:bg-[#E2E7FF] border border-[#6B7FD7]/20 active:scale-[0.98]',
    outline:
      'bg-white text-[#263247] border border-[#E6EAF0] hover:bg-[#F8FAFC] hover:border-[#CBD5E1] active:scale-[0.98]',
    ghost:
      'bg-transparent text-[#667085] hover:text-[#263247] hover:bg-[#F1F5F9]',
    danger:
      'bg-[#FEF0F0] text-[#D97878] border border-[#D97878]/30 hover:bg-[#FDE2E2]',
    success:
      'bg-[#65A98A] text-white hover:bg-[#569477] shadow-xs active:scale-[0.98]',
  };

  const sizes = {
    sm: 'text-xs px-3 py-1.5 gap-1.5',
    md: 'text-sm px-5 py-2.5 gap-2',
    lg: 'text-base px-6 py-3 gap-2.5',
  };

  return (
    <button
      id={id}
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`${baseStyles} ${variants[variant] || variants.primary} ${sizes[size] || sizes.md} ${className}`}
    >
      {Icon && iconPosition === 'left' && <Icon className="w-4 h-4 shrink-0" />}
      <span>{children}</span>
      {Icon && iconPosition === 'right' && <Icon className="w-4 h-4 shrink-0" />}
    </button>
  );
}
