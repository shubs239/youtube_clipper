from youtube_transcript_api import YouTubeTranscriptApi
link_id = "ySvRWHbfvRU"

def get_timestamp():
    transcript_list = YouTubeTranscriptApi.list_transcripts(link_id)
# Get the Hindi transcript, which is auto-generated
    hindi_transcript = transcript_list.find_transcript(['hi']).fetch()
    target_phrase = "कहना चाहते"
    previous_text = ""  # Store the text from the previous snippet
    timestamp_in_hours=[]
    timestamp_in_sec=[]
    for entry in hindi_transcript.snippets:
        combined_text = previous_text + entry.text  # Combine with previous text
        if target_phrase in combined_text:
            # If found in combined text, print the start time of the previous snippet 
            # (or the current if it's at the beginning of the current snippet)
            total_seconds = entry.start
            timestamp_in_sec.append(total_seconds)
            minutes = int(total_seconds // 60)  # Get the integer part of the division
            seconds = int(total_seconds % 60)   # Get the remainder
            hours = int(minutes // 60)          # Calculate hours
            minutes = int(minutes % 60)         # Update minutes after calculating hours
            timestamp_in_hours.append(f"{hours}"+":"+f"{minutes}"+":"+f"{seconds}")
            print(f"Start time: {hours:02d}:{minutes:02d}:{seconds:02d}, Text: {combined_text}") 
            
        
        previous_text = entry.text
    return timestamp_in_hours, timestamp_in_sec

def debate_seg(debate_starts_seconds):
    debate_segments = []
    for i in range(len(debate_starts_seconds)):
        start = debate_starts_seconds[i]
        end = debate_starts_seconds[i+1] if i+1 < len(debate_starts_seconds) else None
        debate_segments.append((start, end))

    return debate_segments
    print("Debate segments (start, end):", debate_segments)

