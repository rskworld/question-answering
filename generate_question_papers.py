# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset
    Description: Generate PDF question papers for all classes/levels with previous year papers
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    This script generates question papers in PDF format for different classes and years.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import os
import json

# Author Information
AUTHOR_INFO = {
    "name": "Molla Samser",
    "website": "https://rskworld.in",
    "email": "help@rskworld.in",
    "phone": "+91 93305 39277"
}

# Question paper templates for different classes
QUESTION_TEMPLATES = {
    "Class 1": {
        "subjects": ["English", "Mathematics", "General Knowledge"],
        "questions_per_subject": 10,
        "marks_per_question": 1,
        "total_marks": 30
    },
    "Class 2": {
        "subjects": ["English", "Mathematics", "Science", "General Knowledge"],
        "questions_per_subject": 15,
        "marks_per_question": 1,
        "total_marks": 60
    },
    "Class 3": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 20,
        "marks_per_question": 1,
        "total_marks": 80
    },
    "Class 4": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 25,
        "marks_per_question": 1,
        "total_marks": 100
    },
    "Class 5": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 25,
        "marks_per_question": 2,
        "total_marks": 200
    },
    "Class 6": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 30,
        "marks_per_question": 2,
        "total_marks": 240
    },
    "Class 7": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 30,
        "marks_per_question": 2,
        "total_marks": 240
    },
    "Class 8": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 30,
        "marks_per_question": 2,
        "total_marks": 240
    },
    "Class 9": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 40,
        "marks_per_question": 2,
        "total_marks": 320
    },
    "Class 10": {
        "subjects": ["English", "Mathematics", "Science", "Social Studies"],
        "questions_per_subject": 50,
        "marks_per_question": 2,
        "total_marks": 400
    },
    "Class 11": {
        "subjects": ["English", "Mathematics", "Physics", "Chemistry", "Biology"],
        "questions_per_subject": 30,
        "marks_per_question": 3,
        "total_marks": 450
    },
    "Class 12": {
        "subjects": ["English", "Mathematics", "Physics", "Chemistry", "Biology"],
        "questions_per_subject": 30,
        "marks_per_question": 3,
        "total_marks": 450
    }
}

# Sample questions database
SAMPLE_QUESTIONS = {
    "Class 1": {
        "English": [
            "What is the first letter of the alphabet?",
            "Fill in the blank: C__T (cat)",
            "Which word rhymes with 'cat'?",
            "What comes after 'B'?",
            "Spell the word: DOG"
        ],
        "Mathematics": [
            "What is 2 + 3?",
            "Count the apples: 🍎🍎🍎",
            "What is 5 - 2?",
            "Which number comes after 9?",
            "What is 1 + 1?"
        ],
        "General Knowledge": [
            "How many days are in a week?",
            "What color is the sun?",
            "Which animal says 'meow'?",
            "How many fingers do you have?",
            "What do we use to see?"
        ]
    },
    "Class 2": {
        "English": [
            "Make a sentence with the word 'happy'.",
            "What is the opposite of 'big'?",
            "Identify the noun: The cat is sleeping.",
            "Fill in: I __ going to school.",
            "What is a verb?"
        ],
        "Mathematics": [
            "What is 10 + 5?",
            "What is 20 - 8?",
            "Count by 2s: 2, 4, __, __",
            "What is 3 × 2?",
            "Which is bigger: 15 or 20?"
        ],
        "Science": [
            "What do plants need to grow?",
            "Name three parts of a plant.",
            "What is the source of light during the day?",
            "Which sense do we use to smell?",
            "What happens to water when it freezes?"
        ],
        "General Knowledge": [
            "How many months are in a year?",
            "What is the capital of India?",
            "Which planet do we live on?",
            "How many continents are there?",
            "What is the largest ocean?"
        ]
    }
}

def generate_sample_questions(class_level, subject, count):
    """Generate sample questions for a subject."""
    questions = []
    base_questions = SAMPLE_QUESTIONS.get(class_level, {}).get(subject, [])
    
    # If we have base questions, use them and extend
    for i in range(count):
        if i < len(base_questions):
            questions.append(f"{i+1}. {base_questions[i]}")
        else:
            # Generate generic questions
            questions.append(f"{i+1}. [Sample Question {i+1} for {subject}]")
    
    return questions

