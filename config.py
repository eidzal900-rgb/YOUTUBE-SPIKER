"""
Elite Content Factory Pro - Configuration Module
Load secrets from:
1. Streamlit Secrets
2. Environment Variables
3. .env file
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# API KEYS
# =========================

def get_secret(key, default=None):
    """
    Priority:
    1. Streamlit secrets
    2. Environment variable
    3. Default
    """
    try:
        import streamlit as st
        if key in st.secrets:
            return st.secrets[key]
    except:
        pass

    return os.getenv(key, default)


YOUTUBE_API_KEY = get_secret("YOUTUBE_API_KEY")
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")

# =========================
# SYSTEM PATHS
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

SCRIPTS_DIR = os.path.join(DATA_DIR, "scripts")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
VIDEO_DIR = os.path.join(OUTPUT_DIR, "videos")

# Auto create folders
for folder in [DATA_DIR, OUTPUT_DIR, SCRIPTS_DIR, AUDIO_DIR, VIDEO_DIR]:
    os.makedirs(folder, exist_ok=True)

# =========================
# VIRAL NICHE DATABASE
# =========================

NICHES = [

    "AI tools 2026",
    "cara buat duit online",
    "fakta pelik dunia",
    "top 5 terbaru",
    "teknologi masa depan",
    "psychology hack manusia",
    "tips interview kerja",
    "sejarah dunia mengejutkan",
    "perang dunia update",
    "apps viral 2026"
]

# =========================
# YOUTUBE SEARCH CONFIG
# =========================

MAX_VIDEOS_PER_NICHE = 30
SEARCH_ORDER = "date"  # date / relevance / viewCount
REGION_CODE = "MY"
LANGUAGE = "ms"

# =========================
# SPIKE DETECTION
# =========================

SPIKE_LIKE_PER_MIN = 40
SPIKE_VIEW_PER_MIN = 150
SPIKE_ENGAGEMENT = 12  # %

SPIKE_SCORE_WEIGHTS = {
    "views": 0.5,
    "likes": 0.3,
    "comments": 0.2
}

# =========================
# VIRAL PREDICTION
# =========================

DECAY_FACTOR = 0.45

MONETIZATION_HIGH = 200000
MONETIZATION_MEDIUM = 50000

# =========================
# AI SCRIPT GENERATION
# =========================

GPT_VARIATIONS = 5
SCRIPT_DURATION = "45-60s"

SCRIPT_TEMPLATE = """
HOOK (0-3s)
{hook}

CONTENT (3-50s)
{content}

CTA (50-60s)
Follow for more viral content.
"""

# =========================
# VIDEO GENERATION
# =========================

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30

SHORT_LENGTH = 60

# =========================
# DASHBOARD CONFIG
# =========================

DASHBOARD_REFRESH_INTERVAL = 30

STATS_FILE = os.path.join(DATA_DIR, "stats.csv")
TRENDS_FILE = os.path.join(DATA_DIR, "trends.csv")
TOP10_FILE = os.path.join(DATA_DIR, "top10_weekly.csv")

# =========================
# AUTOMATION SCHEDULER
# =========================

POLL_INTERVAL_MINUTES = 10
SEARCH_INTERVAL_HOURS = 3

VIDEOS_PER_DAY_LIMIT = 50

# =========================
# LOGGING
# =========================

LOG_LEVEL = "INFO"
LOG_FILE = os.path.join(DATA_DIR, "system.log")

# =========================
# DEBUG MODE
# =========================

DEBUG = False
