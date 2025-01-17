import openai
import os
from dotenv import load_dotenv

# Load the .env file to get the API key
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
def rewrite_paragraph(paragraph, style="formal"):
    prompt = f"Rewrite the following paragraph in a {style} style:\n\n{paragraph}"

    try:
        # Make the API request to OpenAI using gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using the updated model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        # Return the rewritten text
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while trying to rewrite the paragraph."

# Example Usage
paragraph = input("Enter a sentence or a paragraph for the OMEGA AI to rewrite: ")
style = input("What style of writing would you like the OMEGA AI to rewrite for you? There is Casual, Professional, Formal, or Creative. ")
rewritten_paragraph = rewrite_paragraph(paragraph, style)
print(rewritten_paragraph)
