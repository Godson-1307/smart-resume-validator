import React, { useState } from 'react';
import FileUpload from '../components/FileUpload.jsx';
import { useResume } from '../hooks/useResume.js';

export default function ResumeUploader({ onUploaded }) {
  const { handleFileUpload, error, setError } = useResume();
  const [selectedFile, setSelectedFile] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);

  const handleFileSelect = (file) => {
    setSelectedFile(file);
    setError(null);
  };

  const handleRemove = () => {
    setSelectedFile(null);
    setError(null);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;

    setIsProcessing(true);

    const success = await handleFileUpload(
      selectedFile
    );

    setIsProcessing(false);

    if (onUploaded) {
      onUploaded(success);
    }
  };

  return (
    <div id="resume-uploader-container" className="w-full">
      <FileUpload
        selectedFile={selectedFile}
        onFileSelected={handleFileSelect}
        onRemoveFile={handleRemove}
        onAnalyze={handleAnalyze}
        isLoading={isProcessing}
        error={error}
      />
    </div>
  );
}
