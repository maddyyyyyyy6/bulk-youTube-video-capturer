from pytube import YouTube

# Replace this list with the YouTube video URLs you want to download
video_urls = ['url1', 'url2']

for url in video_urls:
    try:
        video = YouTube(url)
        print(f"Downloading '{video.title}'...")
        video.streams.get_highest_resolution().download()
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading '{url}': {e}")
