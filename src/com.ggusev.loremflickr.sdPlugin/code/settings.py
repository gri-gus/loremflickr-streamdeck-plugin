import logging
import os
from pathlib import Path

PLUGIN_LOGS_DIR_PATH: Path = Path(os.environ["PLUGIN_LOGS_DIR_PATH"])
PLUGIN_NAME: str = os.environ["PLUGIN_NAME"]

LOG_FILE_PATH: Path = PLUGIN_LOGS_DIR_PATH / Path(f"{PLUGIN_NAME}.log")
LOG_LEVEL: int = logging.DEBUG

IMAGE_SIZE = 144
LOREM_FLICKR_URL = "https://loremflickr.com"
