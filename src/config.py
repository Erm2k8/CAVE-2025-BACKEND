from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def load_environment():
    load_dotenv(
        os.path.join(BASE_DIR, ".env"),
        override=True,
    )
