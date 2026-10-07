import React, { createContext, useContext, useState } from 'react';

const ResumeContext = createContext(null);

export function ResumeProvider({ children }) {
  const [currentPage, setCurrentPage] = useState('home'); // 'home' | 'upload' | 'validation' | 'analysis' | 'dashboard' | 'career-goals' | 'career-analysis' | 'not-found'
  
  // File & Upload State
  const [resumeId, setResumeId] = useState(null);
  const [uploadedFile, setUploadedFile] = useState(null);
  
  // Validation State
  const [validationResult, setValidationResult] = useState(null);
  const [isValidating, setIsValidating] = useState(false);
  
  // Resume Analysis State
  const [resumeAnalysis, setResumeAnalysis] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisStepIndex, setAnalysisStepIndex] = useState(0);

  // Career Goal & Questionnaire State
  const [careerAnswers, setCareerAnswers] = useState({
    target_role: 'Machine Learning Engineer',
    industry: 'Technology',
    country: 'India',
    city: 'Mumbai',
    work_type: 'Hybrid',
    expected_package: 12,
    experience_level: 'Fresher',
    existing_skills: [],
    custom_role: '',
  });

  // Career Analysis & Roadmap State
  const [careerAnalysis, setCareerAnalysis] = useState(null);
  const [isCareerAnalyzing, setIsCareerAnalyzing] = useState(false);

  // Global Error state
  const [error, setError] = useState(null);

  // Reset entire workflow
  const resetSession = () => {
    setResumeId(null);
    setUploadedFile(null);
    setValidationResult(null);
    setResumeAnalysis(null);
    setCareerAnalysis(null);
    setError(null);
    setAnalysisStepIndex(0);
    setCurrentPage('upload');
  };

  const navigateTo = (pageName) => {
    setError(null);
    setCurrentPage(pageName);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const updateCareerAnswer = (key, value) => {
    setCareerAnswers((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  const value = {
    currentPage,
    setCurrentPage,
    navigateTo,
    resumeId,
    setResumeId,
    uploadedFile,
    setUploadedFile,
    validationResult,
    setValidationResult,
    isValidating,
    setIsValidating,
    resumeAnalysis,
    setResumeAnalysis,
    isAnalyzing,
    setIsAnalyzing,
    analysisStepIndex,
    setAnalysisStepIndex,
    careerAnswers,
    setCareerAnswers,
    updateCareerAnswer,
    careerAnalysis,
    setCareerAnalysis,
    isCareerAnalyzing,
    setIsCareerAnalyzing,
    error,
    setError,
    resetSession,
  };

  return <ResumeContext.Provider value={value}>{children}</ResumeContext.Provider>;
}

export function useResumeContext() {
  const context = useContext(ResumeContext);
  if (!context) {
    throw new Error('useResumeContext must be used within a ResumeProvider');
  }
  return context;
}
