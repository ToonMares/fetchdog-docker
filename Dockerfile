FROM python:3.9


WORKDIR /fetchdogbeta-docker


COPY . /fetchdogbeta-docker


RUN pip install yt-dlp


EXPOSE 8080


CMD ["python", "main.py"]


#docker build -t fetchdog . 
#docker run -e YOUTUBE_API_KEY= -e CHANNEL_ID= -e DOWNLOAD_LATEST_VIDEO=yes -e CHECK_INTERVAL_MINUTES=5 fetchdog  