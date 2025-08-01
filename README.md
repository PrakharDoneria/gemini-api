### 🔄 Updated Sample Request (POST)

You can now include an optional `system_instruction` field to customize the AI's behavior.

```bash
curl -X POST http://127.0.0.1:5000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Create a description for a new music album inspired by nature.",
    "system_instruction": "You are a poetic music critic AI that writes beautiful descriptions of ambient albums."
}'
```

If you omit `system_instruction`, the default will be used:

```bash
curl -X POST http://127.0.0.1:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"input": "Create a description for a new music album inspired by nature."}'
```

You can also use tools like **Postman**, **Insomnia**, or any HTTP client with the same structure.

---

### ✅ Request JSON Fields

| Field                | Type   | Required | Description                                                                |
| -------------------- | ------ | -------- | -------------------------------------------------------------------------- |
| `input`              | string | ✅        | The user prompt to generate a response for.                                |
| `system_instruction` | string | ❌        | (Optional) Custom system instruction to change the AI’s behavior and tone. |

---

### 📤 Sample Response (JSON)

The server responds with a JSON object containing the generated text:

```json
{
  "response": "The album 'Echoes of Nature' brings the sounds of the earth to life, with melodies that capture the essence of forests, rivers, and mountains. Each track immerses the listener in a world of serene beauty and vibrant energy, evoking the majesty of nature's landscapes."
}
```
