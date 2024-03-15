import requests
import random
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key)

result = chat_model.predict("Hey, how are you?")
print(result)

# Function to assign participants to different groups
def assign_group():
    # Modify this function based on your desired allocation logic
    groups = ['specific_feedback', 'general_feedback', 'control_group']
    return random.choice(groups)

# Function to send request to OpenAI API for feedback
def get_ai_feedback(story_text, feedback_amount):
    openai_api_key = 'YOUR_OPENAI_API_KEY'
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {openai_api_key}'}
    data = {
        'prompt': story_text,
        'max_tokens': feedback_amount
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return 'Error: Failed to get AI feedback'

# Function to simulate participant writing creative story
def write_story():
    # Replace this with actual story writing process
    return 'Once upon a time...'

# Function to conduct the A/B experiment
def conduct_experiment(participant_id):
    group = assign_group()
    if group == 'specific_feedback':
        story_text = write_story()
        feedback_amount = 300  # Modify this based on your desired feedback amount
        feedback = get_ai_feedback(story_text, feedback_amount)
        # Send feedback to participant using Qualtrics API
        send_feedback_to_participant(participant_id, feedback)
    elif group == 'general_feedback':
        story_text = write_story()
        feedback_amount = 100  # Modify this based on your desired feedback amount
        feedback = get_ai_feedback(story_text, feedback_amount)
        # Send feedback to participant using Qualtrics API
        send_feedback_to_participant(participant_id, feedback)
    else:  # Control group
        # Participant writes creative story without AI feedback
        story_text = write_story()
        # You can choose to store/control the data for the control group as needed

# Function to send feedback to participant using Qualtrics API
def send_feedback_to_participant(participant_id, feedback):
    # Replace 'YOUR_QUALTRICS_API_KEY' and 'YOUR_SURVEY_ID' with your actual API key and survey ID
    qualtrics_api_key = 'YOUR_QUALTRICS_API_KEY'
    survey_id = 'YOUR_SURVEY_ID'
    url = f'https://yourdatacenterid.qualtrics.com/API/v3/surveys/{survey_id}/responses/{participant_id}'
    headers = {'X-API-Token': qualtrics_api_key}
    data = {
        # Modify this based on your survey structure and feedback question
        'data': {
            'feedback_question': feedback
        }
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Feedback sent to participant {participant_id}')
    else:
        print('Error: Failed to send feedback to participant')

# Main function to simulate participants and conduct the experiment
def main():
    # Simulate 100 participants for demonstration purposes
    num_participants = 100
    for i in range(num_participants):
        participant_id = f'participant_{i}'
        conduct_experiment(participant_id)

 if __name__ == "__main__":
     main()
