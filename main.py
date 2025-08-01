import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

# Configure the API key for Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Default generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create Flask app
app = Flask(__name__)

# Enable CORS for all origins or limit to specific ones
CORS(app, resources={r"/generate": {"origins": "*"}})  # Change "*" to specific origins if needed

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    input_data = data.get("input")
    system_instruction = data.get("system_instruction", "you are a professional music maker ai that makes music with less than 1500 characters")

    if not input_data:
        return jsonify({"error": "No input provided"}), 400

    # Initialize the model with the provided or default system instruction
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    # Start a new chat session
    chat_session = model.start_chat(history=[])
    
    # Send message to the model
    response = chat_session.send_message(input_data)

    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
