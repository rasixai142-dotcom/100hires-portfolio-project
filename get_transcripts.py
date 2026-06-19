from youtube_transcript_api import YouTubeTranscriptApi
import os

videos = {
    "frank-kern": "u39fKX5bLdE",
    "todd-brown": "6LLfLkNXhsk",
    "sam-ovens": "BR9eMcA6uR8",
    "stu-mclaren": "775J4zlKXhI",
    "saurabh-bhatnagar": "x5NhSK2wqQA",
}

os.makedirs("transcripts", exist_ok=True)

for name, video_id in videos.items():
    try:
        ytt = YouTubeTranscriptApi()
        fetched = ytt.fetch(video_id)
        text = "\n".join([t.text for t in fetched])
        
        with open(f"transcripts/{name}.txt", "w", encoding="utf-8") as f:
            f.write(f"# Transcript: {name}\n\n")
            f.write(text)
        
        print(f"✅ Done: {name}")
    except Exception as e:
        print(f"❌ Error {name}: {e}")

print("\nSab complete!")