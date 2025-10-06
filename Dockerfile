FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN adduser --disabled-password --gecos '' mluser
USER mluser
WORKDIR /app

# Copy requirements from poetry export
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY --chown=mluser:mluser . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s \
  CMD curl --fail http://localhost:8000/health || exit 1

CMD ["python", "-m", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
