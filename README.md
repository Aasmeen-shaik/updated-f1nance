# f1nance (Sunflower) 🌻

A comprehensive financial management platform designed for international students (F1 visa holders) to manage their finances, track income/expenses, and stay tax-compliant.

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
