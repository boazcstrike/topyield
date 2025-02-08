from django.core.management.base import BaseCommand
from django.conf import settings

from openai import OpenAI

class Command(BaseCommand):
    help = 'Description of your command'

    def handle(self, *args, **kwargs):
        print("\n===============================")
        print("         Start of Script       ")
        print("===============================\n")

        oai = BoOpenAI()

        gregorian_date = '03-01-1994T08:15'
        lunar_date = oai.convert_gregorian_to_lunar(gregorian_date)
        print(lunar_date)

        print("\n===============================")
        print("         End of Script       ")
        print("===============================\n")

class BoOpenAI():
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o-mini"
        self.max_tokens = 500

    def convert_gregorian_to_lunar(self, gregorian_date):
        prompt = f"Convert {gregorian_date} to a lunar date and give me reading."
        messages = [
            {
            "role": "developer",
            "content": [
                {
                "type": "text",
                "text": """
                    You are a fengshui master. Initially, respond with the "Lunar birthday on gregorian calendar: MM-DD-YYYY hh:mm". Explain the chinese luck, colors and zodiac. First, explain all the bad energies, and negatives. Then explain all the good energies, and positives. Finally, give advise on the future and what to take note of. Remove all syntax.
                """
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                }
            ]
            }
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
        )
        print("\n",response,"\n")
        lunar_date = response.choices[0].message.content.strip()
        return lunar_date