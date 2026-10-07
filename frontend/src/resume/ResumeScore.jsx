import React from 'react';
import ScoreCard from '../components/ScoreCard.jsx';

export default function ResumeScore({ score = 78 }) {
  return (
    <div id="resume-score-overview" className="w-full">
      <ScoreCard
        id="main-resume-score-card"
        score={score}
        title="Overall Resume Score"
        subtitle="Your resume has a strong foundation, but several areas can be improved."
      />
    </div>
  );
}
