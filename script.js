/*
    Project: Question Answering Dataset
    Description: A dataset containing context passages, questions, and answers for training QA models and reading comprehension systems.
    Author: Molla Samser
    Website: https://rskworld.in
    Contact: help@rskworld.in
    Phone: +91 93305 39277
*/

// Load and display dataset preview
document.addEventListener('DOMContentLoaded', function() {
    loadDatasetPreview();
});

/**
 * Load and display a preview of the dataset
 */
async function loadDatasetPreview() {
    try {
        const response = await fetch('squad_format.json');
        const data = await response.json();
        
        const previewContainer = document.getElementById('dataset-preview');
        previewContainer.innerHTML = '';
        
        // Display first 3 examples
        let count = 0;
        for (const item of data.data) {
            if (count >= 3) break;
            
            for (const paragraph of item.paragraphs) {
                if (count >= 3) break;
                
                for (const qa of paragraph.qas) {
                    if (count >= 3) break;
                    
                    const previewItem = document.createElement('div');
                    previewItem.className = 'preview-item';
                    
                    const question = document.createElement('h4');
                    question.textContent = `Q: ${qa.question}`;
                    
                    const context = document.createElement('p');
                    context.textContent = `Context: ${paragraph.context.substring(0, 150)}...`;
                    
                    const answer = document.createElement('p');
                    answer.className = 'answer';
                    answer.textContent = `A: ${qa.answers[0].text}`;
                    
                    previewItem.appendChild(question);
                    previewItem.appendChild(context);
                    previewItem.appendChild(answer);
                    
                    previewContainer.appendChild(previewItem);
                    count++;
                }
            }
        }
        
        if (count === 0) {
            previewContainer.innerHTML = '<p>No data available for preview.</p>';
        }
    } catch (error) {
        console.error('Error loading dataset preview:', error);
        document.getElementById('dataset-preview').innerHTML = 
            '<p>Error loading dataset preview. Please check if the dataset file exists.</p>';
    }
}

/**
 * Smooth scroll to section
 */
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

/**
 * Format dataset statistics
 */
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

