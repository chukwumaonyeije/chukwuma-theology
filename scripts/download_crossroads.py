import os
import urllib.request
import re

url_base = "https://crossroads-sa97qua4.manus.space"
output_dir = "public/crossroads-destiny"

# Create directories
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, "assets"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "manus-storage"), exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def download_file(url, local_path):
    print(f"Downloading {url} to {local_path}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            with open(local_path, "wb") as f:
                f.write(response.read())
        print("Success.")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# List of files to download
downloads = [
    # Main files
    (f"{url_base}/", os.path.join(output_dir, "index.html")),
    (f"{url_base}/assets/index-CgShepij.css", os.path.join(output_dir, "assets", "index-CgShepij.css")),
    (f"{url_base}/assets/index-CjqF-Ml8.js", os.path.join(output_dir, "assets", "index-CjqF-Ml8.js")),
    # Podcast Audio
    (f"{url_base}/manus-storage/sermon_podcast_00b87187.wav", os.path.join(output_dir, "manus-storage", "sermon_podcast_00b87187.wav")),
    # OG Image
    ("https://files.manuscdn.com/webdev_screenshots/2026/05/31/HBpaZfVxBEXJHVarL2FJsD.png", os.path.join(output_dir, "manus-storage", "HBpaZfVxBEXJHVarL2FJsD.png"))
]

# Slides
slides = [
    "slide_1_a3f6633b.webp",
    "slide_2_f81d3dec.webp",
    "slide_3_73f71e73.webp",
    "slide_4_e16adee1.webp",
    "slide_5_6b414b54.webp",
    "slide_6_c6787cf5.webp",
    "slide_7_0deb4c83.webp",
    "slide_8_3ba62047.webp",
    "slide_9_b35c050c.webp",
    "slide_10_26a4e159.webp",
    "slide_11_b9415d06.webp",
    "slide_12_5586b92b.webp",
    "slide_13_b13e1358.webp",
    "slide_14_cfdb1faf.webp",
    "slide_15_0820e73c.webp",
    "slide_16_d15be153.webp",
    "slide_17_49bdea13.webp",
    "slide_18_bcb9ef81.webp"
]

for slide in slides:
    downloads.append((f"{url_base}/manus-storage/{slide}", os.path.join(output_dir, "manus-storage", slide)))

# Execute downloads
for url, path in downloads:
    # Always download code files to ensure rewriting starts from the fresh source
    is_code = path.endswith(".html") or path.endswith(".css") or path.endswith(".js")
    if is_code or not os.path.exists(path):
        download_file(url, path)
    else:
        print(f"File already exists: {path}")

# Rewrite paths in index.html to use absolute subfolder paths
html_path = os.path.join(output_dir, "index.html")
print(f"Rewriting paths in {html_path}...")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace root-relative asset paths with absolute subdirectory paths
html_content = html_content.replace('href="/assets/index-CgShepij.css"', 'href="/chukwuma-theology/crossroads-destiny/assets/index-CgShepij.css"')
html_content = html_content.replace('src="/assets/index-CjqF-Ml8.js"', 'src="/chukwuma-theology/crossroads-destiny/assets/index-CjqF-Ml8.js"')
# Replace OG/Twitter image paths
html_content = re.sub(r'content="https://files\.manuscdn\.com/webdev_screenshots/[^\"]+"', 'content="/chukwuma-theology/crossroads-destiny/manus-storage/HBpaZfVxBEXJHVarL2FJsD.png"', html_content)
# Replace canonical link to local or keep it.
html_content = html_content.replace('<link rel="canonical" href="https://crossroads-sa97qua4.manus.space/" />', '')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Rewrite paths in index.js to use absolute subfolder paths and set wouter base path
js_path = os.path.join(output_dir, "assets", "index-CjqF-Ml8.js")
print(f"Rewriting paths in {js_path}...")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Configure the wouter router base path to match the deployed subdirectory path
js_content = js_content.replace('base:""', 'base:"/chukwuma-theology/crossroads-destiny"')

# Replace absolute "/manus-storage/..." references with subfolder absolute paths
js_content = js_content.replace('"/manus-storage/', '"/chukwuma-theology/crossroads-destiny/manus-storage/')

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print("Scraping and relative path rewriting complete!")

