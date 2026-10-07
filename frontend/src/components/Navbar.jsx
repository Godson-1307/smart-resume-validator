import React from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import { Sparkles, FileText, Compass, RotateCcw, Award } from 'lucide-react';
import Button from './Button.jsx';

export default function Navbar() {
  const { currentPage, navigateTo, resumeAnalysis, careerAnalysis, resetSession } = useResumeContext();

  return (
    <header id="app-navbar" className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-[#E6EAF0]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand Logo */}
        <div
          id="nav-logo"
          onClick={() => navigateTo('home')}
          className="flex items-center gap-2.5 cursor-pointer select-none group"
        >
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-[#6B7FD7] to-[#9B8AFB] flex items-center justify-center text-white shadow-xs group-hover:scale-105 transition-transform duration-200">
            <Sparkles className="w-5 h-5" />
          </div>
          <div>
            <span className="font-bold text-lg text-[#263247] tracking-tight flex items-center gap-1.5">
              ResumeValidator
              <span className="text-[10px] uppercase font-semibold bg-[#EEF1FF] text-[#6B7FD7] px-1.5 py-0.5 rounded-md tracking-wider">
                Smart AI
              </span>
            </span>
          </div>
        </div>

        {/* Primary Links */}
        <nav id="nav-links" className="hidden md:flex items-center gap-1 text-sm font-medium text-[#667085]">
          <button
            id="nav-link-home"
            onClick={() => navigateTo('home')}
            className={`px-3.5 py-2 rounded-lg transition-colors cursor-pointer ${
              currentPage === 'home'
                ? 'text-[#6B7FD7] bg-[#EEF1FF] font-semibold'
                : 'hover:text-[#263247] hover:bg-[#F1F5F9]'
            }`}
          >
            Home
          </button>

          <button
            id="nav-link-upload"
            onClick={() => navigateTo('upload')}
            className={`px-3.5 py-2 rounded-lg transition-colors cursor-pointer ${
              currentPage === 'upload' || currentPage === 'validation' || currentPage === 'analysis'
                ? 'text-[#6B7FD7] bg-[#EEF1FF] font-semibold'
                : 'hover:text-[#263247] hover:bg-[#F1F5F9]'
            }`}
          >
            Analyze Resume
          </button>

          {resumeAnalysis && (
            <button
              id="nav-link-dashboard"
              onClick={() => navigateTo('dashboard')}
              className={`px-3.5 py-2 rounded-lg transition-colors flex items-center gap-1.5 cursor-pointer ${
                currentPage === 'dashboard'
                  ? 'text-[#6B7FD7] bg-[#EEF1FF] font-semibold'
                  : 'hover:text-[#263247] hover:bg-[#F1F5F9]'
              }`}
            >
              <FileText className="w-4 h-4 text-[#6B7FD7]" />
              Dashboard
            </button>
          )}

          {resumeAnalysis && (
            <button
              id="nav-link-career"
              onClick={() => navigateTo(careerAnalysis ? 'career-analysis' : 'career-goals')}
              className={`px-3.5 py-2 rounded-lg transition-colors flex items-center gap-1.5 cursor-pointer ${
                currentPage === 'career-goals' || currentPage === 'career-analysis'
                  ? 'text-[#6B7FD7] bg-[#EEF1FF] font-semibold'
                  : 'hover:text-[#263247] hover:bg-[#F1F5F9]'
              }`}
            >
              <Compass className="w-4 h-4 text-[#9B8AFB]" />
              Career Analysis
            </button>
          )}

          <a
            id="nav-link-howitworks"
            href="#how-it-works"
            onClick={(e) => {
              if (currentPage !== 'home') {
                e.preventDefault();
                navigateTo('home');
                setTimeout(() => {
                  document.getElementById('how-it-works')?.scrollIntoView({ behavior: 'smooth' });
                }, 100);
              }
            }}
            className="px-3.5 py-2 rounded-lg hover:text-[#263247] hover:bg-[#F1F5F9] transition-colors"
          >
            How It Works
          </a>

          <a
            id="nav-link-about"
            href="#about-section"
            onClick={(e) => {
              if (currentPage !== 'home') {
                e.preventDefault();
                navigateTo('home');
                setTimeout(() => {
                  document.getElementById('about-section')?.scrollIntoView({ behavior: 'smooth' });
                }, 100);
              }
            }}
            className="px-3.5 py-2 rounded-lg hover:text-[#263247] hover:bg-[#F1F5F9] transition-colors"
          >
            About
          </a>
        </nav>

        {/* Right Action */}
        <div className="flex items-center gap-3">
          {resumeAnalysis && (
            <Button
              id="nav-btn-reset"
              variant="outline"
              size="sm"
              icon={RotateCcw}
              onClick={resetSession}
              className="text-xs"
            >
              New Scan
            </Button>
          )}

          <Button
            id="nav-cta-analyze"
            variant="primary"
            size="sm"
            onClick={() => navigateTo('upload')}
          >
            Analyze Resume
          </Button>
        </div>
      </div>
    </header>
  );
}
