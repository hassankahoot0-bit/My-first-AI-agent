import ollama


def agent():
    print("Hello! Main tumhara AI Agent hoon.")
    print("Type 'exit' to quit.")

    while True:
        command = input("Tum: ")

        if command.lower() == "exit":
            print("Agent: Allah Hafiz!")
            break

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        print("Agent:", response["message"]["content"])


agent()
