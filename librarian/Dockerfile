# Use the official Python image base to start
FROM python:3.11

# Copy all application code into the /app dir
COPY . /app

# Set working dir to the /app dir
WORKDIR /app

# Copy all relevant requirements
COPY requirements.txt .

# Install requirements 
RUN pip install --no-cache-dir -r requirements.txt

# Set command to run the test client application
CMD sleep 5 && python -m unittest librarian.py
