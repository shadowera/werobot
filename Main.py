import itchat
import requests
import hashlib
import json
from itchat.content import *


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    hash = hashlib.md5()
    print(msg.fromUserName)
    hash.update(msg.fromUserName.encode('utf-8'))
    postdata = {'key': '10cfd9b85d0b4459bcbaabaab5e267da', 'info': msg.text, 'userid': hash.hexdigest()}
    r = requests.post("http://www.tuling123.com/openapi/api", data=postdata)
    print(r.text)
    answer = json.loads(r.text)
    msg.user.send(answer['text'])
    if answer['code'] == '200000':
        msg.user.send(answer['url'])


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


itchat.auto_login(True)
itchat.run(True)
