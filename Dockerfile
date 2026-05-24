# ─── Base Image ───────────────────────────────────────────────
FROM python:3.11-slim

# ─── Set Working Directory ────────────────────────────────────
WORKDIR /app

# ─── Environment Variables ────────────────────────────────────
ENV PORT=5000
ENV CONTAINER_NAME=docker-app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ─── Install Dependencies ─────────────────────────────────────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ─── Copy App Files ───────────────────────────────────────────
COPY . .

# ─── Expose Port ──────────────────────────────────────────────
EXPOSE 5000

# ─── Run the App ──────────────────────────────────────────────
CMD ["python", "app.py"]
