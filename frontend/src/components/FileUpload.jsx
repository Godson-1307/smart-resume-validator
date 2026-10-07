import React, { useRef, useState } from 'react';
import { UploadCloud, FileText, CheckCircle, X, AlertCircle } from 'lucide-react';
import Button from './Button.jsx';
import { formatFileSize, validateSelectedFile } from '../utils/validation.js';

export default function FileUpload({
  id = 'file-upload-box',
  onFileSelected,
  selectedFile,
  onRemoveFile,
  onAnalyze,
  isLoading = false,
  error = null,
}) {
  const [isDragOver, setIsDragOver] = useState(false);
  const fileInputRef = useRef(null);

  const handleDragEnter = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(false);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (!isDragOver) setIsDragOver(true);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragOver(false);

    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      const file = e.dataTransfer.files[0];
      onFileSelected(file);
    }
  };

  const handleManualSelect = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      onFileSelected(file);
    }
  };

  return (
    <div id={id} className="w-full space-y-6">
      
      {/* Upload Zone */}
      {!selectedFile ? (
        <div
          onDragEnter={handleDragEnter}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-3xl p-8 sm:p-12 text-center cursor-pointer transition-all duration-200 ${
            isDragOver
              ? 'border-[#6B7FD7] bg-[#EEF1FF]/60 scale-[1.01]'
              : 'border-[#CBD5E1] bg-white hover:border-[#6B7FD7]/60 hover:bg-[#F8FAFC]'
          }`}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleManualSelect}
            className="hidden"
            id="file-input-hidden"
          />

          <div className="w-16 h-16 rounded-2xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center mx-auto mb-4 transition-transform group-hover:scale-105">
            <UploadCloud className="w-8 h-8" />
          </div>

          <h3 className="text-lg font-bold text-[#263247] mb-1">
            Upload Your Resume
          </h3>
          <p className="text-sm text-[#667085] mb-4">
            Drag & Drop your resume here
          </p>

          <div className="flex items-center justify-center gap-3 my-4">
            <div className="h-px bg-[#E2E8F0] w-16"></div>
            <span className="text-xs uppercase font-semibold text-[#98A2B3]">OR</span>
            <div className="h-px bg-[#E2E8F0] w-16"></div>
          </div>

          <Button
            id="btn-browse-files"
            variant="secondary"
            size="md"
            onClick={(e) => {
              e.stopPropagation();
              fileInputRef.current?.click();
            }}
          >
            Browse Files
          </Button>

          <div className="mt-6 pt-6 border-t border-[#F1F5F9] text-xs text-[#98A2B3] flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-6">
            <span>Supported formats: <strong className="text-[#64748B]">PDF, DOCX, DOC</strong></span>
            <span className="hidden sm:inline">•</span>
            <span>Maximum file size: <strong className="text-[#64748B]">10 MB</strong></span>
          </div>
        </div>
      ) : (
        /* Selected File Card */
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
          <div className="flex items-start justify-between gap-4">
            <div className="flex items-center gap-3.5 min-w-0">
              <div className="w-12 h-12 rounded-xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center shrink-0">
                <FileText className="w-6 h-6" />
              </div>
              <div className="min-w-0">
                <h4 className="font-bold text-[#263247] text-base truncate">
                  {selectedFile.name}
                </h4>
                <div className="flex items-center gap-2 mt-0.5 text-xs text-[#667085]">
                  <span>{formatFileSize(selectedFile.size || 0)}</span>
                  <span>•</span>
                  <span className="flex items-center gap-1 text-[#65A98A] font-medium">
                    <CheckCircle className="w-3.5 h-3.5" /> File selected
                  </span>
                </div>
              </div>
            </div>

            <button
              id="btn-remove-selected-file"
              type="button"
              onClick={onRemoveFile}
              disabled={isLoading}
              className="text-[#98A2B3] hover:text-[#D97878] p-1 rounded-lg hover:bg-[#FEF0F0] transition-colors cursor-pointer"
              title="Remove file"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          <div className="mt-6 pt-5 border-t border-[#F1F5F9] flex flex-col sm:flex-row items-center justify-between gap-3">
            <Button
              id="btn-remove-action"
              variant="outline"
              size="sm"
              onClick={onRemoveFile}
              disabled={isLoading}
              className="w-full sm:w-auto"
            >
              Remove
            </Button>

            <Button
              id="btn-analyze-resume-submit"
              variant="primary"
              size="md"
              onClick={onAnalyze}
              disabled={isLoading}
              className="w-full sm:w-auto font-semibold px-6"
            >
              Analyze Resume
            </Button>
          </div>
        </div>
      )}

      {/* Error Notice */}
      {error && (
        <div className="bg-[#FEF0F0] border border-[#D97878]/30 rounded-2xl p-4 text-xs text-[#9E3939] flex items-start gap-2.5">
          <AlertCircle className="w-4 h-4 shrink-0 text-[#D97878] mt-0.5" />
          <span>{error}</span>
        </div>
      )}



    </div>
  );
}
