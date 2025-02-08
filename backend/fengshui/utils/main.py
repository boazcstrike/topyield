import json

from openai import OpenAI

from django.conf import settings


class BoOpenAI():
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o"
        self.max_tokens = 1800

    def convert_gregorian_to_lunar(self, gregorian_date):
        prompt = f"Convert {gregorian_date} to a lunar date and give me reading."
        messages = [
            {
                "role": "developer",
                "content": [
                    {
                    "type": "text",
                    "text": """
                        You are a fengshui master. Based on the requested gregorian birthday, please respond with a JSON object. Do not put ```json``` and remove all line breaks. Sample:
                        {
                            "gregorian_calendar": "MM/DD/YYYY hh:mm",
                            "gregorian_lunar_calendar": "MM/DD/YYYY hh:mm", # this should be adjusted to the lunar calendar from the gregorian calendar
                            "lunar_calendar": "十二月廿九 丁酉",
                            "zodiac": "Water/Wood Dog",
                            "good_luck_colors_for_this_year": []  # give all,
                            "bad_luck_colors_for_this_year": []  # give all,
                            "good_aspects": [  # give at least 5, at most 10 
                                {
                                    "aspect": "Harmonious relationships",
                                    "percentage": 50,  # based off positive strength of aspect
                                    "short_reason": "sample short reason, 2 sentences."
                                },
                                ...
                            ],
                            "bad_aspects": [  # give at least 5, at most 10
                                {
                                    "aspect": "Relationship conflicts",
                                    "percentage": 25,  # based off negative strength of aspect
                                    "short_reason": "sample short reason, 2 sentences."
                                }
                            ]
                        }  
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
        cleaned_response = response.choices[0].message.content.strip()
        cleaned_response = json.loads(cleaned_response)
        return cleaned_response