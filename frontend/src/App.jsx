// import logo from './logo.svg';
import './App.css';
import homepageimg from './homepageimg.svg'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from './components/Navbar';
import Search from './components/Search'

function App() {
  return (
    <div className="app">
      <header className="App-header">
        <Navbar />
        <div className='content-container'>
          <div className="left-image">
            <img src={homepageimg} alt="Logo" className="logo-image" />
          </div>
          <div className="text-content">
            <h1 className='homepage-header'>Free from biases, start your career fresh with{' '} <span className="typing-effect">cleanSlate.</span></h1>
            <p className='homepage-body'>We believe that everyone deserves to work in an environment where they are respected, valued, and treated equally. At cleanSlate we make discovering Inclusive Companies with Transparent Diversity Ratings accessible</p>
            <Search />
          </div>
        </div>
      </header>
      {/* <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/services" element={<Services />} />
          <Route path="/contact" element={<Contact />} />
        </Routes> */}
    </div>
  );
}

export default App;
