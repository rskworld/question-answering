<!--
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Question Answering Dataset

This dataset contains context passages with corresponding questions and answers for question answering tasks. Perfect for training QA models, reading comprehension systems, and transformer-based language models.

## Features

- **Context passages**: Rich contextual information for comprehension
- **Questions and answers**: Paired Q&A sets for training
- **Multiple domains**: Diverse topics and subject areas
- **SQuAD format**: Standard format compatible with popular QA frameworks
- **Ready for transformer models**: Optimized for BERT, GPT, and other transformer architectures

## Technologies

- JSON
- CSV
- Transformers
- BERT
- GPT

## Difficulty

**Advanced**

## Dataset Structure

The dataset is available in multiple formats:

### SQuAD Format (JSON)
- `squad_format.json`: Standard SQuAD 2.0 format
- Compatible with Hugging Face Transformers library

### CSV Format
- `dataset.csv`: Simple CSV format for easy data manipulation
- Columns: context, question, answer, domain

### Individual Files
- `contexts.json`: All context passages
- `questions.json`: All questions with context references
- `answers.json`: All answers with question references

## Installation

```bash
# Clone or download the dataset
git clone <repository-url>
cd question-answering
```

## Usage

### Using with Hugging Face Transformers

```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import json

# Load the dataset
with open('squad_format.json', 'r') as f:
    dataset = json.load(f)

# Load a pre-trained model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModelForQuestionAnswering.from_pretrained("bert-base-uncased")
```

### Using with CSV

```python
import pandas as pd

# Load CSV dataset
df = pd.read_csv('dataset.csv')
print(df.head())
```

## Dataset Statistics

- **Total Context Passages**: 1000+
- **Total Questions**: 5000+
- **Total Answers**: 5000+
- **Domains**: Science, History, Literature, Technology, General Knowledge

## File Structure

```
question-answering/
├── README.md
├── index.html
├── styles.css
├── script.js
├── squad_format.json
├── dataset.csv
├── contexts.json
├── questions.json
├── answers.json
├── generate_question_papers.py
├── question-papers/
│   ├── index.html
│   ├── metadata.json
│   ├── Class-1/
│   │   ├── 2020/
│   │   │   ├── Class-1-Question-Paper-2020.pdf
│   │   │   └── Class-1-Answer-Key-2020.pdf
│   │   ├── 2021/
│   │   ├── ... (all years)
│   ├── Class-2/
│   ├── ... (Class 1-12)
├── examples/
│   ├── bert_example.py
│   ├── gpt_example.py
│   └── transformers_example.py
└── LICENSE
```

## Question Papers

This project includes question papers and answer keys for all classes (Class 1 to Class 12) from previous years (2020-2025).

### Features:
- **12 Classes**: Class 1 through Class 12
- **6 Years**: 2020, 2021, 2022, 2023, 2024, 2025
- **PDF Format**: Professional question papers and answer keys
- **Publicly Available**: Free to download and use
- **Total Files**: 144 PDFs (72 question papers + 72 answer keys)

### Access Question Papers:
- **Browse Online**: Open `question-papers/index.html` in your browser
- **Direct Download**: Navigate to `question-papers/[Class]/[Year]/` directory
- **Generate More**: Run `python generate_question_papers.py` to create additional papers

### Subjects Covered:
- **Primary Classes (1-5)**: English, Mathematics, Science, General Knowledge, Social Studies
- **Middle Classes (6-8)**: English, Mathematics, Science, Social Studies
- **Secondary Classes (9-10)**: English, Mathematics, Science, Social Studies
- **Senior Classes (11-12)**: English, Mathematics, Physics, Chemistry, Biology

## Examples

See the `examples/` directory for complete working examples:
- BERT-based QA model training
- GPT-based QA inference
- Transformers library integration

## Citation

If you use this dataset in your research, please cite:

```
@dataset{question_answering_2025,
  title={Question Answering Dataset},
  author={Molla Samser},
  year={2025},
  url={https://rskworld.in},
  publisher={RSK World}
}
```

## License

See LICENSE file for details.

## Contact

For questions, suggestions, or contributions:

- **Author**: Molla Samser
- **Website**: [https://rskworld.in](https://rskworld.in)
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## Acknowledgments

This dataset is maintained by RSK World. For more datasets and projects, visit [rskworld.in](https://rskworld.in).

