import requests
import openai
from openai import OpenAI
import random
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI()
openai.api_key=API_KEY # key associated with openai API: sending request to our profile

"Compose a poem that explains the concept of recursion in programming."
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# if __name__ == "__main__": # running this python file directly
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break
#         response = chat_with_gpt(user_input)
#         print("Chatbot: ", response)

# prompt = "Compose a poem that explains the concept of recursion in programming"
# print(chat_with_gpt(prompt))



def assign_group():
    # Modify this function based on your desired allocation logic
    groups = ['specific_feedback', 'general_feedback', 'control_group']
    return random.choice(groups)


# Function to send request to OpenAI API for feedback
def get_ai_feedback(story_text, feedback_amount):
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
    data = {
        'prompt': story_text,
        'max_tokens': feedback_amount
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return 'Error: Failed to get AI feedback'


print(get_ai_feedback("How are you doing today, sir???", 20))