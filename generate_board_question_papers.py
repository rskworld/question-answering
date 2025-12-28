# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset - Board Question Papers
    Description: Generate PDF question papers for West Bengal Board, CBSE, and Competitive Exams
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    This script generates question papers in PDF format for different boards and competitive exams.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
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

# Board configurations
BOARDS = {
    "West Bengal Board": {
        "WBBSE": {
            "full_name": "West Bengal Board of Secondary Education",
            "classes": ["Class 10"],
            "subjects": {
                "Class 10": {
                    "English": {"total_marks": 90, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Mathematics": {"total_marks": 90, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Science": {"total_marks": 90, "duration": "3 hours", "sections": ["Physics", "Chemistry", "Biology"]},
                    "History": {"total_marks": 90, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Geography": {"total_marks": 90, "duration": "3 hours", "sections": ["A", "B", "C"]}
                }
            }
        },
        "WBCHSE": {
            "full_name": "West Bengal Council of Higher Secondary Education",
            "classes": ["Class 12"],
            "subjects": {
                "Class 12": {
                    "English": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Mathematics": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Physics": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Chemistry": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Biology": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "History": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Geography": {"total_marks": 100, "duration": "3 hours", "sections": ["A", "B", "C"]}
                }
            }
        }
    },
    "CBSE": {
        "CBSE": {
            "full_name": "Central Board of Secondary Education",
            "classes": ["Class 10", "Class 12"],
            "subjects": {
                "Class 10": {
                    "English": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Mathematics": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]},
                    "Science": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]},
                    "Social Science": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]}
                },
                "Class 12": {
                    "English": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C"]},
                    "Mathematics": {"total_marks": 80, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]},
                    "Physics": {"total_marks": 70, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]},
                    "Chemistry": {"total_marks": 70, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]},
                    "Biology": {"total_marks": 70, "duration": "3 hours", "sections": ["A", "B", "C", "D", "E"]}
                }
            }
        }
    }
}

# Competitive Exams
COMPETITIVE_EXAMS = {
    "JEE Main": {
        "full_name": "Joint Entrance Examination Main",
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "total_marks": 300,
        "duration": "3 hours",
        "sections": ["Section A (MCQ)", "Section B (Numerical)"],
        "paper_type": "Paper 1 (B.E./B.Tech)"
    },
    "JEE Advanced": {
        "full_name": "Joint Entrance Examination Advanced",
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "total_marks": 360,
        "duration": "3 hours",
        "sections": ["Section 1", "Section 2", "Section 3"],
        "paper_type": "Paper 1"
    },
    "NIT": {
        "full_name": "National Institute of Technology Entrance",
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "total_marks": 300,
        "duration": "3 hours",
        "sections": ["Section A", "Section B"],
        "paper_type": "B.Tech Entrance"
    },
    "WBJEE": {
        "full_name": "West Bengal Joint Entrance Examination",
        "subjects": ["Mathematics", "Physics", "Chemistry"],
        "total_marks": 200,
        "duration": "2 hours",
        "sections": ["Category 1", "Category 2", "Category 3"],
        "paper_type": "Engineering Entrance"
    }
}

