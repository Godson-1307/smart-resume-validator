import React, { useState } from 'react';
import SkillBadge from '../components/SkillBadge.jsx';
import Button from '../components/Button.jsx';
import { Check, Edit3, Plus, Sparkles } from 'lucide-react';
import { COMMON_SKILLS } from '../utils/constants.js';

export default function SkillSelector({ skills = [], onChange }) {
  const [isEditing, setIsEditing] = useState(false);
  const [newSkillInput, setNewSkillInput] = useState('');
  const [isConfirmed, setIsConfirmed] = useState(false);

  const handleRemove = (skillToRemove) => {
    const updated = skills.filter((s) => s !== skillToRemove);
    onChange(updated);
  };

  const handleAdd = (e) => {
    e?.preventDefault();
    if (!newSkillInput.trim()) return;
    const trimmed = newSkillInput.trim();
    if (!skills.includes(trimmed)) {
      onChange([...skills, trimmed]);
    }
    setNewSkillInput('');
  };

  const handleAddSuggested = (skillName) => {
    if (!skills.includes(skillName)) {
      onChange([...skills, skillName]);
    }
  };

  return (
    <div id="career-skill-selector" className="space-y-5">
      <div className="bg-[#F8FAFC] border border-[#E2E8F0] rounded-2xl p-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4 pb-3 border-b border-[#E2E8F0]">
          <div>
            <span className="text-[10px] uppercase font-bold tracking-wider text-[#6B7FD7] bg-[#EEF1FF] px-2 py-0.5 rounded-md">
              Auto-Extracted from Resume
            </span>
            <h4 className="text-sm font-bold text-[#263247] mt-1">Detected Skills</h4>
          </div>

          <div className="flex items-center gap-2">
            {!isEditing ? (
              <Button
                variant="outline"
                size="sm"
                icon={Edit3}
                onClick={() => setIsEditing(true)}
                className="text-xs"
              >
                Edit Skills
              </Button>
            ) : (
              <Button
                variant="secondary"
                size="sm"
                icon={Check}
                onClick={() => setIsEditing(false)}
                className="text-xs"
              >
                Done Editing
              </Button>
            )}

            <Button
              variant={isConfirmed ? 'success' : 'primary'}
              size="sm"
              icon={Check}
              onClick={() => setIsConfirmed(true)}
              className="text-xs"
            >
              {isConfirmed ? '✓ Confirmed' : 'Yes, Correct'}
            </Button>
          </div>
        </div>

        {/* Skill Badges List */}
        <div className="flex flex-wrap gap-2 min-h-[48px] items-center">
          {skills.map((skill, idx) => (
            <SkillBadge
              key={idx}
              skill={skill}
              type="existing"
              onRemove={isEditing ? handleRemove : null}
              size="md"
            />
          ))}
        </div>

        {/* Edit mode: Add new skill */}
        {isEditing && (
          <div className="mt-4 pt-4 border-t border-[#E2E8F0] space-y-3">
            <form onSubmit={handleAdd} className="flex gap-2">
              <input
                type="text"
                value={newSkillInput}
                onChange={(e) => setNewSkillInput(e.target.value)}
                placeholder="Add a new skill (e.g. AWS, Kubernetes)..."
                className="flex-1 px-3.5 py-2 text-xs sm:text-sm bg-white border border-[#CBD5E1] rounded-xl focus:outline-hidden focus:ring-2 focus:ring-[#6B7FD7]/20"
              />
              <Button type="submit" variant="primary" size="sm" icon={Plus}>
                Add
              </Button>
            </form>

            <div className="flex flex-wrap items-center gap-1.5 pt-1">
              <span className="text-[11px] text-[#94A3B8] mr-1 flex items-center gap-1">
                <Sparkles className="w-3 h-3" /> Quick add:
              </span>
              {COMMON_SKILLS.filter((s) => !skills.includes(s))
                .slice(0, 6)
                .map((s) => (
                  <button
                    key={s}
                    type="button"
                    onClick={() => handleAddSuggested(s)}
                    className="text-[11px] px-2 py-0.5 rounded-md bg-white border border-[#E2E8F0] text-[#64748B] hover:border-[#6B7FD7] hover:text-[#6B7FD7] transition-colors cursor-pointer"
                  >
                    + {s}
                  </button>
                ))}
            </div>
          </div>
        )}
      </div>

      <div className="p-3 bg-[#EEF1FF]/50 border border-[#6B7FD7]/20 rounded-xl text-xs text-[#4F62BD]">
        Are these skills correct? You can click <strong>Edit Skills</strong> to add missing tools or remove outdated competencies.
      </div>
    </div>
  );
}
