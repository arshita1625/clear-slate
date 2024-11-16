import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import LocationList from "./components/LocationList";
import AddLocationForm from "./components/AddLocationForm";
import { useNavigate } from "react-router-dom";
import { Button, TextField, List, ListItem } from '@mui/material';
import "./App.css";

function App() {
    const [locations, setLocations] = useState([]);
    const [searchQuery, setSearchQuery] = useState("")
    const [filteredLocations, setFilteredLocations] = useState(locations);
    const navigate = useNavigate();
    const fetchLocations = () => {
        fetch("http://127.0.0.1:5000/locations")
            .then((response) => response.json())  // Parse the JSON data from the response
            .then((data) => {
                setLocations(data);  // Update the state with the fetched data
            })
            .catch((error) => {
                console.error("Error fetching locations:", error);  // Handle errors
            });

    };
    useEffect(() => {
        fetchLocations()
    }, [])
    const handleSuggestionClick = (location) => {
        // Set the search query to the clicked suggestion and clear the suggestions
        setSearchQuery(location.name);
        setFilteredLocations([]);
    };
    const handleSearchChange = (e) => {
        const query = e.target.value;
        setSearchQuery(query);

        // Filter locations based on search query
        if (query === '') {
            setFilteredLocations([]);
        } else {
            const result = locations.filter((location) =>
                location.name.toLowerCase().includes(query.toLowerCase())
            );
            setFilteredLocations(result);
        }
    };
    const getLocations = () => {
        console.log("inside getlocations")
        const result = locations.filter((location) =>
            location.name.toLowerCase().includes(searchQuery.toLowerCase())
        );
        setFilteredLocations(result); // Update filtered locations
        navigate("/location-details")
    };

    const addLocation = (location) => {
        fetch("http://127.0.0.1:5000/add_location", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",  // Specify the content type
            },
            body: JSON.stringify(location),  // Convert the location data to a JSON string
        })
            .then((response) => response.json())  // Parse the JSON response
            .then((data) => {
                setLocations((prevLocations) => [...prevLocations, data]);  // Update the state with the new location
            })
            .catch((error) => {
                console.error("Error adding location:", error);  // Handle errors
            });

    };

    return (
        <div className="app">
            <Header />
            <div className="search-bar">
                <input type="text" placeholder="Enter location..." value={searchQuery}
                    onChange={handleSearchChange} />
                <button onClick={getLocations}>Search</button>
                {filteredLocations.length > 0 && (
                    <ul style={{ border: '1px solid #ccc', padding: '0', listStyleType: 'none', maxHeight: '200px', overflowY: 'auto' }}>
                        {filteredLocations.map((location) => (
                            <li
                                key={location.id}
                                style={{ padding: '8px', cursor: 'pointer' }}
                                onClick={() => handleSuggestionClick(location)}
                            >
                                {location.name}
                            </li>
                        ))}
                    </ul>
                )}
            </div>
            {/* <LocationList locations={locations} /> */}
            <AddLocationForm addLocation={addLocation} />
        </div>
    );
}

export default App;
