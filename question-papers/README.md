<!--
    Project: Question Answering Dataset - Question Papers
    Description: Question papers and answer keys for all classes and previous years
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Question Papers - All Classes

This directory contains question papers and answer keys for all classes (Class 1 to Class 12) from previous years (2020-2025).

## Overview

- **Total Classes**: 12 (Class 1 to Class 12)
- **Available Years**: 2020, 2021, 2022, 2023, 2024, 2025
- **Format**: PDF (Portable Document Format)
- **Total Files**: 144 PDFs
  - 72 Question Papers
  - 72 Answer Keys

## Directory Structure

```
question-papers/
├── index.html              # Browse all question papers
├── README.md              # This file
├── metadata.json          # Metadata about all generated papers
├── Class-1/
│   ├── 2020/
│   │   ├── Class-1-Question-Paper-2020.pdf
│   │   └── Class-1-Answer-Key-2020.pdf
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/
├── Class-2/
├── Class-3/
├── ... (Class 4-11)
└── Class-12/
```

## Subjects by Class

### Primary Classes (Class 1-5)
- English
- Mathematics
- Science
- General Knowledge (Class 1-2)
- Social Studies (Class 3-5)

### Middle Classes (Class 6-8)
- English
- Mathematics
- Science
- Social Studies

### Secondary Classes (Class 9-10)
- English
- Mathematics
- Science
- Social Studies

### Senior Classes (Class 11-12)
- English
- Mathematics
- Physics
- Chemistry
- Biology

## How to Use

### Browse Online
1. Open `index.html` in your web browser
2. Use filters to find papers by class or year
3. Click on "Question Paper" or "Answer Key" to download

### Direct Access
Navigate to the specific class and year folder:
```
question-papers/Class-10/2024/
```

### Generate More Papers
Run the generation script from the main directory:
```bash
python generate_question_papers.py
```

## Paper Details

Each question paper includes:
- Exam information (Year, Class, Date, Total Marks, Duration)
- General instructions
- Questions organized by subject/section
- Author information in footer

Each answer key includes:
- Answers organized by subject
- Question numbers with corresponding answers
- Author information in footer

## File Naming Convention

- **Question Papers**: `Class-[N]-Question-Paper-[YEAR].pdf`
- **Answer Keys**: `Class-[N]-Answer-Key-[YEAR].pdf`

Example:
- `Class-10-Question-Paper-2024.pdf`
- `Class-10-Answer-Key-2024.pdf`

## Technical Details

- **PDF Library**: ReportLab (Python)
- **Page Size**: A4
- **Encoding**: UTF-8
- **Font**: Helvetica (Standard PDF font)

## Author Information

All question papers and answer keys include author information:

- **Name**: Molla Samser
- **Website**: [https://rskworld.in](https://rskworld.in)
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## License

These question papers are provided for educational purposes. See the main LICENSE file for details.

## Contact

For questions, suggestions, or to report issues:

- **Website**: [https://rskworld.in](https://rskworld.in)
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## Updates

To add more question papers:
1. Edit `generate_question_papers.py`
2. Add questions to the `SAMPLE_QUESTIONS` dictionary
3. Run the script to generate new PDFs

---

**Created by Molla Samser - RSK World**  
**https://rskworld.in**

