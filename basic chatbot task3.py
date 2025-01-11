import random

class Chatbot:
    def __init__(self):
        self.greetings = ['hi', 'hello', 'hey', 'howdy', 'hola']
        self.responses = [
            "I'm here to help you. How can I assist you?",
            "Hello! What can I do for you today?",
            "Hey there! How can I be of assistance?"
        ]
        self.farewells = ['bye', 'goodbye', 'see you', 'later']
        self.farewell_responses = [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care! Come back if you need anything!"
        ]
        self.unknown_responses = [
            "Sorry, I didn't quite understand that.",
            "Could you rephrase your question?",
            "I'm not sure how to respond to that."
        ]
        
    def preprocess_input(self, user_input):
        # Convert input to lowercase for uniform matching
        return user_input.lower()

    def respond(self, user_input):
        # Preprocess the user input
        user_input = self.preprocess_input(user_input)
        
        # Check for greeting
        if any(greeting in user_input for greeting in self.greetings):
            return random.choice(self.responses)
        
        # Check for farewell
        elif any(farewell in user_input for farewell in self.farewells):
            return random.choice(self.farewell_responses)
        
        # Default response if no match found
        else:
            return random.choice(self.unknown_responses)

def main():
    print("Chatbot: Hello! I'm your assistant. Type 'bye' to exit.")
    bot = Chatbot()

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for farewell
        if any(farewell in user_input.lower() for farewell in bot.farewells):
            print("Chatbot:", bot.respond(user_input))
            break
        
        # Get chatbot's response
        response = bot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
