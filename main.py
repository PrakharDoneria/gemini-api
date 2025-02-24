import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS  # Import CORS

# Configure the API key for Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model with the desired configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    system_instruction="you are a professional music maker ai that makes music with less than 1500 characters",
)

# Create Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/generate": {"origins": ["https://sunosynth-ai.web.app", "https://sunosynth-web.vercel.app"]}})
# You can specify allowed origins

# Route to handle POST requests for chat generation
@app.route('/generate', methods=['POST'])
def generate():
    # Get input from the POST request
    input_data = request.json.get("input")

    if not input_data:
        return jsonify({"error": "No input provided"}), 400
    
    # Start the chat session (one per request for stateless interaction)
    chat_session = model.start_chat(history=[])
    
    # Send the input message to the model
    response = chat_session.send_message(input_data)
    
    # Return the response from the model as JSON
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
