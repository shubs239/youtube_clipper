import yt_dlp

video_id = "ySvRWHbfvRU"  # Replace with your video ID
video_url = f"https://www.youtube.com/watch?v={video_id}"

# Configure yt-dlp to download the best MP4 format
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '/content/%(title)s.%(ext)s',  # Save to Colab's /content directory
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=True)
    filename = ydl.prepare_filename(info)

print(f"Downloaded video: {filename}")