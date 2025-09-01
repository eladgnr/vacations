import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";

interface LikeData {
    destination: string;
    likes: number;
}

export default function TopLikes() {
    const [likesData, setLikesData] = useState<LikeData[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_STATS_API_URL}/top-likes`, {
                withCredentials: true,
            })
            .then((res) => {
                console.log("Fetched likes data:", res.data);
                setLikesData(res.data);
                setLoading(false);
            })
            .catch((err) => {
                console.error("Failed to fetch likes data", err);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div className="container py-4">
                <div className="d-flex justify-content-center">
                    <div className="spinner-border" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="container py-4">
            <div className="d-flex justify-content-between align-items-center mb-4">
                <h2>Top Liked Vacations</h2>
                <Link to="/stats-homepage" className="btn btn-secondary">
                    ← Back to Homepage
                </Link>
            </div>

            {likesData.length > 0 ? (
                <>
                    {/* Chart */}
                    <div className="card mb-4">
                        <div className="card-header">
                            <h5 className="card-title mb-0">Vacation Likes Distribution</h5>
                        </div>
                        <div className="card-body">
                            <ResponsiveContainer width="100%" height={400}>
                                <BarChart
                                    data={likesData}
                                    margin={{ top: 20, right: 30, left: 20, bottom: 60 }}
                                >
                                    <CartesianGrid strokeDasharray="3 3" />
                                    <XAxis
                                        dataKey="destination"
                                        angle={-45}
                                        textAnchor="end"
                                        height={80}
                                        fontSize={12}
                                    />
                                    <YAxis />
                                    <Tooltip
                                        formatter={(value) => [value, "Likes"]}
                                        labelStyle={{ color: '#333' }}
                                    />
                                    <Bar
                                        dataKey="likes"
                                        fill="#0d6efd"
                                        radius={[4, 4, 0, 0]}
                                    />
                                </BarChart>
                            </ResponsiveContainer>
                        </div>
                    </div>

                    {/* Summary Table */}
                    <div className="card">
                        <div className="card-header">
                            <h5 className="card-title mb-0">Detailed Rankings</h5>
                        </div>
                        <div className="card-body">
                            <div className="table-responsive">
                                <table className="table table-striped">
                                    <thead className="table-dark">
                                        <tr>
                                            <th>Rank</th>
                                            <th>Destination</th>
                                            <th>Likes</th>
                                            <th>Popularity</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {likesData.map((item, index) => (
                                            <tr key={item.destination}>
                                                <td>
                                                    {index === 0 && <span className="badge bg-warning">🥇</span>}
                                                    {index === 1 && <span className="badge bg-secondary">🥈</span>}
                                                    {index === 2 && <span className="badge bg-success">🥉</span>}
                                                    {index > 2 && <span className="badge bg-light text-dark">#{index + 1}</span>}
                                                </td>
                                                <td className="fw-bold">{item.destination}</td>
                                                <td>
                                                    <span className="badge bg-primary">{item.likes}</span>
                                                </td>
                                                <td>
                                                    <div className="progress" style={{ height: '20px' }}>
                                                        <div
                                                            className="progress-bar"
                                                            style={{
                                                                width: `${(item.likes / Math.max(...likesData.map(d => d.likes))) * 100}%`
                                                            }}
                                                        >
                                                            {item.likes > 0 && `${item.likes} likes`}
                                                        </div>
                                                    </div>
                                                </td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                    {/* Statistics Summary */}
                    <div className="row mt-4">
                        <div className="col-md-4">
                            <div className="card text-center">
                                <div className="card-body">
                                    <h5 className="card-title">Total Vacations</h5>
                                    <h3 className="text-primary">{likesData.length}</h3>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-4">
                            <div className="card text-center">
                                <div className="card-body">
                                    <h5 className="card-title">Total Likes</h5>
                                    <h3 className="text-success">
                                        {likesData.reduce((sum, item) => sum + item.likes, 0)}
                                    </h3>
                                </div>
                            </div>
                        </div>
                        <div className="col-md-4">
                            <div className="card text-center">
                                <div className="card-body">
                                    <h5 className="card-title">Most Popular</h5>
                                    <h3 className="text-warning">
                                        {likesData[0]?.destination || "N/A"}
                                    </h3>
                                </div>
                            </div>
                        </div>
                    </div>
                </>
            ) : (
                <div className="alert alert-info">
                    <h4>No likes data available</h4>
                    <p>There are currently no vacation likes to display.</p>
                </div>
            )}
        </div>
    );
}