from pytube import YouTube
# use a file with urls
# or a other .py with array of urls to keep the code neat
# Replace this list with the YouTube video URLs you want to download
video_urls = ['url1', 'url2']

# we can also do this from a file with url names
with open("urls.txt", "r") as file:
    # Read the contents of the file and split by new line character
    urls = file.read().split("\n")

for url in urls:
    try:
        video = YouTube(url)
        print(f"Downloading '{video.title}'...")
        video.streams.get_highest_resolution().download()
        print("Download complete!")
    except Exception as e:
        print(f"Error downloading '{url}': {e}")
        
        

