from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the message history with a system prompt
messages = [
    {
        "role": "system", 
        "content": "You are an AI therapist that listens and reflects back with empathy."
    }
]

def get_gpt_response(user_input):
    from openai import OpenAI
    client = OpenAI()

    # Add the user's message to the history
    messages.append({
        "role": "user", 
        "content": user_input
    })

    try:
        # Call the GPT API with the full message history
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=1.2
        )
        # Extract and clean the assistant's reply
        assistant_reply = response.choices[0].message.content.strip()

        # Add the assistant's reply to the message history
        messages.append({
            "role": "assistant", 
            "content": assistant_reply
        })

        return assistant_reply
    except Exception as e:
        print(f"[GPT Error] {e}")
        return