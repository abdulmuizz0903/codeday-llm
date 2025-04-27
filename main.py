import groq, os, requests, markdown
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()
app = Flask(__name__)
CORS(app)
GROQ_KEY = os.getenv("GROQ_KEY")

groq_client = groq.Groq(api_key=GROQ_KEY)

@app.route('/chat', methods=['POST'])
def chat():
    incoming = request.get_json()
    if "messages" not in incoming:
        return jsonify({"error": "No messages provided"}), 400
    try: 
        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=incoming["messages"],
            temperature=1,
            max_tokens=96,
        )
        reply = markdown.markdown(response.choices[0].message.content)
        response = jsonify({"role": "assistant", "content": reply})
        print(f"<--- REPLY: {response.get_json()} --->")
        return response, 200
    except Exception as e:
        print(f"<--- AN ERROR OCCURED {e}--->")
        return jsonify({"error": str(e)}), 500
        


if __name__ == "__main__":
    app.run(debug=True, port=2718)
