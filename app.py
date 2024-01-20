import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['''I'm doing well, thank you!', 'I'm fine, thanks for asking.''']),
    (r'what is your name', ['I am a chatbot.', 'You can call me Chat Assistant.']),
    # Add more patterns as needed
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm a simple chatbot. Ask me anything or just say hi.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
