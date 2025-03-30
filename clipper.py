import ffmpeg
import os

def process_debate(
    input_path: str,
    output_dir: str,
    segment: tuple,
    intro_path: str = "intros/intro.mp4",
    disclaimer_path: str = "disclaimers/disclaimer.mp4"
) -> str:
    """
    Adds intro/disclaimer to the debate clip WITHOUT cropping.
    Intro/disclaimer are scaled to match the debate clip's resolution.
    """
    os.makedirs(output_dir, exist_ok=True)
    start, end = segment
    output_path = os.path.join(output_dir, f"debate_{start}_{end}.mp4")

    # 1. Get resolution of the debate clip
    probe = ffmpeg.probe(input_path)
    video_stream = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    width = int(video_stream['width'])
    height = int(video_stream['height'])

    # 2. Clip the debate segment (original resolution)
    debate_clip = ffmpeg.input(input_path, ss=start, to=end)

    # 3. Scale intro/disclaimer to match debate clip's resolution
    input_intro = (
        ffmpeg.input(intro_path)
        .filter('scale', width, height, force_original_aspect_ratio='increase')
        .filter('pad', width, height, '(ow-iw)/2', '(oh-ih)/2')  # Center with padding
    )

    input_disclaimer = (
        ffmpeg.input(disclaimer_path)
        .filter('scale', width, height, force_original_aspect_ratio='increase')
        .filter('pad', width, height, '(ow-iw)/2', '(oh-ih)/2')
    )

    # 4. Concatenate intro + disclaimer + debate
    (
        ffmpeg.concat(
            input_intro,
            input_disclaimer,
            debate_clip,
            v=1, a=1
        )
        .output(output_path, vcodec='libx264', crf=23, acodec='aac')
        .overwrite_output()
        .run()
    )

    return output_path