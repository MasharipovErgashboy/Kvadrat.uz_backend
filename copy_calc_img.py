import shutil
import os

src = "/home/ergashboy/.gemini/antigravity/brain/80609d68-9b71-4d13-bddd-4c23a08b6f6b/calculator_header_meeting_1769030803609.png"
dst = "/home/ergashboy/Desktop/kvadratuz_frontend/public/calculator-header.png"

try:
    shutil.copy(src, dst)
    print("Success")
except Exception as e:
    print(f"Error: {e}")
