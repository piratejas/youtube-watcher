import logging
import sys
import requests
from config import config


def main():
    logging.info("Starting app...")

    response = requests.get(
        "https://www.googleapis.com/youtube/v3/playlistItems",
        params={
            "key": config["google_api_key"],
        },
    )

    logging.debug("Got response: %s", response.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
