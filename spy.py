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

# 👇 PUBLIC SERVERS LIST (Fail-safe)
INSTANCES = [
    "https://inv.tux.pizza",
    "https://vid.puffyan.us",
    "https://invidious.projectsegfau.lt",
    "https://yt.artemislena.eu",
    "https://invidious.einfachzocken.eu"
]

def get_json(path):
    # Har server ko try karega jab tak data na mile
    for instance in INSTANCES:
        try:
            url = f"{instance}/api/v1{path}"
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                return response.json()
        except:
            continue
    return None

def analyze_channel(handle):
    print(f"\n🕵️‍♂️ Analyzing: @{handle} ...")
    
    # 1. Channel dhundo
    search_data = get_json(f"/search?q={handle}&type=channel")
    
    if not search_data:
        print(f"❌ Server connect nahi hua. Retrying...")
        return

    channel_id = None
    # Exact match dhundo
    for item in search_data:
        if item.get('author', '').replace(" ", "").lower() == handle.lower():
            channel_id = item['authorId']
            break
            
    # Agar exact na mile, toh pehla wala lelo
    if not channel_id and len(search_data) > 0:
        channel_id = search_data[0]['authorId']

    if not channel_id:
        print(f"❌ Channel nahi mila.")
        return

    # 2. Videos aur Tags nikalo
    videos_data = get_json(f"/channels/{channel_id}/videos")
    
    if not videos_data:
        print("❌ Videos list khaali hai.")
        return

    all_tags = []
    categories = []
    
    print(f"   ⏳ Checking last 10 videos for Tags & Category...")
    
    for video in videos_data[:10]:
        # A. Category (Genre)
        if 'genre' in video and video['genre']:
            categories.append(video['genre'])
            
        # B. Tags (Keywords) - Video ke andar se
        if 'videoId' in video:
            vid_detail = get_json(f"/videos/{video['videoId']}")
            if vid_detail:
                # Kabhi kabhi category andar hoti hai
                if 'genre' in vid_detail and vid_detail['genre']:
                    categories.append(vid_detail['genre'])
                # Main Tags
                if 'keywords' in vid_detail:
                    all_tags.extend(vid_detail['keywords'])
                
    # --- FINAL REPORT ---
    print(f"✅ SUCCESS: @{handle}")

    # 1. Category Print karo
    if categories:
        common_cat = Counter(categories).most_common(1)[0][0]
        print(f"   📂 CATEGORY: {common_cat}")
    else:
        print("   📂 CATEGORY: Not Found (Hidden)")

    # 2. Tags Print karo
    if all_tags:
        print("   🏷️  VIRAL TAGS:")
        top_tags = Counter(all_tags).most_common(15) # Top 15 tags
        for tag, count in top_tags:
            print(f"      - {tag}")
    else:
        print("      (No hidden tags found)")
    
    print("-" * 40)
    time.sleep(1)

if __name__ == "__main__":
    print("🚀 STARTING SPY BOT V3.0 (BINA LOGIN WALA)...")
    for handle in TARGET_HANDLES:
        analyze_channel(handle)
    print("🏁 MISSION COMPLETE.")
