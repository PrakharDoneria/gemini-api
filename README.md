### Sample Request (POST)

```bash
curl -X POST http://127.0.0.1:5000/generate -H "Content-Type: application/json" -d '{"input": "Create a description for a new music album inspired by nature."}'
```

Alternatively, you can use tools like Postman or any HTTP client to make the request with the same structure.

### Sample Response (JSON)

The server will respond with a JSON object containing the generated text. Here's an example response:

```json
{
  "response": "The album 'Echoes of Nature' brings the sounds of the earth to life, with melodies that capture the essence of forests, rivers, and mountains. Each track immerses the listener in a world of serene beauty and vibrant energy, evoking the majesty of nature's landscapes."
}
```