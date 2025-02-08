from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .utils.main import BoOpenAI


class FengShuiReadingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        birth_date_time = request.data.get('gregorian_birthday')
        bo_openai = BoOpenAI()
        reading = bo_openai.convert_gregorian_to_lunar(birth_date_time)
        return Response({'reading': reading})