# Sample questions for different boards
SAMPLE_QUESTIONS = {
    "West Bengal Board": {
        "Class 10": {
            "English": {
                "Section A": [
                    "1. Read the following passage and answer the questions that follow:",
                    "2. Write a letter to your friend describing your visit to a historical place.",
                    "3. Change the following sentences as directed:"
                ],
                "Section B": [
                    "4. Write a paragraph on 'Importance of Education'.",
                    "5. Fill in the blanks with appropriate words:"
                ],
                "Section C": [
                    "6. Answer any two of the following questions:",
                    "7. Write a short story beginning with 'Once upon a time...'"
                ]
            },
            "Mathematics": {
                "Section A": [
                    "1. If x² + y² = 25 and xy = 12, find the value of (x + y)².",
                    "2. Solve: 2x + 3y = 7, 3x - 2y = 4",
                    "3. Find the area of a triangle with sides 5cm, 12cm, and 13cm."
                ],
                "Section B": [
                    "4. Prove that the angles opposite to equal sides of an isosceles triangle are equal.",
                    "5. In a circle, if two chords are equal, prove that their corresponding arcs are equal."
                ],
                "Section C": [
                    "6. Solve the quadratic equation: x² - 5x + 6 = 0",
                    "7. Find the value of sin 30° + cos 60° - tan 45°"
                ]
            }
        },
        "Class 12": {
            "Mathematics": {
                "Section A": [
                    "1. Evaluate: ∫(x² + 2x + 1)dx",
                    "2. Find the derivative of y = sin(x² + 1)",
                    "3. If A = [1 2; 3 4], find A⁻¹"
                ],
                "Section B": [
                    "4. Solve the differential equation: dy/dx + y = eˣ",
                    "5. Find the area bounded by the curve y = x² and the line y = 4"
                ],
                "Section C": [
                    "6. Using integration, find the area of the region bounded by the parabola y² = 4x and the line x = 4",
                    "7. Find the maximum and minimum values of f(x) = x³ - 3x² + 2"
                ]
            }
        }
    },
    "CBSE": {
        "Class 10": {
            "Mathematics": {
                "Section A": [
                    "1. The HCF of two numbers is 27 and their LCM is 162. If one number is 54, find the other.",
                    "2. Find the roots of the quadratic equation: 2x² - 7x + 3 = 0",
                    "3. In an AP, if a = 5, d = 3, find the 10th term."
                ],
                "Section B": [
                    "4. Prove that √5 is irrational.",
                    "5. Find the coordinates of the point which divides the line segment joining (2,3) and (4,5) in the ratio 2:3."
                ],
                "Section C": [
                    "6. A train travels 360 km at a uniform speed. If the speed had been 5 km/h more, it would have taken 1 hour less for the same journey. Find the speed of the train.",
                    "7. The sum of the 4th and 8th terms of an AP is 24 and the sum of the 6th and 10th terms is 44. Find the first three terms of the AP."
                ]
            }
        }
    },
    "Competitive": {
        "JEE Main": {
            "Mathematics": [
                "1. If the system of equations x + y + z = 6, x + 2y + 3z = 10, x + 2y + λz = μ has infinitely many solutions, then find λ and μ.",
                "2. The number of real roots of the equation x⁴ - 4x³ + 12x² + x - 1 = 0 is:",
                "3. Let f(x) = x² + x + 1, x ∈ R. The number of points in R where f(f(x)) = 0 is:"
            ],
            "Physics": [
                "1. A particle moves in a straight line with constant acceleration. If it covers 10m in the first second and 20m in the next second, find its acceleration.",
                "2. Two charges +q and -q are placed at points A and B respectively. The electric field at the midpoint of AB is:",
                "3. A ray of light is incident on a glass slab at an angle of 45°. If the refractive index of glass is 1.5, find the angle of refraction."
            ],
            "Chemistry": [
                "1. The IUPAC name of CH₃CH₂CH₂COOH is:",
                "2. In the reaction 2A + B → C, if the rate of disappearance of A is 0.1 mol L⁻¹ s⁻¹, find the rate of formation of C.",
                "3. The number of σ and π bonds in benzene (C₆H₆) are:"
            ]
        },
        "NIT": {
            "Mathematics": [
                "1. If log₁₀2 = 0.3010, find the number of digits in 2¹⁰⁰.",
                "2. The value of lim(x→0) (sin x / x) is:",
                "3. If A and B are two events such that P(A) = 0.3, P(B) = 0.5 and P(A∩B) = 0.2, find P(A∪B)."
            ],
            "Physics": [
                "1. A body of mass 2kg is moving with velocity 10 m/s. If a force of 5N acts on it for 2 seconds, find the final velocity.",
                "2. The work done in moving a charge of 2μC from point A to point B in an electric field is 10 J. Find the potential difference between A and B.",
                "3. A wire of resistance R is stretched to double its length. Find the new resistance."
            ],
            "Chemistry": [
                "1. The electronic configuration of chromium (Cr) is:",
                "2. The pH of a 0.01 M solution of HCl is:",
                "3. The number of isomers possible for C₄H₁₀ is:"
            ]
        }
    }
}

