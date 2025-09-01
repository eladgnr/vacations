import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

export default function About() {
    return (
        <div className="container mt-4">
            {/* Banner Section */}
            <div
                className="p-5 mb-4 bg-light rounded-3 shadow-sm position-relative"
                style={{
                    backgroundImage: "url('/images/banner.jpg')",
                    backgroundSize: "cover",
                    backgroundPosition: "center",
                    minHeight: "250px"
                }}
            >
                {/* Dark overlay for better text readability */}
                <div
                    className="position-absolute top-0 start-0 w-100 h-100 rounded-3"
                    style={{ backgroundColor: "rgba(0, 0, 0, 0.4)" }}
                ></div>

                <div className="container-fluid py-5 text-white position-relative" style={{ zIndex: 2 }}>
                    <h1 className="display-5 fw-bold">About This Project</h1>
                    <p className="col-md-8 fs-5" style={{ textShadow: "2px 2px 4px rgba(0,0,0,0.8)" }}>
                        Learn more about the Vacations project and the developer behind it.
                    </p>
                    <Link to="/stats-homepage" className="btn btn-dark btn-lg">
                        ← Back to Homepage
                    </Link>
                </div>
            </div>

            {/* Cards Section */}
            <div className="row g-4">
                {/* Project Overview Card */}
                <div className="col-md-6">
                    <div className="card h-100 shadow-sm">
                        <div className="card-body">
                            <h4 className="card-title mb-3">
                                <i className="bi bi-laptop me-2"></i> Project Overview
                            </h4>
                            <p className="card-text">
                                This is a full-stack project called <strong>Vacations</strong>.
                                It is built with <strong>Python</strong> and <strong>Django</strong> on the backend,
                                <strong>React</strong> for frontend functionality, and
                                <strong>PostgreSQL</strong> as the database.
                                The system manages users, countries, and vacations, while also providing
                                statistics dashboards through a dedicated Django app.
                                It supports both admin and user roles, authentication, vacation booking,
                                likes, and modern UI features. The project is fully containerized using Docker Compose.
                            </p>

                            <h6 className="mt-4 mb-2">Key Features:</h6>
                            <ul className="list-unstyled">
                                <li><i className="bi bi-check-circle text-success me-2"></i>User authentication & role management</li>
                                <li><i className="bi bi-check-circle text-success me-2"></i>Vacation booking system</li>
                                <li><i className="bi bi-check-circle text-success me-2"></i>Likes & ratings functionality</li>
                                <li><i className="bi bi-check-circle text-success me-2"></i>Interactive statistics dashboard</li>
                                <li><i className="bi bi-check-circle text-success me-2"></i>Responsive React frontend</li>
                                <li><i className="bi bi-check-circle text-success me-2"></i>Docker containerization</li>
                            </ul>
                        </div>
                    </div>
                </div>

                {/* About Me Card */}
                <div className="col-md-6">
                    <div className="card h-100 shadow-sm">
                        <div className="card-body">
                            <h4 className="card-title mb-3">
                                <i className="bi bi-person-circle me-2"></i> About Me
                            </h4>
                            <p className="card-text">
                                I'm <strong>Elad K.</strong>, a junior developer from Israel.
                                Passionate about full-stack development, learning new technologies,
                                and building real-world projects like this one.
                            </p>

                            <h6 className="mt-4 mb-2">Technologies Used:</h6>
                            <div className="d-flex flex-wrap gap-2">
                                <span className="badge bg-primary">Python</span>
                                <span className="badge bg-success">Django</span>
                                <span className="badge bg-info">React</span>
                                <span className="badge bg-warning text-dark">TypeScript</span>
                                <span className="badge bg-secondary">PostgreSQL</span>
                                <span className="badge bg-dark">Docker</span>
                                <span className="badge bg-primary">Bootstrap</span>
                                <span className="badge bg-info">REST API</span>
                            </div>

                            <h6 className="mt-4 mb-2">Project Links:</h6>
                            <div className="d-flex gap-2">
                                <Link to="/stats-homepage" className="btn btn-outline-primary btn-sm">
                                    <i className="bi bi-bar-chart me-1"></i>Statistics
                                </Link>
                                <a
                                    href="http://localhost:8000"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="btn btn-outline-success btn-sm"
                                >
                                    <i className="bi bi-globe me-1"></i>Main App
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Additional Information */}
            <div className="row g-4 mt-2">
                <div className="col-12">
                    <div className="card shadow-sm">
                        <div className="card-body">
                            <h4 className="card-title mb-3">
                                <i className="bi bi-info-circle me-2"></i> Project Architecture
                            </h4>
                            <div className="row">
                                <div className="col-md-4 mb-3">
                                    <h6><i className="bi bi-server me-2"></i>Backend Services</h6>
                                    <ul className="list-unstyled ms-3">
                                        <li>Main Django App (Port 8000)</li>
                                        <li>Stats Backend (Port 8001)</li>
                                        <li>PostgreSQL Database</li>
                                        <li>RESTful API endpoints</li>
                                    </ul>
                                </div>
                                <div className="col-md-4 mb-3">
                                    <h6><i className="bi bi-display me-2"></i>Frontend</h6>
                                    <ul className="list-unstyled ms-3">
                                        <li>React with TypeScript</li>
                                        <li>Vite development server</li>
                                        <li>Bootstrap styling</li>
                                        <li>Chart visualizations</li>
                                    </ul>
                                </div>
                                <div className="col-md-4 mb-3">
                                    <h6><i className="bi bi-box me-2"></i>Deployment</h6>
                                    <ul className="list-unstyled ms-3">
                                        <li>Docker Compose orchestration</li>
                                        <li>Multi-container setup</li>
                                        <li>Volume persistence</li>
                                        <li>Environment configuration</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}