# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    Transformers Example: Using Hugging Face Transformers Library
    This example demonstrates how to use the dataset with various transformer models.
"""

import json
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
from datasets import Dataset
from transformers import TrainingArguments, Trainer

def load_squad_dataset(file_path='../squad_format.json'):
    """
    Load the SQuAD format dataset.
    
    Args:
        file_path (str): Path to the dataset JSON file
        
    Returns:
        dict: Loaded dataset
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    return dataset

def load_csv_dataset(file_path='../dataset.csv'):
    """
    Load the CSV format dataset.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    df = pd.read_csv(file_path)
    return df

def convert_squad_to_hf_dataset(squad_data):
    """
    Convert SQuAD format to Hugging Face Dataset format.
    
    Args:
        squad_data (dict): SQuAD format dataset
        
    Returns:
        list: List of examples in HF format
    """
    examples = []
    for article in squad_data['data']:
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            for qa in paragraph['qas']:
                if not qa['is_impossible']:
                    example = {
                        'context': context,
                        'question': qa['question'],
                        'answers': {
                            'text': [qa['answers'][0]['text']],
                            'answer_start': [qa['answers'][0]['answer_start']]
                        }
                    }
                    examples.append(example)
    return examples

def use_qa_pipeline(model_name="distilbert-base-uncased-distilled-squad"):
    """
    Use Hugging Face question-answering pipeline.
    
    Args:
        model_name (str): Name of the pre-trained model
    """
    print(f"\nUsing QA Pipeline with model: {model_name}")
    qa_pipeline = pipeline("question-answering", model=model_name)
    
    # Example usage
    context = "Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans."
    question = "What is Artificial Intelligence?"
    
    result = qa_pipeline(question=question, context=context)
    print(f"\nQuestion: {question}")
    print(f"Answer: {result['answer']}")
    print(f"Score: {result['score']:.4f}")

def use_auto_model(model_name="bert-base-uncased"):
    """
    Use AutoModel for question answering.
    
    Args:
        model_name (str): Name of the pre-trained model
    """
    print(f"\nUsing AutoModel with: {model_name}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    
    context = "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France."
    question = "Where is the Eiffel Tower located?"
    
    inputs = tokenizer(question, context, return_tensors="pt", padding=True, truncation=True)
    
    with model.eval():
        outputs = model(**inputs)
        start_logits = outputs.start_logits
        end_logits = outputs.end_logits
    
    # Get answer span
    answer_start = start_logits.argmax()
    answer_end = end_logits.argmax() + 1
    
    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end])
    )
    
    print(f"\nQuestion: {question}")
    print(f"Answer: {answer}")

def analyze_dataset():
    """
    Analyze the dataset and show statistics.
    """
    print("\n" + "=" * 60)
    print("Dataset Analysis")
    print("=" * 60)
    
    # Load SQuAD format
    squad_data = load_squad_dataset()
    print(f"\nSQuAD Format:")
    print(f"  Version: {squad_data.get('version', 'N/A')}")
    print(f"  Number of articles: {len(squad_data['data'])}")
    
    total_paragraphs = sum(len(article['paragraphs']) for article in squad_data['data'])
    print(f"  Total paragraphs: {total_paragraphs}")
    
    total_questions = 0
    for article in squad_data['data']:
        for paragraph in article['paragraphs']:
            total_questions += len(paragraph['qas'])
    print(f"  Total questions: {total_questions}")
    
    # Load CSV format
    df = load_csv_dataset()
    print(f"\nCSV Format:")
    print(f"  Total rows: {len(df)}")
    print(f"  Columns: {', '.join(df.columns)}")
    print(f"  Domains: {', '.join(df['domain'].unique())}")
    
    print("\nFirst few examples from CSV:")
    print(df.head())

def main():
    """
    Main function to demonstrate various transformer models.
    """
    print("=" * 60)
    print("Hugging Face Transformers Example")
    print("Author: Molla Samser - https://rskworld.in")
    print("=" * 60)
    
    # Analyze dataset
    analyze_dataset()
    
    # Example 1: Using QA Pipeline (easiest)
    print("\n" + "=" * 60)
    print("Example 1: Using QA Pipeline")
    print("=" * 60)
    use_qa_pipeline()
    
    # Example 2: Using AutoModel
    print("\n" + "=" * 60)
    print("Example 2: Using AutoModel")
    print("=" * 60)
    use_auto_model()
    
    print("\n" + "=" * 60)
    print("Examples completed!")
    print("=" * 60)
    print("\nFor training custom models, see the Hugging Face documentation:")
    print("https://huggingface.co/docs/transformers/training")

if __name__ == "__main__":
    main()

