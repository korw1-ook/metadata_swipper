# 🛡️ MetadataTotal — Metadata Privacy & Exposure Analyzer

> Detect. Assess. Sanitize.  
> A privacy-focused metadata analysis and protection web application.

---

## 🚀 Overview

**MetadataTotal** is a Flask-based web application designed to identify and mitigate privacy risks caused by hidden metadata inside digital files.

Images and documents often contain invisible information that may unintentionally expose personal identity, geographic location, device fingerprints, or editing history.  
MetadataTotal enables users to analyze this data and safely remove it before sharing files online.

---

## 🔍 What MetadataTotal Detects

- 📍 GPS coordinates and location data  
- 👤 Author and creator identity  
- 🧰 Editing software fingerprints  
- 📷 Camera and device information  
- 📄 Embedded PDF document metadata  

Each detected field is analyzed to determine potential privacy exposure.

---

## ✨ Core Features

### 🔎 Metadata Detection
- Forensic-grade analysis using **ExifTool (read-only)**
- Supports image and document metadata inspection
- Detects EXIF, XMP, IPTC, and document metadata

### 📊 Exposure Risk Analysis
- Severity-based scoring engine
- Low / Medium / Critical classification
- Visual exposure percentage indicator

### 🧠 Privacy Intelligence
- Identifies identity leakage
- Detects GPS and location exposure
- Flags device fingerprinting and edit history

### 🧼 Safe Metadata Sanitization
- No destructive overwriting
- No structure modification
- Files are rebuilt cleanly
- Original quality and integrity preserved

### 📥 Secure Download
- Internal / External / Public sharing profiles
- One-click sanitized file export
- Temporary file processing only

---

## 📁 Supported File Types

| File Type | Detection | Safe Cleaning |
|----------|-----------|----------------|
| JPG | ✅ | ✅ |
| JPEG | ✅ | ✅ |
| PNG | ✅ | ✅ |
| PDF | ✅ | ✅ |

---

## ⚠️ Why MetadataTotal Is Different

Many metadata cleaners directly strip internal file structures, which often results in corrupted images or broken documents.

MetadataTotal follows a **safe rebuild methodology**:
- Metadata is extracted in read-only mode
- Original content is reconstructed cleanly
- File structure and integrity remain intact

This approach reflects professional privacy and digital forensic workflows.

---

## 🏗️ Application Flow

