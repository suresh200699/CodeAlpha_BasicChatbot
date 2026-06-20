def chatbot():
    print("=== CodeAlpha Basic Chatbot ===")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I am a Python Chatbot.")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
