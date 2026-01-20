# 🛡️ MetadataTotal  
### Metadata Privacy & Exposure Analysis Platform

> A cybersecurity-focused web tool for detecting hidden metadata risks and safely removing sensitive information without damaging file integrity.

---

<p align="center">
  <b>Digital Forensics • Privacy Engineering • Metadata Analysis</b>
</p>

---

## 🔍 Why Metadata Matters

Files shared online often contain **invisible forensic data**.

This hidden metadata can expose:

- 📍 Exact GPS coordinates  
- 👤 Author identity  
- 📷 Device and camera model  
- 🧠 Editing software fingerprints  
- 🕒 Creation and modification timelines  

These artifacts are commonly used in:

- OSINT investigations  
- Digital profiling  
- Social engineering preparation  
- Identity correlation attacks  

**MetadataTotal** makes these risks visible — before the file is shared.

---

## ⚙️ What MetadataTotal Does

✔ Detects real metadata using forensic-grade tools  
✔ Classifies exposure severity  
✔ Calculates privacy risk score  
✔ Safely removes sensitive metadata  
✔ Preserves file integrity  
✔ Works completely offline  

No cloud.  
No tracking.  
No destructive modification.

---

## 🧠 Core Features

### 🔎 Metadata Detection
- EXIF, XMP, IPTC analysis
- GPS coordinate extraction
- Author & creator discovery
- Software and device fingerprint detection
- Read-only forensic scanning

### 🚨 Exposure Risk Engine
- Severity classification:
  - **Low** – harmless data
  - **Medium** – identity indicators
  - **Critical** – location & tracking risk
- Visual exposure percentage
- Sharing safety guidance

### 🧼 Safe Sanitization
- No file corruption
- No EXIF rewriting
- Rebuild-based cleaning
- Output remains visually identical
- Compatible with forensic-safe workflows

---

## 🧩 Architecture Flow

```
Upload File
     ↓
Metadata Extraction (ExifTool - Read Only)
     ↓
Forensic Classification Engine
     ↓
Exposure Risk Calculation
     ↓
Sharing Context Selection
     ↓
Safe File Rebuild
     ↓
Clean File Download
```

---

## 📂 Supported File Types

| File Type | Metadata Detection | Safe Cleaning |
|----------|--------------------|----------------|
| JPG | ✅ | ✅ |
| JPEG | ✅ | ✅ |
| PNG | ✅ | ✅ |
| PDF | ✅ | ✅ |

---

## 🧰 Technology Stack

| Layer | Technology |
|------|-------------|
| Backend | Python · Flask |
| Metadata Engine | ExifTool |
| Image Processing | Pillow |
| PDF Handling | PyPDF2 |
| Frontend | HTML · CSS · JavaScript |
| Platform | Windows / Linux |

---

## 🚀 Installation

### 1️⃣ Clone repository
```bash
git clone https://github.com/yourusername/MetadataTotal.git
cd MetadataTotal
```

---

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install ExifTool

Download from:

https://exiftool.org

Rename:
```
exiftool(-k).exe → exiftool.exe
```

Place it in:
- project root **or**
- system PATH

---

### 4️⃣ Run the server
```bash
python app.py
```

Open:
```
http://127.0.0.1:5000
```

---

## 🔐 Privacy & Security Principles

- Temporary file handling only
- No permanent storage
- No cloud uploads
- No third-party APIs
- Local-first processing
- Designed for privacy research

This project intentionally follows **defensive security design**.

---

## 🎓 Learning Value

This project demonstrates understanding of:

- Metadata forensics
- Privacy threat modeling
- OSINT exposure risks
- Secure file handling
- Non-destructive sanitization
- Flask backend architecture
- Cybersecurity-focused UI logic

---

## ⚠️ Disclaimer

This tool is intended strictly for:

- cybersecurity education  
- digital forensics learning  
- privacy awareness  
- defensive research  

Misuse for surveillance, unauthorized tracking, or privacy invasion is not permitted.

---

## 👤 Author

**Korounganba**  
Cybersecurity Student  

Focus Areas:
- Privacy Engineering  
- Digital Forensics  
- OSINT Risk Analysis  
- Defensive Security  

---


