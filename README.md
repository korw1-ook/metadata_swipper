# 🛡️ MetadataTotal  
**Metadata Privacy & Exposure Analysis Tool**

---

## Overview

Modern files often contain **hidden metadata** that users are unaware of when sharing documents or images online.

This metadata can silently expose:

- GPS location
- Device information
- Author identity
- Editing history
- Software fingerprints

**MetadataTotal** is a forensic-style web application built with Flask that detects and safely removes sensitive metadata while preserving file integrity.

The project focuses on **privacy risk analysis**, not just metadata cleaning.

---

## Problem Statement

Most users assume that deleting visible content is enough before sharing a file.

In reality, metadata can reveal:

- where a photo was taken  
- which device was used  
- who created or edited the file  
- what software processed it  

This information is frequently exploited during:

- OSINT investigations  
- digital profiling  
- identity correlation  
- social engineering reconnaissance  

MetadataTotal addresses this problem by providing **visibility, risk scoring, and safe sanitization**.

---

## Key Capabilities

### Metadata Detection
- Forensic-grade metadata extraction using ExifTool (read-only)
- EXIF, XMP, IPTC, and document metadata support
- GPS coordinate identification
- Author and creator attribution detection
- Software and device fingerprint analysis

### Exposure Risk Assessment
- Severity-based classification:
  - Low
  - Medium
  - Critical
- Exposure percentage calculation
- Visual risk representation

### Safe Metadata Removal
- No destructive overwriting
- No EXIF tampering
- File rebuilt cleanly
- Maintains original image or document integrity

### Privacy-Focused Workflow
- Temporary file processing only
- No permanent storage
- No third-party services
- Local execution supported

---

## Architecture Flow

```
User Upload
     ↓
Metadata Extraction (ExifTool - Read Only)
     ↓
Risk Classification Engine
     ↓
Exposure Score Calculation
     ↓
User Sharing Policy Selection
     ↓
Safe File Rebuild
     ↓
Clean File Download
```

---

## Supported File Types

| File Type | Detection | Safe Cleaning |
|----------|------------|----------------|
| JPG | ✅ | ✅ |
| JPEG | ✅ | ✅ |
| PNG | ✅ | ✅ |
| PDF | ✅ | ✅ |

---

## Technology Stack

| Layer | Technology |
|------|-------------|
| Backend | Python, Flask |
| Metadata Engine | ExifTool |
| Image Processing | Pillow |
| PDF Processing | PyPDF2 |
| Frontend | HTML, CSS, JavaScript |
| Platform | Cross-platform (Windows / Linux) |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/MetadataTotal.git
cd MetadataTotal
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install ExifTool

Download from:

https://exiftool.org

Rename:

```
exiftool(-k).exe → exiftool.exe
```

Place it either:

- in the project root  
- or in your system PATH  

---

### 4. Run the application

```bash
python app.py
```

Access in browser:

```
http://127.0.0.1:5000
```

---

## Privacy & Security Design

- Files processed in temporary directories
- No metadata stored permanently
- No cloud uploads
- No external APIs
- No user tracking

The tool is intentionally designed to minimize data exposure during analysis.

---

## Disclaimer

This project is intended for:

- cybersecurity education
- privacy awareness
- forensic learning
- defensive research

It must not be used for illegal surveillance, unauthorized investigation, or privacy violation.

---

## Learning Value

This project demonstrates practical understanding of:

- metadata forensics
- privacy threat modeling
- OSINT exposure analysis
- secure file handling
- safe sanitization techniques
- Flask backend architecture
- cybersecurity-oriented UI design

---

## Author

**Korounganba**  
Cybersecurity Student  
Focus Areas:  
Privacy Engineering · Digital Forensics · Security Analysis

---

