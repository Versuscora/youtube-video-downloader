# youtube_downloader.py

from pytube import YouTube
import os

def download_video():
    # Prompt the user to enter a YouTube link
    link = input("Please enter the YouTube link: ")

    # Set the download path
    download_path = './download'

    try:
        # Create a YouTube object
        yt = YouTube(link)

        # Display video title and view count
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")

        # Get the highest resolution stream available
        yd = yt.streams.get_highest_resolution()

        # Ensure the download folder exists
        os.makedirs(download_path, exist_ok=True)

        # Download the video
        print("Downloading...")
        yd.download(download_path)
        print(f"Downloaded successfully to {download_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_video()
