"""Post a reel from catalog.json to Instagram through the official Instagram Graph API (Reels publishing).
Run by .github/workflows/publish.yml when the repo OWNER submits a "publish: <slug> to instagram" issue.
Also runnable by hand:  python tools/publish.py <slug> instagram [--dry-run]

Needs repository secrets (Settings > Secrets and variables > Actions):
  IG_USER_ID       the Instagram professional account id (a Business/Creator account linked to a Facebook Page)
  IG_ACCESS_TOKEN  a long-lived token with instagram_basic + instagram_content_publish (Meta app)
Optional variable: IG_GRAPH_VERSION (default v21.0)
Without the secrets it does a dry run: it validates everything and says what it would post, and posts nothing.

Flow: create a REELS media container from the public video URL (GitHub Pages) -> poll until FINISHED ->
media_publish -> fetch the permalink -> mark the reel posted in catalog.json (the workflow commits it).
"""
import os, sys, json, time, argparse, pathlib, datetime, urllib.request, urllib.parse, urllib.error
sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument("slug"); ap.add_argument("platform"); ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
cat = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
reel = next((r for r in cat["reels"] if r["slug"] == a.slug), None)
if not reel: sys.exit(f"no reel '{a.slug}' in catalog.json")
if a.platform != "instagram": sys.exit(f"automatic posting supports instagram only (got {a.platform}); use the page's manual buttons for others")
if reel.get("posted", {}).get("instagram"): sys.exit(f"already posted: {reel['posted']['instagram']['url']}")

hub = cat.get("hub_url", "").rstrip("/") + "/"
abs_url = lambda key: urllib.parse.urljoin(urllib.parse.urljoin(hub, reel.get("base", "./")), reel["files"][key])
video, cover = abs_url("video"), (abs_url("thumbnail") if reel["files"].get("thumbnail") else None)
caption = (reel.get("caption", "") + ("\n\n" + " ".join("#" + t.lstrip("#") for t in reel.get("hashtags", [])) if reel.get("hashtags") else ""))[:2200]
if len(reel.get("hashtags", [])) > 5: sys.exit("more than 5 hashtags: Instagram rejects these")

# the video must be publicly reachable for Instagram to fetch it
try:
    with urllib.request.urlopen(urllib.request.Request(video, method="HEAD"), timeout=30) as r:
        assert r.status == 200, r.status
except Exception as e:
    sys.exit(f"video URL not reachable ({video}): {e}")

uid, token = os.environ.get("IG_USER_ID"), os.environ.get("IG_ACCESS_TOKEN")
ver = os.environ.get("IG_GRAPH_VERSION") or "v21.0"
print(f"reel: {reel['title']}\nvideo: {video}\ncover: {cover}\ncaption ({len(caption)} chars):\n{caption}\n")
if a.dry_run or not (uid and token):
    print("DRY RUN: IG_USER_ID / IG_ACCESS_TOKEN not set (or --dry-run). Nothing was posted.")
    sys.exit(0)

G = f"https://graph.facebook.com/{ver}"
def call(method, path, **params):
    params["access_token"] = token
    data = urllib.parse.urlencode(params).encode() if method == "POST" else None
    u = f"{G}/{path}" + ("" if method == "POST" else "?" + urllib.parse.urlencode(params))
    try:
        with urllib.request.urlopen(urllib.request.Request(u, data=data, method=method), timeout=60) as r: return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Graph API {method} {path} failed: {e.code} {e.read().decode(errors='replace')[:400]}")

params = dict(media_type="REELS", video_url=video, caption=caption, share_to_feed="true")
if cover: params["cover_url"] = cover
container = call("POST", f"{uid}/media", **params)["id"]
print("container", container)
for _ in range(60):                                   # up to ~10 minutes for Instagram to fetch and process
    st = call("GET", container, fields="status_code,status").get("status_code")
    print("status", st)
    if st == "FINISHED": break
    if st in ("ERROR", "EXPIRED"): sys.exit(f"Instagram could not process the video: {st}")
    time.sleep(10)
else:
    sys.exit("timed out waiting for Instagram to process the video")
media = call("POST", f"{uid}/media_publish", creation_id=container)["id"]
link = call("GET", media, fields="permalink").get("permalink", "")
print("posted", link)
reel.setdefault("posted", {})["instagram"] = {"url": link, "date": datetime.date.today().isoformat(), "media_id": media}
reel["status"] = "posted"
(ROOT / "catalog.json").write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as f: f.write(f"permalink={link}\n")
