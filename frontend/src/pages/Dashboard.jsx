import React, { useState } from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import ResumeScore from '../resume/ResumeScore.jsx';
import ScoreBreakdown from '../resume/ScoreBreakdown.jsx';
import ResumeInformation from '../resume/ResumeInformation.jsx';
import ResumeStrengths from '../resume/ResumeStrengths.jsx';
import ResumeWeaknesses from '../resume/ResumeWeaknesses.jsx';
import ImprovementList from '../resume/ImprovementList.jsx';
import Button from '../components/Button.jsx';
import { ArrowRight, Compass, Sparkles, FileText, CheckCircle2, RotateCcw } from 'lucide-react';

export default function Dashboard() {
  const { resumeAnalysis, navigateTo, resetSession } = useResumeContext();
  const [activeTab, setActiveTab] = useState('overview'); // 'overview' | 'information' | 'improvements'

  if (!resumeAnalysis) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center">
        <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8">
          <p className="text-[#667085] mb-4">No resume analysis found. Please upload a resume first.</p>
          <Button variant="primary" onClick={() => navigateTo('upload')}>
            Upload Resume
          </Button>
        </div>
      </div>
    );
  }

  const { overall_score, categories, candidate, education, experience, skills, strengths, weaknesses, recommendations } =
    resumeAnalysis;

  return (
    <div id="page-resume-dashboard" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-8">
      
      {/* Top Banner & Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white border border-[#E6EAF0] rounded-3xl p-6 sm:p-8 shadow-xs">
        <div>
          <div className="flex items-center gap-2 mb-1.5">
            <span className="text-[10px] uppercase font-bold tracking-wider text-[#65A98A] bg-[#EDF7F1] px-2.5 py-0.5 rounded-md border border-[#65A98A]/30">
              ✓ Validated Resume
            </span>
            <span className="text-xs text-[#98A2B3]">•</span>
            <span className="text-xs text-[#64748B] font-medium">{candidate?.name || 'Resume'}</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-[#263247] tracking-tight">
            Resume Analysis Dashboard
          </h1>
          <p className="text-xs sm:text-sm text-[#667085] mt-1">
            Complete ATS diagnostics, category scoring, and actionable rewrites.
          </p>
        </div>

        {/* CTA to Step 2: Career Goal Section */}
        <div className="flex items-center gap-3">
          <Button
            id="btn-dashboard-proceed-career"
            variant="primary"
            size="md"
            icon={Compass}
            iconPosition="right"
            onClick={() => navigateTo('career-goals')}
            className="font-bold px-6 shadow-md shadow-[#6B7FD7]/20"
          >
            Map Career Goals
          </Button>
        </div>
      </div>

      {/* Tabs Navigation */}
      <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2 text-sm font-medium">
        <button
          type="button"
          onClick={() => setActiveTab('overview')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer ${
            activeTab === 'overview'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          Score & Breakdown
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('improvements')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer flex items-center gap-1.5 ${
            activeTab === 'improvements'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          <span>Improvements & Rewrites</span>
          <span className="text-[11px] bg-[#D97878] text-white px-1.5 py-0.2 rounded-full">
            {recommendations?.length || 4}
          </span>
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('information')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer ${
            activeTab === 'information'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          Extracted Data
        </button>
      </div>

      {/* Main Tab: Overview */}
      {activeTab === 'overview' && (
        <div className="space-y-8 animate-fadeIn">
          {/* Top Score & Score Breakdown Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 items-start">
            <div className="lg:col-span-1">
              <ResumeScore score={overall_score} />
            </div>
            <div className="lg:col-span-2">
              <ScoreBreakdown categories={categories} />
            </div>
          </div>

          {/* Strengths & Weaknesses (Section 14 & 15) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <ResumeStrengths strengths={strengths} />
            <ResumeWeaknesses weaknesses={weaknesses} />
          </div>

          {/* Inline Improvement Preview */}
          <ImprovementList recommendations={recommendations} />
        </div>
      )}

      {/* Tab: Improvements */}
      {activeTab === 'improvements' && (
        <div className="space-y-6 animate-fadeIn">
          <ImprovementList recommendations={recommendations} />
        </div>
      )}

      {/* Tab: Extracted Data */}
      {activeTab === 'information' && (
        <div className="space-y-6 animate-fadeIn">
          <ResumeInformation data={resumeAnalysis} />
        </div>
      )}

      {/* Bottom Floating Step 2 Prompt (Section 17) */}
      <div className="bg-gradient-to-r from-[#EEF1FF] to-[#F3F0FF] border border-[#6B7FD7]/30 rounded-3xl p-6 sm:p-8 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div className="space-y-1 text-center sm:text-left">
          <span className="text-xs uppercase font-bold tracking-wider text-[#6B7FD7]">
            Stage 2: Career Alignment
          </span>
          <h3 className="text-xl font-bold text-[#263247]">
            Now Let's Understand Your Career Goal
          </h3>
          <p className="text-xs sm:text-sm text-[#667085] max-w-xl">
            Tell us where you want to go, and we'll compare your current profile with your target role and salary expectations.
          </p>
        </div>

        <Button
          id="btn-bottom-start-career-goal"
          variant="primary"
          size="lg"
          icon={ArrowRight}
          iconPosition="right"
          onClick={() => navigateTo('career-goals')}
          className="shrink-0 px-8"
        >
          Begin Career Questionnaire
        </Button>
      </div>

    </div>
  );
}
