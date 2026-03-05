import os
import csv
import json
import time
import datetime
import random
import pandas as pd
from googleapiclient.discovery import build
import openai

# =========================
# CONFIG
# =========================

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

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

MAX_VIDEOS_PER_NICHE = 10

SPIKE_LIKE_PER_MIN = 40
SPIKE_VIEW_PER_MIN = 150
SPIKE_ENGAGEMENT = 12

DATA_DIR = "data"
TRENDS_FILE = f"{DATA_DIR}/trends.csv"
SCRIPTS_DIR = f"{DATA_DIR}/scripts"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(SCRIPTS_DIR, exist_ok=True)

# =========================
# INIT YOUTUBE API
# =========================

youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# =========================
# SEARCH VIDEOS
# =========================

def search_videos():

    videos = []

    for niche in NICHES:

        try:

            request = youtube.search().list(
                q=niche,
                part="snippet",
                type="video",
                order="viewCount",
                maxResults=MAX_VIDEOS_PER_NICHE
            )

            response = request.execute()

            for item in response["items"]:

                videos.append({
                    "video_id": item["id"]["videoId"],
                    "title": item["snippet"]["title"],
                    "niche": niche
                })

        except Exception as e:
            print("Search error:", e)

    return videos

# =========================
# GET VIDEO STATS
# =========================

def get_video_stats(video_ids):

    stats = {}

    try:

        request = youtube.videos().list(
            part="statistics",
            id=",".join(video_ids)
        )

        response = request.execute()

        for item in response["items"]:

            vid = item["id"]

            stats[vid] = {
                "view": int(item["statistics"].get("viewCount", 0)),
                "like": int(item["statistics"].get("likeCount", 0))
            }

    except Exception as e:
        print("Stats error:", e)

    return stats

# =========================
# SPIKE CALCULATION
# =========================

def calculate_metrics(view, like):

    view_per_min = view / 60
    like_per_min = like / 60

    engagement = (like / view * 100) if view > 0 else 0

    spike = (
        like_per_min > SPIKE_LIKE_PER_MIN
        and view_per_min > SPIKE_VIEW_PER_MIN
        and engagement > SPIKE_ENGAGEMENT
    )

    return like_per_min, view_per_min, engagement, spike

# =========================
# PREDICT VIRAL
# =========================

def predict_views(view_per_min):

    decay = 0.45

    predicted = view_per_min * 60 * 24 * decay

    if predicted > 1000000:
        status = "WEAPON"
    elif predicted > 200000:
        status = "HIGH"
    elif predicted > 50000:
        status = "MEDIUM"
    else:
        status = "LOW"

    return int(predicted), status

# =========================
# GPT SCRIPT GENERATOR
# =========================

def generate_scripts(title, variations=3):

    scripts = []

    for i in range(variations):

        try:

            prompt = f"""
Buat script YouTube Shorts 45-60 saat.

Tajuk:
{title}

Format:
Hook kuat
3 point fakta
Ending CTA follow

Variasi ke {i+1}.
"""

            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}],
                temperature=0.7
            )

            script = response["choices"][0]["message"]["content"]

            scripts.append(script)

        except Exception as e:

            print("GPT error:", e)

    return scripts

# =========================
# SAVE SCRIPTS
# =========================

def save_scripts(video_id, scripts):

    for i, script in enumerate(scripts):

        filename = f"{SCRIPTS_DIR}/{video_id}_{i+1}.txt"

        with open(filename, "w", encoding="utf-8") as f:

            f.write(script)

# =========================
# SAVE TREND DATA
# =========================

def save_trends(data):

    file_exists = os.path.isfile(TRENDS_FILE)

    with open(TRENDS_FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "time",
                "video_id",
                "title",
                "niche",
                "view",
                "like",
                "view_per_min",
                "like_per_min",
                "engagement",
                "predicted_views",
                "status",
                "score"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

# =========================
# MAIN PIPELINE
# =========================

def main():

    print("ELITE CONTENT FACTORY STARTED")

    videos = search_videos()

    video_ids = [v["video_id"] for v in videos]

    stats = get_video_stats(video_ids)

    results = []

    for video in videos:

        vid = video["video_id"]

        if vid not in stats:
            continue

        view = stats[vid]["view"]
        like = stats[vid]["like"]

        like_pm, view_pm, engagement, spike = calculate_metrics(view, like)

        predicted, status = predict_views(view_pm)

        score = (like_pm * 0.4) + (view_pm * 0.3) + (engagement * 0.3)

        record = {
            "time": str(datetime.datetime.now()),
            "video_id": vid,
            "title": video["title"],
            "niche": video["niche"],
            "view": view,
            "like": like,
            "view_per_min": round(view_pm,2),
            "like_per_min": round(like_pm,2),
            "engagement": round(engagement,2),
            "predicted_views": predicted,
            "status": status,
            "score": round(score,2)
        }

        results.append(record)

        if spike:

            print("SPIKE DETECTED:", video["title"])

            scripts = generate_scripts(video["title"])

            save_scripts(vid, scripts)

    save_trends(results)

    rank_weekly()

    print("SYSTEM FINISHED")

# =========================
# WEEKLY RANKING
# =========================

def rank_weekly():

    try:

        df = pd.read_csv(TRENDS_FILE)

        top = (
            df.sort_values("score", ascending=False)
            .groupby("niche")
            .head(10)
        )

        top.to_csv(f"{DATA_DIR}/top10_weekly.csv", index=False)

        print("Top 10 updated")

    except Exception as e:

        print("Ranking error:", e)

# =========================
# RUN
# =========================

if __name__ == "__main__":
    main()
