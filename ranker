import pandas as pd

def rank_top10(trends_csv="data/trends.csv"):
    df = pd.read_csv(trends_csv)
    top10_per_niche = df.groupby("niche").apply(lambda x: x.sort_values("score", ascending=False).head(10))
    top10_per_niche.to_csv("data/top10_weekly.csv", index=False)
