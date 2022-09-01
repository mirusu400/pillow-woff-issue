import requests
import os
from PIL import ImageFont

r = requests.get("https://cdn.jsdelivr.net/korean-webfonts/1/orgs/othrs/kywa/Youth/Youth.woff2", stream=True)
with open("Youth.woff2", "wb") as f:
    f.write(r.content)

print("Trying to get Font ...\t", end="...")

try:
    font = ImageFont.truetype("Youth.woff2")
    print("Success")
except Exception as e:
    print("Failed " + str(e))
finally:
    os.remove("Youth.woff2")
