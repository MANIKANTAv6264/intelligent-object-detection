from groq import Groq
from dotenv import dotenv_values

env = dotenv_values(".env")

client = Groq(api_key=env.get("GroqAPIKey"))
MODEL = env.get("Model_name")

def ask_brain(question):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant. Use general internet knowledge. "
                        "If exact identification is not possible, explain the limitation clearly."
                    )
                },
                {"role": "user", "content": question}
            ],
            max_tokens=120,
            temperature=0.4
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Groq API Error:", e)
        return "Sorry, I could not fetch information right now."
