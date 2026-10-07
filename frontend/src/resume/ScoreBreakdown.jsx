import React from 'react';
import ProgressBar from '../components/ProgressBar.jsx';
import { Award, Briefcase, GraduationCap, Code2, Layout, FileSearch, Sparkles, CheckCheck } from 'lucide-react';

export default function ScoreBreakdown({ categories = {} }) {
  const defaultCategories = {
    ats_compatibility: 82,
    skills: 75,
    experience: 80,
    education: 90,
    projects: 72,
    formatting: 76,
    keyword_match: 74,
    achievements: 68,
    ...categories,
  };

  const metricDefs = [
    {
      key: 'ats_compatibility',
      label: 'ATS Compatibility',
      icon: CheckCheck,
      color: '#65A98A',
      desc: 'Machine readability & parseability',
    },
    {
      key: 'education',
      label: 'Education',
      icon: GraduationCap,
      color: '#6B7FD7',
      desc: 'Degree relevance & institutional standing',
    },
    {
      key: 'experience',
      label: 'Experience',
      icon: Briefcase,
      color: '#6B7FD7',
      desc: 'Role context & demonstrated progression',
    },
    {
      key: 'formatting',
      label: 'Formatting',
      icon: Layout,
      color: '#9B8AFB',
      desc: 'Typography hierarchy & margin balance',
    },
    {
      key: 'skills',
      label: 'Skills',
      icon: Code2,
      color: '#6B7FD7',
      desc: 'Tooling density & domain coverage',
    },
    {
      key: 'keyword_match',
      label: 'Keyword Match',
      icon: FileSearch,
      color: '#9B8AFB',
      desc: 'Industry standard terminology alignment',
    },
    {
      key: 'projects',
      label: 'Projects',
      icon: Sparkles,
      color: '#D9A441',
      desc: 'Technical complexity & live deployments',
    },
    {
      key: 'achievements',
      label: 'Achievements',
      icon: Award,
      color: '#D9A441',
      desc: 'Measurable metric outcomes & KPI impact',
    },
  ];

  return (
    <div id="score-breakdown-section" className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
      <div className="flex items-center justify-between mb-6 pb-4 border-b border-[#F1F5F9]">
        <div>
          <h3 className="text-base font-bold text-[#263247]">Score Categories</h3>
          <p className="text-xs text-[#667085]">Comprehensive breakdown across 8 critical screening parameters</p>
        </div>
        <span className="text-xs font-semibold text-[#6B7FD7] bg-[#EEF1FF] px-2.5 py-1 rounded-lg">
          8 Evaluated Metrics
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {metricDefs.map((metric) => {
          const val = defaultCategories[metric.key] ?? 70;
          const Icon = metric.icon;

          return (
            <div
              key={metric.key}
              className="p-3.5 rounded-xl border border-[#E2E8F0] hover:border-[#CBD5E1] bg-[#F8FAFC]/50 transition-colors"
            >
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                  <div className="w-7 h-7 rounded-lg bg-white border border-[#E2E8F0] flex items-center justify-center text-[#6B7FD7]">
                    <Icon className="w-3.5 h-3.5" />
                  </div>
                  <div>
                    <h4 className="text-xs font-bold text-[#263247]">{metric.label}</h4>
                    <p className="text-[10px] text-[#94A3B8]">{metric.desc}</p>
                  </div>
                </div>

                <div className="text-right">
                  <span className="text-sm font-extrabold text-[#263247]">{val}</span>
                  <span className="text-[10px] text-[#94A3B8]">/100</span>
                </div>
              </div>

              <ProgressBar value={val} color={metric.color} height="h-2" />
            </div>
          );
        })}
      </div>
    </div>
  );
}
