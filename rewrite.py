import openai
import os
from dotenv import load_dotenv

# Load the .env file to get the API key
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY") or "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"
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
paragraph = "This is an example paragraph that needs improvement."
rewritten_paragraph = rewrite_paragraph(paragraph, style="professional")
print(rewritten_paragraph)
