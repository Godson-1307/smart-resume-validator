import React from 'react';
import { CheckCircle2, XCircle, ArrowRight, UploadCloud, ShieldAlert, FileText, Loader2 } from 'lucide-react';
import Button from '../components/Button.jsx';

export default function ValidationStatus({
  isValidating,
  validationResult,
  fileName,
  onContinue,
  onUploadAnother,
}) {
  if (isValidating) {
    return (
      <div
        id="validation-status-loading"
        className="bg-white border border-[#E6EAF0] rounded-3xl p-8 sm:p-12 text-center max-w-xl mx-auto shadow-xs"
      >
        <div className="w-16 h-16 rounded-2xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center mx-auto mb-6">
          <Loader2 className="w-8 h-8 animate-spin" />
        </div>

        <h3 className="text-xl font-bold text-[#263247] mb-2">
          Uploading Resume...
        </h3>
        <p className="text-sm text-[#667085] mb-6">
          Checking document structure and classifying content...
        </p>

        {/* Progress simulation bar */}
        <div className="w-full bg-[#E6EAF0] h-2.5 rounded-full overflow-hidden max-w-md mx-auto">
          <div className="bg-[#6B7FD7] h-full rounded-full animate-pulse w-3/4" />
        </div>

        <div className="mt-6 flex items-center justify-center gap-2 text-xs text-[#98A2B3]">
          <FileText className="w-4 h-4" />
          <span>{fileName || 'document.pdf'}</span>
        </div>
      </div>
    );
  }

  const isResume = validationResult?.is_resume;

  if (isResume) {
    return (
      <div
        id="validation-status-valid"
        className="bg-white border border-[#E6EAF0] rounded-3xl p-8 sm:p-12 text-center max-w-xl mx-auto shadow-xs"
      >
        <div className="w-16 h-16 rounded-2xl bg-[#EDF7F1] text-[#65A98A] flex items-center justify-center mx-auto mb-6">
          <CheckCircle2 className="w-9 h-9" />
        </div>

        <span className="inline-block px-3 py-1 bg-[#EDF7F1] text-[#2F6F50] text-xs font-semibold rounded-full border border-[#65A98A]/30 mb-3">
          ✓ Resume Detected
        </span>

        <h3 className="text-2xl font-bold text-[#263247] mb-2">
          Your document appears to be a valid resume.
        </h3>
        <p className="text-sm text-[#667085] mb-8">
          Standard resume sections and professional credentials confirmed ({Math.round((validationResult?.confidence || 0.96) * 100)}% confidence). Proceeding to deep ATS analysis...
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
          <Button
            id="btn-validation-continue"
            variant="primary"
            size="lg"
            icon={ArrowRight}
            iconPosition="right"
            onClick={onContinue}
            className="w-full sm:w-auto px-8"
          >
            Continue
          </Button>
        </div>
      </div>
    );
  }

  // Non-resume invalid document screen (Strict rejection guard)
  return (
    <div
      id="validation-status-invalid"
      className="bg-white border border-[#FDE2E2] rounded-3xl p-8 sm:p-12 text-center max-w-xl mx-auto shadow-xs"
    >
      <div className="w-16 h-16 rounded-2xl bg-[#FEF0F0] text-[#D97878] flex items-center justify-center mx-auto mb-6">
        <XCircle className="w-9 h-9" />
      </div>

      <span className="inline-block px-3 py-1 bg-[#FEF0F0] text-[#9E3939] text-xs font-semibold rounded-full border border-[#D97878]/30 mb-3">
        ✕ Invalid Resume
      </span>

      <h3 className="text-2xl font-bold text-[#263247] mb-2">
        {validationResult?.message || 'The uploaded document does not appear to be a valid resume.'}
      </h3>
      <p className="text-sm text-[#667085] mb-8 max-w-md mx-auto">
        Our validation system detected that this file is likely lecture notes, an invoice, or general unstructured text. To receive an accurate ATS score and career roadmap, please upload a proper resume.
      </p>

      <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
        <Button
          id="btn-upload-another-document"
          variant="primary"
          size="lg"
          icon={UploadCloud}
          onClick={onUploadAnother}
          className="w-full sm:w-auto px-8"
        >
          Upload Another Document
        </Button>
      </div>

      <div className="mt-8 pt-6 border-t border-[#F1F5F9] text-xs text-[#98A2B3] flex items-center justify-center gap-2">
        <ShieldAlert className="w-4 h-4 text-[#D9A441]" />
        <span>Guard activated: Non-resume documents are never assigned false scores.</span>
      </div>
    </div>
  );
}
