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

interface VacationLikes {
    country: string;
    title: string; // backend returns vacation title
    likes: number;
}

export default function TopLikes() {
    const [vacations, setVacations] = useState<VacationLikes[]>([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_WEB_API_URL}/api/likes/per-vacation/`, {
                withCredentials: true,
            })
            .then((res) => setVacations(res.data))
            .catch((err) => console.error("Error fetching top likes:", err));
    }, []);

    const chartData = {
        labels: vacations.map((d) => `${d.title} (${d.country})`),
        datasets: [
            {
                label: "Likes",
                data: vacations.map((d) => d.likes),
                backgroundColor: "rgba(255, 99, 132, 0.6)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1,
            },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
            legend: { position: "top" as const },
            title: { display: true, text: "Top Liked Vacations" },
        },
    };

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2>Top Liked Vacations</h2>
                <Link to="/stats-homepage" className="btn btn-secondary">
                    ⬅ Back to Homepage
                </Link>
            </div>

            {/* Chart */}
            {vacations.length > 0 ? (
                <div className="card p-3">
                    <Bar data={chartData} options={options} />
                </div>
            ) : (
                <p>No vacation likes data available.</p>
            )}

            {/* Table */}
            {vacations.length > 0 && (
                <div className="card p-3 mt-4">
                    <h4 className="text-center">Detailed Breakdown</h4>
                    <table className="table table-striped text-center">
                        <thead className="table-dark">
                            <tr>
                                <th>Country</th>
                                <th>Title</th>
                                <th>Likes</th>
                            </tr>
                        </thead>
                        <tbody>
                            {vacations.map((v, i) => (
                                <tr key={i}>
                                    <td>{v.country}</td>
                                    <td>{v.title}</td>
                                    <td>{v.likes}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}
