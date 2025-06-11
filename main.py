#main.py

import os
import sys
from dotenv import load_dotenv
load_dotenv()


api_key = os.environ.get("GEMINI_API_KEY")
from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def main():

    # Function to get the user prompt from command line arguments
    def get_prompt():
        if len(sys.argv) < 2:
            print("Usage: python main.py <prompt>")
            sys.exit(1)
        prompt = sys.argv[1]
        return prompt

    prompt = get_prompt()

    # Create and track message history with the user prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    # Generate content using the Gemini model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
    )

    # New command line argument for verbose output
    if "--verbose" in sys.argv:
        print(response.text)
        print(f"User prompt:", sys.argv[1])
        print(f"Prompt tokens:", response.usage_metadata.prompt_token_count)
        print(f"Response tokens:", response.usage_metadata.candidates_token_count)
    else:
        print(response.text)

if __name__ == "__main__":
    main()
    print("Done.")
