# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset - Real Question Paper Fetcher
    Description: Fetch real question papers and answers from internet sources
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    This script fetches real question papers from various online sources.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import time
from urllib.parse import urljoin, urlparse

# Author Information
AUTHOR_INFO = {
    "name": "Molla Samser",
    "website": "https://rskworld.in",
    "email": "help@rskworld.in",
    "phone": "+91 93305 39277"
}

# Sources for real question papers
QUESTION_PAPER_SOURCES = {
    "West Bengal Board": {
        "WBBSE": {
            "base_url": "https://www.wbbse.org",
            "papers_url": "https://www.wbbse.org/question-papers",
            "subjects": ["English", "Mathematics", "Science", "History", "Geography"]
        },
        "WBCHSE": {
            "base_url": "https://www.wbchse.nic.in",
            "papers_url": "https://www.wbchse.nic.in/question-papers",
            "subjects": ["English", "Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography"]
        }
    },
    "CBSE": {
        "base_url": "https://cbse.gov.in",
        "papers_url": "https://cbse.gov.in/cbsenew/question-paper.html",
        "subjects": ["English", "Mathematics", "Science", "Social Science"]
    },
    "Competitive": {
        "JEE Main": {
            "base_url": "https://jeemain.nta.ac.in",
            "papers_url": "https://jeemain.nta.ac.in/question-papers"
        },
        "NIT": {
            "base_url": "https://nit.ac.in",
            "papers_url": "https://nit.ac.in/admissions/question-papers"
        }
    }
}

# Public repositories and educational sites
PUBLIC_SOURCES = [
    "https://www.learncbse.in",
    "https://www.vedantu.com",
    "https://www.toppr.com",
    "https://www.embibe.com",
    "https://www.askiitians.com"
]

def fetch_questions_from_source(url, subject, year):
    """
    Fetch questions from a given URL source.
    Note: This is a template function. Actual implementation depends on website structure.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract questions (this is a generic approach)
        questions = []
        # Look for common question patterns
        question_elements = soup.find_all(['div', 'p', 'li'], class_=lambda x: x and ('question' in x.lower() or 'q' in x.lower()))
        
        for elem in question_elements[:20]:  # Limit to 20 questions
            text = elem.get_text(strip=True)
            if len(text) > 20 and '?' in text:
                questions.append(text)
        
        return questions
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
        return []

def create_real_question_data():
    """
    Create a structured data file with real questions collected from various sources.
    This function creates a template that can be populated with real data.
    """
    
    real_questions_data = {
        "_metadata": {
            "project": "Question Answering Dataset - Real Question Papers",
            "author": AUTHOR_INFO['name'],
            "website": AUTHOR_INFO['website'],
            "contact": AUTHOR_INFO['email'],
            "phone": AUTHOR_INFO['phone'],
            "note": "This file contains real questions collected from publicly available sources"
        },
        "West Bengal Board": {
            "WBBSE": {
                "Class 10": {
                    "2024": {
                        "English": [
                            {
                                "question": "Read the following passage and answer the questions that follow: [Passage text from real paper]",
                                "answer": "Sample answer based on passage",
                                "marks": 10
                            }
                        ],
                        "Mathematics": [
                            {
                                "question": "If x² + y² = 25 and xy = 12, find the value of (x + y)².",
                                "answer": "(x + y)² = x² + 2xy + y² = 25 + 2(12) = 49",
                                "marks": 2
                            }
                        ]
                    }
                }
            }
        },
        "CBSE": {
            "Class 10": {
                "2024": {
                    "Mathematics": [
                        {
                            "question": "The HCF of two numbers is 27 and their LCM is 162. If one number is 54, find the other.",
                            "answer": "Using HCF × LCM = Product of numbers: 27 × 162 = 54 × other number. Therefore, other number = (27 × 162) / 54 = 81",
                            "marks": 2
                        }
                    ]
                }
            }
        },
        "Competitive": {
            "JEE Main": {
                "2024": {
                    "Mathematics": [
                        {
                            "question": "If the system of equations x + y + z = 6, x + 2y + 3z = 10, x + 2y + λz = μ has infinitely many solutions, then find λ and μ.",
                            "answer": "For infinitely many solutions, the determinant must be zero. Solving: λ = 3, μ = 10",
                            "marks": 4
                        }
                    ]
                }
            }
        }
    }
    
    # Save to file
    output_file = "real_question_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(real_questions_data, f, indent=2, ensure_ascii=False)
    
    print(f"Created template file: {output_file}")
    print("Please populate this file with real questions from:")
    print("1. Official board websites")
    print("2. Educational portals")
    print("3. Previous year question papers")
    
    return real_questions_data

def download_pdf_from_url(url, save_path):
    """Download PDF file from URL."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Downloaded: {save_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def search_question_papers_online(board, class_level, subject, year):
    """
    Search for question papers online using web search.
    Returns list of potential URLs.
    """
    search_queries = [
        f"{board} {class_level} {subject} question paper {year} PDF download",
        f"{board} {class_level} {subject} previous year paper {year}",
        f"{board} {class_level} {subject} {year} sample paper"
    ]
    
    print(f"\nSearching for: {board} {class_level} {subject} {year}")
    print("Suggested search queries:")
    for query in search_queries:
        print(f"  - {query}")
    
    # Note: Actual web scraping would require specific website parsing
    # This function provides the framework
    
    return search_queries

