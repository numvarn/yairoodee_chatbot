from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextSendMessage, FlexSendMessage, BubbleContainer, ImageComponent, URIAction, BoxComponent
)

# Create your views here.
line_bot_api = LineBotApi(
    'OfUecJfUK9JXszTysTV2DJmN3P9ckblUryfYIW+LUh/AWXt9KPL26U5cl1sPFcsCmAUd7d5uJfDvxqlDEGCuz8AncGqLozRrkCQBzxQ1nvaChSiqjo4ml37/Q8oUSNadaYVOmT14p8vlaHpEXm8mIwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('18faa98b8de47b520f83083dbc4ff534')


def index(request):
    return HttpResponse("This is Yairoodee's chatbot.")


@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def callback(request):
    req = request.data
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']

    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    return Response(status=HTTP_200_OK)
