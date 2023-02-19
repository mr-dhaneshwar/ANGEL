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