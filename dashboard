import pandas as pd

def dashboard(trends_csv="data/trends.csv"):
    df = pd.read_csv(trends_csv)
    summary = df.groupby("niche").agg({
        "video_id": "count",
        "like_per_min": "mean",
        "view_per_min": "mean",
        "score": "mean"
    }).reset_index()
    print(summary)
