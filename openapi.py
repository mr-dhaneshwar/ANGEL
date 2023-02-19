import openai
import time

openai.api_key = "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"

def angel(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    time.sleep(1)
    return message