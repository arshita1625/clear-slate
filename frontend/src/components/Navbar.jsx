// src/components/Navbar.jsx
import React from "react";
import { Link } from "react-router-dom"; // Import Link from react-router-dom
import './Navbar.css'; // Create a separate CSS file for navbar styling

function Navbar() {
  return (
    <nav className="navbar">
        <div className="navbar-left">
        <h2 className="company-name">cleanSlate</h2> {/* Company name aligned to left */}
      </div>
      <div className="navbar-center">
      <ul className="navbar-links">
        <li>
          <Link to="/" className="navbar-link">Home</Link>
        </li>
        <li>
          <Link to="/about" className="navbar-link">About</Link>
        </li>
        <li>
          <Link to="/services" className="navbar-link">Services</Link>
        </li>
        <li>
          <Link to="/contact" className="navbar-link">Contact</Link>
        </li>
      </ul>
      </div>
    </nav>
  );
}

export default Navbar;
