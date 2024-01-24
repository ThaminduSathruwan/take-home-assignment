from client import Client
from promptHandler import PromptHandler

def main():
    client = Client("John", "Doe", "john.doe@example.com", "English")
    prompt_handler = PromptHandler(client)
    print(prompt_handler.get_formatted_prompt("short"))
    
if __name__ == "__main__":
    main()