def create_question_paper(class_level, year, output_dir="question-papers"):
    """Create a PDF question paper for a specific class and year."""
    
    # Create directory structure
    class_dir = os.path.join(output_dir, class_level.replace(" ", "-"))
    year_dir = os.path.join(class_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)
    
    # File path
    filename = f"{class_level.replace(' ', '-')}-Question-Paper-{year}.pdf"
    filepath = os.path.join(year_dir, filename)
    
    # Create PDF
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#283593'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    normal_style = styles['Normal']
    
    # Header
    story.append(Paragraph(f"<b>{class_level} - Question Paper {year}</b>", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Exam Information
    exam_info = [
        ["Exam Year:", str(year)],
        ["Class:", class_level],
        ["Date:", datetime.now().strftime("%d/%m/%Y")],
        ["Total Marks:", str(QUESTION_TEMPLATES[class_level]["total_marks"])],
        ["Time Duration:", "2 Hours"]
    ]
    
    info_table = Table(exam_info, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e3f2fd')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Instructions
    story.append(Paragraph("<b>General Instructions:</b>", heading_style))
    instructions = [
        "1. All questions are compulsory.",
        "2. Read all questions carefully before answering.",
        "3. Write your answers clearly and legibly.",
        "4. Check your answers before submitting.",
        "5. Use black or blue pen only."
    ]
    for instruction in instructions:
        story.append(Paragraph(instruction, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Questions by Subject
    template = QUESTION_TEMPLATES[class_level]
    question_num = 1
    
    for subject in template["subjects"]:
        story.append(Paragraph(f"<b>Section {template['subjects'].index(subject) + 1}: {subject}</b>", heading_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Generate questions
        questions = generate_sample_questions(class_level, subject, template["questions_per_subject"])
        
        for q in questions:
            story.append(Paragraph(q, normal_style))
            story.append(Spacer(1, 0.1*inch))
        
        story.append(Spacer(1, 0.2*inch))
    
    # Footer with author info
    story.append(Spacer(1, 0.5*inch))
    footer_text = f"""
    <i>Question Paper prepared by: {AUTHOR_INFO['name']}<br/>
    Website: {AUTHOR_INFO['website']} | Email: {AUTHOR_INFO['email']} | Phone: {AUTHOR_INFO['phone']}</i>
    """
    story.append(Paragraph(footer_text, styles['Italic']))
    
    # Build PDF
    doc.build(story)
    print(f"Generated: {filepath}")
    return filepath

def create_answer_key(class_level, year, output_dir="question-papers"):
    """Create answer key PDF for a question paper."""
    
    # Create directory structure
    class_dir = os.path.join(output_dir, class_level.replace(" ", "-"))
    year_dir = os.path.join(class_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)
    
    # File path
    filename = f"{class_level.replace(' ', '-')}-Answer-Key-{year}.pdf"
    filepath = os.path.join(year_dir, filename)
    
    # Create PDF
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=30,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#283593'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    normal_style = styles['Normal']
    answer_style = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        textColor=colors.HexColor('#2e7d32'),
        leftIndent=20
    )
    
    # Header
    story.append(Paragraph(f"<b>{class_level} - Answer Key {year}</b>", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Answer Key by Subject
    template = QUESTION_TEMPLATES[class_level]
    
    for subject in template["subjects"]:
        story.append(Paragraph(f"<b>{subject} - Answers</b>", heading_style))
        story.append(Spacer(1, 0.1*inch))
        
        # Generate sample answers
        num_questions = template["questions_per_subject"]
        for i in range(1, num_questions + 1):
            answer_text = f"Q{i}: [Answer {i} for {subject}]"
            story.append(Paragraph(answer_text, answer_style))
            story.append(Spacer(1, 0.05*inch))
        
        story.append(Spacer(1, 0.2*inch))
    
    # Footer
    story.append(Spacer(1, 0.5*inch))
    footer_text = f"""
    <i>Answer Key prepared by: {AUTHOR_INFO['name']}<br/>
    Website: {AUTHOR_INFO['website']} | Email: {AUTHOR_INFO['email']} | Phone: {AUTHOR_INFO['phone']}</i>
    """
    story.append(Paragraph(footer_text, styles['Italic']))
    
    # Build PDF
    doc.build(story)
    print(f"Generated: {filepath}")
    return filepath

def generate_all_question_papers(years=[2020, 2021, 2022, 2023, 2024, 2025]):
    """Generate question papers for all classes and years."""
    
    print("=" * 60)
    print("Generating Question Papers for All Classes")
    print(f"Author: {AUTHOR_INFO['name']} - {AUTHOR_INFO['website']}")
    print("=" * 60)
    
    generated_files = []
    
    for class_level in QUESTION_TEMPLATES.keys():
        print(f"\nGenerating papers for {class_level}...")
        for year in years:
            try:
                qp_path = create_question_paper(class_level, year)
                ak_path = create_answer_key(class_level, year)
                generated_files.append({
                    "class": class_level,
                    "year": year,
                    "question_paper": qp_path,
                    "answer_key": ak_path
                })
            except Exception as e:
                print(f"Error generating {class_level} {year}: {e}")
    
    # Save metadata
    metadata_file = os.path.join("question-papers", "metadata.json")
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump({
            "_metadata": {
                "project": "Question Answering Dataset - Question Papers",
                "author": AUTHOR_INFO['name'],
                "website": AUTHOR_INFO['website'],
                "contact": AUTHOR_INFO['email'],
                "phone": AUTHOR_INFO['phone']
            },
            "generated_files": generated_files,
            "total_papers": len(generated_files)
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'=' * 60}")
    print(f"Generated {len(generated_files)} question papers with answer keys")
    print(f"{'=' * 60}")
    
    return generated_files

if __name__ == "__main__":
    # Generate papers for recent years
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    generate_all_question_papers(years)

