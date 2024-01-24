class PromptHandler:
    def __init__(self, client):
        self.client = client
        
    def set_client_details(self, first_name, last_name, email, language):
        self.client.set_first_name(first_name)
        self.client.set_last_name(last_name)
        self.client.set_email(email)
        self.client.set_language(language)
        
    def get_formatted_prompt(self, type):
        transcripts = {
            "short": {
                "English": """
                    Coach: 'How do you feel about the situation?' 
                    Client: 'I'm a bit overwhelmed.'
                    ...< 100+ lines >...
                """
            }
        }
        
        prompt_template = f"""
            You're an ICF MCC certified coach, responsible for training individuals to meet international coaching standards.

            Following are your client details:
            First Name: {self.client.first_name}
            Last Name: {self.client.last_name}
            Email: {self.client.email}
            Preferred Language: {self.client.language}

            Following is a sample script that explains how coaching should be carried out.
            Format: {type}
            Script:
            {transcripts.get(type, {}).get(self.client.language)}

            Please follow the instructions carefully and ensure each session is fruitful.
            """
        
        return prompt_template
    