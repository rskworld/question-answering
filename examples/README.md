<!--
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
-->

# Question Answering Dataset - Code Examples

This directory contains example code for using the Question Answering Dataset with various transformer models.

## Examples

### 1. BERT Example (`bert_example.py`)

Demonstrates how to use BERT models for question answering:

```bash
python bert_example.py
```

**Features:**
- Loading SQuAD format dataset
- Using BERT tokenizer and model
- Using Hugging Face pipeline for easy inference
- Custom prediction function

### 2. GPT Example (`gpt_example.py`)

Demonstrates how to use GPT models for question answering:

```bash
python gpt_example.py
```

**Features:**
- Loading SQuAD format dataset
- Using GPT-2 tokenizer and model
- Generating answers with language models
- Prompt formatting for GPT

### 3. Transformers Example (`transformers_example.py`)

Comprehensive example using Hugging Face Transformers library:

```bash
python transformers_example.py
```

**Features:**
- Loading both SQuAD and CSV formats
- Using QA pipeline
- Using AutoModel and AutoTokenizer
- Dataset analysis and statistics
- Converting between formats

## Installation

Install required packages:

```bash
pip install transformers torch datasets pandas
```

For GPU support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Usage

1. Navigate to the examples directory:
   ```bash
   cd examples
   ```

2. Run any example:
   ```bash
   python bert_example.py
   ```

3. Modify the examples to use your own models or fine-tune on the dataset.

## Models Used

- **BERT**: `bert-base-uncased`
- **GPT-2**: `gpt2`
- **DistilBERT**: `distilbert-base-uncased-distilled-squad`

## Customization

You can modify the examples to:
- Use different pre-trained models
- Fine-tune models on the dataset
- Add custom preprocessing
- Implement custom training loops
- Evaluate model performance

## Contact

For questions or support:
- **Author**: Molla Samser
- **Website**: [https://rskworld.in](https://rskworld.in)
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

