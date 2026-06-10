#!/usr/bin/env python3
"""
Replace all educacion screenshots with clean Pexels stock photos.
Target: 596x880px, unique per signal (md5 dedup).
"""

import os, hashlib, time, urllib.request, urllib.parse, re, json, random
from pathlib import Path
from PIL import Image, ImageOps
import io

OUT_DIR = Path(__file__).parent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
W, H = 596, 880

# ── Keyword map: filename → ordered list of Pexels search terms (concrete + literal)
KEYWORDS = {
    # MACRO 1 — INVENTOLOGÍA DE LA ADULTEZ
    "macro-1-0-accelerec-skills-hiring.png":         ["professional laptop working office", "job interview professional", "resume cv professional"],
    "macro-1-1-tiktok-skillsnotdegrees.png":          ["young professional skills training workshop", "coding student computer learning", "self taught learning laptop"],
    "macro-1-1-interviewguys-skills-hiring-2025.png": ["job interview handshake professional", "hiring manager interview office", "business recruitment professional"],
    "macro-1-2-wef-future-of-jobs.png":               ["technology professional upskilling training", "adult learning online course laptop", "career development workshop"],
    "macro-1-2-coursera-global-skills-report.png":    ["online learning certificate digital badge", "woman studying tablet online course", "professional certification online"],
    "macro-1-3-jhu-homeschool-growth.png":            ["homeschool child learning home table", "mother teaching child at home", "child studying books at home table"],
    "macro-1-3-cbsmiami-microschools.png":            ["small classroom children group learning", "children studying together small group", "kids learning classroom cozy"],
    "macro-1-3-theschoolhouse-microschools.png":      ["child reading book home cozy", "homeschool student notebook writing", "children learning outdoor nature"],
    "macro-1-4-onecodesoft-bigtech-skills.png":       ["young person coding computer tech", "programmer laptop coffee shop", "tech student coding startup"],
    "macro-1-4-tiktok-gapyear.png":                   ["young traveler backpack adventure travel", "gap year young adult travel freedom", "young person hiking backpack outdoors"],
    "macro-1-5-worldbank-learning-poverty.png":       ["child reading book school classroom africa", "student learning poverty school developing", "child writing notebook school"],
    "macro-1-5-unausa-naep-scores.png":               ["student test exam writing school desk", "child classroom test concentration", "student struggling reading school"],

    # MACRO 2 — LOS HERNÁNDEZ ARE PROMPTED
    "macro-2-0-demandsage-ai-education-stats.png":    ["artificial intelligence education technology classroom", "student using ai laptop school", "technology education digital future"],
    "macro-2-1-futuremarketinsights-ai-tutor.png":    ["student laptop studying online tutor", "child online learning home computer", "student video call tutor online"],
    "macro-2-1-globalsociety-khanmigo-ai-tools.png":  ["ai chatbot education student phone", "young student phone learning app", "student smartphone study app"],
    "macro-2-1-khanmigo-demo.png":                    ["student tablet learning app interface", "child ipad educational app learning", "young student tablet homework help"],
    "macro-2-1-khanmigo-hero-landing.png":            ["ai tutor student computer glow", "student laptop night studying glow", "young person studying laptop screen dark"],
    "macro-2-2-duolingo-landing.png":                 ["language learning app smartphone fun", "woman phone language learning app", "young person learning language phone smiling"],
    "macro-2-2-duolingo-streaks-gamification.png":    ["gamification phone app streak reward", "person celebrating phone app achievement", "mobile learning game reward phone"],
    "macro-2-2-strivecloud-duolingo-hero.png":        ["mobile app learning engagement gamification", "phone screen learning colorful app", "person using colorful mobile app learning"],
    "macro-2-3-nerdynav-chatgpt-cheating-infographic.png": ["student laptop writing essay night", "college student typing essay computer", "student doing homework laptop focused"],
    "macro-2-3-edweek-ai-cheating.png":               ["teacher reviewing student work classroom", "educator reviewing paper school desk", "teacher checking student assignment classroom"],
    "macro-2-3-nerdynav-student-usage-chart.png":     ["student phone classroom using technology", "teenager phone school desk studying", "high school student smartphone typing"],
    "macro-2-4-coursera-google-cert.png":             ["digital badge certificate laptop professional", "online certificate award professional", "person laptop certificate achievement"],
    "macro-2-4-fortune-microcredentials.png":         ["professional linkedin profile laptop career", "microcredential digital badge phone", "career growth professional certification badge"],
    "macro-2-4-edsurge-digital-credentials.png":      ["blockchain digital certificate verification", "digital credential phone screen professional", "professional digital portfolio laptop"],
    "macro-2-5-hmtv-ai-profesor-rd-chrome.png":       ["professor teaching technology smart classroom", "teacher using laptop classroom modern", "educator technology classroom presentation"],
    "macro-2-5-hmtv-ai-profesor-rd.png":              ["teacher whiteboard classroom technology modern", "professor laptop university classroom", "teacher ai classroom technology university"],
    "macro-2-5-scielo-ai-educacion-rd.png":           ["university professor research laptop office", "academic researcher reading study university", "professor office books university study"],

    # MACRO 3 — ALGORITMO DEL HOGAR
    "macro-3-0-tiktok-studytok-tag.png":              ["student phone social media studying", "teenager tiktok phone bed studying", "young person phone social media learning"],
    "macro-3-0-smiletutor-studytok.png":              ["student aesthetic notes desk study", "aesthetic study desk flat lay notes", "student colorful notes stationery desk"],
    "macro-3-0-accio-edutok-stats.png":               ["educational content creator phone video", "young person filming educational video phone", "content creator phone filming study"],
    "macro-3-1-youtube-studywithme.png":              ["study with me laptop desk lamp night", "student studying cozy desk lamp aesthetic", "student desk aesthetic lamp books studying night"],
    "macro-3-1-southeastarrow-studytok.png":          ["student filming study session phone desk", "young person recording study session", "student social media studying live stream"],
    "macro-3-2-informationmatters-genz-tiktok-search.png": ["gen z phone search information social media", "young person phone research social media", "teenager phone searching scrolling"],
    "macro-3-2-uqualio-genz-video-learning.png":      ["gen z watching video learning phone", "young person watching educational video", "student watching video tutorial laptop"],
    "macro-3-3-cto-microlearning.png":                ["short video learning phone micro content", "mobile microlearning content phone", "person watching short video phone learning"],
    "macro-3-3-nyssba-microlearning-k12.png":          ["elementary school technology classroom tablet", "kids using tablet school learning", "children classroom ipad learning technology"],
    "macro-3-3-linkedin-learning-ui.png":             ["professional online course laptop office", "business professional online learning laptop", "professional development online training laptop"],
    "macro-3-4-tiktok-careertok.png":                 ["career day in life professional video", "professional filming day in my life", "young professional filming career video phone"],
    "macro-3-4-youtube-careertok.png":                ["young professional office career lifestyle", "career advice professional mentor young", "professional showing career path workspace"],
    "macro-3-4-contentgrip-tiktok-genz.png":          ["gen z career social media content creator", "young professional content creator workplace", "teenager content creator career social media"],
    "macro-3-5-boomerang-tiktok-parental.png":        ["mother toddler learning app tablet", "mom child learning ipad together", "mother child educational app tablet home"],
    "macro-3-5-youtube-msrachel.png":                 ["toddler watching educational video screen", "child watching learning video tablet", "young child educational content screen colorful"],
}


