"""Fetch the channel's YouTube RSS feed and write videos.json for the site."""
import json
import urllib.request
import xml.etree.ElementTree as ET

CHANNEL_ID = "UCA57RiUshgiwowe0LOTJ7DQ"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def first_line(text, limit=220):
    """First non-empty line of the video description, trimmed for the card."""
    for line in (text or "").splitlines():
        line = line.strip()
        if line:
            return line[:limit].rsplit(" ", 1)[0] + "…" if len(line) > limit else line
    return ""


def main():
    with urllib.request.urlopen(FEED_URL, timeout=30) as resp:
        root = ET.fromstring(resp.read())

    videos = []
    for entry in root.findall("atom:entry", NS):
        videos.append({
            "id": entry.find("yt:videoId", NS).text,
            "title": entry.find("atom:title", NS).text,
            "description": first_line(
                entry.find("media:group/media:description", NS).text
            ),
            "published": entry.find("atom:published", NS).text,
        })

    videos.sort(key=lambda v: v["published"], reverse=True)

    with open("videos.json", "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Wrote {len(videos)} video(s) to videos.json")


if __name__ == "__main__":
    main()
