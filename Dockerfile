# Use a lightweight Python base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
# This step is cached, so it only reruns if requirements.txt changes
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Streamlit application code into the container
COPY . .

# Expose the port Streamlit runs on (default is 8501)
EXPOSE 8501

# Command to run the Streamlit application
# --server.port sets the port for Streamlit
# --server.enableCORS False and --server.enableXsrfProtection False are often needed for Cloud Run
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=False", "--server.enableXsrfProtection=False"]
