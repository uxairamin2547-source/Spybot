import requests
import time
from collections import Counter

# 👇 TARGET CHANNELS
TARGET_HANDLES = [
    "FixClipss",
    "Insane_Cinema",
    "Fresh2Movies",
    "MartianMeloDrama",
    "smith58",
    "bullymovie1995"
]

# 👇 Reliable Public Instances (Servers)
INSTANCES = [
    "https://inv.tux.pizza",
    "https://vid.puffyan.us",
    "https://invidious.projectsegfau.lt",
    "https://yt.artemislena.eu"
]

def get_json(path):
    # Try different servers until one works
    for instance in INSTANCES:
        try:
            url = f"{instance}/api/v1{path}"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                return response.json()
        except:
            continue
    return None

def analyze_channel(handle):
    print(f"\n🕵️‍♂️ Jasoosi: @{handle} ...")
    
    # 1. Search Channel
    search_data = get_json(f"/search?q={handle}&type=channel")
    
    if not search_data:
        print(f"❌ Server busy, retrying next...")
        return

    channel_id = None
    # Try to match handle exactly
    for item in search_data:
        if item.get('author', '').replace(" ", "").lower() == handle.lower():
            channel_id = item['authorId']
            break
            
    if not channel_id and len(search_data) > 0:
        channel_id = search_data[0]['authorId']

    if not channel_id:
        print(f"❌ Channel ID Not Found.")
        return

    # 2. Get Videos
    videos_data = get_json(f"/channels/{channel_id}/videos")
    
    if not videos_data:
        print("❌ No videos found.")
        return

    all_tags = []
    categories = []
    
    print(f"   ⏳ Scanning last 10 videos...")
    
    for video in videos_data[:10]:
        # Category check
        if 'genre' in video and video['genre']:
            categories.append(video['genre'])
            
        # Tags Check (Video ID se detail nikalo)
        if 'videoId' in video:
            vid_detail = get_json(f"/videos/{video['videoId']}")
            if vid_detail:
                # Category confirm karo detail se bhi
                if 'genre' in vid_detail and vid_detail['genre']:
                    categories.append(vid_detail['genre'])
                # Tags
                if 'keywords' in vid_detail:
                    all_tags.extend(vid_detail['keywords'])
                
    # --- REPORT ---
    print(f"✅ REPORT FOR: @{handle}")

    if categories:
        common_cat = Counter(categories).most_common(1)[0][0]
        print(f"   📂 Main Category: {common_cat}")
    else:
        print("   📂 Category: Not Found (Likely 'Film & Animation' hidden)")

    if all_tags:
        print("   🏷️  TOP HIDDEN TAGS:")
        top_tags = Counter(all_tags).most_common(10)
        for tag, count in top_tags:
            print(f"      - {tag}")
    else:
        print("      (No hidden tags found)")
    
    print("-" * 40)
    time.sleep(1)

if __name__ == "__main__":
    print("🚀 STARTING FINAL PUBLIC SPY BOT (No Login)...")
    for handle in TARGET_HANDLES:
        analyze_channel(handle)
    print("🏁 MISSION COMPLETE.")
