import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";
import axios from "axios";

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface CountryData {
    country: string;
    count: number;
}

export default function VacationsPerCountry() {
    const [data, setData] = useState<CountryData[]>([]);


    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_STATS_API_URL}/vacations-per-country`, {
                withCredentials: true,
            })
            .then((res) => {
                console.log("Fetched data:", res.data);   // ✅ here
                setData(res.data);
            })
            .catch((err) => console.error("Failed to fetch vacations per country", err));
    }, []);


    const chartData = {
        labels: data.map((d) => d.country),
        datasets: [
            {
                label: "Vacations",
                data: data.map((d) => d.count),
                backgroundColor: "rgba(54, 162, 235, 0.6)",
            },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: { position: "top" as const },
            title: {
                display: true,
                text: "Vacations Per Country",
            },
        },
    };

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2>Vacations Per Country</h2>
                <Link to="/stats-homepage" className="btn btn-secondary">
                    ⬅ Back to Homepage
                </Link>
            </div>

            {data.length > 0 ? (
                <Bar data={chartData} options={options} />
            ) : (
                <p>No data available</p>
            )}
        </div>
    );
}
