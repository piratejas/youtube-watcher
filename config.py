from dotenv import load_dotenv
import os

load_dotenv()

config = {
	"google_api_key": os.environ.get("GOOGLE_API_KEY"),
	"youtube_playlist_id": os.environ.get("YOUTUBE_PLAYLIST_ID"),
}