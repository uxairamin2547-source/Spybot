from pytubefix import Channel, YouTube
import time
from collections import Counter

# 👇 TARGET CHANNELS (Sirf Handle likho)
TARGET_HANDLES = [
    "FixClipss",
    "Insane_Cinema",
    "Fresh2Movies",
    "MartianMeloDrama",
    "smith58",
    "bullymovie1995"
]

def analyze_channel(handle):
    print(f"\n🕵️‍♂️ Connecting to: @{handle} ...")
    
    try:
        # 1. Channel Page par jao
        url = f"https://www.youtube.com/@{handle}"
        c = Channel(url)
        
        # 2. Videos list nikalo (Shorts + Videos mix hoti hain)
        # Hum pehli 5 videos check karenge
        videos = c.videos
        
        if not videos:
            print("❌ Koi video nahi mili (shayad channel empty hai).")
            return

        print(f"   ⏳ Found videos! Scanning last 5 uploads...")
        
        all_tags = []
        categories = []
        
        # Sirf Top 5 videos ko scan karo taaki fast rahe
        count = 0
        for video in videos:
            if count >= 5: break
            
            try:
                # Video Details Fetch karo
                print(f"      Scanning: {video.title[:30]}...")
                
                # Tags (Keywords)
                if video.keywords:
                    all_tags.extend(video.keywords)
                
                # Category (Metadata se nikalne ki koshish)
                # Note: Pytubefix kabhi kabhi category seedha nahi deta, 
                # par tags hi main game hain.
                
            except Exception as e:
                continue
            
            count += 1

        # --- FINAL REPORT ---
        print(f"✅ REPORT FOR: @{handle}")

        # Tags Print karo (Sabse Zaroori)
        if all_tags:
            print("   🏷️  TOP HIDDEN TAGS:")
            # Top 10 sabse common tags
            top_tags = Counter(all_tags).most_common(10)
            for tag, count in top_tags:
                print(f"      - {tag}")
        else:
            print("      (Tags hidden or not found)")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Error: {e} (YouTube ne roka, next try karenge)")
    
    time.sleep(2) # Thoda sa break lo taaki bot pakda na jaye

if __name__ == "__main__":
    print("🚀 STARTING PYTUBEFIX SPY BOT (Anti-Block Mode)...")
    for handle in TARGET_HANDLES:
        analyze_channel(handle)
    print("🏁 MISSION COMPLETE.")
