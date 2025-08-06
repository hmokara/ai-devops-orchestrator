import os
import openai

def get_error_summary(error_log, api_key):
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert DevOps assistant."},
            {"role": "user", "content": f"Summarize and suggest quick fix for this error log:\n{error_log}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
        exit(1)
    with open("sample_error.log", "r") as f:
        error_log = f.read()
    summary = get_error_summary(error_log, api_key)
    print("Error Summary & Fix:\n", summary)
