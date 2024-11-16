import React, { useState } from "react";

const AddLocationForm = ({ addLocation }) => {
    const [formData, setFormData] = useState({ name: "", type: "", address: "" });

    const handleSubmit = (e) => {
        e.preventDefault();
        addLocation(formData);
        setFormData({ name: "", type: "", address: "" });
    };

    return (
        <form className="add-location-form" onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Name"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="Type (e.g., restroom, club)"
                value={formData.type}
                onChange={(e) => setFormData({ ...formData, type: e.target.value })}
            />
            <input
                type="text"
                placeholder="Address"
                value={formData.address}
                onChange={(e) => setFormData({ ...formData, address: e.target.value })}
            />
            <button type="submit">Add Location</button>
        </form>
    );
};

export default AddLocationForm;
