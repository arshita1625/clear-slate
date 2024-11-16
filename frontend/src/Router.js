import React from 'react';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom';
import LocationDetails from './components/LocationDetails';
function Routess() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<App />} />
                <Route path="/location-details" element={<LocationDetails />} />
            </Routes>
        </Router>


    );
}

export default Routess;
