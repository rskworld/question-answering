# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    BERT Example: Using BERT for Question Answering
    This example demonstrates how to use the dataset with BERT-based models.
"""

import json
import torch
from transformers import BertTokenizer, BertForQuestionAnswering
from transformers import pipeline

def load_dataset(file_path='../squad_format.json'):
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

def prepare_bert_input(context, question, tokenizer, max_length=512):
    """
    Prepare input for BERT model.
    
    Args:
        context (str): Context passage
        question (str): Question to answer
        tokenizer: BERT tokenizer
        max_length (int): Maximum sequence length
        
    Returns:
        dict: Tokenized inputs
    """
    # BERT expects [CLS] question [SEP] context [SEP]
    inputs = tokenizer.encode_plus(
        question,
        context,
        add_special_tokens=True,
        max_length=max_length,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )
    return inputs

def predict_answer(context, question, model, tokenizer):
    """
    Predict answer using BERT model.
    
    Args:
        context (str): Context passage
        question (str): Question to answer
        model: BERT model for question answering
        tokenizer: BERT tokenizer
        
    Returns:
        str: Predicted answer
    """
    inputs = prepare_bert_input(context, question, tokenizer)
    
    with torch.no_grad():
        outputs = model(**inputs)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits
        
        # Get the most likely start and end positions
        start_idx = torch.argmax(start_scores)
        end_idx = torch.argmax(end_scores)
        
        # Decode the answer
        answer_tokens = inputs['input_ids'][0][start_idx:end_idx+1]
        answer = tokenizer.decode(answer_tokens, skip_special_tokens=True)
        
    return answer

def main():
    """
    Main function to demonstrate BERT question answering.
    """
    print("=" * 60)
    print("BERT Question Answering Example")
    print("Author: Molla Samser - https://rskworld.in")
    print("=" * 60)
    
    # Load dataset
    print("\nLoading dataset...")
    dataset = load_dataset()
    
    # Initialize BERT model and tokenizer
    print("Loading BERT model...")
    model_name = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForQuestionAnswering.from_pretrained(model_name)
    model.eval()
    
    # Alternative: Use pipeline (easier approach)
    print("\nUsing Hugging Face pipeline (easier approach)...")
    qa_pipeline = pipeline("question-answering", model=model_name, tokenizer=model_name)
    
    # Get first example from dataset
    if dataset['data']:
        first_article = dataset['data'][0]
        if first_article['paragraphs']:
            first_paragraph = first_article['paragraphs'][0]
            context = first_paragraph['context']
            
            if first_paragraph['qas']:
                first_qa = first_paragraph['qas'][0]
                question = first_qa['question']
                correct_answer = first_qa['answers'][0]['text']
                
                print(f"\nContext: {context[:200]}...")
                print(f"\nQuestion: {question}")
                print(f"Correct Answer: {correct_answer}")
                
                # Predict using pipeline
                result = qa_pipeline(question=question, context=context)
                print(f"\nPredicted Answer: {result['answer']}")
                print(f"Confidence Score: {result['score']:.4f}")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

