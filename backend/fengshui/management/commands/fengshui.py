from django.core.management.base import BaseCommand
from django.conf import settings

from fengshui.utils.fengshui import BoOpenAI


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
