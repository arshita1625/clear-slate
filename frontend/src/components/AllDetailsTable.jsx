import * as React from 'react';
import Box from '@mui/material/Box';
import { DataGrid } from '@mui/x-data-grid';
import { useEffect } from 'react';
import { useState } from 'react';
import { LinearProgress } from '@mui/material';
import Cookies from "js-cookie";
import { FaArrowUp, FaArrowDown } from 'react-icons/fa';
import GraphData from './reportGraphs';
// import "../App.css";
export default function DataGridDemo() {
    const [locations, setLocations] = useState([])
    const [columns, setColumns] = useState([]);
    const handleRoleClick = () => {
        return (
            <GraphData />
        )
    }
    const fetchLocations = () => {
        fetch("http://127.0.0.1:5000/locations")
            .then((response) => response.json())  // Parse the JSON data from the response
            .then((data) => {
                if (data.length > 0) {
                    const dynamicColumns = Object.keys(data[0]).map(key => ({
                        field: key,
                        headerName: key.charAt(0).toUpperCase() + key.slice(1), // Capitalize first letter of the column name
                        width: 200,  // Set a default width, adjust as needed
                        editable: true, // Make it editable if needed
                    })).filter(column => column.field !== 'id' & column.field != "description" & column.field != "ageScore" & column.field != "disabilityScore" & column.field != "feminineScore" & column.field != "masculineScore" & column.field != "racialScore" & column.field != "score" & column.field != "sexualityScore" & column.field != "label");;
                    dynamicColumns.push({
                        field: 'progress',
                        headerName: 'Rating',
                        width: 250,
                        renderCell: (params) => {
                            const progress = (1 - params.row.score) * 100
                            const isPositive = progress > 50;
                            // const color = progress > 50 ? 'green' : 'red';
                            return (
                                <div
                                    style={{
                                        width: "100%",
                                        display: "flex",
                                        alignItems: "center",
                                        gap: "0.5rem",
                                    }}
                                >
                                    <LinearProgress
                                        variant="determinate"
                                        value={progress}
                                        sx={{
                                            height: 10,
                                            width: "80%", // Ensure consistent width
                                            // backgroundColor: progress > 50 ? "green" : "red",
                                            borderRadius: "1rem",
                                            backgroundColor: "none"
                                        }}
                                    />
                                    <span>{`${Math.round(progress)}%`}</span>
                                    {isPositive ? (
                                        <FaArrowUp style={{ color: 'green' }} />
                                    ) : (
                                        <FaArrowDown style={{ color: 'red' }} />
                                    )}
                                </div>


                            );
                        }
                    });
                    const roleColumn = dynamicColumns.find((col) => col.field === 'role');
                    if (roleColumn) {
                        roleColumn.renderCell = (params) => (
                            <span
                                style={{ color: 'blue', cursor: 'pointer' }}
                                onClick={() => handleRoleClick()}
                            >
                                {params.row.role}
                            </span>
                        );
                    }
                    const otherColumns = dynamicColumns.filter((col) => col.field !== 'role');
                    const reorderedColumns = roleColumn
                        ? [roleColumn, ...otherColumns]
                        : dynamicColumns;
                    setColumns(reorderedColumns);  // Update columns state
                    const formattedData = data.map((item, index) => ({
                        id: index + 1, // Assign a unique ID (you can adjust this as needed)
                        ...item,
                        progress: item.progress || 0,
                    }));

                    setLocations(formattedData);
                }
            })
            .catch((error) => {
                console.error("Error fetching locations:", error);  // Handle errors
            });

    };
    useEffect(() => {
        fetchLocations()
    }, [])
    // const role_type = "Software Engineer"
    // const area_type = "Toronto"
    const role_type = decodeURIComponent(Cookies.get("rolee"));
    const area_type = decodeURIComponent(Cookies.get("areaa"));
    const filteredLocations = locations.filter(
        (location) => location.role === role_type && location.area === area_type
    );
    return (
        <div style={{ border: "2px solid #FDE4D1", backgroundColor: "#FDE4D1" }}>
            <Box sx={{ height: "100%", width: '71.5vw', overflow: 'auto', margin: "4rem", marginleft: "4rem" }}>
                <DataGrid
                    rows={filteredLocations}
                    columns={columns}
                    initialState={{
                        // pagination: {
                        //     paginationModel: {
                        //         pageSize: 10,
                        //     },
                        // },
                    }}
                    // pageSizeOptions={[5]}
                    // checkboxSelection
                    disableRowSelectionOnClick
                    getRowId={(row) => row.id}
                />
            </Box>
        </div>

    );
}
