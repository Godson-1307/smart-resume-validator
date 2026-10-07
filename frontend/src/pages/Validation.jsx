import React from 'react';
import { useResume } from '../hooks/useResume.js';
import ValidationStatus from '../resume/ValidationStatus.jsx';

export default function Validation() {
  const {
    isValidating,
    validationResult,
    uploadedFile,
    startAnalysis,
    resetSession,
    navigateTo,
  } = useResume();

  const handleContinue = () => {
    startAnalysis();
  };

  const handleUploadAnother = () => {
    resetSession();
    navigateTo('upload');
  };

  return (
    <div id="page-validation" className="max-w-2xl mx-auto px-4 py-12 sm:py-16">
      <ValidationStatus
        isValidating={isValidating}
        validationResult={validationResult}
        fileName={uploadedFile?.name}
        onContinue={handleContinue}
        onUploadAnother={handleUploadAnother}
      />
    </div>
  );
}
