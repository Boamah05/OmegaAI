import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to set up OpenAI API key
def initialize_openai():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key is missing. Please set it in the .env file.")

# Function to generate a recipe using the provided ingredients
def generate_recipe(ingredients):
    initialize_openai()  # Ensure API key is set
    if not ingredients:
        raise ValueError("Ingredients list cannot be empty.")

    prompt = f"Create a detailed recipe using the following ingredients: {', '.join(ingredients)}."
    
    try:
        # Use ChatCompletion API with the gpt-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative and helpful chef."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7  # Adjust creativity level
        )
        # Return the generated recipe
        return response['choices'][0]['message']['content'].strip()

    except openai.error.OpenAIError as e:
        # Catch and handle OpenAI-specific errors
        return f"OpenAI API error: {e}"
    except Exception as e:
        # Catch any other errors
        return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    ingredients = ["chicken", "garlic", "onion", "olive oil", "lemon"]
    recipe = generate_recipe(ingredients)
    print("Generated Recipe:\n")
    print(recipe)
