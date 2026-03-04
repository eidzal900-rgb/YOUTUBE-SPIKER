"""
Elite Content Factory Pro - Configuration Module
Secrets will be loaded from Streamlit dashboard or environment variables
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (loaded from environment or dashboard input)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Niche List - 10 viral niches
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

# YouTube Search Configuration
MAX_VIDEOS_PER_NICHE = 30
SEARCH_ORDER = "date"  # or "relevance"

# Spike Detection Thresholds
SPIKE_LIKE_PER_MIN = 40
SPIKE_VIEW_PER_MIN = 150
SPIKE_ENGAGEMENT = 12  # percentage

# Prediction Configuration
DECAY_FACTOR = 0.45  # Realistic for YouTube Shorts
MONETIZATION_HIGH = 200000
MONETIZATION_MEDIUM = 50000

# Script Generation
GPT_VARIATIONS = 5
SCRIPT_DURATION = "45-60s"

# Dashboard Configuration
DASHBOARD_REFRESH_INTERVAL = 30  # seconds
DATA_DIR = "data"
STATS_FILE = "data/stats.csv"
TRENDS_FILE = "data/trends.csv"
TOP10_FILE = "data/top10_weekly.csv"
SCRIPTS_DIR = "data/scripts"

# Polling Configuration
POLL_INTERVAL_MINUTES = 10
SEARCH_INTERVAL_HOURS = 3