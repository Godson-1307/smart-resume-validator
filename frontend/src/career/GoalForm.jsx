import React, { useState } from 'react';
import { useResumeContext } from '../context/ResumeContext.jsx';
import RoleSelector from './RoleSelector.jsx';
import LocationSelector from './LocationSelector.jsx';
import ExperienceSelector from './ExperienceSelector.jsx';
import SalaryInput from './SalaryInput.jsx';
import SkillSelector from './SkillSelector.jsx';
import Button from '../components/Button.jsx';
import { ArrowLeft, ArrowRight, CheckCircle, Sparkles, Compass } from 'lucide-react';

export default function GoalForm({ onSubmit, isSubmitting = false }) {
  const { careerAnswers, updateCareerAnswer } = useResumeContext();
  const [currentStep, setCurrentStep] = useState(1);
  const totalSteps = 5;

  const stepTitles = [
    { num: 1, title: 'Target Role', desc: 'Specify what position you are aiming for' },
    { num: 2, title: 'Industry & Location', desc: 'Where and in which vertical do you want to work?' },
    { num: 3, title: 'Experience Level', desc: 'What seniority level matches your expectations?' },
    { num: 4, title: 'Target Package', desc: 'Compensation range you are targeting' },
    { num: 5, title: 'Confirm Skills', desc: 'Verify skills detected from your resume' },
  ];

  const handleNext = () => {
    if (currentStep < totalSteps) {
      setCurrentStep((prev) => prev + 1);
    } else {
      onSubmit(careerAnswers);
    }
  };

  const handleBack = () => {
    if (currentStep > 1) {
      setCurrentStep((prev) => prev - 1);
    }
  };

  const currentStepInfo = stepTitles[currentStep - 1];

  return (
    <div id="career-goal-form-wizard" className="bg-white border border-[#E6EAF0] rounded-3xl p-6 sm:p-10 shadow-xs max-w-2xl mx-auto">
      
      {/* Top Header & Step Tracker */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-lg bg-[#EEF1FF] text-[#6B7FD7] flex items-center justify-center">
              <Compass className="w-4 h-4" />
            </div>
            <span className="text-xs font-bold uppercase tracking-wider text-[#6B7FD7]">
              Career Profile Setup
            </span>
          </div>
          <span className="text-xs font-semibold text-[#64748B]">
            Step {currentStep} of {totalSteps}
          </span>
        </div>

        <h3 className="text-xl sm:text-2xl font-bold text-[#263247]">
          {currentStepInfo.title}
        </h3>
        <p className="text-xs sm:text-sm text-[#667085] mt-1">
          {currentStepInfo.desc}
        </p>

        {/* Visual Progress Line */}
        <div className="w-full bg-[#E6EAF0] h-2 rounded-full overflow-hidden mt-5 flex">
          <div
            className="bg-[#6B7FD7] h-full rounded-full transition-all duration-300"
            style={{ width: `${(currentStep / totalSteps) * 100}%` }}
          />
        </div>
      </div>

      {/* Step Contents */}
      <div className="min-h-[280px] mb-8">
        {currentStep === 1 && (
          <RoleSelector
            value={careerAnswers.target_role}
            onChange={(val) => updateCareerAnswer('target_role', val)}
          />
        )}

        {currentStep === 2 && (
          <LocationSelector
            industry={careerAnswers.industry}
            onIndustryChange={(val) => updateCareerAnswer('industry', val)}
            country={careerAnswers.country}
            onCountryChange={(val) => updateCareerAnswer('country', val)}
            city={careerAnswers.city}
            onCityChange={(val) => updateCareerAnswer('city', val)}
            workType={careerAnswers.work_type}
            onWorkTypeChange={(val) => updateCareerAnswer('work_type', val)}
          />
        )}

        {currentStep === 3 && (
          <ExperienceSelector
            value={careerAnswers.experience_level}
            onChange={(val) => updateCareerAnswer('experience_level', val)}
          />
        )}

        {currentStep === 4 && (
          <SalaryInput
            value={careerAnswers.expected_package}
            onChange={(val) => updateCareerAnswer('expected_package', val)}
          />
        )}

        {currentStep === 5 && (
          <SkillSelector
            skills={careerAnswers.existing_skills || []}
            onChange={(val) => updateCareerAnswer('existing_skills', val)}
          />
        )}
      </div>

      {/* Bottom Nav Buttons */}
      <div className="pt-6 border-t border-[#F1F5F9] flex items-center justify-between">
        <Button
          id="btn-career-step-back"
          variant="outline"
          size="md"
          icon={ArrowLeft}
          onClick={handleBack}
          disabled={currentStep === 1 || isSubmitting}
        >
          Back
        </Button>

        <Button
          id="btn-career-step-next"
          variant="primary"
          size="md"
          icon={currentStep === totalSteps ? Sparkles : ArrowRight}
          iconPosition="right"
          onClick={handleNext}
          disabled={isSubmitting}
          className="font-semibold px-6"
        >
          {currentStep === totalSteps ? (isSubmitting ? 'Analyzing Goal...' : 'Generate Career Analysis') : 'Next'}
        </Button>
      </div>

    </div>
  );
}
