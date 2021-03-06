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

    reply(intent, text, reply_token, id, disname)

    return Response(status=HTTP_200_OK)


def reply(intent, text, reply_token, id, disname):
    if intent == 'Intent5':
        # ตั้งค่าข้อความตอบกลับ Flex Message
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents=BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url='https://s.isanook.com/sp/0/rp/r/w728/ya0xa0m1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL3NwLzAvdWQvMjY4LzEzNDAwNTgvcmUoMSkuanBn.jpg',
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri='http://www.sanook.com', label='label')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        {
                            "type": "text",
                            "text": "Brown Cafe",
                            "weight": "bold",
                            "size": "xl"
                        },
                    ],
                ),
            ),
        )

        # ตั้งค่าข้อความตอบกลับ Text Message
        text_message = TextSendMessage(
            text='สวัสดี {} \nทดสอบสำเร็จ'.format(disname))

        # line_bot_api.reply_message(reply_token, text_message)
        line_bot_api.reply_message(reply_token, [flex_message, text_message])
