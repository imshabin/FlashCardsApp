import React from 'react';
import { Routes, Route } from 'react-router-dom';
import LandingPage from '../components/pages/LandingPage';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      {/* Add other routes here */}
    </Routes>
  );
};

export default AppRoutes;