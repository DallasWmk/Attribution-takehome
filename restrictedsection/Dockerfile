# Use the offical Python image base to start
FROM python:3.11

# Copy all application code into the /app dir
COPY . /app

# Set /app as working dir
WORKDIR /app

# Copy all relevant requirements
COPY requirements.txt .

# Install requirements 
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for flask
EXPOSE 5000

# Set python as the entrypoint 
#ENTRYPOINT [ "python" ]

# Set command to start the flask server
CMD ["./app.py"]
