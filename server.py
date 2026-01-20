import os
import json
import tempfile
import subprocess

from flask import Flask, render_template, request, abort, send_file
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

app = Flask(__name__)

EXIFTOOL = "exiftool"
ALLOWED = {"jpg", "jpeg", "png", "pdf"}

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


# ======================================================
# METADATA DETECTION
# ======================================================

def extract_metadata(path):
    result = subprocess.run(
        [EXIFTOOL, "-json", "-G", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    data = json.loads(result.stdout)[0]
    metadata = []

    for k, v in data.items():
        if k.lower() in ["sourcefile", "filename", "directory"]:
            continue

        lk = k.lower()
        level = "Low"

        if "gps" in lk:
            level = "Critical"
        elif "author" in lk or "creator" in lk or "software" in lk:
            level = "Medium"

        metadata.append({
            "label": k.replace(":", " "),
            "value": str(v),
            "level": level
        })

    return metadata


# ======================================================
# RISK SCORE
# ======================================================

def risk_score(metadata):
    critical = 0
    medium = 0

    for m in metadata:
        if m["level"] == "Critical":
            critical += 1
        elif m["level"] == "Medium":
            medium += 1

    score = (critical * 35) + (medium * 15)
    return min(score, 100)


# ======================================================
# SAFE REBUILD
# ======================================================

def rebuild_file(src, dst):
    ext = src.rsplit(".", 1)[-1].lower()

    if ext in ["jpg", "jpeg", "png"]:
        img = Image.open(src)
        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))
        clean.save(dst)

    elif ext == "pdf":
        reader = PdfReader(src)
        writer = PdfWriter()

        for p in reader.pages:
            writer.add_page(p)

        writer.add_metadata({})
        with open(dst, "wb") as f:
            writer.write(f)


# ======================================================
# ROUTES
# ======================================================

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    f = request.files.get("file")
    if not f:
        abort(400)

    ext = f.filename.rsplit(".", 1)[-1].lower()
    if ext not in ALLOWED:
        abort(400)

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix="." + ext)
    tmp.close()
    f.save(tmp.name)

    metadata = extract_metadata(tmp.name)
    exposure = risk_score(metadata)

    return render_template(
        "analysis.html",
        metadata=metadata,
        exposure=exposure,
        temp_path=tmp.name
    )


@app.route("/sanitize", methods=["POST"])
def sanitize():
    src = request.form.get("temp_path")
    share = request.form.get("share", "internal")

    if not src or not os.path.exists(src):
        return "Invalid file", 400

    ext = src.rsplit(".", 1)[-1].lower()
    out = tempfile.NamedTemporaryFile(delete=False, suffix="." + ext)
    out.close()

    rebuild_file(src, out.name)
    os.remove(src)

    return send_file(
        out.name,
        as_attachment=True,
        download_name=f"clean_{share}.{ext}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
