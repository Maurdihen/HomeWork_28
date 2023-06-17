from django.http import JsonResponse
from django.views import View

class MainView(View):

    def get(self, *args, **kwargs):
        try:
            return JsonResponse({"status": "ok"}, status=200)
        except:
            return JsonResponse({"status": "bad"}, status=404)
