import React from 'react';
import { User, Mail, Phone, MapPin, GraduationCap, Code2, Briefcase } from 'lucide-react';
import SkillBadge from '../components/SkillBadge.jsx';

export default function ResumeInformation({ data = {} }) {
  const candidate = data.candidate || {
    name: 'Godson Nadar',
    email: 'example@email.com',
    phone: 'XXXXXXXXXX',
    location: 'Mumbai, India',
  };

  const education = data.education || [
    { degree: 'B.E. Artificial Intelligence & Machine Learning', institution: 'SFIT' },
  ];

  const skills = data.skills || ['Python', 'Machine Learning', 'HTML', 'CSS', 'JavaScript', 'SQL', 'React'];
  const experience = data.experience || [];

  return (
    <div id="resume-information-section" className="space-y-4">
      
      {/* Personal Info Box */}
      <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
        <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-4">
          <User className="w-4 h-4 text-[#6B7FD7]" /> Personal Information
        </h4>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
          <div className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
            <span className="text-[10px] text-[#94A3B8] uppercase font-semibold block mb-0.5">Name</span>
            <span className="font-bold text-[#263247] text-sm">{candidate.name}</span>
          </div>

          <div className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
            <span className="text-[10px] text-[#94A3B8] uppercase font-semibold block mb-0.5">Email</span>
            <span className="font-medium text-[#475569] truncate block">{candidate.email}</span>
          </div>

          <div className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
            <span className="text-[10px] text-[#94A3B8] uppercase font-semibold block mb-0.5">Phone</span>
            <span className="font-medium text-[#475569]">{candidate.phone}</span>
          </div>

          <div className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
            <span className="text-[10px] text-[#94A3B8] uppercase font-semibold block mb-0.5">Location</span>
            <span className="font-medium text-[#475569]">{candidate.location}</span>
          </div>
        </div>
      </div>

      {/* Education & Experience in 2 columns */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Education Box */}
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
          <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
            <GraduationCap className="w-4 h-4 text-[#6B7FD7]" /> Education
          </h4>
          <div className="space-y-2">
            {education.map((edu, idx) => (
              <div key={idx} className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                <p className="font-bold text-xs text-[#263247]">{edu.degree}</p>
                <p className="text-xs text-[#64748B] mt-0.5">{edu.institution}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Extracted Experience */}
        <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
          <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
            <Briefcase className="w-4 h-4 text-[#6B7FD7]" /> Extracted Experience
          </h4>
          <div className="space-y-2">
            {experience.length > 0 ? (
              experience.map((exp, idx) => (
                <div key={idx} className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0]">
                  <div className="flex justify-between items-center text-xs">
                    <span className="font-bold text-[#263247]">{exp.role}</span>
                    <span className="text-[#6B7FD7] font-medium">{exp.duration}</span>
                  </div>
                  <p className="text-xs text-[#64748B] mt-0.5">{exp.company}</p>
                </div>
              ))
            ) : (
              <div className="p-3 bg-[#F8FAFC] rounded-xl border border-[#E2E8F0] text-xs text-[#64748B]">
                Academic & Project Based Experience
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Extracted Skills */}
      <div className="bg-white border border-[#E6EAF0] rounded-2xl p-6 shadow-xs">
        <h4 className="text-xs font-bold uppercase tracking-wider text-[#64748B] flex items-center gap-2 mb-3">
          <Code2 className="w-4 h-4 text-[#6B7FD7]" /> Extracted Skills ({skills.length})
        </h4>
        <div className="flex flex-wrap gap-2">
          {skills.map((skill, idx) => (
            <SkillBadge key={idx} skill={skill} type="default" size="md" />
          ))}
        </div>
      </div>

    </div>
  );
}
