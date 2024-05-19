FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the requirements
RUN pip install yt-dlp requests

# Default port
EXPOSE 8080

# Run the script
CMD ["python", "main.py"]
