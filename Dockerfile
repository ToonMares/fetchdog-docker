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

# How to run it

# docker build -t fetchdog . 
# docker run -e YOUTUBE_API_KEY='YOUR_API_KEY' -e CHANNEL_ID='YOUR_CHANNEL_ID' -e DOWNLOAD_LATEST_VIDEO='yes' -e CHECK_INTERVAL_MINUTES='5' -e DOWNLOAD_DIR='/downloads' -v  -p 8080:8080 my_fetchdog_container
