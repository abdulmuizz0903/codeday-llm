"""
CodeDay LLM Workshop Demo
A simple script to demonstrate how to interact with Large Language Models
Perfect for learning the basics of AI conversation!
"""

import groq, json, requests, os
from dotenv import load_dotenv

# Load environment variables (like our API key)
load_dotenv()

# This list will store our entire conversation with the AI
conversation_history = []

# Get our API key from environment variables (keeps it secret!)
GROQ_KEY = os.getenv("GROQ_KEY")
groq_client = groq.Groq(api_key=GROQ_KEY)

print("🤖 Welcome to the CodeDay LLM Workshop!")
print("💬 Start chatting with the AI. Type 'Q' to quit.")
print("-" * 50)

while True:
    user_input = input("\n🧑‍💻 You: ")
    
    if user_input.upper() == "Q":
        print("\n👋 Thanks for chatting! See you next time!")
        break
    
    # Don't process empty messages
    if not user_input.strip():
        print("⚠️ Please enter a message!")
        continue
        
    try:
        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_input})
        
        print("🤔 AI is thinking...")
        
        # Send conversation to the AI model
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",          # The AI model we're using
            messages=conversation_history,    # Our conversation so far
            temperature=1,                    # How creative should the AI be? (0-2)
            max_tokens=96,                   # Maximum length of response
            top_p=0.8,                       # Another creativity control
            frequency_penalty=0.5,           # Reduce repetition
            presence_penalty=0              # Encourage new topics
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content
        
        # Add AI response to conversation history
        conversation_history.append({"role": "assistant", "content": ai_response})
        
        # Display the response
        print(f"\n🤖 AI: {ai_response}")
        print(f"📊 Messages in conversation: {len(conversation_history)}")
        
    except Exception as e:
        print(f"❌ Oops! Something went wrong: {e}")
        print("🔄 Let's try again!")
        # Remove the user message since we couldn't process it
        if conversation_history and conversation_history[-1]["role"] == "user":
            conversation_history.pop()
        continue