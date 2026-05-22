FROM python:3.10-slim

# Install git
RUN apt update && apt install -y git

# Create working directory
WORKDIR /NIK-Forward-Bot

# Copy requirements first
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start app
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]
