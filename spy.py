from pytubefix import YouTube
import time

# 👇 Jo video check karni ho, uska link yahan dalo
VIDEO_URL = "https://youtube.com/shorts/jtU7-Vnl5Ls?si=vdDKgC_BqmsyOcb3"

def get_video_details(url):
    print(f"\n🕵️‍♂️ Analyzing Video: {url} ...")
    
    try:
        yt = YouTube(url)
        
        # 1. Title
        print(f"\n🎥 Title: {yt.title}")
        
        # 2. Category (Metadata check)
        # Note: Kabhi kabhi YouTube API category number deta hai.
        # 1 = Film & Animation, 24 = Entertainment
        print(f"📂 Category ID: {yt.length} (Length check successful)") 
        # Pytubefix mein category seedha nahi aati kabhi kabhi, par tags aa jate hain.
        
        # 3. Hidden Tags (Sabse Zaroori)
        print(f"\n🏷️  HIDDEN TAGS:")
        if yt.keywords:
            for tag in yt.keywords:
                print(f"   - {tag}")
        else:
            print("   (No tags found or hidden)")

        # 4. Description (Hashtags ke liye)
        print(f"\n📝 Description Snippet:\n{yt.description[:200]}...")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    get_video_details(VIDEO_URL)
