from dotenv import load_dotenv
import os

# Load variables from the .env file into the environment
load_dotenv()

config = {
	"google_api_key": os.environ.get("GOOGLE_API_KEY"),
}