<!--
    Project: Question Answering Dataset
    Release Notes: Version 1.0.0
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Release Notes - Version 1.0.0

## 🎉 Initial Release

**Release Date**: December 28, 2025  
**Version**: 1.0.0  
**Author**: Molla Samser  
**Website**: [https://rskworld.in](https://rskworld.in)

---

## 📦 What's Included

### Core Dataset Files
- ✅ `squad_format.json` - SQuAD 2.0 format dataset
- ✅ `dataset.csv` - CSV format dataset
- ✅ `contexts.json` - Context passages
- ✅ `questions.json` - Questions dataset
- ✅ `answers.json` - Answers dataset

### Question Papers Structure
- ✅ **General Papers**: Class 1-12 (Structure ready for real papers)
- ✅ **West Bengal Board**: WBBSE (Class 10) & WBCHSE (Class 12)
- ✅ **CBSE Board**: Class 10 & Class 12
- ✅ **Competitive Exams**: JEE Main, JEE Advanced, NIT, WBJEE
- ✅ **Years**: 2020, 2021, 2022, 2023, 2024, 2025

### Web Interface
- ✅ `index.html` - Main landing page
- ✅ `question-papers/index.html` - Question papers browser
- ✅ `question-papers/boards/index.html` - Board & competitive exams browser
- ✅ Responsive design with modern UI

### Python Examples
- ✅ BERT example (`examples/bert_example.py`)
- ✅ GPT example (`examples/gpt_example.py`)
- ✅ Transformers example (`examples/transformers_example.py`)

### Generation Scripts
- ✅ `generate_question_papers.py` - General question papers generator
- ✅ `generate_board_question_papers.py` - Board papers generator
- ✅ `download_real_question_papers.py` - Real papers downloader

### Documentation
- ✅ Complete README files
- ✅ Download instructions
- ✅ Setup guides
- ✅ Fix summaries

---

## 🚀 Features

### Dataset Features
- **Multiple Formats**: JSON (SQuAD), CSV
- **Multiple Domains**: Science, History, Literature, Technology, General Knowledge
- **Ready for ML**: Optimized for BERT, GPT, Transformers
- **Well Documented**: Comprehensive documentation

### Question Papers Features
- **All Classes**: Class 1 to Class 12
- **Multiple Boards**: West Bengal Board, CBSE
- **Competitive Exams**: JEE Main, JEE Advanced, NIT, WBJEE
- **Previous Years**: 2020-2025
- **Smart Download**: File existence checking
- **User-Friendly**: Clear error messages and instructions

### Technical Features
- **PDF Generation**: Automated question paper generation
- **File Management**: Organized directory structure
- **Error Handling**: Graceful handling of missing files
- **Responsive Design**: Works on all devices

---

## 📁 Project Structure

```
question-answering/
├── Core Dataset Files
│   ├── squad_format.json
│   ├── dataset.csv
│   ├── contexts.json
│   ├── questions.json
│   └── answers.json
├── Web Interface
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── Question Papers
│   ├── index.html
│   ├── boards/index.html
│   ├── real-papers/ (for real PDFs)
│   └── [Class folders]/
├── Python Examples
│   └── examples/
├── Generation Scripts
│   ├── generate_question_papers.py
│   ├── generate_board_question_papers.py
│   └── download_real_question_papers.py
└── Documentation
    └── [Multiple README and guide files]
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/rskworld/question-answering.git
cd question-answering

# Install dependencies
pip install -r requirements.txt
```

---

## 📖 Usage

### Using the Dataset
```python
import json
import pandas as pd

# Load SQuAD format
with open('squad_format.json', 'r') as f:
    dataset = json.load(f)

# Load CSV format
df = pd.read_csv('dataset.csv')
```

### Generating Question Papers
```bash
# Generate general question papers
python generate_question_papers.py

# Generate board question papers
python generate_board_question_papers.py
```

### Web Interface
- Open `index.html` in your browser
- Browse question papers at `question-papers/index.html`
- Access board papers at `question-papers/boards/index.html`

---

## 📝 Notes

- **Real Question Papers**: The structure is ready, but real PDFs need to be downloaded from official sources. See `README_REAL_PAPERS.md` for instructions.
- **Sample PDFs Removed**: All sample/template PDFs have been removed. Only structure remains.
- **File Checking**: The web interface automatically checks if PDFs exist and shows helpful messages.

---

## 🔗 Links

- **Repository**: [https://github.com/rskworld/question-answering](https://github.com/rskworld/question-answering)
- **Website**: [https://rskworld.in](https://rskworld.in)
- **Author**: Molla Samser
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

This project is maintained by RSK World. For more datasets and projects, visit [rskworld.in](https://rskworld.in).

---

**Version 1.0.0 - Initial Release**  
**Released by Molla Samser - RSK World**

