import React from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import Button from '../components/Button.jsx';
import { FileQuestion, Home } from 'lucide-react';

export default function NotFound() {
  const { navigateTo } = useResumeContext();

  return (
    <div id="page-not-found" className="max-w-md mx-auto px-4 py-24 text-center">
      <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8 shadow-xs space-y-4">
        <div className="w-14 h-14 rounded-2xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center mx-auto">
          <FileQuestion className="w-7 h-7" />
        </div>
        <h2 className="text-2xl font-bold text-[#263247]">Page Not Found</h2>
        <p className="text-xs sm:text-sm text-[#667085]">
          The page you requested does not exist or has been moved.
        </p>
        <div className="pt-2">
          <Button
            variant="primary"
            size="md"
            icon={Home}
            onClick={() => navigateTo('home')}
            className="w-full"
          >
            Back to Home
          </Button>
        </div>
      </div>
    </div>
  );
}
