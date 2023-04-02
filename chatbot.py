# Define a function that takes a user input and returns the chatbot's response
def chatbot_response(input_message):
    if input_message.lower() == "hello":
        return "Hello, how can I help you?"
    elif input_message.lower() == "what is openai?":
        return "OpenAI is a private research laboratory that aims to develop and direct artificial intelligence (AI) in ways that benefit humanity as a whole. The company was founded by Elon Musk, Sam Altman and others in 2015 and is headquartered in San Francisco. OpenAI was created in part because of its founders' existential concerns about the potential for catastrophe resulting from carelessness and misuse of general-purpose AI. The company has a long-term focus on fundamental advances in AI and its capabilities. The founders of the company and other investors started the company with a $1 billion endowment. In February 2018, Elon Musk left the company due to a potential conflict of interest with his work at Tesla, the automotive and clean energy company inspired by Nikola Tesla."
    elif input_message.lower() == "what is dall-e?":
        return "DALL·E 2 is an AI system that can create realistic images and art from a description in natural language."
    elif input_message.lower() == "how can we use pixelpotion?":
        return "Head over the given repository <a href='https://github.com/Diya84/Pixelpotion.git'>https://github.com/Diya84/Pixelpotion</a> and follows the steps in the read.me to use the webpage."
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

# A while loop that continuously asks for user input and outputs the chatbot's response
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        chatbot_output = chatbot_response(user_input)
        print("Chatbot: " + chatbot_output)
