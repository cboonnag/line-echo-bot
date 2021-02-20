from flask import Flask, render_template, make_response
from flask import request, abort 
from config import * 

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import requests 
import json 
import os 
import time 

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@app.route("/")
def home():
    return "HOME"

@handler.default()
def default(event):      
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = int(os.environ.get('PORT',8080)))