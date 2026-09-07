# Basic Chatbot


import datetime


def chatbot(user_input):

    if user_input == "hi" or user_input == "hello":
        print("Chatbot:", "Hi! How can I help you?")

    elif user_input == "what is ai":
        print("Chatbot:",
              "AI is Artificial Intelligence, that performs tasks that require human intelligence.")

    elif user_input == "how are you" or user_input == "how are you?":
        print("Chatbot:", "I am good, thank you!")

    elif user_input == "help":
        print("Chatbot:",
              "Hi! I am a Rule-Based Chatbot. How can I help you?")

    elif user_input == "what is the current date and time?":
        current_date_time = datetime.datetime.now()

        date = current_date_time.strftime("%d-%m-%Y")
        time = current_date_time.strftime("%I:%M %p")

        print("Chatbot:", "Date:", date)
        print("Chatbot:", "Time:", time)

    else:
        print("Chatbot:", "Invalid response. Type 'help' for assistance.")


while True:

    print("=" * 30)

    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Chatbot:", "Thank you! Goodbye!")
        print("=" * 30)
        break

    chatbot(user_input)