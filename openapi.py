import openai
import time

openai.api_key = "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"

def angel(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    time.sleep(1)
    return message

# while True:
#     x = input('enter prompt: ')
#     y = angel(x)
#     print(y)