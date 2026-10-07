import React from 'react';
import ResumeUploader from '../resume/ResumeUploader.jsx';
import { useResumeContext } from '../context/ResumeContext.jsx';
import { Sparkles, ShieldCheck, FileCheck } from 'lucide-react';

export default function UploadResume() {
  const { navigateTo } = useResumeContext();

  return (
    <div id="page-upload-resume" className="max-w-3xl mx-auto px-4 py-8 sm:py-12 space-y-8">
      
      {/* Page Header */}
      <div className="text-center space-y-3">
        <span className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-3 py-1 rounded-full">
          <FileCheck className="w-3.5 h-3.5" /> Step 1: Upload & Classification
        </span>
        <h1 className="text-3xl sm:text-4xl font-black text-[#263247] tracking-tight">
          Upload Your Resume
        </h1>
        <p className="text-sm sm:text-base text-[#667085] max-w-xl mx-auto">
          Our intelligent classification engine ensures only genuine resumes are scored, protecting you against inaccurate generic results.
        </p>
      </div>

      {/* Main Upload Box */}
      <div className="bg-white border border-[#E6EAF0] rounded-3xl p-6 sm:p-10 shadow-xs">
        <ResumeUploader />
      </div>

      {/* Safety Notice */}
      <div className="flex items-center justify-center gap-2 text-xs text-[#98A2B3] text-center">
        <ShieldCheck className="w-4 h-4 text-[#65A98A]" />
        <span>Strict document validation: Random documents and notes are automatically rejected.</span>
      </div>

    </div>
  );
}
