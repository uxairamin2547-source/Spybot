import os
from googleapiclient.discovery import build

# 👇 JIS VIDEO KI JASOOSI KARNI HAI, USKI ID YAHAN DALO
# (Link: https://youtube.com/shorts/jtU7-Vnl5Ls... -> ID: jtU7-Vnl5Ls)
VIDEO_ID = "67R6ifKUh8s"

# 👇 Category ID ka Map (YouTube codes ko English mein badalne ke liye)
CATEGORY_MAP = {
    "1": "Film & Animation",
    "2": "Autos & Vehicles",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "20": "Gaming",
    "22": "People & Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology"
}

def spy_video():
    # GitHub Secret se API Key uthayega
    api_key = os.environ.get("API_KEY")
    
    if not api_key:
        print("❌ Error: 'API_KEY' nahi mila! GitHub Secrets check karo.")
        return

    try:
        # YouTube se connection
        youtube = build("youtube", "v3", developerKey=api_key)
        
        print(f"🕵️‍♂️ Analyzing Video ID: {VIDEO_ID} ...")
        
        # Data maango
        request = youtube.videos().list(
            part="snippet",
            id=VIDEO_ID
        )
        response = request.execute()

        if not response['items']:
            print("❌ Video nahi mili (ID galat ho sakti hai).")
            return

        item = response['items'][0]['snippet']
        
        # --- REPORT PRINT KARO ---
        print("\n" + "="*40)
        print(f"🎥 TITLE: {item['title']}")
        
        # Category
        cat_id = item.get('categoryId', 'Unknown')
        cat_name = CATEGORY_MAP.get(cat_id, f"Other (ID: {cat_id})")
        print(f"📂 CATEGORY: {cat_name}")
        
        # Tags (Sabse Zaroori)
        tags = item.get('tags', [])
        
        if tags:
            print(f"\n🏷️  HIDDEN TAGS ({len(tags)} found):")
            for tag in tags:
                print(f"   - {tag}")
        else:
            print("\n🏷️  TAGS: Is video mein koi tags nahi hain (Khali hai).")
            
        print("="*40 + "\n")

    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    spy_video()
