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


def assign_group():
    # Modify this function based on your desired allocation logic
    groups = ['specific_feedback', 'general_feedback', 'control_group']
    return random.choice(groups)


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



def get_ai_feedback(story_text, feedback_amount, group_modality):
  """Sends a request to the OpenAI API for feedback on the provided story text.
        davinci-002: focus on longer more coherent text & ability to understand complex instructions -> specific_feedback
        gpt-3.5-turbo: emphasis on creativity for creative braintstorming or generating new ideas -> general_feedback

    Args:
        story_text: The text of the story to get feedback on.
        feedback_amount: The maximum number of tokens for the response (length of feedback).
        group_modality: The modality of the feedback (specific_feedback, general_feedback, or control_group).

    Returns:
        The AI-generated feedback as a string, or an error message if unsuccessful.
    """
  try:
    if group_modality == "specific_feedback":
        model = "gpt-3.5-turbo"
    elif group_modality == "general_feedback":
        model = "gpt-3.5-turbo"
    elif group_modality == "control_group":
        return "No AI feedback is needed for the control group."
    else:
        return "Error: Invalid group modality. Please provide either 'specific_feedback', 'general_feedback', or 'control_group'."
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a creative writer, skilled in providing feedback on the creative works of others with creative flair. Your job is to provide creative feedback to the story of the human. Give the human ideas on how to continue his story line or what they may include"},
            {"role": "user", "content": story_text}],
        max_tokens=feedback_amount,
        temperature=0.7,
        n=1  # Generate only one response (feedback)
    )
    return response.choices[0].message.content.strip() # Extract and clean the feedback text
  except Exception as e:
    return f"Error: Failed to get AI feedback: {e}"
  




print(get_ai_feedback("There once was a ship that put the sea the name of the ship was the billy of tea!", 50, "general_feedback"))