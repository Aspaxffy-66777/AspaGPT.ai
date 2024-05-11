import openai

def main():
    prompt = "Merhaba, size nasıl yardımcı olabilirim?"

    while True:
        user_input = input("> ")

        if user_input.lower() == "çık":
            break

        response = generate_response(prompt, user_input)
        print(response)

def generate_response(prompt, user_input):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )

    response = completion.choices[0].text.strip()
    prompt += "\n" + user_input + "\n" + response

    return response

if __name__ == "__main__":
    main()
