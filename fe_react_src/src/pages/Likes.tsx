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

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

interface LikesData {
    country: string;
    likes: number;
}

export default function Likes() {
    const [totalLikes, setTotalLikes] = useState<number>(0);
    const [likesData, setLikesData] = useState<LikesData[]>([]);

    useEffect(() => {
        // Fetch total likes
axios
  .get(`${import.meta.env.VITE_WEB_API_URL}/api/likes/total/`, { withCredentials: true })
  .then((res) => setTotalLikes(res.data.totalLikes))
  .catch((err) => console.error("Error fetching total likes:", err));

// Fetch likes per country
axios
  .get(`${import.meta.env.VITE_WEB_API_URL}/api/likes/per-country/`, { withCredentials: true })
  .then((res) => setLikesData(res.data))
  .catch((err) => console.error("Error fetching likes per country:", err));

    }, []);


    const chartData = {
        labels: likesData.map((d) => d.country),
        datasets: [
            {
                label: "Likes",
                data: likesData.map((d) => d.likes),
                backgroundColor: "rgba(54, 162, 235, 0.6)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1,
            },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: { position: "top" as const },
            title: { display: true, text: "Likes per Country" },
        },
    };

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2>Likes Statistics</h2>
                <Link to="/stats-homepage" className="btn btn-secondary">
                    ⬅ Back to Homepage
                </Link>
            </div>

            {/* Total Likes */}
            <div className="card text-center bg-primary text-white mb-4">
                <div className="card-body">
                    <h3>Total Likes</h3>
                    <h1>{totalLikes}</h1>
                </div>
            </div>

            {/* Likes per Country Chart */}
            {likesData.length > 0 ? (
                <div className="card p-3">
                    <Bar data={chartData} options={options} />
                </div>
            ) : (
                <p>No likes data available.</p>
            )}
        </div>
    );
}
