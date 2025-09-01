import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Vacations from "./pages/Vacations";
import Stats from "./pages/Stats";
import NotFound from "./pages/NotFound";
import StatsHomepage from "./pages/StatsHomepage";
import VacationsPerCountry from "./pages/VacationsPerCountry";
import VacationsOverdue from "./pages/VacationsOverdue";
import Likes from "./pages/Likes";        // ✅ new
import TopLikes from "./pages/TopLikes";  // ✅ new
import About from "./pages/About";

export default function App() {
    const location = useLocation();
    const showNavbar = location.pathname !== "/stats-homepage";

    return (
        <>
            {showNavbar && <Navbar />}
            <Routes>
                <Route path="/" element={<Navigate to="/stats-homepage" replace />} />
                <Route path="/vacations" element={<Vacations />} />
                <Route path="/stats-homepage" element={<StatsHomepage />} />
                <Route path="/vacations-per-country" element={<VacationsPerCountry />} />
                <Route path="/vacations-overdue" element={<VacationsOverdue />} />
                <Route path="/likes" element={<Likes />} />          {/* ✅ new */}
                <Route path="/top-likes" element={<TopLikes />} />   {/* ✅ new */}
                <Route path="*" element={<NotFound />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </>
    );
}
