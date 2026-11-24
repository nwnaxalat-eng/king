from flask import Flask, request, jsonify, send_from_directory
from urllib.parse import urlparse
from rahad_all_downloader import alldl
import logging

app = Flask(__name__, static_folder="static")
logging.basicConfig(level=logging.INFO)

def valid_tiktok_url(url):
    try:
        p = urlparse(url)
        host = (p.hostname or "").lower()
        return p.scheme in ("http", "https") and (host == "tiktok.com" or host.endswith(".tiktok.com"))
    except Exception:
        return False

@app.get("/")
def home():
    return send_from_directory("static", "index.html")

@app.get("/health")
def health():
    return jsonify({"ok": True, "service": "KING"})

@app.post("/api/tiktok")
def tiktok():
    data = request.get_json(silent=True) or {}
    url = (data.get("url") or "").strip()
    if not valid_tiktok_url(url):
        return jsonify({"success": False, "error": "تکایە لینکی دروستی TikTok بنووسە."}), 400
    try:
        result = alldl.tiktok(url)
        if not isinstance(result, dict) or not result.get("videoUrl"):
            return jsonify({"success": False, "error": "لینکی ڤیدیۆ نەدۆزرایەوە. دواتر هەوڵ بدەرەوە."}), 502
        return jsonify({"success": True, "video_url": result["videoUrl"]})
    except Exception:
        app.logger.exception("TikTok provider failed")
        return jsonify({"success": False, "error": "سێرڤەری داگرتنی TikTok وەڵام ناداتەوە."}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
