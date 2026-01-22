import shutil
import os

src = "/home/ergashboy/.gemini/antigravity/brain/80609d68-9b71-4d13-bddd-4c23a08b6f6b/happy_family_home_photo_1769032243767.png"
dst = "/home/ergashboy/Desktop/kvadratuz_frontend/public/family-home.png"

try:
    shutil.copy(src, dst)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