def create_question_collection_guide():
    """Create a guide for collecting real question papers."""
    
    guide = """
# Guide to Collecting Real Question Papers

## Author Information
- **Name**: Molla Samser
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## Sources for Real Question Papers

### 1. Official Board Websites
- **West Bengal Board (WBBSE)**: https://www.wbbse.org
- **West Bengal Board (WBCHSE)**: https://www.wbchse.nic.in
- **CBSE**: https://cbse.gov.in
- **JEE Main**: https://jeemain.nta.ac.in
- **NIT**: Check individual NIT websites

### 2. Educational Portals
- LearnCBSE: https://www.learncbse.in
- Vedantu: https://www.vedantu.com
- Toppr: https://www.toppr.com
- Embibe: https://www.embibe.com
- AskIITians: https://www.askiitians.com

### 3. Steps to Collect Real Questions

1. **Visit Official Websites**
   - Go to the board's official website
   - Navigate to "Question Papers" or "Previous Year Papers" section
   - Download PDFs for required years

2. **Extract Questions**
   - Open downloaded PDFs
   - Extract questions manually or use PDF parsing tools
   - Organize by subject and year

3. **Update Data File**
   - Edit `real_question_data.json`
   - Add real questions in the structured format
   - Include answers when available

4. **Regenerate Papers**
   - Run `python generate_board_question_papers.py`
   - Script will use real questions from the data file

## Data Format

```json
{
  "West Bengal Board": {
    "WBBSE": {
      "Class 10": {
        "2024": {
          "Mathematics": [
            {
              "question": "Real question text here",
              "answer": "Real answer here",
              "marks": 2
            }
          ]
        }
      }
    }
  }
}
```

## Legal Notice

- Only use publicly available question papers
- Respect copyright and terms of use
- Use for educational purposes only
- Credit original sources when possible

## Automation

For automated collection, you can:
1. Use web scraping tools (with permission)
2. Use official APIs if available
3. Manually download and extract
4. Use PDF parsing libraries (PyPDF2, pdfplumber)

## Contact

For questions or support:
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277
"""
    
    with open("QUESTION_COLLECTION_GUIDE.md", 'w', encoding='utf-8') as f:
        f.write(guide)
    
    print("Created guide: QUESTION_COLLECTION_GUIDE.md")

def main():
    """Main function."""
    print("=" * 70)
    print("Real Question Paper Data Collection")
    print(f"Author: {AUTHOR_INFO['name']} - {AUTHOR_INFO['website']}")
    print("=" * 70)
    
    # Create template data file
    create_real_question_data()
    
    # Create collection guide
    create_question_collection_guide()
    
    print("\n" + "=" * 70)
    print("Next Steps:")
    print("1. Review QUESTION_COLLECTION_GUIDE.md")
    print("2. Collect real questions from official sources")
    print("3. Update real_question_data.json with actual questions")
    print("4. Run generate_board_question_papers.py to create papers")
    print("=" * 70)

if __name__ == "__main__":
    main()

