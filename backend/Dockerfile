FROM python:3.9-slim
WORKDIR /app
COPY main.py .
RUN pip install fastapi[all] databases[postgresql] sqlalchemy asyncpg uvicorn
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
