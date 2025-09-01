import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav style={{ padding: "1rem", background: "#f5f5f5" }}>
            <Link to="/" style={{ marginRight: "1rem" }}>Home</Link>
            <Link to="/vacations" style={{ marginRight: "1rem" }}>Vacations</Link>
            <Link to="/stats-homepage">Stats</Link> {/* single entry */}
        </nav>

    );
}
