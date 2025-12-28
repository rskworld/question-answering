
# Guide to Collecting Real Question Papers

## Author Information
- **Name**: Molla Samser
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277

## Sources for Real Question Papers

### 1. Official Board Websites
- **West Bengal Board (WBBSE)**: https://www.wbbse.org
- **West Bengal Board (WBCHSE)**: https://www.wbchse.nic.in
- **CBSE**: https://cbse.gov.in
- **JEE Main**: https://jeemain.nta.ac.in
- **NIT**: Check individual NIT websites

### 2. Educational Portals
- LearnCBSE: https://www.learncbse.in
- Vedantu: https://www.vedantu.com
- Toppr: https://www.toppr.com
- Embibe: https://www.embibe.com
- AskIITians: https://www.askiitians.com

### 3. Steps to Collect Real Questions

1. **Visit Official Websites**
   - Go to the board's official website
   - Navigate to "Question Papers" or "Previous Year Papers" section
   - Download PDFs for required years

2. **Extract Questions**
   - Open downloaded PDFs
   - Extract questions manually or use PDF parsing tools
   - Organize by subject and year

3. **Update Data File**
   - Edit `real_question_data.json`
   - Add real questions in the structured format
   - Include answers when available

4. **Regenerate Papers**
   - Run `python generate_board_question_papers.py`
   - Script will use real questions from the data file

## Data Format

```json
{
  "West Bengal Board": {
    "WBBSE": {
      "Class 10": {
        "2024": {
          "Mathematics": [
            {
              "question": "Real question text here",
              "answer": "Real answer here",
              "marks": 2
            }
          ]
        }
      }
    }
  }
}
```

## Legal Notice

- Only use publicly available question papers
- Respect copyright and terms of use
- Use for educational purposes only
- Credit original sources when possible

## Automation

For automated collection, you can:
1. Use web scraping tools (with permission)
2. Use official APIs if available
3. Manually download and extract
4. Use PDF parsing libraries (PyPDF2, pdfplumber)

## Contact

For questions or support:
- **Website**: https://rskworld.in
- **Email**: help@rskworld.in
- **Phone**: +91 93305 39277
