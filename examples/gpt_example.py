# -*- coding: utf-8 -*-
"""
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
    
    GPT Example: Using GPT for Question Answering
    This example demonstrates how to use the dataset with GPT-based models.
"""

import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

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

def format_prompt(context, question):
    """
    Format prompt for GPT model.
    
    Args:
        context (str): Context passage
        question (str): Question to answer
        
    Returns:
        str: Formatted prompt
    """
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    return prompt

def generate_answer(context, question, model, tokenizer, max_length=200):
    """
    Generate answer using GPT model.
    
    Args:
        context (str): Context passage
        question (str): Question to answer
        model: GPT model
        tokenizer: GPT tokenizer
        max_length (int): Maximum generation length
        
    Returns:
        str: Generated answer
    """
    prompt = format_prompt(context, question)
    
    # Tokenize input
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate answer
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=len(inputs[0]) + max_length,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    # Decode the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Extract answer (text after "Answer:")
    if "Answer:" in generated_text:
        answer = generated_text.split("Answer:")[-1].strip()
    else:
        answer = generated_text[len(prompt):].strip()
    
    return answer

def main():
    """
    Main function to demonstrate GPT question answering.
    """
    print("=" * 60)
    print("GPT Question Answering Example")
    print("Author: Molla Samser - https://rskworld.in")
    print("=" * 60)
    
    # Load dataset
    print("\nLoading dataset...")
    dataset = load_dataset()
    
    # Initialize GPT model and tokenizer
    print("Loading GPT-2 model...")
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    model.eval()
    
    # Set pad token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    
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
                
                # Generate answer
                print("\nGenerating answer with GPT-2...")
                generated_answer = generate_answer(context, question, model, tokenizer)
                print(f"\nGenerated Answer: {generated_answer}")
    
    print("\n" + "=" * 60)
    print("Note: GPT-2 is a general language model and may not perform")
    print("as well as specialized QA models like BERT for this task.")
    print("For better results, consider using GPT-3, GPT-4, or fine-tuned models.")
    print("=" * 60)

if __name__ == "__main__":
    main()

