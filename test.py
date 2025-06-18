import requests
import base64

with open("test.jpg", "rb") as f:
    img_bytes = f.read()

img_b64 = base64.b64encode(img_bytes).decode("utf-8")

res = requests.post("http://localhost:11434/api/generate", json={
    "model": "llava",
    "prompt": "Describe this image.",
    "images": [img_b64]
})

print(res.text)
