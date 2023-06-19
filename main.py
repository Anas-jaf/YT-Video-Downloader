from pytube import YouTube

# Prompt the user for the YouTube video URL
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = YouTube(video_url)

# Select the highest quality stream available
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()
