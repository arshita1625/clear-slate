// src/components/SearchComponent.jsx
import React, { useState } from 'react';
import './Search.css';
import Cookies from "js-cookie";
import { useNavigate } from 'react-router-dom';
function Search() {
  const [jobRole, setJobRole] = useState('');
  const [location, setLocation] = useState('');
  const navigate = useNavigate()
  const handleSearch = () => {
    const sanitizedJobRole = jobRole.trim().replace(/[^a-zA-Z0-9\s]/g, ''); // Keep only alphanumeric characters and spaces
    const sanitizedLocation = location.trim().replace(/[^a-zA-Z0-9\s]/g, '')
    Cookies.set("rolee", encodeURIComponent(sanitizedJobRole)); // Encode before storing in cookies
    Cookies.set("areaa", encodeURIComponent(sanitizedLocation));
    // Cookies.set("rolee", jobRole)
    // Cookies.set("areaa", location)
    navigate("/details")
  };

  return (
    <div className="search-container">
      <input
        type="text"
        placeholder="Job Role"
        value={jobRole}
        onChange={(e) => setJobRole(e.target.value)}
        className="search-input"
      />
      <input
        type="text"
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
        className="search-input"
      />
      <button onClick={handleSearch} className="search-button">Search</button>
    </div>
  );
}

export default Search;
