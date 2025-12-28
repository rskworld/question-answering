<!--
    Project: Question Answering Dataset - Real Question Papers
    Description: Instructions for using real question papers instead of samples
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Real Question Papers - Setup Guide

## Important Notice

**All sample/template question papers have been removed.**

To use **REAL question papers**, please follow these steps:

## Step 1: Download Real Question Papers

### Option A: Manual Download (Recommended)

1. **Visit Official Sources:**
   - **West Bengal Board**: https://www.wbbse.org and https://www.wbchse.nic.in
   - **CBSE**: https://cbse.gov.in
   - **JEE Main**: https://jeemain.nta.ac.in
   - **WBJEE**: https://www.wbjeeb.in

2. **Download PDFs for years 2020-2025**

3. **Save to correct folders:**
   ```
   question-papers/real-papers/
   ├── boards/
   │   ├── West-Bengal-Board/
   │   │   ├── Class-10/
   │   │   │   ├── Mathematics/
   │   │   │   │   ├── 2020/
   │   │   │   │   ├── 2021/
   │   │   │   │   └── ... (2022-2025)
   │   │   │   └── [Other Subjects]/
   │   │   └── Class-12/
   │   └── CBSE/
   └── competitive/
       ├── JEE-Main/
       ├── JEE-Advanced/
       ├── NIT/
       └── WBJEE/
   ```

### Option B: Use Download Script

```bash
python download_real_question_papers.py
```

**Note**: Many websites require manual download due to:
- Login requirements
- CAPTCHA protection
- Terms of service
- Dynamic content

## Step 2: File Naming Convention

Name your downloaded PDFs as:

- **West Bengal**: `WBBSE-Class-10-Mathematics-2024.pdf`
- **CBSE**: `CBSE-Class-10-Mathematics-2024.pdf`
- **JEE Main**: `JEE-Main-Mathematics-2024.pdf`
- **NIT**: `NIT-Mathematics-2024.pdf`
- **WBJEE**: `WBJEE-Mathematics-2024.pdf`

## Step 3: Recommended Sources

### West Bengal Board

1. **Official Websites:**
   - WBBSE: https://www.wbbse.org
   - WBCHSE: https://www.wbchse.nic.in

2. **Educational Portals:**
   - LearnCBSE: https://www.learncbse.in
   - Vedantu: https://www.vedantu.com
   - Toppr: https://www.toppr.com

### CBSE Board

1. **Official**: https://cbse.gov.in
2. **LearnCBSE**: https://www.learncbse.in/cbse-previous-year-question-papers
3. **Vedantu**: https://www.vedantu.com/cbse

### Competitive Exams

1. **JEE Main:**
   - Official: https://jeemain.nta.ac.in
   - Motion: https://howrah.motion.ac.in/answer-keys-solutions.php
   - Vedantu: https://www.vedantu.com/jee-main

2. **JEE Advanced:**
   - Official: https://www.jeeadv.ac.in
   - Vedantu: https://www.vedantu.com/jee-advanced

3. **WBJEE:**
   - Official: https://www.wbjeeb.in
   - Testbook: https://testbook.com/wb-jee/previous-year-papers
   - ExamSIDE: https://questions.examside.com/past-years/year-wise/jee/wb-jee

4. **NIT:**
   - Vedantu: https://www.vedantu.com/nit
   - Embibe: https://www.embibe.com/exams/nit

## Step 4: Verify Downloads

After downloading, verify:
- ✅ PDF files are valid (open and check)
- ✅ Files are named correctly
- ✅ Files are in correct folders
- ✅ Years 2020-2025 are covered

## Step 5: Update Browse Interface

The browse interface at `question-papers/boards/index.html` will automatically show real papers once they are in the `real-papers` folder.

## Legal Notice

- ✅ Only download from official or authorized sources
- ✅ Respect copyright and terms of use
- ✅ Use for educational purposes only
- ✅ Do not redistribute copyrighted material without permission

## Current Status

- ❌ **Sample PDFs**: Removed
- ✅ **Directory Structure**: Created
- ✅ **Download Script**: Ready
- ⏳ **Real Papers**: Need to be downloaded manually

## Contact

For questions or support:
- **Author**: Molla Samser
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

**Note**: Real question papers must be downloaded manually from official sources. The script provides structure and instructions, but actual PDFs need to be obtained from board/exam websites.

