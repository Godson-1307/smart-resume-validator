import React from 'react';
import { Sparkles, ShieldCheck, Cpu } from 'lucide-react';

export default function Footer() {
  return (
    <footer id="app-footer" className="bg-white border-t border-[#E6EAF0] py-12 mt-20 text-[#667085] text-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
          
          {/* Brand Info */}
          <div className="md:col-span-2 space-y-3">
            <div className="flex items-center gap-2">
              <div className="w-7 h-7 rounded-lg bg-[#6B7FD7] flex items-center justify-center text-white">
                <Sparkles className="w-4 h-4" />
              </div>
              <span className="font-bold text-base text-[#263247]">Smart Resume Validator</span>
            </div>
            <p className="text-[#667085] text-sm max-w-md leading-relaxed">
              An intelligent resume classification and career roadmap platform. Validates genuine resume documents, scores ATS compatibility, identifies experience gaps, and builds target role roadmaps.
            </p>
            <div className="flex items-center gap-4 text-xs text-[#98A2B3] pt-2">
              <span className="flex items-center gap-1">
                <ShieldCheck className="w-3.5 h-3.5 text-[#65A98A]" /> Strictly validates genuine resumes
              </span>
              <span className="flex items-center gap-1">
                <Cpu className="w-3.5 h-3.5 text-[#6B7FD7]" /> AI Career Mapping Engine
              </span>
            </div>
          </div>

          {/* Workflow Steps */}
          <div>
            <h4 className="font-semibold text-[#263247] text-xs uppercase tracking-wider mb-3">Validation Flow</h4>
            <ul className="space-y-2 text-xs">
              <li>1. Document Classification</li>
              <li>2. Non-Resume Rejection Guard</li>
              <li>3. Deep ATS Breakdown</li>
              <li>4. Strengths & Weaknesses</li>
              <li>5. Career Gap Assessment</li>
            </ul>
          </div>

          {/* Supported Formats */}
          <div>
            <h4 className="font-semibold text-[#263247] text-xs uppercase tracking-wider mb-3">Specifications</h4>
            <ul className="space-y-2 text-xs">
              <li>Supported: PDF, DOCX, DOC</li>
              <li>Max File Size: 10 MB</li>
              <li>Strict Anti-Random Guard</li>
              <li>6-Month Career Roadmaps</li>
              <li>Package (LPA) Gap Analysis</li>
            </ul>
          </div>
        </div>

        <div className="pt-6 border-t border-[#E6EAF0] flex flex-col sm:flex-row items-center justify-between text-xs text-[#98A2B3]">
          <p>© {new Date().getFullYear()} Smart Resume Validator. Built according to Frontend Specification.</p>
          <p className="mt-2 sm:mt-0">Light, subtle & chill design system</p>
        </div>
      </div>
    </footer>
  );
}
