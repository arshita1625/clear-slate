import * as React from 'react';
import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2'; // Import Bar chart from react-chartjs-2
import { Box } from '@mui/material';
import { LinearProgress } from '@mui/material';
import { Chart as ChartJS } from 'chart.js/auto'; // Automatically registers necessary chart types

export default function GraphData() {
    // Prepare chart data
    const chartData = {
        labels: ['female', 'male'], // X-axis labels as location areas
        datasets: [
            {
                label: 'Feminine Score',
                data: [22, 0], // Feminine score data
                backgroundColor: 'rgba(255, 99, 132, 0.6)',  // Bar color for feminine scores
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1,
            },
            {
                label: 'Masculine Score',
                data: [0, 78], // Masculine score data
                backgroundColor: 'rgba(54, 162, 235, 0.6)',  // Bar color for masculine scores
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
            },
        ],
    };

    return (
        // <div>{data}</div>
        <Box sx={{ height: 500, width: '100%' }}>

            <Bar
                data={chartData}
                options={{
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top',
                        },
                        tooltip: {
                            callbacks: {
                                label: (tooltipItem) => {
                                    return `${tooltipItem.dataset.label}: ${tooltipItem.raw.toFixed(2)}`;
                                },
                            },
                        },
                    },
                    scales: {
                        y: {
                            beginAtZero: true, // Ensure the y-axis starts from 0
                        },
                    },
                }}
            />
        </Box>
    );
}
