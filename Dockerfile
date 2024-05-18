FROM python:3.9

# Set the working directory in the container
WORKDIR /fetchdogz-dockerz

# Copy the current directory contents into the container at /fetchdocker
COPY . /fetchdogz-dockerz

# Install any needed dependencies specified in requirements.txt
RUN pip install yt-dlp

# Expose the port the app runs on
EXPOSE 8080

# Run the specified command within the container
CMD ["python", "main.py"]


#docker build -t fetchdog . 
#docker run -e YOUTUBE_API_KEY= -e CHANNEL_ID= -e DOWNLOAD_LATEST_VIDEO=yes -e CHECK_INTERVAL_MINUTES=5 fetchdog  