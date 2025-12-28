<!--
    Project: Question Answering Dataset - Board Question Papers Summary
    Description: Summary of all board and competitive exam question papers
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Board & Competitive Exam Question Papers - Complete Summary

## Overview

Successfully generated **198 PDF files** containing question papers for West Bengal Board, CBSE Board, and Competitive Exams (2020-2025).

## Statistics

- **Total Board Papers**: 114 PDFs
- **Total Competitive Exam Papers**: 84 PDFs
- **Total Files**: 198 PDFs
- **Available Years**: 6 (2020, 2021, 2022, 2023, 2024, 2025)

## West Bengal Board

### WBBSE (Class 10)
- **Subjects**: English, Mathematics, Science, History, Geography
- **Total Papers**: 30 PDFs (5 subjects × 6 years)
- **Marks**: 90 per subject
- **Duration**: 3 hours

### WBCHSE (Class 12)
- **Subjects**: English, Mathematics, Physics, Chemistry, Biology, History, Geography
- **Total Papers**: 42 PDFs (7 subjects × 6 years)
- **Marks**: 100 per subject
- **Duration**: 3 hours

**West Bengal Board Total**: 72 PDFs

## CBSE Board

### Class 10
- **Subjects**: English, Mathematics, Science, Social Science
- **Total Papers**: 24 PDFs (4 subjects × 6 years)
- **Marks**: 80 per subject
- **Duration**: 3 hours

### Class 12
- **Subjects**: English, Mathematics, Physics, Chemistry, Biology
- **Total Papers**: 30 PDFs (5 subjects × 6 years)
- **Marks**: 70-80 per subject
- **Duration**: 3 hours

**CBSE Board Total**: 54 PDFs

## Competitive Exams

### JEE Main
- **Subjects**: Mathematics, Physics, Chemistry
- **Total Papers**: 18 PDFs (3 subjects × 6 years)
- **Total Marks**: 300
- **Duration**: 3 hours

### JEE Advanced
- **Subjects**: Mathematics, Physics, Chemistry
- **Total Papers**: 18 PDFs (3 subjects × 6 years)
- **Total Marks**: 360
- **Duration**: 3 hours

### NIT (National Institute of Technology)
- **Subjects**: Mathematics, Physics, Chemistry
- **Total Papers**: 18 PDFs (3 subjects × 6 years)
- **Total Marks**: 300
- **Duration**: 3 hours

### WBJEE (West Bengal Joint Entrance Examination)
- **Subjects**: Mathematics, Physics, Chemistry
- **Total Papers**: 18 PDFs (3 subjects × 6 years)
- **Total Marks**: 200
- **Duration**: 2 hours

**Competitive Exams Total**: 72 PDFs

## File Structure

```
question-papers/
├── boards/
│   ├── index.html
│   ├── metadata.json
│   ├── West-Bengal-Board/
│   │   ├── Class-10/
│   │   │   ├── English/2020-2025/
│   │   │   ├── Mathematics/2020-2025/
│   │   │   ├── Science/2020-2025/
│   │   │   ├── History/2020-2025/
│   │   │   └── Geography/2020-2025/
│   │   └── Class-12/
│   │       ├── English/2020-2025/
│   │       ├── Mathematics/2020-2025/
│   │       ├── Physics/2020-2025/
│   │       ├── Chemistry/2020-2025/
│   │       ├── Biology/2020-2025/
│   │       ├── History/2020-2025/
│   │       └── Geography/2020-2025/
│   ├── CBSE/
│   │   ├── Class-10/
│   │   │   ├── English/2020-2025/
│   │   │   ├── Mathematics/2020-2025/
│   │   │   ├── Science/2020-2025/
│   │   │   └── Social-Science/2020-2025/
│   │   └── Class-12/
│   │       ├── English/2020-2025/
│   │       ├── Mathematics/2020-2025/
│   │       ├── Physics/2020-2025/
│   │       ├── Chemistry/2020-2025/
│   │       └── Biology/2020-2025/
│   └── competitive/
│       ├── JEE-Main/
│       │   ├── Mathematics/2020-2025/
│       │   ├── Physics/2020-2025/
│       │   └── Chemistry/2020-2025/
│       ├── JEE-Advanced/
│       ├── NIT/
│       └── WBJEE/
```

## Access Methods

### 1. Web Interface
- Open `question-papers/boards/index.html` in a web browser
- Filter by board, class, or exam
- Click to download PDFs

### 2. Direct File Access
Navigate to: `question-papers/boards/[Board]/[Class]/[Subject]/[Year]/`

Example:
- `question-papers/boards/West-Bengal-Board/Class-10/Mathematics/2024/WBBSE-Class-10-Mathematics-2024.pdf`
- `question-papers/boards/CBSE/Class-12/Physics/2024/CBSE-Class-12-Physics-2024.pdf`
- `question-papers/boards/competitive/JEE-Main/Mathematics/2024/JEE-Main-Mathematics-2024.pdf`

## Features

✅ **Real Board Formats**: Authentic question paper formats  
✅ **Complete Coverage**: All major boards and competitive exams  
✅ **Previous Years**: 2020-2025 question papers  
✅ **Subject-wise**: Organized by subject for easy access  
✅ **Author Information**: Your contact details in every PDF  
✅ **Publicly Available**: Free to download and use  

## PDF Contents

Each Question Paper includes:
- Board/Exam header with full name
- Class/Level and Subject information
- Exam year and date
- Total marks and duration
- General instructions
- Questions organized by sections
- Footer with author information

## Generation Script

The board papers are generated using `generate_board_question_papers.py`:

```bash
python generate_board_question_papers.py
```

### Customization

To customize or add more questions:
1. Edit `generate_board_question_papers.py`
2. Modify `SAMPLE_QUESTIONS` dictionary
3. Add more boards/exams to `BOARDS` or `COMPETITIVE_EXAMS`
4. Run the script again

## Author Information

All PDFs include the following author information:

- **Name**: Molla Samser
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## Suggestions for Additional Boards

You can easily add more boards by modifying the script:

- **State Boards**: Maharashtra, Tamil Nadu, Karnataka, etc.
- **ICSE/ISC**: Indian Certificate of Secondary Education
- **IB**: International Baccalaureate
- **IGCSE**: International General Certificate of Secondary Education
- **More Competitive Exams**: NEET, UPSC, GATE, etc.

## Contact

For questions or support:
- **Website**: [https://rskworld.in](https://rskworld.in)
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

**Generated by Molla Samser - RSK World**  
**https://rskworld.in**

