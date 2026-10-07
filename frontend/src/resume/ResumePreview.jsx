import React from 'react';
import { User, Mail, Phone, MapPin, GraduationCap, Briefcase, Code } from 'lucide-react';
import SkillBadge from '../components/SkillBadge.jsx';

export default function ResumePreview({ resumeData }) {
  if (!resumeData) return null;

  const { candidate, education, experience, skills } = resumeData;

  return (
    <div
      id="resume-preview-panel"
      className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs space-y-6"
    >
      {/* Header / Personal Info */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-5 border-b border-[#F1F5F9] gap-4">
        <div>
          <span className="text-[10px] font-bold tracking-wider uppercase text-[#98A2B3] block mb-1">
            Personal Information
          </span>
          <h3 className="text-xl font-bold text-[#263247] flex items-center gap-2">
            <User className="w-5 h-5 text-[#6B7FD7]" />
            {candidate?.name || 'Candidate Name'}
          </h3>
        </div>

        <div className="flex flex-wrap gap-3 text-xs text-[#667085]">
          {candidate?.email && (
            <span className="flex items-center gap-1.5 bg-[#F8FAFC] px-2.5 py-1 rounded-md border border-[#E2E8F0]">
              <Mail className="w-3.5 h-3.5 text-[#6B7FD7]" /> {candidate.email}
            </span>
          )}
          {candidate?.phone && (
            <span className="flex items-center gap-1.5 bg-[#F8FAFC] px-2.5 py-1 rounded-md border border-[#E2E8F0]">
              <Phone className="w-3.5 h-3.5 text-[#6B7FD7]" /> {candidate.phone}
            </span>
          )}
          {candidate?.location && (
            <span className="flex items-center gap-1.5 bg-[#F8FAFC] px-2.5 py-1 rounded-md border border-[#E2E8F0]">
              <MapPin className="w-3.5 h-3.5 text-[#6B7FD7]" /> {candidate.location}
            </span>
          )}
        </div>
      </div>

      {/* Education */}
      <div>
        <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
          <GraduationCap className="w-4 h-4 text-[#6B7FD7]" /> Education
        </h4>
        <div className="space-y-2">
          {education?.map((item, idx) => (
            <div
              key={idx}
              className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl p-3 text-xs flex justify-between items-center"
            >
              <div>
                <p className="font-bold text-[#263247]">{item.degree}</p>
                <p className="text-[#64748B]">{item.institution}</p>
              </div>
              {item.year && (
                <span className="text-[11px] font-semibold text-[#94A3B8] bg-white px-2 py-0.5 rounded border border-[#CBD5E1]">
                  {item.year}
                </span>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Experience */}
      <div>
        <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
          <Briefcase className="w-4 h-4 text-[#6B7FD7]" /> Experience
        </h4>
        <div className="space-y-2.5">
          {experience?.map((exp, idx) => (
            <div
              key={idx}
              className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-xl p-3.5 text-xs space-y-1"
            >
              <div className="flex justify-between items-center">
                <span className="font-bold text-[#263247]">{exp.role}</span>
                <span className="text-[11px] font-medium text-[#6B7FD7] bg-[#EEF1FF] px-2 py-0.5 rounded-md">
                  {exp.duration}
                </span>
              </div>
              <p className="text-[#64748B] font-medium">{exp.company}</p>
              {exp.description && (
                <p className="text-[#475569] leading-relaxed pt-1">{exp.description}</p>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Skills */}
      <div>
        <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
          <Code className="w-4 h-4 text-[#6B7FD7]" /> Detected Skills ({skills?.length || 0})
        </h4>
        <div className="flex flex-wrap gap-1.5">
          {skills?.map((sk, idx) => (
            <SkillBadge key={idx} skill={sk} type="default" size="sm" />
          ))}
        </div>
      </div>
    </div>
  );
}
