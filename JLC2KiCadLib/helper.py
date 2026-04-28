import logging
import sys
import requests


def get_easyeda_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }


def set_logging(logging_level, logging_file):
    LOGGING_FILE = "JLC2KiCad_lib.log"

    if logging_file:
        logging.basicConfig(
            filename=LOGGING_FILE, format="%(asctime)s - %(levelname)s - %(message)s"
        )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging_level)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
