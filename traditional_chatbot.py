class TraditionalChatbot:
    def __init__(self):
        self.responses = {
            "weather": "The weather today is sunny.",
            "news": "Here are the latest headlines.",
            "help": "How can I assist you today?",
        }

    def get_response(self, user_input):
        for keyword in self.responses:
            if keyword in user_input.lower():
                return self.responses[keyword]
        return "Sorry, I don't understand that."

if __name__ == "__main__":
    bot = TraditionalChatbot()
    print("Traditional Chatbot. Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")
