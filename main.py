import os
import requests
import subprocess
import time

# Function to read API key from an environment variable
def read_api_key():
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        print("Error: YouTube API key not found in environment variables.")
    return api_key

# Function to fetch the latest video from the given channel URL using YouTube Data API
def fetch_latest_video(api_key, channel_id):
    try:
        url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet&order=date&maxResults=1"
        response = requests.get(url)
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            latest_video = data['items'][0]
            title = latest_video['snippet']['title']
            video_id = latest_video['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            return title, video_url
        else:
            print("No videos found on the channel.")
            return None, None
    except Exception as e:
        print("An error occurred while fetching the latest video:", e)
        return None, None

# Function to download the video using yt-dlp
def download_video(video_url):
    try:
        subprocess.run(["yt-dlp", video_url])
        print("Video downloaded successfully.")
    except Exception as e:
        print("An error occurred while downloading the video:", e)

# Main function
def main():
    api_key = read_api_key()
    if not api_key:
        return

    channel_id = os.getenv('CHANNEL_ID')
    if not channel_id:
        print("Error: Channel ID not found in environment variables.")
        return

    # Initial fetch
    prev_title, prev_video_url = fetch_latest_video(api_key, channel_id)
    if prev_title and prev_video_url:
        print(f"Latest video: {prev_title}")
        print(f"Video URL: {prev_video_url}")
        # Download the latest video if specified
        download_choice = os.getenv('DOWNLOAD_LATEST_VIDEO', '').lower()
        if download_choice == "yes":
            download_video(prev_video_url)

    else:
        print("Error: Unable to fetch the latest video. Please check the channel ID and API key.")
        return

    # Get the interval between checks
    interval_minutes = os.getenv('CHECK_INTERVAL_MINUTES')
    if not interval_minutes:
        print("Error: Check interval not specified.")
        return

    interval = int(interval_minutes) * 60

    # Continuous loop to check for new videos
    while True:
        time.sleep(interval)
        title, video_url = fetch_latest_video(api_key, channel_id)
        if title and video_url and (title != prev_title or video_url != prev_video_url):
            print(f"New video found: {title}")
            download_video(video_url)
            prev_title, prev_video_url = title, video_url
        else:
            if title is not None:  # If title is None, it means no videos were found
                print(f"Latest video: {title}")
                print(f"Video URL: {video_url}")
            print("No new videos found.")

if __name__ == "__main__":
    main()