def fetch_pexels_image_url(query: str) -> str | None:
    """Search Pexels and return a direct image URL for a portrait-ratio photo."""
    encoded = urllib.parse.quote_plus(query)
    url = f"https://www.pexels.com/search/{encoded}/"
    req = urllib.request.Request(url, headers={**HEADERS, "Accept": "text/html"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            html = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"    Fetch error for '{query}': {e}")
        return None

    # Extract photo IDs from Pexels HTML — they appear in URLs like /photo/SLUG-XXXXX/
    ids = re.findall(r'pexels\.com/photo/[^/"]+?-(\d{5,12})/', html)
    # Also try data-photo-id or similar
    ids2 = re.findall(r'"id":(\d{5,12})', html)
    ids = ids + ids2
    # Deduplicate, keep order
    seen = set()
    unique_ids = []
    for i in ids:
        if i not in seen:
            seen.add(i)
            unique_ids.append(i)

    if not unique_ids:
        return None

    # Try first 5 IDs to find one that resolves
    for photo_id in unique_ids[:5]:
        img_url = (
            f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg"
            f"?auto=compress&cs=tinysrgb&w=900&h=1320&fit=crop"
        )
        return img_url  # Return first candidate; download_image will verify

    return None


def download_image(url: str) -> bytes | None:
    """Download image bytes from URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 5000:
            return None
        return data
    except Exception as e:
        print(f"    Download error: {e}")
        return None


def crop_to_target(data: bytes) -> bytes:
    """Resize+crop image to 596x880 using PIL ImageOps.fit."""
    img = Image.open(io.BytesIO(data)).convert("RGB")
    img = ImageOps.fit(img, (W, H), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def main():
    used_hashes = {}  # md5 -> filename
    results = {"replaced": [], "failed": [], "duplicates": []}

    files = sorted(KEYWORDS.keys())
    total = len(files)
    print(f"\nStarting stock photo replacement for {total} files...\n")

    for i, filename in enumerate(files, 1):
        out_path = OUT_DIR / filename
        keywords_list = KEYWORDS[filename]
        print(f"[{i:02d}/{total}] {filename}")

        success = False
        for kw_idx, kw in enumerate(keywords_list):
            print(f"    Trying: '{kw}'")
            img_url = fetch_pexels_image_url(kw)
            if not img_url:
                print(f"    No URL found for '{kw}'")
                time.sleep(1)
                continue

            print(f"    URL: {img_url[:80]}...")
            raw = download_image(img_url)
            if not raw:
                print(f"    Download failed")
                time.sleep(1)
                continue

            cropped = crop_to_target(raw)
            h = md5(cropped)

            if h in used_hashes:
                print(f"    DUPLICATE of {used_hashes[h]} — trying next keyword")
                results["duplicates"].append(f"{filename} ~ {used_hashes[h]}")
                time.sleep(1)
                if kw_idx < len(keywords_list) - 1:
                    continue
                # Last keyword still duplicate — accept it with a note
                out_path.write_bytes(cropped)
                used_hashes[h] = filename
                results["replaced"].append(filename)
                print(f"    SAVED (accepted duplicate — no unique alternative)")
                success = True
                break

            out_path.write_bytes(cropped)
            used_hashes[h] = filename
            results["replaced"].append(filename)
            print(f"    SAVED ({len(cropped)//1024}KB, md5={h[:8]})")
            success = True
            break  # Got unique image, move on

        if not success:
            results["failed"].append(filename)
            print(f"    FAILED — all keywords exhausted")

        # Pace between requests
        time.sleep(random.uniform(0.8, 1.5))

    # ── Summary
    print("\n" + "="*60)
    print(f"REPLACED:   {len(results['replaced'])} / {total}")
    print(f"FAILED:     {len(results['failed'])}")
    print(f"DUPLICATES detected (retried): {len(results['duplicates'])}")
    if results["failed"]:
        print("\nFailed files:")
        for f in results["failed"]:
            print(f"  {f}")
    if results["duplicates"]:
        print("\nDuplicate pairs:")
        for d in results["duplicates"]:
            print(f"  {d}")

    # Final md5 uniqueness check
    print("\n── Final md5 uniqueness check ──")
    final_hashes = {}
    dup_found = []
    for f in OUT_DIR.glob("*.png"):
        if f.name == "replace_stock.py":
            continue
        h = md5(f.read_bytes())
        if h in final_hashes:
            dup_found.append(f"{f.name} == {final_hashes[h]}")
        else:
            final_hashes[h] = f.name
    if dup_found:
        print(f"DUPLICATES REMAIN: {len(dup_found)}")
        for d in dup_found:
            print(f"  {d}")
    else:
        print("CERO DUPLICADOS (md5 único por archivo)")

    print("\nDone.")


if __name__ == "__main__":
    main()
