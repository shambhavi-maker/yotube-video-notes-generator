from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import re

def extract_video_id(url):
    """Extract the video ID from a YouTube URL."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_available_languages(video_id):
    """Get a list of available subtitle languages for the video."""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        available_languages = {t.language: t.language_code for t in transcript_list}
        return available_languages
    except TranscriptsDisabled:
        return {}
    except Exception as e:
        return {"Error": str(e)}

def get_subtitles(video_id, lang_code):
    """Fetch subtitles in the specified language."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang_code])
        subtitles = "\n".join([entry["text"] for entry in transcript])
        return subtitles
    except NoTranscriptFound:
        return "❌ No subtitles found for the selected language."
    except Exception as e:
        return f"Error: {str(e)}"