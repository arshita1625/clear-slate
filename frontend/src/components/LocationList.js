import React from "react";

const LocationList = ({ locations }) => (
    <ul className="location-list">
        {locations.map((location) => (
            <li key={location.id}>
                <h3>{location.name}</h3>
                <p>{location.type}</p>
                <p>{location.address}</p>
            </li>
        ))}
    </ul>
);

export default LocationList;
