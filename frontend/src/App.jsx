import React from 'react';
import { ResumeProvider, useResumeContext } from './context/ResumeContext.jsx';
import Navbar from './components/Navbar.jsx';
import Footer from './components/Footer.jsx';
import Home from './pages/Home.jsx';
import UploadResume from './pages/UploadResume.jsx';
import Validation from './pages/Validation.jsx';
import Analysis from './pages/Analysis.jsx';
import Dashboard from './pages/Dashboard.jsx';
import CareerGoals from './pages/CareerGoals.jsx';
import CareerAnalysis from './pages/CareerAnalysis.jsx';
import NotFound from './pages/NotFound.jsx';

function AppContent() {
  const { currentPage } = useResumeContext();

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'upload':
        return <UploadResume />;
      case 'validation':
        return <Validation />;
      case 'analysis':
        return <Analysis />;
      case 'dashboard':
        return <Dashboard />;
      case 'career-goals':
        return <CareerGoals />;
      case 'career-analysis':
        return <CareerAnalysis />;
      default:
        return <NotFound />;
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#F7F9FC] text-[#263247]">
      <Navbar />
      <main className="flex-1">
        {renderPage()}
      </main>
      <Footer />
    </div>
  );
}

export default function App() {
  return (
    <ResumeProvider>
      <AppContent />
    </ResumeProvider>
  );
}
