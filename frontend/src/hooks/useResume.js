import { useState } from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import { uploadResume, validateResume, analyzeResume } from '../services/resumeApi.js';
import { validateSelectedFile } from '../utils/validation.js';

export function useResume() {
  const context = useResumeContext();
  const [uploadProgress, setUploadProgress] = useState(0);

  const handleFileUpload = async (file) => {
    context.setError(null);

    // 1. Basic frontend file validation (size, extension)
    const clientValidation = validateSelectedFile(file);
    if (!clientValidation.isValid) {
      context.setError(clientValidation.error);
      return false;
    }

    try {
      context.setIsValidating(true);
      context.setUploadedFile({
        name: file.name,
        size: file.size,
        type: file.type,
      });
      context.navigateTo('validation');

      // 2. Upload to server
      const uploadRes = await uploadResume(file);
      const rId = uploadRes.resume_id || 'res_' + Date.now();
      context.setResumeId(rId);

      // 3. Document classification & resume validation
      const valResult = await validateResume(rId, {
        filename: file.name,
        mockInvalid: uploadRes.mockInvalid,
      });

      context.setValidationResult(valResult);
      context.setIsValidating(false);

      return valResult.is_resume;
    } catch (err) {
      context.setIsValidating(false);
      context.setError(err.message || 'Unable to process document. Please try again.');
      return false;
    }
  };

  const startAnalysis = async () => {
    if (!context.resumeId) return;

    try {
      context.setIsAnalyzing(true);
      context.navigateTo('analysis');
      context.setAnalysisStepIndex(0);

      // Progress through visual loading steps as specified in Section 10
      const stepsInterval = setInterval(() => {
        context.setAnalysisStepIndex((prev) => (prev < 4 ? prev + 1 : prev));
      }, 500);

      const analysisData = await analyzeResume(context.resumeId, {
        filename: context.uploadedFile?.name,
      });

      clearInterval(stepsInterval);
      context.setResumeAnalysis(analysisData);

      // Pre-fill existing skills for Career Goals section
      if (analysisData.skills && analysisData.skills.length > 0) {
        context.updateCareerAnswer('existing_skills', analysisData.skills);
      }

      context.setIsAnalyzing(false);
      context.navigateTo('dashboard');
    } catch (err) {
      context.setIsAnalyzing(false);
      context.setError(err.message || 'Unable to analyze your resume. Please try again.');
      context.navigateTo('upload');
    }
  };

  return {
    ...context,
    uploadProgress,
    handleFileUpload,
    startAnalysis,
  };
}
