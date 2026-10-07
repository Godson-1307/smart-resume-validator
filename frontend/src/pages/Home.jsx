import React from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import Button from '../components/Button.jsx';
import ScoreCard from '../components/ScoreCard.jsx';
import {
  Sparkles,
  ArrowRight,
  ShieldCheck,
  Award,
  TrendingUp,
  Target,
  FileCheck2,
  Cpu,
  CheckCircle2,
  FileText,
  Compass,
  Zap,
} from 'lucide-react';

export default function Home() {
  const { navigateTo, resetSession } = useResumeContext();

  const handleGetStarted = () => {
    resetSession();
    navigateTo('upload');
  };

  const featureCards = [
    {
      icon: ShieldCheck,
      title: 'Resume Validation',
      desc: 'Deep structural document classification. Strictly rejects non-resume files before false scoring begins.',
      color: 'text-[#65A98A]',
      bg: 'bg-[#EDF7F1]',
    },
    {
      icon: Award,
      title: 'ATS / Resume Score',
      desc: 'Multidimensional 8-metric benchmark evaluating keyword density, formatting, and measurable achievements.',
      color: 'text-[#6B7FD7]',
      bg: 'bg-[#EEF1FF]',
    },
    {
      icon: TrendingUp,
      title: 'Resume Improvement',
      desc: 'Direct actionable rewrites replacing passive project notes with quantified result-oriented bullet points.',
      color: 'text-[#9B8AFB]',
      bg: 'bg-[#F3F0FF]',
    },
    {
      icon: Target,
      title: 'Career Goal Analysis',
      desc: 'Aligns your verified skill profile with real-world target roles, location preferences, and expected LPA package.',
      color: 'text-[#D9A441]',
      bg: 'bg-[#FFF7E8]',
    },
    {
      icon: Compass,
      title: 'Personalized Skill Recommendations',
      desc: 'Synthesizes an exact 6-month month-by-month roadmap with deliverables to land your target role.',
      color: 'text-[#6B7FD7]',
      bg: 'bg-[#EEF1FF]',
    },
  ];

  return (
    <div id="page-home" className="space-y-24 py-6 sm:py-12">
      
      {/* Hero Section */}
      <section className="text-center max-w-4xl mx-auto px-4 sm:px-6">
        
        {/* Magic UI Style Announcement Badge (matching reference image) */}
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-[#E6EAF0] shadow-xs text-xs font-medium text-[#263247] mb-8 hover:border-[#6B7FD7]/40 transition-colors">
          <span className="flex items-center justify-center w-5 h-5 rounded-full bg-[#EEF1FF] text-[#6B7FD7] text-[10px]">
            ✨
          </span>
          <span className="font-semibold text-[#6B7FD7]">Announcement</span>
          <span className="text-[#98A2B3]">•</span>
          <span>Introducing Smart Resume Validator</span>
          <ArrowRight className="w-3.5 h-3.5 text-[#98A2B3]" />
        </div>

        {/* Hero Heading (Section 5) */}
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black text-[#263247] tracking-tight leading-[1.15] mb-6">
          Your Resume Shouldn't Just Exist. <br />
          <span className="bg-gradient-to-r from-[#6B7FD7] via-[#8594E6] to-[#9B8AFB] bg-clip-text text-transparent">
            It Should Get You Hired.
          </span>
        </h1>

        {/* Hero Subtitle (Section 5) */}
        <p className="text-base sm:text-lg text-[#667085] max-w-2xl mx-auto leading-relaxed mb-8">
          Upload your resume, validate it, understand its strengths and weaknesses, and get personalized career improvement suggestions based on your target role.
        </p>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3.5">
          <Button
            id="hero-btn-analyze"
            variant="primary"
            size="lg"
            icon={Sparkles}
            onClick={handleGetStarted}
            className="w-full sm:w-auto px-8 shadow-md shadow-[#6B7FD7]/20"
          >
            Analyze My Resume
          </Button>

          <Button
            id="hero-btn-howitworks"
            variant="outline"
            size="lg"
            onClick={() => {
              document.getElementById('how-it-works')?.scrollIntoView({ behavior: 'smooth' });
            }}
            className="w-full sm:w-auto px-8"
          >
            How It Works
          </Button>
        </div>

        <p className="text-xs text-[#98A2B3] mt-3">
          100% Client-Ready Frontend Architecture • Strictly Rejects Non-Resumes
        </p>

        {/* Interactive Hero UI Preview Mockup (matching reference screenshot) */}
        <div className="mt-14 max-w-4xl mx-auto bg-white rounded-3xl border border-[#E6EAF0] shadow-xl overflow-hidden text-left">
          {/* Mockup browser window header */}
          <div className="bg-[#F8FAFC] border-b border-[#E6EAF0] px-4 py-3 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="w-3 h-3 rounded-full bg-[#EF4444]/70"></span>
              <span className="w-3 h-3 rounded-full bg-[#F59E0B]/70"></span>
              <span className="w-3 h-3 rounded-full bg-[#10B981]/70"></span>
              <div className="ml-3 px-3 py-0.5 rounded-md bg-white border border-[#E2E8F0] text-[11px] text-[#94A3B8] font-mono">
                smart-resume-validator.internal/analysis
              </div>
            </div>
            <span className="text-[11px] font-semibold text-[#65A98A] bg-[#EDF7F1] px-2 py-0.5 rounded">
              ● Live Validation Active
            </span>
          </div>

          {/* Mockup internal content */}
          <div className="p-6 sm:p-8 grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
            <div className="flex flex-col items-center justify-center p-4 bg-[#F8FAFC] rounded-2xl border border-[#E2E8F0]">
              <span className="text-[10px] font-bold uppercase tracking-wider text-[#98A2B3] mb-2">Overall Score</span>
              <div className="text-4xl font-black text-[#6B7FD7]">78<span className="text-xs text-[#98A2B3]">/100</span></div>
              <span className="mt-2 text-xs font-semibold px-2.5 py-0.5 rounded-full bg-[#EEF1FF] text-[#4F62BD]">
                Good Foundation
              </span>
            </div>

            <div className="md:col-span-2 space-y-3">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-[#263247]">Candidate: Godson Nadar</span>
                <span className="text-[#65A98A] font-bold">✓ Valid Resume Confirmed</span>
              </div>

              <div className="space-y-1.5 text-xs">
                <div className="flex justify-between text-[#64748B]">
                  <span>ATS Compatibility</span>
                  <span className="font-bold text-[#263247]">82%</span>
                </div>
                <div className="w-full bg-[#E2E8F0] h-2 rounded-full overflow-hidden">
                  <div className="bg-[#65A98A] h-full w-[82%]" />
                </div>
              </div>

              <div className="space-y-1.5 text-xs">
                <div className="flex justify-between text-[#64748B]">
                  <span>Target Role Alignment (ML Engineer)</span>
                  <span className="font-bold text-[#263247]">76%</span>
                </div>
                <div className="w-full bg-[#E2E8F0] h-2 rounded-full overflow-hidden">
                  <div className="bg-[#6B7FD7] h-full w-[76%]" />
                </div>
              </div>

              <div className="pt-2 flex flex-wrap gap-1.5">
                <span className="text-[10px] px-2 py-0.5 rounded bg-[#EDF7F1] text-[#2F6F50] font-medium">Python</span>
                <span className="text-[10px] px-2 py-0.5 rounded bg-[#EDF7F1] text-[#2F6F50] font-medium">Machine Learning</span>
                <span className="text-[10px] px-2 py-0.5 rounded bg-[#FFF7E8] text-[#8F6516] font-medium">→ Need PyTorch</span>
                <span className="text-[10px] px-2 py-0.5 rounded bg-[#F3F0FF] text-[#6C56CE] font-medium">+ Add MLOps</span>
              </div>
            </div>
          </div>
        </div>

      </section>

      {/* Feature Cards Grid (Section 5) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <span className="text-xs uppercase font-bold tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-2.5 py-1 rounded-md">
            Engineered For Placement
          </span>
          <h2 className="text-2xl sm:text-3xl font-extrabold text-[#263247] mt-3">
            More Than Just An ATS Score
          </h2>
          <p className="text-sm text-[#667085] mt-2">
            Most checkers output a vanity number. We analyze your entire career profile against real hiring standards.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {featureCards.map((feat, idx) => {
            const Icon = feat.icon;
            return (
              <div
                key={idx}
                className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs hover:shadow-md hover:border-[#CBD5E1] transition-all"
              >
                <div className={`w-10 h-10 rounded-xl ${feat.bg} ${feat.color} flex items-center justify-center mb-4`}>
                  <Icon className="w-5 h-5" />
                </div>
                <h3 className="text-base font-bold text-[#263247] mb-2 flex items-center gap-1.5">
                  <span className="text-[#65A98A]">✓</span> {feat.title}
                </h3>
                <p className="text-xs sm:text-sm text-[#667085] leading-relaxed">
                  {feat.desc}
                </p>
              </div>
            );
          })}
        </div>
      </section>

      {/* How It Works Section */}
      <section id="how-it-works" className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="bg-white border border-[#E6EAF0] rounded-3xl p-8 sm:p-12 shadow-xs">
          <div className="text-center max-w-xl mx-auto mb-10">
            <span className="text-xs font-bold uppercase tracking-wider text-[#6B7FD7]">
              Step-by-Step Flow
            </span>
            <h3 className="text-2xl font-bold text-[#263247] mt-1">
              How Smart Resume Validator Operates
            </h3>
            <p className="text-xs sm:text-sm text-[#667085] mt-2">
              A closed-loop pipeline preventing invalid document scoring while unlocking precise career roadmaps.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 relative">
            <div className="space-y-2 p-4 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0]">
              <span className="w-7 h-7 rounded-lg bg-[#6B7FD7] text-white text-xs font-bold flex items-center justify-center">1</span>
              <h4 className="font-bold text-sm text-[#263247]">Document Check</h4>
              <p className="text-xs text-[#667085]">
                Upload PDF or DOCX. The backend classifies if it is a genuine resume or random notes.
              </p>
            </div>

            <div className="space-y-2 p-4 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0]">
              <span className="w-7 h-7 rounded-lg bg-[#6B7FD7] text-white text-xs font-bold flex items-center justify-center">2</span>
              <h4 className="font-bold text-sm text-[#263247]">Score & Extract</h4>
              <p className="text-xs text-[#667085]">
                Parse education, work history, verified skills, and strengths into an ATS diagnostic dashboard.
              </p>
            </div>

            <div className="space-y-2 p-4 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0]">
              <span className="w-7 h-7 rounded-lg bg-[#6B7FD7] text-white text-xs font-bold flex items-center justify-center">3</span>
              <h4 className="font-bold text-sm text-[#263247]">Career Goal Match</h4>
              <p className="text-xs text-[#667085]">
                Enter target role, desired LPA compensation, and city to calculate concrete skill gaps.
              </p>
            </div>

            <div className="space-y-2 p-4 rounded-xl bg-[#F8FAFC] border border-[#E2E8F0]">
              <span className="w-7 h-7 rounded-lg bg-[#6B7FD7] text-white text-xs font-bold flex items-center justify-center">4</span>
              <h4 className="font-bold text-sm text-[#263247]">Action Roadmap</h4>
              <p className="text-xs text-[#667085]">
                Follow a 6-month timeline with deliverables to close gaps and pass top-tier job screens.
              </p>
            </div>
          </div>

          <div className="mt-10 pt-8 border-t border-[#F1F5F9] text-center">
            <Button
              variant="primary"
              size="md"
              icon={ArrowRight}
              iconPosition="right"
              onClick={handleGetStarted}
            >
              Start Your Resume Analysis
            </Button>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about-section" className="max-w-4xl mx-auto px-4 sm:px-6 text-center">
        <div className="p-8 sm:p-10 rounded-3xl bg-gradient-to-b from-[#EEF1FF]/60 to-white border border-[#6B7FD7]/20">
          <h3 className="text-xl font-bold text-[#263247] mb-3">
            The Philosophy of Smart Resume Validator
          </h3>
          <p className="text-sm text-[#667085] leading-relaxed max-w-2xl mx-auto mb-6">
            "The final product should feel like: Upload a resume → understand the resume → understand the person's career goal → compare the two → tell the user exactly what to improve. So the core intelligence is not just Resume → Score, but Resume + Current Skills + Experience + Target Role + Package → Personalized Career Analysis."
          </p>
          <div className="flex items-center justify-center gap-6 text-xs text-[#98A2B3]">
            <span>Clean Architecture</span>
            <span>•</span>
            <span>REST API Bridge</span>
            <span>•</span>
            <span>Tailwind v4 Design System</span>
          </div>
        </div>
      </section>

    </div>
  );
}
