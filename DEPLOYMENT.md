# 🚀 Deployment Guide: f1nance

Follow these instructions to deploy your improved **f1nance** project to the web.

## 1. Backend Deployment (Render)

We recommend [Render](https://render.com) for the FastAPI backend.

1.  **Create a New Web Service**: Connect your GitHub repository.
2.  **Environment**: Python.
3.  **Build Command**: `cd server && pip install -r requirements.txt`
4.  **Start Command**: `cd server && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5.  **Environment Variables**:
    *   `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`: Your PostgreSQL credentials (use Render's Managed PostgeSQL).
    *   `JWT_SECRET_KEY`: A long random string.
    *   `SMTP_USER` / `SMTP_PASSWORD`: Your email credentials.
    *   `ALLOWED_ORIGINS`: `["https://your-frontend-url.vercel.app"]`
    *   `ENVIRONMENT`: `production`

---

## 2. Frontend Deployment (Vercel)

We recommend [Vercel](https://vercel.com) for the React frontend.

1.  **Import Project**: Connect GitHub and select the `client` folder as the Root Directory.
2.  **Framework Preset**: Vite.
3.  **Environment Variables**:
    *   `VITE_API_BASE_URL`: `https://your-backend-url.onrender.com/api/v1`
4.  **Deploy**: Hit the deploy button!

---

## 3. Post-Deployment
Once you have your URLs:
1.  Go back to Render and update `ALLOWED_ORIGINS` with your specific Vercel URL.
2.  Your app is now live!
