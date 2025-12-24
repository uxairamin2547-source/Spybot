import yt_dlp
import datetime
from collections import Counter

# 👇 YAHAN UN CHANNELS KE NAAM LIKHO JINHE "SPY" KARNA HAI
# (Maine aapke diye hue top competitors daal diye hain)
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
    
    url = f"https://www.youtube.com/@{username}/shorts"
    
    # Options: Sirf Data nikalo, Video download mat karo (Fast)
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'playlist_end': 10, # 👈 Last 10 videos check karega
        'ignoreerrors': True,
    }

    upload_hours = []
    all_tags = []
    categories = []

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 1. Channel Page Scan karo
            info = ydl.extract_info(url, download=False)
            
            if 'entries' not in info:
                print("❌ Channel not found or no Shorts.")
                return

            # 2. Har video ke andar ja kar details nikalo
            print(f"   ⏳ Scanning last {len(info['entries'])} videos...")
            
            for entry in info['entries']:
                video_url = entry.get('url')
                if not video_url: continue
                
                # Deep Scan individual video for Tags & Time
                with yt_dlp.YoutubeDL({'quiet': True}) as v_ydl:
                    vid_info = v_ydl.extract_info(video_url, download=False)
                    
                    # A. Time Nikalo
                    if 'upload_date' in vid_info:
                        # Note: YouTube often hides exact time, but we get the Date.
                        # We will try to guess logic or just show tags/category which is key.
                        pass 

                    # B. Hidden Tags Nikalo
                    if 'tags' in vid_info and vid_info['tags']:
                        all_tags.extend(vid_info['tags'])
                    
                    # C. Category Nikalo
                    if 'categories' in vid_info and vid_info['categories']:
                        categories.extend(vid_info['categories'])

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return

    # --- REPORT GENERATION ---
    print(f"✅ REPORT FOR: {username}")
    
    # 1. Best Category
    if categories:
        common_cat = Counter(categories).most_common(1)[0][0]
        print(f"   📂 Main Category: {common_cat}")
    else:
        print("   📂 Category: Not Found")

    # 2. Top Hidden Tags
    if all_tags:
        print("   🏷️  TOP 10 HIDDEN TAGS:")
        top_tags = Counter(all_tags).most_common(10)
        for tag, count in top_tags:
            print(f"      - {tag}")
    else:
        print("      (No hidden tags found)")

    print("-" * 40)

if __name__ == "__main__":
    print("🚀 STARTING SPY BOT...")
    for user in TARGET_CHANNELS:
        analyze_channel(user)
    print("🏁 SPY MISSION COMPLETE.")
