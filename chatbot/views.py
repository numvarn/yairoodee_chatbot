from django.shortcuts import render, HttpResponse
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextSendMessage, FlexSendMessage, BubbleContainer, ImageComponent, URIAction, BoxComponent
)

# Create your views here.


def index(request):
    return HttpResponse("This is Yairoodee's chatbot.")
