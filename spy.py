import yt_dlp
import datetime
from collections import Counter
import time
import random

# 👇 TARGET CHANNELS
TARGET_CHANNELS = [
    "FixClipss",
    "Insane_Cinema",
    "Fresh2Movies",
    "MartianMeloDrama",
    ".smith58",
    "bullymovie1995"
]

def analyze_channel(username):
    print(f"\n🕵️‍♂️ Analyzing: {username} ...")
    
    # Android Client Trick use karenge
    url = f"https://www.youtube.com/@{username}/shorts"
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': True, 
        'playlist_end': 5,  # 👈 Sirf last 5 videos check karenge (Safe Mode)
        'ignoreerrors': True,
        # 👇 JAADU: Hum khud ko 'Android Phone' batayenge
        'extractor_args': {'youtube': {'player_client': ['android']}},
        'sleep_interval': 2 # Har request ke baad 2 sec rukenge
    }

    all_tags = []
    categories = []

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 1. Channel Scan
            print(f"   📲 Connecting as Android App...")
            info = ydl.extract_info(url, download=False)
            
            if 'entries' not in info:
                print("❌ Channel access denied (Still blocked).")
                return

            print(f"   ⏳ Found videos, digging deeper...")
            
            # 2. Deep Scan
            for entry in info['entries']:
                if not entry: continue
                video_url = entry.get('url')
                
                # Individual video scan
                # Yahan bhi Android bankar jayenge
                with yt_dlp.YoutubeDL({
                    'quiet': True,
                    'extractor_args': {'youtube': {'player_client': ['android']}}
                }) as v_ydl:
                    try:
                        vid_info = v_ydl.extract_info(video_url, download=False)
                        
                        # Tags nikalo
                        if 'tags' in vid_info and vid_info['tags']:
                            all_tags.extend(vid_info['tags'])
                        
                        # Category nikalo
                        if 'categories' in vid_info and vid_info['categories']:
                            categories.extend(vid_info['categories'])
                            
                    except: continue

    except Exception as e:
        print(f"⚠️ Blocked: {e}")
        return

    # --- REPORT ---
    print(f"✅ REPORT FOR: {username}")
    
    if categories:
        common_cat = Counter(categories).most_common(1)[0][0]
        print(f"   📂 Main Category: {common_cat}")
    else:
        print("   📂 Category: Not Found")

    if all_tags:
        print("   🏷️  TOP HIDDEN TAGS:")
        top_tags = Counter(all_tags).most_common(10)
        for tag, count in top_tags:
            print(f"      - {tag}")
    else:
        print("      (No hidden tags found)")

    print("-" * 40)
    time.sleep(3) # Channel change karne se pehle 3 sec ruko

if __name__ == "__main__":
    print("🚀 STARTING ANDROID SPY BOT...")
    for user in TARGET_CHANNELS:
        analyze_channel(user)
    print("🏁 MISSION COMPLETE.")
