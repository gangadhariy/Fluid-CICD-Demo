# Base Image
FROM python:3.12-slim

# Set Working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app.py to the working directory
COPY app.py .


EXPOSE 5000

# Run the python script
CMD ["python","app.py"]