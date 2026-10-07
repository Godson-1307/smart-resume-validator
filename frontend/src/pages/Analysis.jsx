import React from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import { CheckCircle2, Loader2, Circle, Sparkles, Cpu } from 'lucide-react';

export default function Analysis() {
  const { analysisStepIndex, uploadedFile } = useResumeContext();

  const loadingSteps = [
    { label: 'Reading document', desc: 'Parsing binary streams and text structures' },
    { label: 'Detecting resume sections', desc: 'Identifying Education, Experience, and Skills' },
    { label: 'Extracting skills', desc: 'Matching toolchains against industry taxonomy' },
    { label: 'Calculating resume score', desc: 'Running multidimensional ATS rubric' },
    { label: 'Preparing recommendations', desc: 'Generating tailored improvement bullet points' },
  ];

  return (
    <div id="page-analysis-loading" className="max-w-xl mx-auto px-4 py-16 text-center">
      <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8 sm:p-12 shadow-xs space-y-6">
        
        <div className="w-16 h-16 rounded-2xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center mx-auto mb-2 animate-pulse">
          <Cpu className="w-8 h-8" />
        </div>

        <div>
          <span className="text-xs uppercase font-bold tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-3 py-0.5 rounded-full">
            AI Engine Active
          </span>
          <h2 className="text-2xl font-bold text-[#263247] mt-2">
            Analyzing Your Resume
          </h2>
          <p className="text-xs text-[#667085] mt-1">
            {uploadedFile?.name ? `Scanning ${uploadedFile.name}` : 'Deep algorithmic inspection in progress...'}
          </p>
        </div>

        {/* Step-by-step checklist matching Section 10 */}
        <div className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-2xl p-6 text-left space-y-4 my-6">
          {loadingSteps.map((step, idx) => {
            const isCompleted = idx < analysisStepIndex;
            const isCurrent = idx === analysisStepIndex;
            const isPending = idx > analysisStepIndex;

            return (
              <div
                key={idx}
                className={`flex items-start gap-3 transition-opacity duration-300 ${
                  isPending ? 'opacity-40' : 'opacity-100'
                }`}
              >
                <div className="shrink-0 mt-0.5">
                  {isCompleted ? (
                    <CheckCircle2 className="w-5 h-5 text-[#65A98A]" />
                  ) : isCurrent ? (
                    <Loader2 className="w-5 h-5 text-[#6B7FD7] animate-spin" />
                  ) : (
                    <Circle className="w-5 h-5 text-[#CBD5E1]" />
                  )}
                </div>

                <div className="min-w-0">
                  <p className={`text-sm font-semibold ${isCurrent ? 'text-[#6B7FD7]' : isCompleted ? 'text-[#263247]' : 'text-[#94A3B8]'}`}>
                    {step.label}
                  </p>
                  <p className="text-xs text-[#64748B]">
                    {step.desc}
                  </p>
                </div>
              </div>
            );
          })}
        </div>

        <div className="w-full bg-[#E2E8F0] h-2 rounded-full overflow-hidden">
          <div
            className="bg-[#6B7FD7] h-full rounded-full transition-all duration-500"
            style={{ width: `${Math.min(100, (analysisStepIndex / (loadingSteps.length - 1)) * 100)}%` }}
          />
        </div>

        <p className="text-[11px] text-[#98A2B3]">
          Please wait while the system completes natural language evaluation.
        </p>

      </div>
    </div>
  );
}
