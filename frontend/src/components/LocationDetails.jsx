import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Button } from '@mui/material';

function LocationDetails() {
    // const { locationName } = useParams();
    // const clubs = clubsData[locationName] || [];
    const [locations, setLocations] = useState([])
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
    console.log("inside location details");

    useEffect(() => {
        fetchLocations()
    }, [])
    const openInMaps = (address) => {
        // Open the address in Google Maps
        window.open(`https://www.google.com/maps?q=${encodeURIComponent(address)}`, '_blank');
    };

    return (
        <div style={{ border: "2px solid red" }}>
            <h2>Clubs & Support Groups</h2>
            <TableContainer component={Paper}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>Name</TableCell>
                            <TableCell>Rating</TableCell>
                            <TableCell>Address</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {locations.map((club) => (
                            <TableRow key={club.id}>
                                <TableCell>{club.name}</TableCell>
                                <TableCell>{club.rating}</TableCell>
                                <TableCell>
                                    <Button onClick={() => openInMaps(club.address)} variant="outlined">
                                        {club.address}
                                    </Button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    );
}

export default LocationDetails;
