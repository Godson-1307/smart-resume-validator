/**
 * Formats score and returns assessment tier label & color
 */
export function getScoreAssessment(score) {
  if (score >= 85) {
    return {
      label: 'Exceptional',
      desc: 'Top-tier resume ready for high-volume competitive screening.',
      badgeClass: 'bg-[#EDF7F1] text-[#2F6F50] border-[#65A98A]/30',
      color: '#65A98A',
    };
  } else if (score >= 70) {
    return {
      label: 'Good Foundation',
      desc: 'Strong foundation, but several targeted areas can be improved.',
      badgeClass: 'bg-[#EEF1FF] text-[#4F62BD] border-[#6B7FD7]/30',
      color: '#6B7FD7',
    };
  } else if (score >= 50) {
    return {
      label: 'Room to Improve',
      desc: 'Needs critical additions in metrics, formatting, or keyword depth.',
      badgeClass: 'bg-[#FFF7E8] text-[#8F6516] border-[#D9A441]/30',
      color: '#D9A441',
    };
  } else {
    return {
      label: 'Needs Major Revision',
      desc: 'Lacks standard section hierarchy and quantifiable achievements.',
      badgeClass: 'bg-[#FEF0F0] text-[#9E3939] border-[#D97878]/30',
      color: '#D97878',
    };
  }
}

export function formatCurrencyLPA(val) {
  if (!val) return '₹ 0 LPA';
  return `₹ ${val} LPA`;
}
