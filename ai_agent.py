import openai
import os

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your API key string

class AIAgent:
    def __init__(self):
        self.model = "gpt-3.5-turbo"

    def get_response(self, user_input):
        # OpenAI API call to generate a response
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message["content"]

if __name__ == "__main__":
    ai_agent = AIAgent()
    print("AI Agent using OpenAI. Type 'exit' to stop.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ai_agent.get_response(user_input)
        print(f"AI Agent: {response}")
