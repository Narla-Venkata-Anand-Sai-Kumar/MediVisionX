FROM python:3.9
# Set the working directory
WORKDIR /app

# Install system dependencies for OpenCV and TensorFlow
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*  

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt


EXPOSE 5100

# Run the application
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5100", "app:app"]
