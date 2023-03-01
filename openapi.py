import openai
import time

openai.api_key = ""

def angel(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )

    message = completions.choices[0].text
    # time.sleep(1)
    return message