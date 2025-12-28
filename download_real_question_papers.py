# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset - Real Question Paper Downloader
    Description: Download real question papers from internet sources
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    This script downloads real question papers from various online sources.
"""

import requests
import os
import json
from urllib.parse import urljoin
import time

# Author Information
AUTHOR_INFO = {
    "name": "Molla Samser",
    "website": "https://rskworld.in",
    "email": "help@rskworld.in",
    "phone": "+91 93305 39277"
}

# Real question paper sources (publicly available)
REAL_PAPER_SOURCES = {
    "West Bengal Board": {
        "WBBSE": {
            "Class 10": {
                "base_urls": [
                    "https://www.wbbse.org/question-papers",
                    "https://www.learncbse.in/west-bengal-board-class-10-question-papers",
                    "https://www.vedantu.com/question-paper/west-bengal-board-class-10"
                ],
                "subjects": ["English", "Mathematics", "Science", "History", "Geography"]
            }
        },
        "WBCHSE": {
            "Class 12": {
                "base_urls": [
                    "https://www.wbchse.nic.in/question-papers",
                    "https://www.learncbse.in/west-bengal-board-class-12-question-papers"
                ],
                "subjects": ["English", "Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography"]
            }
        }
    },
    "CBSE": {
        "Class 10": {
            "base_urls": [
                "https://cbse.gov.in/cbsenew/question-paper.html",
                "https://www.learncbse.in/cbse-previous-year-question-papers-class-10",
                "https://www.vedantu.com/cbse/previous-year-question-paper-class-10"
            ],
            "subjects": ["English", "Mathematics", "Science", "Social Science"]
        },
        "Class 12": {
            "base_urls": [
                "https://cbse.gov.in/cbsenew/question-paper.html",
                "https://www.learncbse.in/cbse-previous-year-question-papers-class-12"
            ],
            "subjects": ["English", "Mathematics", "Physics", "Chemistry", "Biology"]
        }
    },
    "Competitive": {
        "JEE Main": {
            "base_urls": [
                "https://jeemain.nta.ac.in/question-papers",
                "https://www.vedantu.com/jee-main/previous-year-question-papers",
                "https://www.embibe.com/exams/jee-main-previous-year-papers"
            ],
            "subjects": ["Mathematics", "Physics", "Chemistry"]
        },
        "JEE Advanced": {
            "base_urls": [
                "https://www.jeeadv.ac.in/question-papers",
                "https://www.vedantu.com/jee-advanced/previous-year-question-papers"
            ],
            "subjects": ["Mathematics", "Physics", "Chemistry"]
        },
        "NIT": {
            "base_urls": [
                "https://www.vedantu.com/nit/previous-year-question-papers",
                "https://www.embibe.com/exams/nit-previous-year-papers"
            ],
            "subjects": ["Mathematics", "Physics", "Chemistry"]
        },
        "WBJEE": {
            "base_urls": [
                "https://www.wbjeeb.in/question-papers",
                "https://www.vedantu.com/wbjee/previous-year-question-papers",
                "https://testbook.com/wb-jee/previous-year-papers"
            ],
            "subjects": ["Mathematics", "Physics", "Chemistry"]
        }
    }
}

# Direct download links for real question papers (2020-2025)
DIRECT_DOWNLOAD_LINKS = {
    "West Bengal Board": {
        "WBBSE-Class-10-Mathematics-2024": "https://www.wbbse.org/uploads/question_papers/2024/Class10_Mathematics_2024.pdf",
        "WBBSE-Class-10-English-2024": "https://www.wbbse.org/uploads/question_papers/2024/Class10_English_2024.pdf",
        # Add more direct links as available
    },
    "CBSE": {
        "CBSE-Class-10-Mathematics-2024": "https://cbse.gov.in/cbsenew/question-papers/2024/Class10_Math_2024.pdf",
        # Add more direct links as available
    }
}

def download_pdf(url, save_path, max_retries=3):
    """Download PDF from URL with retry mechanism."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for attempt in range(max_retries):
        try:
            print(f"Downloading: {url} (Attempt {attempt + 1})")
            response = requests.get(url, headers=headers, timeout=30, stream=True, allow_redirects=True)
            
            if response.status_code == 200:
                # Check if it's a PDF
                content_type = response.headers.get('Content-Type', '')
                if 'pdf' in content_type.lower() or url.lower().endswith('.pdf'):
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    
                    with open(save_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    
                    file_size = os.path.getsize(save_path)
                    if file_size > 1000:  # At least 1KB
                        print(f"Downloaded: {save_path} ({file_size} bytes)")
                        return True
                    else:
                        os.remove(save_path)
                        print(f"File too small, may not be valid PDF")
                else:
                    print(f"Not a PDF file (Content-Type: {content_type})")
            else:
                print(f"HTTP {response.status_code}: {url}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        
        if attempt < max_retries - 1:
            time.sleep(2)  # Wait before retry
    
    return False

def create_real_paper_structure():
    """Create directory structure for real question papers."""
    base_dir = "question-papers/real-papers"
    
    structure = {
        "boards/West-Bengal-Board": ["Class-10", "Class-12"],
        "boards/CBSE": ["Class-10", "Class-12"],
        "competitive/JEE-Main": ["Mathematics", "Physics", "Chemistry"],
        "competitive/JEE-Advanced": ["Mathematics", "Physics", "Chemistry"],
        "competitive/NIT": ["Mathematics", "Physics", "Chemistry"],
        "competitive/WBJEE": ["Mathematics", "Physics", "Chemistry"]
    }
    
    for base_path, subdirs in structure.items():
        for subdir in subdirs:
            full_path = os.path.join(base_dir, base_path, subdir)
            os.makedirs(full_path, exist_ok=True)
            print(f"Created: {full_path}")
    
    return base_dir

def download_from_direct_links():
    """Download papers from direct links if available."""
    base_dir = "question-papers/real-papers"
    downloaded = 0
    
    for board, papers in DIRECT_DOWNLOAD_LINKS.items():
        for paper_name, url in papers.items():
            try:
                # Determine save path
                if "WBBSE" in paper_name or "WBCHSE" in paper_name:
                    parts = paper_name.split("-")
                    if len(parts) >= 6:
                        class_level = parts[2] + "-" + parts[3]
                        subject = parts[4]
                        year = parts[5]
                        save_path = os.path.join(base_dir, "boards", "West-Bengal-Board", class_level, subject, year, f"{paper_name}.pdf")
                    else:
                        print(f"Skipping {paper_name}: Invalid format")
                        continue
                elif "CBSE" in paper_name:
                    parts = paper_name.split("-")
                    if len(parts) >= 5:
                        class_level = parts[1] + "-" + parts[2]
                        subject = parts[3]
                        year = parts[4]
                        save_path = os.path.join(base_dir, "boards", "CBSE", class_level, subject, year, f"{paper_name}.pdf")
                    else:
                        print(f"Skipping {paper_name}: Invalid format")
                        continue
                else:
                    continue
                
                if download_pdf(url, save_path):
                    downloaded += 1
                time.sleep(1)  # Be polite to servers
            except Exception as e:
                print(f"Error processing {paper_name}: {e}")
                continue
    
    return downloaded

def create_download_instructions():
    """Create instructions file for manual download."""
    instructions = f"""
# Instructions for Downloading Real Question Papers

## Author Information
- **Name**: {AUTHOR_INFO['name']}
- **Website**: {AUTHOR_INFO['website']}
- **Email**: {AUTHOR_INFO['email']}
- **Phone**: {AUTHOR_INFO['phone']}

## Recommended Sources for Real Question Papers

### West Bengal Board

#### WBBSE (Class 10)
1. **Official Website**: https://www.wbbse.org
   - Go to "Question Papers" section
   - Download PDFs for 2020-2025

2. **LearnCBSE**: https://www.learncbse.in/west-bengal-board-class-10-question-papers
   - Previous year papers with solutions

3. **Vedantu**: https://www.vedantu.com/question-paper/west-bengal-board-class-10
   - Free downloadable PDFs

#### WBCHSE (Class 12)
1. **Official Website**: https://www.wbchse.nic.in
   - Navigate to "Question Papers" section

2. **LearnCBSE**: https://www.learncbse.in/west-bengal-board-class-12-question-papers

### CBSE Board

#### Class 10 & 12
1. **Official Website**: https://cbse.gov.in
   - Go to "Question Papers" section
   - Download previous year papers

2. **LearnCBSE**: https://www.learncbse.in/cbse-previous-year-question-papers
   - Comprehensive collection

3. **Vedantu**: https://www.vedantu.com/cbse/previous-year-question-paper
   - Subject-wise papers

### Competitive Exams

#### JEE Main
1. **Official**: https://jeemain.nta.ac.in
2. **Vedantu**: https://www.vedantu.com/jee-main/previous-year-question-papers
3. **Embibe**: https://www.embibe.com/exams/jee-main-previous-year-papers
4. **Motion**: https://howrah.motion.ac.in/answer-keys-solutions.php

#### JEE Advanced
1. **Official**: https://www.jeeadv.ac.in
2. **Vedantu**: https://www.vedantu.com/jee-advanced/previous-year-question-papers

#### NIT
1. **Vedantu**: https://www.vedantu.com/nit/previous-year-question-papers
2. **Embibe**: https://www.embibe.com/exams/nit-previous-year-papers

#### WBJEE
1. **Official**: https://www.wbjeeb.in
2. **Testbook**: https://testbook.com/wb-jee/previous-year-papers
3. **Vedantu**: https://www.vedantu.com/wbjee/previous-year-question-papers
4. **ExamSIDE**: https://questions.examside.com/past-years/year-wise/jee/wb-jee

## Download Steps

1. **Visit the source website**
2. **Navigate to question papers section**
3. **Select year (2020-2025)**
4. **Select subject**
5. **Download PDF**
6. **Save to appropriate folder:**
   - `question-papers/real-papers/boards/[Board]/[Class]/[Subject]/[Year]/`

## File Naming Convention

- West Bengal: `WBBSE-Class-10-Mathematics-2024.pdf`
- CBSE: `CBSE-Class-10-Mathematics-2024.pdf`
- JEE Main: `JEE-Main-Mathematics-2024.pdf`
- NIT: `NIT-Mathematics-2024.pdf`
- WBJEE: `WBJEE-Mathematics-2024.pdf`

## Automated Download

Run the script:
```bash
python download_real_question_papers.py
```

Note: Some websites may require manual download due to:
- Login requirements
- CAPTCHA protection
- Dynamic content loading
- Terms of service restrictions

## Legal Notice

- Only download from official or authorized sources
- Respect copyright and terms of use
- Use for educational purposes only
- Do not redistribute copyrighted material without permission

## Contact

For questions or support:
- **Website**: {AUTHOR_INFO['website']}
- **Email**: {AUTHOR_INFO['email']}
- **Phone**: {AUTHOR_INFO['phone']}
"""
    
    with open("DOWNLOAD_REAL_PAPERS_INSTRUCTIONS.md", 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("Created: DOWNLOAD_REAL_PAPERS_INSTRUCTIONS.md")

def main():
    """Main function."""
    print("=" * 70)
    print("Real Question Paper Downloader")
    print(f"Author: {AUTHOR_INFO['name']} - {AUTHOR_INFO['website']}")
    print("=" * 70)
    
    # Create directory structure
    print("\n1. Creating directory structure...")
    base_dir = create_real_paper_structure()
    
    # Create instructions
    print("\n2. Creating download instructions...")
    create_download_instructions()
    
    # Try downloading from direct links
    print("\n3. Attempting to download from direct links...")
    downloaded = download_from_direct_links()
    
    print(f"\n{'=' * 70}")
    print(f"Downloaded {downloaded} real question papers")
    print(f"{'=' * 70}")
    print("\nNext Steps:")
    print("1. Review DOWNLOAD_REAL_PAPERS_INSTRUCTIONS.md")
    print("2. Manually download papers from recommended sources")
    print("3. Save PDFs to: question-papers/real-papers/")
    print("4. Update the system to use real papers instead of samples")
    print("=" * 70)

if __name__ == "__main__":
    main()

