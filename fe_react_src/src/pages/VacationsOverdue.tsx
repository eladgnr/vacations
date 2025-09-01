import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";

interface Vacation {
    id: number;
    title: string;
    country: string;
    start_date: string;
    end_date: string;
}

export default function VacationsOverdue() {
    const [vacations, setVacations] = useState<Vacation[]>([]);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_STATS_API_URL}/vacations-overdue`, {
                withCredentials: true,
            })
            .then((res) => {
                console.log("Fetched data:", res.data);   // ✅ check what comes from backend
                setVacations(res.data);                  // ✅ use the correct setter
            })
            .catch((err) => console.error("Failed to fetch overdue vacations", err));
    }, []);

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h2>Vacations Status</h2>
                <Link to="/stats-homepage" className="btn btn-secondary">
                    ⬅ Back to Homepage
                </Link>
            </div>

            {/* Legend */}
            <div className="mb-3">
                <span className="badge bg-danger">Overdue</span>
            </div>

            {vacations.length > 0 ? (
                <table className="table table-striped text-center">
                    <thead className="table-dark">
                        <tr>
                            <th>Country</th>
                            <th>Title</th>
                            <th>Start Date</th>
                            <th>End Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        {vacations.map((v) => (
                            <tr key={v.id} className="table-danger fw-bold">
                                <td>{v.country}</td>
                                <td>{v.title}</td>
                                <td>{v.start_date}</td>
                                <td>{v.end_date}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>No overdue vacations found.</p>
            )}
        </div>
    );
}
