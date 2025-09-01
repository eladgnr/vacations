import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";

interface UserData {
    user_id: number;
    username: string;
    email: string;
    is_staff: boolean;
    is_superuser: boolean;
}

export default function StatsHomepage() {
    const [identifier, setIdentifier] = useState("");
    const [password, setPassword] = useState("");
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [userData, setUserData] = useState<UserData | null>(null);

    // ✅ Auto-check login state when page loads
    useEffect(() => {
        axios
            .get(`${import.meta.env.VITE_STATS_API_URL}/whoami`, { withCredentials: true })
            .then((res) => {
                setIsLoggedIn(true);
                setUserData(res.data);
            })
            .catch(() => {
                setIsLoggedIn(false);
                setUserData(null);
            });
    }, []);

    // Login with stats backend
    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const res = await axios.post(
                `${import.meta.env.VITE_STATS_API_URL}/custom_login`,
                { username: identifier, password },
                {
                    withCredentials: true,
                    headers: { "Content-Type": "application/json" },
                }
            );

            if (res.data.status === "ok") {
                const whoami = await axios.get(
                    `${import.meta.env.VITE_STATS_API_URL}/whoami`,
                    { withCredentials: true }
                );
                setIsLoggedIn(true);
                setUserData(whoami.data);
            } else {
                alert("❌ Invalid credentials");
            }
        } catch (err: any) {
            console.error("❌ Login failed:", err.response?.data || err.message);
            alert("❌ Invalid credentials");
        }
    };

    // Logout
    const handleLogout = async () => {
        try {
            await axios.post(
                `${import.meta.env.VITE_STATS_API_URL}/custom_logout`,
                {},
                { withCredentials: true }
            );
        } catch (err) {
            console.warn("Logout request failed, but clearing state anyway.");
        }
        setIsLoggedIn(false);
        setIdentifier("");
        setPassword("");
        setUserData(null);
    };

    return (
        <div
            style={{
                position: "relative",
                minHeight: "100vh",
                width: "100%",
                background: `url('https://cdn.pixabay.com/photo/2017/08/30/01/05/analytics-2697949_1280.jpg') no-repeat center center fixed`,
                backgroundSize: "cover",
            }}
        >
            {/* Dark overlay */}
            <div
                style={{
                    backgroundColor: "rgba(0, 0, 0, 0.6)",
                    position: "absolute",
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                }}
            ></div>

            {/* Centered content */}
            <div
                style={{
                    position: "relative",
                    zIndex: 2,
                    color: "white",
                    textAlign: "center",
                    minHeight: "100vh",
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center",
                }}
            >
                <h1>📊 Statistics Dashboard</h1>
                <p>Welcome to the statistics site for the Vacations Project.</p>

                {/* About link - visible to everyone */}
                <div className="mb-4">
                    <Link to="/about" className="btn btn-outline-light btn-lg">
                        Learn More About This Project
                    </Link>
                </div>

                {isLoggedIn && userData ? (
                    <div className="d-flex flex-column align-items-center mb-3">
                        <span className="mb-2">
                            ✅ Logged in as: <strong>{userData.username}</strong>{" "}
                            ({userData.email || "no email"})
                        </span>
                        {userData.is_superuser && (
                            <span className="badge bg-success mb-2">Admin Access</span>
                        )}
                        <button onClick={handleLogout} className="btn btn-danger">
                            Logout
                        </button>
                    </div>
                ) : (
                    <form
                        onSubmit={handleLogin}
                        className="d-flex justify-content-center gap-2 mb-3"
                    >
                        <input
                            type="text"
                            placeholder="Username"
                            className="form-control w-25 w-sm-50 w-75"
                            value={identifier}
                            onChange={(e) => setIdentifier(e.target.value)}
                        />
                        <input
                            type="password"
                            placeholder="Password"
                            className="form-control w-25 w-sm-50 w-75"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <button
                            type="submit"
                            className="btn btn-primary"
                            disabled={!identifier || !password}
                        >
                            Login
                        </button>
                    </form>
                )}

                {isLoggedIn && (
                    <>
                        <h3 className="mb-3">Available Statistics</h3>
                        <div className="d-grid gap-3 w-50 mx-auto">
                            <Link to="/vacations-per-country" className="btn btn-light">
                                Vacations Per Country
                            </Link>
                            <Link to="/vacations-overdue" className="btn btn-light">
                                Overdue Vacations
                            </Link>
                            <Link to="/likes" className="btn btn-light">
                                Likes
                            </Link>
                            <Link to="/top-likes" className="btn btn-light">
                                Top Liked Vacations
                            </Link>
                        </div>
                    </>
                )}
            </div>
        </div>
    );
}