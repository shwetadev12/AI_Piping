import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import View from './components';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<View />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
