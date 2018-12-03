from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from summarizer.Summarize import doMagic
import json
import html


@csrf_exempt
def challenge(request):
    if request.method == "POST":
        channelId = request.POST.get('channelId')
        user = request.POST.get('user')
        token = request.POST.get('token')
        summarized = doMagic(channelId, user, token)
        res = ""
        for cluster in summarized:
            for msgObj in cluster:
                res += msgObj.get('text')+"\n\n"
                # res+="##"+msgObj.get('user')+"\n"+"###"+msgObj.get('text')+"\n\n"
                # res += '''<div class='c-message c-message--light'><div class='c-message__gutter'><a href='#' class='c-message__avatar c-avatar c-avatar--interactive' tabindex='-1' aria-hidden='true' style='height: 36px; line-height: 36px; width: 36px;'><img class='c-avatar__image' src='https://ca.slack-edge.com/TEB7A27B7-UEDJTMQCQ-g0564e5b9f3a-48'></a></div><div class='c-message__content'><div class='c-message__content_header'><span class='c-message__sender'><a class='c-message__sender_link' href='#'>''' + \
                #     msgObj.get('user')+'''</a></span></div><span class='c-message__body c-message__body--dir' >''' + \
                #     msgObj.get('text')+'''</span></div></div>'''
                # res.replace('&', '&amp;')
                # res.replace('<', '&lt;')
                # res.replace('>', '&gt;')
        output = {"res": res}

    return JsonResponse(output)
