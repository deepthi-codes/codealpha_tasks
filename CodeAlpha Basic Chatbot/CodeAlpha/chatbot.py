def chatbot():
    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can say 'hello', ask 'how are you', or type 'bye' to exit.")

    while True:
        user_message = input("You: ").strip().lower()

        if user_message == "hello":
            print("Chatbot: Hi!")
        elif user_message == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_message == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that message.")


if __name__ == "__main__":
    chatbot()