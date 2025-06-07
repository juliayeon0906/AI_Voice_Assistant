from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_gpt_response(user_input):
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=False,
            messages=[
                {
                    "role": "system", 
                    "content": "You are an AI therapist that listens and reflects back with empathy."
                },
                {
                    "role": "user",
                    "content": user_input
                },
            ],
            temperature=1.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[GPT Error] {e}")
        return