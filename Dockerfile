# Use a Python base image compatible with Raspberry Pi (ARM architecture)
FROM python:3.9-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Command to run your bot
CMD ["python", "main.py"]
