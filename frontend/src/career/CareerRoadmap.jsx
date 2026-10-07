import React from 'react';
import { Calendar, CheckCircle2, Flag, ArrowRight, BookOpen, Layers } from 'lucide-react';

export default function CareerRoadmap({ roadmap = [] }) {
  const defaultRoadmap = [
    {
      month: 1,
      title: 'Deep Learning Fundamentals',
      focus: 'Neural network architectures, loss optimization, backprop',
      deliverable: 'Baseline model implementations on benchmark vision dataset',
    },
    {
      month: 2,
      title: 'PyTorch + Advanced ML',
      focus: 'Custom dataset loaders, regularization, TorchVision pipelines',
      deliverable: 'Performance benchmark comparison script and documentation',
    },
    {
      month: 3,
      title: 'Model Deployment',
      focus: 'FastAPI serving, ONNX runtime, Docker containerization',
      deliverable: 'REST API service with Swagger specs and Dockerfile',
    },
    {
      month: 4,
      title: 'Docker + Cloud',
      focus: 'Cloud registry, automated CI/CD builds, secrets management',
      deliverable: 'Continuous integration workflow triggered on PR merges',
    },
    {
      month: 5,
      title: 'Build Production Project',
      focus: 'Full-stack application integrating live inferences and metrics',
      deliverable: 'Production deployed URL with comprehensive project README',
    },
    {
      month: 6,
      title: 'Resume + Interview Preparation',
      focus: 'Quantified metric achievements, LeetCode, system design',
      deliverable: 'Polished role-targeted resume and active interview scheduling',
    },
  ];

  const items = roadmap.length > 0 ? roadmap : defaultRoadmap;

  return (
    <div id="career-roadmap-section" className="bg-white border border-[#E6EAF0] rounded-2xl p-6 sm:p-8 shadow-xs">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-8 pb-4 border-b border-[#F1F5F9]">
        <div>
          <span className="text-[10px] uppercase font-bold tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-2.5 py-0.5 rounded-md">
            Career Action Plan
          </span>
          <h3 className="text-xl font-bold text-[#263247] mt-1">Your 6-Month Career Roadmap</h3>
          <p className="text-xs text-[#667085]">A structured, milestone-driven progression to reach your target role</p>
        </div>
        <div className="flex items-center gap-2 text-xs font-semibold text-[#6B7FD7] bg-[#EEF1FF] px-3 py-1.5 rounded-xl self-start sm:self-auto">
          <Calendar className="w-4 h-4" />
          <span>6 Months Horizon</span>
        </div>
      </div>

      {/* Timeline view */}
      <div className="relative border-l-2 border-[#E2E8F0] ml-3 sm:ml-6 pl-6 sm:pl-8 space-y-8">
        {items.map((milestone, idx) => (
          <div key={idx} className="relative group">
            {/* Circle Node */}
            <div className="absolute -left-[31px] sm:-left-[39px] top-0 w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-white border-2 border-[#6B7FD7] flex items-center justify-center text-[#6B7FD7] font-bold text-xs shadow-xs group-hover:scale-110 group-hover:bg-[#6B7FD7] group-hover:text-white transition-all">
              {milestone.month}
            </div>

            {/* Content card */}
            <div className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl p-4 sm:p-5 hover:border-[#6B7FD7]/40 hover:bg-white transition-all shadow-xs">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1 mb-2">
                <span className="text-[11px] font-bold uppercase tracking-wider text-[#6B7FD7]">
                  Month {milestone.month}
                </span>
                <span className="text-[11px] text-[#94A3B8] font-medium flex items-center gap-1">
                  <Flag className="w-3 h-3 text-[#D9A441]" /> Milestone Target
                </span>
              </div>

              <h4 className="text-base font-bold text-[#263247] mb-1.5">
                {milestone.title}
              </h4>

              <p className="text-xs sm:text-sm text-[#475569] leading-relaxed mb-3">
                {milestone.focus}
              </p>

              {milestone.deliverable && (
                <div className="pt-2.5 border-t border-[#E2E8F0] flex items-start gap-2 text-xs text-[#64748B]">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#65A98A] shrink-0 mt-0.5" />
                  <span>
                    <strong className="text-[#263247]">Deliverable:</strong> {milestone.deliverable}
                  </span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
