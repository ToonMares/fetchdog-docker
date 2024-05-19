# FetchDog with Docker (beta)

**FetchDog** is your very own YouTube watchdog that allows you to monitor a channel set by you for new video uploads and automatically download them, all within a docker container.

## What Can FetchDog Do?

**FetchDog** offers the following features:

### Monitor Channels

You can specify the channel ID of the YouTube channel you want to monitor.

### Automatic Downloads

**FetchDog** automatically downloads new videos from the selected channel.

### Customizable Interval

You can set the interval between checks to control how often **FetchDog** looks for new videos.

## How to Set it Up

### 1. Obtain a YouTube Data API Key

Before using **FetchDog**, you need to obtain a YouTube Data API key from the Google Cloud Console. Follow these steps:

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the YouTube Data API for your project.
- Create credentials for the API and obtain an API key.

### 2. Pull the Docker Image

docker pull toonmares/fetchdog

### 2. Run FetchDog in Docker

docker run -e YOUTUBE_API_KEY='YOUR_API_KEY' \
           -e CHANNEL_ID='THE CHANNEL YOU WANT TO MONITOR' \
           -e DOWNLOAD_LATEST_VIDEO='yes' \
           -e CHECK_INTERVAL_MINUTES='5' \
           -e DOWNLOAD_DIR='/downloads' \
           -v 'LOCAL PATH' \
           -p 8080:8080 toonmares/fetchdog
