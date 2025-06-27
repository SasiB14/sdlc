import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API KEY")

client = OpenAI(api_key=api_key)

def classify_into_sdlc(text: str) -> dict:
    prompt = f"""
    Classify the following project document into the 5 SDLC phases (Requirements, Design, Implementation, Testing, Maintenance).
    Return a JSON with each phase as a key and its content as value.
    
    Document:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert software engineer."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    try:
        return eval(content) if isinstance(content, str) else content
    except:
        return {"Error": "Failed to parse response"}
