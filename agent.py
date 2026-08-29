def agent():
    print("Hello! Main tumhara AI Agent hoon.")
    print("Main tumhare commands ka wait kar raha hoon.")

    while True:
        command = input("Tum: ")

        if command.lower() == "exit":
            print("Agent: Allah Hafiz!")
            break

        print("Agent:", command)


agent()
