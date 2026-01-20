# 🛡️ MetadataTotal — Metadata Privacy & Exposure Analyzer

Detect. Assess. Sanitize.  
A privacy-focused metadata analysis and protection web application.

---

## Overview

MetadataTotal is a Flask-based web application designed to detect and safely remove hidden metadata from images and documents before sharing them online.

Digital files often contain invisible information such as GPS location, device details, author identity, editing software fingerprints, and timestamps.  
This tool helps users identify privacy risks and generate clean, metadata-free files without corruption.

---

## What This Tool Detects

- GPS coordinates and location data  
- Author and creator identity  
- Editing software fingerprints  
- Camera and device information  
- Embedded PDF document metadata  

Each detected field is evaluated to determine privacy exposure severity.

---

## Features

- Metadata detection using ExifTool (read-only)
- Exposure risk scoring (Low / Medium / Critical)
- Visual exposure percentage
- Safe metadata removal
- File reconstruction without corruption
- Supports JPG, JPEG, PNG, and PDF
- Temporary file handling only
- Clean and responsive user interface

---

## Supported File Types

| File Type | Detection | Cleaning |
|---------|-----------|----------|
| JPG | Yes | Yes |
| JPEG | Yes | Yes |
| PNG | Yes | Yes |
| PDF | Yes | Yes |

---

## Why MetadataTotal

Most metadata cleaners directly modify file structures, often resulting in corrupted images or broken PDF documents.

MetadataTotal follows a safer design:

- Metadata extraction is read-only
- Original content is rebuilt cleanly
- File integrity and quality are preserved

This approach reflects real-world privacy and digital forensic workflows.

---

## Application Flow

Browser  
↓  
Flask Web Application  
↓  
ExifTool Metadata Analysis  
↓  
Risk Scoring Engine  
↓  
Safe File Rebuild  
↓  
Sanitized Download  

---

## Technology Stack

- Python 3
- Flask
- ExifTool
- Pillow
- PyPDF2
- HTML / CSS

---

## Project Structure

MetadataTotal  
├── server.py  
├── templates  
│   ├── upload.html  
│   └── analysis.html  
├── static  
│   └── css  
│       ├── upload.css  
│       └── analysis.css  
├── requirements.txt  
└── README.md  

---

## Installation (Linux Recommended)

Clone the repository:

git clone https://github.com/yourusername/MetadataTotal.git  
cd MetadataTotal  

Create virtual environment:

python3 -m venv myenv  
source myenv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

Install ExifTool:

sudo apt install exiftool -y  

Run the application:

python server.py  

Open in browser:

http://127.0.0.1:5000

---

## Deployment

Designed for Linux-based hosting.

Recommended platform: Render

Build command:

apt-get update && apt-get install -y exiftool && pip install -r requirements.txt

Start command:

gunicorn server:app

---

## Privacy & Security

- Files processed temporarily
- No permanent storage
- No third-party APIs
- Privacy-first design

---

## Disclaimer

This project is intended for educational and privacy-awareness purposes only.  
Do not use this tool for unauthorized or illegal activities.

---

## Author

Korounganba  
Cybersecurity Student  
Focus: Privacy • Digital Forensics

---

