from fetch_captions_with_time import get_debate_segments
from download_yt_video import download_video
from clipper import process_debate

def main(video_id: str):
    # Step 1: Get debate timestamps
    segments = get_debate_segments(video_id)
    print(f"Found {len(segments)} debates.")
    
    # Step 2: Download video
    video_path = download_video(video_id)
    print(f"Downloaded: {video_path}")
    
    # Step 3: Process each debate
    for idx, segment in enumerate(segments):
        output_path = process_debate(video_path, "outputs", segment)
        print(f"Processed debate {idx+1}: {output_path}")

if __name__ == "__main__":
    video_id = "ySvRWHbfvRU"  # Replace with your video ID
    main(video_id)