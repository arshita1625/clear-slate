import React from 'react';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom';
import LocationDetails from './components/LocationDetails';
import DataGridDemo from './components/AllDetailsTable';
import App from './App';
function Routess() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<App />} />
                {/* <Route path="/location-details" element={<LocationDetails />} /> */}
                <Route path="/details" element={<DataGridDemo />} />
            </Routes>
        </Router>


    );
}

export default Routess;
