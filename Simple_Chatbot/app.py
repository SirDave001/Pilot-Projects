import json
import random

# Load intents from intents.json file
with open("intents.json", "r") as file:
    intents = json.load(file)["intents"]


# Helper function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    # Iterate through intents to find a matching pattern
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    # Fallback response if no pattern is matched
    return "I'm not sure how to respond to that. Try asking something else, or say 'bye' to end the chat!"


# Step 1: Greeting the User
print("Hello! What's your name?")
user_name = input()  # Get the user's name
print(f"Nice to meet you, {user_name}!")

# Step 2: Basic Conversation Loop
while True:
    print("How can I help you today?")
    user_input = input().lower()  # Get user's conversational prompt

    # Check for goodbye patterns directly to exit the program
    if any(pattern in user_input for pattern in ["bye", "exit", "goodbye"]):
        print(f"Goodbye, {user_name}! It was a pleasure chatting with you. Have a wonderful day ahead!!")
        break  # Exit the loop to end the program

    # Get and print the chatbot's response
    response = get_response(user_input)
    print(response)