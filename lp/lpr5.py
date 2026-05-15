# Elementary Chatbot for Customer Interaction

def chatbot():
    print("=== Welcome to Customer Support Chatbot ===")
    print("Type 'hello' to start chatting")
    print("Type 'bye' to exit")
    print()

    while True:
        user = input("You: ").lower()

        # Greeting
        if user == "hello" or user == "hi":
            print("Bot: Hello! How can I help you today?")

        # Asking about products
        elif "product" in user:
            print("Bot: We offer laptops, मोबाइल phones, and accessories.")

        # Asking about price
        elif "price" in user:
            print("Bot: Prices depend on the product. Please tell me the product name.")

        # Asking about order status
        elif "order" in user or "status" in user:
            print("Bot: Please enter your order ID on our website to check the order status.")

        # Asking about delivery
        elif "delivery" in user:
            print("Bot: Delivery usually takes 3 to 5 working days.")

        # Asking about return policy
        elif "return" in user:
            print("Bot: Our return policy allows returns within 7 days of delivery.")

        # Asking about contact info
        elif "contact" in user or "phone" in user:
            print("Bot: You can contact us at 9876543210.")

        # Asking about office timings
        elif "timing" in user or "hours" in user:
            print("Bot: Our customer support is available from 9 AM to 6 PM.")

        # Exit condition
        elif user == "bye":
            print("Bot: Thank you for visiting. Have a nice day!")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I did not understand that. Please try another question.")

# Run chatbot
chatbot()

