# 🔐 MetadataTotal  
### Metadata Privacy & Exposure Analysis Platform

MetadataTotal is a cybersecurity-focused web application designed to identify, assess, and safely neutralize hidden metadata inside digital files before they are shared.

The project addresses a critical privacy risk often overlooked by users — **embedded metadata leakage** — and demonstrates applied knowledge of digital forensics, privacy engineering, and secure file handling.

---

## 🧠 Problem Statement

Files shared online frequently contain invisible metadata such as:

- GPS coordinates revealing physical location  
- Author and creator identities  
- Device and camera fingerprints  
- Editing software history  
- Document creation timelines  

This information can expose individuals, organizations, and operational environments without their awareness.

MetadataTotal was built to **detect these risks, quantify exposure, and eliminate sensitive metadata without corrupting the original file content**.

---

## 🎯 Project Objectives

- Detect forensic metadata using industry-standard tools  
- Classify metadata based on privacy impact  
- Calculate realistic exposure risk percentage  
- Apply sharing-based sanitization policies  
- Preserve original file integrity  
- Ensure zero file retention  

---

## 🚀 Key Capabilities

- 🔍 Deep metadata inspection via ExifTool  
- 🧪 Risk classification (Low / Medium / Critical)  
- 📊 Dynamic exposure scoring system  
- 🧠 Sharing-context privacy policy model  
- 🛡 Safe file reconstruction (no corruption)  
- 📥 Secure download of sanitized files  
- ❌ No database  
- ❌ No permanent file storage  
- ❌ No user tracking  

---

## 🧬 Supported File Formats

| File Type | Metadata Detection | Safe Cleaning |
|----------|-------------------|----------------|
| JPG | ✅ | ✅ |
| JPEG | ✅ | ✅ |
| PNG | ✅ | ✅ |
| PDF | ✅ | ✅ |

---

## 🧱 System Architecture

```
User Upload
     │
     ▼
Temporary In-Memory File
     │
     ▼
ExifTool Metadata Extraction
     │
     ▼
Metadata Classification Engine
     │
     ▼
Exposure Risk Calculation
     │
     ▼
Sharing Policy Selection
     │
     ▼
Safe File Rebuild Engine
     │
     ▼
Sanitized File Download
```

All files are deleted immediately after processing.

---

## 🧪 Detection Methodology

MetadataTotal uses **ExifTool**, a forensic-grade utility widely adopted by:

- Digital forensic investigators  
- Incident response teams  
- SOC analysts  
- Cybercrime laboratories  

Detected metadata includes:

- GPS coordinates  
- Camera and device identifiers  
- Editing software fingerprints  
- Author and creator identity  
- Embedded document properties  

Each metadata field is evaluated and categorized by privacy impact.

---

## 📊 Exposure Scoring Logic

Risk scoring is calculated dynamically to avoid misleading results.

| Risk Level | Interpretation |
|----------|----------------|
| Low | Minimal privacy impact |
| Medium | Identifiable information present |
| Critical | High-risk personal or location exposure |

This prevents false alerts such as reporting high risk when only harmless metadata exists.

---

## 🧹 Sanitization Strategy (No File Corruption)

MetadataTotal does **not directly strip metadata blocks**, which commonly causes broken or unreadable files.

Instead, it uses a **secure rebuild approach**:

### Image Files
- Pixel data is reconstructed
- Metadata containers are excluded
- Visual output remains identical

### PDF Files
- Pages are reassembled
- Metadata dictionaries removed
- Document structure preserved

This guarantees:

- No file corruption  
- No format damage  
- No preview issues  

---

## ⚙️ Local Installation (Linux)

Designed for Linux environments and suitable for VPS deployment.

```bash
git clone https://github.com/korw1-ook/MetadataTotal.git
cd MetadataTotal

python3 -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt
sudo apt install exiftool -y

python3 server.py
```

Access the application at:

```
http://127.0.0.1:5000
```

---

## 🧰 Technology Stack

- **Backend:** Python (Flask)  
- **Metadata Engine:** ExifTool  
- **Image Processing:** Pillow  
- **PDF Processing:** PyPDF2  
- **Frontend:** HTML5, CSS3  
- **Platform:** Linux  
- **Deployment:** Production-ready  

---

## 🔐 Privacy & Security Design

MetadataTotal follows strict privacy-first principles:

- Files processed temporarily only  
- No persistent storage  
- No database usage  
- No logging of user content  
- Immediate deletion after download  

The application is safe for demonstrations, testing, and controlled environments.

---

## 🎓 Learning Outcomes

This project demonstrates practical understanding of:

- Digital forensics fundamentals  
- Metadata exposure analysis  
- Privacy risk modeling  
- Secure file handling  
- Temporary file isolation  
- Defensive cybersecurity engineering  

---

## ⚠️ Disclaimer

This tool is intended strictly for:

- Educational purposes  
- Privacy analysis  
- Defensive cybersecurity research  

It must not be used to evade lawful investigations or violate applicable regulations.

The author assumes no responsibility for misuse.

---

## 👤 Author

**Korounganba**  
Cybersecurity Student  

Focus Areas:

- Digital Forensics  
- Privacy Engineering  
- Threat Detection  
- Security Tool Development  

---

> *If metadata exists, exposure exists — until it is removed.*
