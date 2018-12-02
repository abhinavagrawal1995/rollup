from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def challenge(request):
    if request.method == "POST":
        channelName = request.POST.get('channelName')
        msgArr = [{"user": "U012AB3CDE", "text": channelName},
                  {"user": "U012AB3CDE", "text": "Hello world"}]

    return JsonResponse(msgArr, safe=False)
