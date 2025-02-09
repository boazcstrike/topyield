from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .utils.main import BoOpenAI


class FengShuiReadingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """sample response:
        {
            "reading": {
                "gregorian_calendar": "03/01/1994 08:15",
                "gregorian_lunar_calendar": "01/19/1994 08:15",
                "lunar_calendar": "一月十九 甲戌",
                "zodiac": "Wood Dog",
                "good_luck_colors_for_this_year": [
                    "Green",
                    "Brown",
                    "Gold"
                ],
                "bad_luck_colors_for_this_year": [
                    "Red",
                    "Black"
                ],
                "good_aspects": [
                    {
                        "aspect": "Harmonious relationships",
                        "short_reason": "Strong social connections foster mutual support."
                    },
                    {
                        "aspect": "Career advancement",
                        "short_reason": "Opportunities for growth and recognition in the workplace."
                    },
                    {
                        "aspect": "Financial stability",
                        "short_reason": "Smart investments yield positive returns."
                    },
                    {
                        "aspect": "Health improvements",
                        "short_reason": "Increase in energy and well-being this year."
                    },
                    {
                        "aspect": "Personal development",
                        "short_reason": "Focus on self-growth leads to new insights."
                    }
                ],
                "bad_aspects": [
                    {
                        "aspect": "Relationship conflicts",
                        "short_reason": "Miscommunication may lead to misunderstandings."
                    },
                    {
                        "aspect": "Work-related stress",
                        "short_reason": "Increased workload may cause pressure."
                    },
                    {
                        "aspect": "Health concerns",
                        "short_reason": "Potential for seasonal illnesses."
                    },
                    {
                        "aspect": "Financial risks",
                        "short_reason": "Be cautious with new ventures."
                    },
                    {
                        "aspect": "Travel complications",
                        "short_reason": "Possible delays or disruptions in travel plans."
                    }
                ],
            }
        }
        """

        birth_date_time = request.data.get('gregorian_birthday')
        bo_openai = BoOpenAI()
        reading = bo_openai.convert_gregorian_to_lunar(birth_date_time)
        return Response({'reading': reading})
