# Gemini-Powered Test Company Knowledge Assistant & Simple Gemini Test  
**A simple Python app test that answers company questions using Gemini AI and semantic search**  

---

## Project Description  
This application allows employees to ask questions about company policies and procedures. It uses:  
- **Gemini 1.5 Flash** for generating natural language responses  
- **Sentence Transformers** for converting text to numerical vectors  
- **FAISS** for efficient similarity search of documents  

---

## Prerequisites  
- Python 3.13+  
- Git  
- Google API key ([Get it here](https://aistudio.google.com/))  

---

## Installation  
### 1. Clone the repository  
```bash  
git clone https://github.com/hakoom911/ai-test.git  
cd ai-test
```  

### 2. Create and activate virtual environment  
```bash  
# Create environment  
python -m venv venv  

# Activate environment  
# Windows:  
venv\Scripts\activate  
# macOS/Linux:  
source venv/bin/activate  
```  

### 3. Install dependencies  
```bash  
pip install -r requirements.txt  
```  

---

## Configuration  
1. Create `config.py` in the project root directory  
2. Add your Gemini API key:  
```python  
# config.py  
GEMINI_API_KEY = "your_actual_api_key_here"  # Get from https://aistudio.google.com/  
```  

> ⚠️ **Important**: Never commit this file to GitHub! It's protected by .gitignore  

---

## Running the Application  
```bash  
# With activated environment  
python knowledge_assistant.py  
```  

### Example Output  
```  
Question: How do I request leave?  
Answer: To apply for leave, go to the HR portal and click 'Leave Request'.  
        Fill in the dates and reason for your leave.  
```  

---

## Project Structure  
```  
your-repo/  
├── venv/                   # Virtual environment (ignored by Git)  
├── .gitignore              # Excludes sensitive files  
├── knowledge_assistant.py  # Main application  
├── requirements.txt        # Dependencies list  
├── config.py               # API configuration (local only)  
├── README.md               # This documentation  
└── company_knowledge.py    # Customize your knowledge base here  
```  

---

## Customizing Knowledge Base  
Edit `company_knowledge.py` to add your company's specific information:  
```python  
# Sample knowledge base - modify with your content  
docs = [  
    "Leave policy: Submit requests at least 3 days in advance through HR portal",  
    "IT support: Email helpdesk@company.com or call x1234",  
    "Expense reports: Submit within 30 days using Finance app",  
    # Add more entries here  
]  
```  

---

## Troubleshooting  
| Issue | Solution |  
|-------|----------|  
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |  
| FAISS installation fails | Use `pip install faiss-cpu --no-cache` |  
| Gemini API errors | Verify API key at [Google AI Studio](https://aistudio.google.com/) |  
| Python not found | Ensure Python is added to PATH during installation |  
| Virtual environment issues | Delete venv folder and recreate with `python -m venv venv` |  

---

## Contributing  
1. Fork the repository  
2. Create your feature branch:  
```bash  
git checkout -b feature/new-feature  
```  
3. Commit changes:  
```bash  
git commit -m 'Add new feature'  
```  
4. Push to branch:  
```bash  
git push origin feature/new-feature  
```  
5. Open a Pull Request  


[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

> **Note**: Remember to activate your virtual environment each time you work on the project!