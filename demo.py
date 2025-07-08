import groq, json, requests, os
from dotenv import load_dotenv

load_dotenv()

conversation_history = []

GROQ_KEY=os.getenv("GROQ_KEY")
groq_client = groq.Groq(api_key=GROQ_KEY)
while True:
    user_input = input("Enter your next prompt. Enter \"Q\" to quit. \n >>>")
    if user_input == "Q":
        break
    else:
        try:
            conversation_history.append({"role": "user", "content": user_input})
            response = groq_client.chat.completions.create(
                model="llama3-8b-8192",
                messages=conversation_history,
                temperature=1,
                max_tokens=96,
                top_p=0.8,
                frequency_penalty=0.5,
                presence_penalty=0
            )
            formatted_response = response.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": formatted_response})
            print(conversation_history)
            print(f"----- \n Groq:{formatted_response} \n-----")
        except Exception as e:
            print(f"<<< AN ERROR OCCURED >>> \n {e} \n --------------------------------------------")
            continue