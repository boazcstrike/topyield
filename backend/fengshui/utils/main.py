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
                        You are a fengshui master. It is 2025, the year of the snake. Based on the requested gregorian birthday, please respond with a JSON object. Do not put ```json``` and remove all line breaks. If possible, reference as much chinese idioms as possible but use english as the main language. Be poetic, deep, and creative. Sample:
                        {
                            "gregorian_calendar": "MM/DD/YYYY hh:mm",
                            "gregorian_lunar_calendar": "MM/DD/YYYY hh:mm", # this should be adjusted to the lunar calendar from the gregorian calendar
                            "lunar_calendar": "十二月廿九 丁酉",
                            "zodiac": "Water/Wood Dog 木狗",
                            "zodiac_vs_this_year": "explain the synergy and bad side for the zodiac",
                            "good_luck_colors_for_this_year": []  # give all,
                            "bad_luck_colors_for_this_year": []  # give all,
                            "good_aspects": [  # give at least 5, at most 10
                                {
                                    "aspect": "Harmonious relationships",
                                    "short_reason": "sample short reason, 2 sentences please."
                                },
                                ...
                            ],
                            "bad_aspects": [  # give at least 5, at most 10
                                {
                                    "aspect": "Relationship conflicts",
                                    "short_reason": "sample short reason, 2 sentences please."
                                },
                                ...
                            ],
                            "business_advise": "> 3 sentences",
                            "relationship_advise": "> 3 sentences.",
                            "life_advise": "< 10 sentences",
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
        print(f"\nPrompt tokens: {response.usage.prompt_tokens}")
        print(f"Completion tokens: {response.usage.completion_tokens}")
        print(f"Total tokens: {response.usage.total_tokens}")
        cleaned_response = response.choices[0].message.content.strip()
        cleaned_response = json.loads(cleaned_response)
        return cleaned_response