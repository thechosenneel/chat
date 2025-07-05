import google.generativeai as genai

# Configuration - replace with your actual API key
GEMINI_API_KEY = "AIzaSyDHHL0WlrPbL2tC9nVkZXJ6skbsElRQeTg"
MODEL_NAME = "gemini-1.5-flash"  # Update if the exact model name is different

def generate_response(prompt: str) -> str:
    """
    Generate a response using the Gemini API based on custom user input.
    
    Args:
        prompt: The user's custom input/question
        
    Returns:
        Generated response as a string
    """
    try:
        # Configure the Gemini client
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Generate response
        response = model.generate_content(prompt)
        
        return response.text
    
    except Exception as e:
        return f"An error occurred while generating response: {str(e)}"

def main():
    """
    Main chatbot loop to interact with the user.
    """
    print("\n=== Gemini Chatbot ===")
    print("You can ask me anything or request specific content.\n")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye!")
            break
            
        if not user_input:
            print("Please enter your question or request.")
            continue
            
        print("\nThinking...\n")
        
        # Generate and display response
        response = generate_response(user_input)
        
        print("Assistant:", response)
        print()  # Add empty line for better readability

if __name__ == "__main__":
    main()
