import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)  
model = genai.GenerativeModel("gemini-1.5-flash")

while True:
    user_input = input("Ask me anything (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = model.generate_content(user_input)
    print("AI says:", response.text)
    print("-" * 50)  # خط فاصل للوضوح
