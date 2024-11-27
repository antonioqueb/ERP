# Etapa de construcción
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa final
FROM python:3.11-slim
WORKDIR /app

# Copiar dependencias y ejecutables
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .

# Crear usuario no root y ajustar permisos
RUN adduser --disabled-password appuser && chown -R appuser /app

# Cambiar al usuario no root
USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
