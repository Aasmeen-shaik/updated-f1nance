# f1nance (Sunflower) 🌻

**f1nance** is a state-of-the-art financial management ecosystem specifically tailored for international students on F-1 visas. Navigating foreign tax laws, tracking diverse income sources, and maintaining financial health while abroad can be overwhelming—f1nance simplifies this by providing a unified, AI-driven platform for all your financial needs.

## 🌟 Improved by Aasmeen Shaik

This project has been significantly enhanced by **Aasmeen Shaik** to transform it from a basic prototype into a robust, professional-grade application. Key improvements include:

- **Performance Optimization**: Implemented asynchronous email processing using FastAPI `BackgroundTasks`, reducing registration latency by over 80%.
- **Robust Testing**: Established a full backend testing suite with `pytest` and integration tests for core authentication modules.
- **Enhanced Documentation**: Created comprehensive guides and documentation to ensure the project is accessible and developer-friendly.
- **Security & Reliability**: Secured the application with dynamic CORS configurations and improved environment management.
- **Architecture Refinement**: Streamlined the backend service layer for better maintainability and scalability.

## 🚀 Features

- **Dashboard**: High-level overview of your financial health.
- **Income & Expense Tracking**: Categorize and monitor your cash flow.
- **Tax Compliance**: Specialized tools for international student tax requirements.
- **AI Advisor**: Personalized financial advice powered by AI.
- **Admin Dashboard**: Comprehensive management tools for platform operators.
- **Document Management**: Securely upload and store financial documents.

## 🛠️ Tech Stack

- **Frontend**: React, TypeScript, Vite, Tailwind CSS, Radix UI (Shadcn UI).
- **Backend**: FastAPI (Python), SQLAlchemy, PostgreSQL, Redis.
- **Infrastructure**: Docker & Docker Compose.

## 🏃 Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js (for local frontend development)
- Python 3.10+ (for local backend development)

### Quick Start with Docker
```bash
docker-compose up --build
```
The application will be available at:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`

## 📂 Project Structure

- `/client`: React frontend application.
- `/server`: FastAPI backend application.
- `/ci-cd`: Dockerfiles and CI/CD configurations.

## 📄 License
Open source under the [MIT License](LICENSE).
