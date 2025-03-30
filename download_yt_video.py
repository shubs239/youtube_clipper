import yt_dlp
import os

def download_video(video_id: str, output_dir: str = "downloads") -> str:
    """
    Returns path to downloaded video file.
    """
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f"{output_dir}/%(id)s.%(ext)s",
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        raise Exception(f"Download failed: {e}")