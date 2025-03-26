# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . /app/

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the application when the container starts
CMD ["streamlit", "run", "gerundium-brand-voting-app.py"]
