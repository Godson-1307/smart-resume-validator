import React from 'react';
import { AlertTriangle, RefreshCw, XCircle } from 'lucide-react';
import Button from './Button.jsx';

export default function ErrorMessage({
  id,
  title = 'An error occurred',
  message,
  onRetry,
  onDismiss,
  variant = 'error', // 'error' | 'warning'
}) {
  const isWarning = variant === 'warning';

  return (
    <div
      id={id}
      className={`rounded-2xl p-4 sm:p-5 border shadow-xs ${
        isWarning
          ? 'bg-[#FFF7E8] border-[#D9A441]/40 text-[#8C6212]'
          : 'bg-[#FEF0F0] border-[#D97878]/40 text-[#9E3939]'
      }`}
    >
      <div className="flex items-start gap-3">
        {isWarning ? (
          <AlertTriangle className="w-5 h-5 shrink-0 text-[#D9A441] mt-0.5" />
        ) : (
          <XCircle className="w-5 h-5 shrink-0 text-[#D97878] mt-0.5" />
        )}

        <div className="flex-1 min-w-0">
          <h4 className="text-sm font-bold text-[#263247]">{title}</h4>
          <p className="text-xs sm:text-sm mt-1 text-[#667085] leading-relaxed">
            {message}
          </p>

          {(onRetry || onDismiss) && (
            <div className="flex items-center gap-2 mt-3">
              {onRetry && (
                <Button
                  size="sm"
                  variant="outline"
                  icon={RefreshCw}
                  onClick={onRetry}
                  className="text-xs bg-white"
                >
                  Try Again
                </Button>
              )}
              {onDismiss && (
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={onDismiss}
                  className="text-xs"
                >
                  Dismiss
                </Button>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
