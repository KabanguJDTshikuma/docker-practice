# Use the Python3.7.2 image
FROM python:3-alpine

# Copy the current directory contents into the container at /app
COPY app /app

WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start
CMD ["python", "app.py"]