def create_board_question_paper(board_name, board_code, class_level, subject, year, output_dir="question-papers"):
    """Create a PDF question paper for a specific board, class, subject, and year."""
    
    # Create directory structure
    board_dir = os.path.join(output_dir, "boards", board_name.replace(" ", "-"))
    class_dir = os.path.join(board_dir, class_level.replace(" ", "-"))
    subject_dir = os.path.join(class_dir, subject.replace(" ", "-"))
    year_dir = os.path.join(subject_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)
    
    # Get board configuration
    board_config = BOARDS[board_name][board_code]
    subject_config = board_config["subjects"][class_level][subject]
    
    # File path
    filename = f"{board_code}-{class_level.replace(' ', '-')}-{subject.replace(' ', '-')}-{year}.pdf"
    filepath = os.path.join(year_dir, filename)
    
    # Create PDF
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1a237e'),
        spaceAfter=20,
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
    
    # Header
    story.append(Paragraph(f"<b>{board_config['full_name']}</b>", title_style))
    story.append(Paragraph(f"<b>{class_level} - {subject} Question Paper {year}</b>", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Exam Information
    exam_info = [
        ["Board:", board_config['full_name']],
        ["Class:", class_level],
        ["Subject:", subject],
        ["Year:", str(year)],
        ["Total Marks:", str(subject_config['total_marks'])],
        ["Duration:", subject_config['duration']],
        ["Date:", datetime.now().strftime("%d/%m/%Y")]
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
        "1. This question paper contains multiple sections.",
        "2. All questions are compulsory.",
        "3. Read all questions carefully before answering.",
        "4. Write your answers clearly and legibly.",
        "5. Use black or blue pen only.",
        "6. Check your answers before submitting."
    ]
    for instruction in instructions:
        story.append(Paragraph(instruction, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Questions by Section
    sections = subject_config.get('sections', ['A', 'B', 'C'])
    questions = SAMPLE_QUESTIONS.get(board_name, {}).get(class_level, {}).get(subject, {})
    
    for section in sections:
        story.append(Paragraph(f"<b>Section {section}</b>", heading_style))
        story.append(Spacer(1, 0.1*inch))
        
        section_questions = questions.get(f"Section {section}", [])
        if not section_questions:
            # Generate generic questions
            for i in range(1, 4):
                story.append(Paragraph(f"Q{i}. [Question {i} for Section {section}]", normal_style))
                story.append(Spacer(1, 0.15*inch))
        else:
            for q in section_questions:
                story.append(Paragraph(q, normal_style))
                story.append(Spacer(1, 0.15*inch))
        
        story.append(Spacer(1, 0.2*inch))
    
    # Footer
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

def create_competitive_exam_paper(exam_name, subject, year, output_dir="question-papers"):
    """Create a PDF question paper for competitive exams."""
    
    # Create directory structure
    exam_dir = os.path.join(output_dir, "competitive", exam_name.replace(" ", "-"))
    subject_dir = os.path.join(exam_dir, subject.replace(" ", "-"))
    year_dir = os.path.join(subject_dir, str(year))
    os.makedirs(year_dir, exist_ok=True)
    
    # Get exam configuration
    exam_config = COMPETITIVE_EXAMS[exam_name]
    
    # File path
    filename = f"{exam_name.replace(' ', '-')}-{subject}-{year}.pdf"
    filepath = os.path.join(year_dir, filename)
    
    # Create PDF
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#c62828'),
        spaceAfter=20,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#d32f2f'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    normal_style = styles['Normal']
    
    # Header
    story.append(Paragraph(f"<b>{exam_config['full_name']}</b>", title_style))
    story.append(Paragraph(f"<b>{subject} - {year}</b>", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Exam Information
    exam_info = [
        ["Exam:", exam_config['full_name']],
        ["Paper Type:", exam_config['paper_type']],
        ["Subject:", subject],
        ["Year:", str(year)],
        ["Total Marks:", str(exam_config['total_marks'])],
        ["Duration:", exam_config['duration']]
    ]
    
    info_table = Table(exam_info, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ffebee')),
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
    story.append(Paragraph("<b>Instructions:</b>", heading_style))
    instructions = [
        "1. This question paper contains multiple choice and numerical type questions.",
        "2. Read all instructions carefully.",
        "3. Mark your answers on the OMR sheet (if applicable).",
        "4. Negative marking may apply for wrong answers.",
        "5. Use black or blue pen only."
    ]
    for instruction in instructions:
        story.append(Paragraph(instruction, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Questions
    story.append(Paragraph(f"<b>{subject} Questions</b>", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    questions = SAMPLE_QUESTIONS.get("Competitive", {}).get(exam_name, {}).get(subject, [])
    if questions:
        for q in questions:
            story.append(Paragraph(q, normal_style))
            story.append(Spacer(1, 0.2*inch))
    else:
        for i in range(1, 11):
            story.append(Paragraph(f"Q{i}. [Question {i} for {subject}]", normal_style))
            story.append(Spacer(1, 0.15*inch))
    
    # Footer
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

def generate_all_board_papers(years=[2020, 2021, 2022, 2023, 2024, 2025]):
    """Generate question papers for all boards and years."""
    
    print("=" * 70)
    print("Generating Board Question Papers")
    print(f"Author: {AUTHOR_INFO['name']} - {AUTHOR_INFO['website']}")
    print("=" * 70)
    
    generated_files = []
    
    # Generate board papers
    for board_name, board_data in BOARDS.items():
        print(f"\nGenerating papers for {board_name}...")
        for board_code, board_config in board_data.items():
            for class_level in board_config["classes"]:
                for subject in board_config["subjects"][class_level].keys():
                    for year in years:
                        try:
                            filepath = create_board_question_paper(
                                board_name, board_code, class_level, subject, year
                            )
                            generated_files.append({
                                "type": "board",
                                "board": board_name,
                                "board_code": board_code,
                                "class": class_level,
                                "subject": subject,
                                "year": year,
                                "filepath": filepath
                            })
                        except Exception as e:
                            print(f"Error generating {board_name} {class_level} {subject} {year}: {e}")
    
    # Generate competitive exam papers
    print(f"\nGenerating competitive exam papers...")
    for exam_name in COMPETITIVE_EXAMS.keys():
        exam_config = COMPETITIVE_EXAMS[exam_name]
        for subject in exam_config["subjects"]:
            for year in years:
                try:
                    filepath = create_competitive_exam_paper(exam_name, subject, year)
                    generated_files.append({
                        "type": "competitive",
                        "exam": exam_name,
                        "subject": subject,
                        "year": year,
                        "filepath": filepath
                    })
                except Exception as e:
                    print(f"Error generating {exam_name} {subject} {year}: {e}")
    
    # Save metadata
    metadata_file = os.path.join("question-papers", "boards", "metadata.json")
    os.makedirs(os.path.dirname(metadata_file), exist_ok=True)
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump({
            "_metadata": {
                "project": "Question Answering Dataset - Board Question Papers",
                "author": AUTHOR_INFO['name'],
                "website": AUTHOR_INFO['website'],
                "contact": AUTHOR_INFO['email'],
                "phone": AUTHOR_INFO['phone']
            },
            "generated_files": generated_files,
            "total_papers": len(generated_files)
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'=' * 70}")
    print(f"Generated {len(generated_files)} board and competitive exam papers")
    print(f"{'=' * 70}")
    
    return generated_files

if __name__ == "__main__":
    years = [2020, 2021, 2022, 2023, 2024, 2025]
    generate_all_board_papers(years)

