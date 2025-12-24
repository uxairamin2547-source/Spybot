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
        
        # 2. Description Check for Hashtags
        print(f"\n📝 Description Snippet:")
        print(yt.description[:200]) # Pehle 200 words dikhayega
        
        # 3. Hidden Tags (Keywords)
        print(f"\n🏷️  HIDDEN TAGS:")
        if yt.keywords:
            for tag in yt.keywords:
                print(f"   - {tag}")
        else:
            print("   (No hidden tags found inside metadata)")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    get_video_details(VIDEO_URL)
