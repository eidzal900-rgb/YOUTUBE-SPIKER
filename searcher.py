import requests
import json
from config import niches  # Assuming that niches is a list of niche strings

def scrape_youtube_videos(api_key):
    videos = []
    for niche in niches:
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={niche}&key={{api_key}}'
        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            video_id = item['id'].get('videoId')
            if video_id:
                video_info = {
                    'video_id': video_id,
                    'title': item['snippet']['title'],
                    'publishedAt': item['snippet']['publishedAt'],
                    'niche': niche
                }
                videos.append(video_info)

    return videos
