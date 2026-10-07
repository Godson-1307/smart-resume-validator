import React, { useState } from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import CareerGap from '../career/CareerGap.jsx';
import SkillRecommendations from '../career/SkillRecommendations.jsx';
import CareerRoadmap from '../career/CareerRoadmap.jsx';
import Button from '../components/Button.jsx';
import { Compass, Sparkles, ArrowLeft, RotateCcw, FileText, CheckCircle2, ChevronRight, Target, IndianRupee } from 'lucide-react';
import SkillBadge from '../components/SkillBadge.jsx';

export default function CareerAnalysis() {
  const { careerAnalysis, isCareerAnalyzing, resumeAnalysis, navigateTo, resetSession } = useResumeContext();
  const [activeTab, setActiveTab] = useState('summary'); // 'summary' | 'roadmap' | 'gap' | 'roles'

  if (isCareerAnalyzing) {
    return (
      <div id="career-analysis-loading" className="max-w-xl mx-auto px-4 py-20 text-center">
        <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8 sm:p-12 shadow-xs space-y-6">
          <div className="w-16 h-16 rounded-2xl bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center mx-auto animate-spin">
            <Compass className="w-8 h-8" />
          </div>

          <h2 className="text-2xl font-bold text-[#263247]">
            Analyzing Your Career Goal...
          </h2>
          <p className="text-xs text-[#667085] max-w-sm mx-auto">
            Comparing your verified resume profile with target market benchmarks, seniority expectations, and compensation tiers...
          </p>

          <div className="space-y-2 text-xs text-[#64748B] max-w-xs mx-auto text-left pt-4">
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-[#65A98A]" /> Current Profile Extracted
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-[#6B7FD7] animate-pulse" /> Skill & Experience Comparison
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-[#9B8AFB] animate-pulse" /> Generating 6-Month Action Roadmap
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!careerAnalysis) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center">
        <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8">
          <p className="text-[#667085] mb-4">No career analysis found. Please complete the career questionnaire first.</p>
          <Button variant="primary" onClick={() => navigateTo('career-goals')}>
            Go to Career Questionnaire
          </Button>
        </div>
      </div>
    );
  }

  const {
    target_role,
    existing_skills,
    skills_to_improve,
    recommended_skills,
    recommendations,
    roadmap,
    package_analysis,
    matched_roles,
  } = careerAnalysis;

  return (
    <div id="page-career-analysis" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-8">
      
      {/* Top Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white border border-[#E6EAF0] rounded-3xl p-6 sm:p-8 shadow-xs">
        <div>
          <div className="flex items-center gap-2 mb-1.5">
            <span className="text-[10px] uppercase font-bold tracking-wider text-[#9B8AFB] bg-[#F3F0FF] px-2.5 py-0.5 rounded-md border border-[#9B8AFB]/30">
              Career Strategy Activated
            </span>
            <span className="text-xs text-[#98A2B3]">•</span>
            <span className="text-xs text-[#64748B] font-medium">Target: {target_role}</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-[#263247] tracking-tight">
            Personalized Career Architecture
          </h1>
          <p className="text-xs sm:text-sm text-[#667085] mt-1">
            Bridging the gap between your present resume and your {target_role} target.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <Button
            variant="outline"
            size="sm"
            icon={FileText}
            onClick={() => navigateTo('dashboard')}
            className="text-xs"
          >
            View Resume Score
          </Button>

          <Button
            variant="primary"
            size="sm"
            icon={RotateCcw}
            onClick={() => navigateTo('career-goals')}
            className="text-xs"
          >
            Adjust Goals
          </Button>
        </div>
      </div>

      {/* Tabs */}
      <div className="flex items-center gap-2 border-b border-[#E2E8F0] pb-2 text-sm font-medium overflow-x-auto">
        <button
          type="button"
          onClick={() => setActiveTab('summary')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer whitespace-nowrap ${
            activeTab === 'summary'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          Career Dashboard Summary
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('gap')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer whitespace-nowrap ${
            activeTab === 'gap'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          Skill Gap Analysis
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('roadmap')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer whitespace-nowrap ${
            activeTab === 'roadmap'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          6-Month Action Roadmap
        </button>
        <button
          type="button"
          onClick={() => setActiveTab('roles')}
          className={`px-4 py-2 rounded-xl transition-all cursor-pointer whitespace-nowrap ${
            activeTab === 'roles'
              ? 'bg-[#EEF1FF] text-[#6B7FD7] font-bold shadow-xs'
              : 'text-[#64748B] hover:text-[#263247]'
          }`}
        >
          Matched Roles
        </button>
      </div>

      {/* Tab 1: Final Career Dashboard (Section 32) */}
      {activeTab === 'summary' && (
        <div className="space-y-8 animate-fadeIn">
          
          {/* Section 32: Final Career Dashboard Box */}
          <div className="bg-white border border-[#E6EAF0] rounded-3xl p-6 sm:p-8 shadow-xs space-y-6">
            <div className="flex items-center justify-between pb-4 border-b border-[#F1F5F9]">
              <span className="text-xs font-black uppercase tracking-widest text-[#64748B]">
                CAREER PROFILE
              </span>
              <span className="text-xs font-semibold text-[#65A98A] bg-[#EDF7F1] px-2.5 py-0.5 rounded-full">
                Active Assessment
              </span>
            </div>

            {/* Score & Targets */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pb-6 border-b border-[#F1F5F9]">
              <div className="p-4 rounded-2xl bg-[#F8FAFC] border border-[#E2E8F0]">
                <span className="text-[11px] font-bold uppercase text-[#94A3B8] block mb-1">
                  Current Resume Score
                </span>
                <span className="text-2xl font-black text-[#6B7FD7]">
                  {resumeAnalysis?.overall_score || 78}/100
                </span>
              </div>

              <div className="p-4 rounded-2xl bg-[#F8FAFC] border border-[#E2E8F0]">
                <span className="text-[11px] font-bold uppercase text-[#94A3B8] block mb-1">
                  Target Role
                </span>
                <span className="text-lg font-bold text-[#263247] truncate block">
                  {target_role}
                </span>
              </div>

              <div className="p-4 rounded-2xl bg-[#F8FAFC] border border-[#E2E8F0]">
                <span className="text-[11px] font-bold uppercase text-[#94A3B8] block mb-1">
                  Target Package
                </span>
                <span className="text-2xl font-black text-[#263247] flex items-center">
                  ₹{package_analysis?.expected_package || 12} LPA
                </span>
              </div>
            </div>

            {/* Skills & Skills to Improve (Section 32) */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pb-6 border-b border-[#F1F5F9]">
              <div>
                <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2.5">
                  Current Skills
                </h4>
                <div className="flex flex-wrap gap-1.5">
                  {existing_skills.map((sk, idx) => (
                    <SkillBadge key={idx} skill={sk} type="existing" size="sm" />
                  ))}
                </div>
              </div>

              <div>
                <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] mb-2.5">
                  Skills To Improve
                </h4>
                <div className="flex flex-wrap gap-1.5">
                  {skills_to_improve.concat(recommended_skills.slice(0, 2)).map((sk, idx) => (
                    <SkillBadge key={idx} skill={sk} type="improve" size="sm" />
                  ))}
                </div>
              </div>
            </div>

            {/* Recommendations Counts & Links */}
            <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-2">
              <div className="flex items-center gap-6 text-xs text-[#64748B]">
                <div>
                  <span className="font-bold text-[#263247]">{resumeAnalysis?.recommendations?.length || 8}</span> resume recommendations
                </div>
                <div>
                  <span className="font-bold text-[#263247]">{recommendations.length}</span> career strategy steps
                </div>
              </div>

              <div className="flex items-center gap-3 w-full sm:w-auto">
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => navigateTo('dashboard')}
                  className="w-full sm:w-auto text-xs"
                >
                  View Resume Analysis
                </Button>
                <Button
                  variant="primary"
                  size="sm"
                  onClick={() => setActiveTab('roadmap')}
                  className="w-full sm:w-auto text-xs font-bold"
                >
                  View Career Roadmap
                </Button>
              </div>
            </div>
          </div>

          {/* Quick preview of Gap & Recommendations */}
          <CareerGap
            targetRole={target_role}
            alreadyHave={existing_skills}
            needToImprove={skills_to_improve}
            missingRecommended={recommended_skills}
            packageAnalysis={package_analysis}
          />

          <SkillRecommendations
            targetRole={target_role}
            recommendations={recommendations}
            matchedRoles={matched_roles}
          />

          <CareerRoadmap roadmap={roadmap} />
        </div>
      )}

      {/* Tab 2: Skill Gap */}
      {activeTab === 'gap' && (
        <div className="space-y-6 animate-fadeIn">
          <CareerGap
            targetRole={target_role}
            alreadyHave={existing_skills}
            needToImprove={skills_to_improve}
            missingRecommended={recommended_skills}
            packageAnalysis={package_analysis}
          />

          <SkillRecommendations
            targetRole={target_role}
            recommendations={recommendations}
            matchedRoles={matched_roles}
          />
        </div>
      )}

      {/* Tab 3: Roadmap */}
      {activeTab === 'roadmap' && (
        <div className="space-y-6 animate-fadeIn">
          <CareerRoadmap roadmap={roadmap} />
        </div>
      )}

      {/* Tab 4: Matched Roles */}
      {activeTab === 'roles' && (
        <div className="space-y-6 animate-fadeIn">
          <SkillRecommendations
            targetRole={target_role}
            recommendations={recommendations}
            matchedRoles={matched_roles}
          />
        </div>
      )}

    </div>
  );
}
