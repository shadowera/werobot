import json

import itchatmp
import requests

appId = 'wxe31287e98a274894'
appSecret = '3d8b928b3263ad3fc88e497a5f494abc'

url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appId, appSecret)

r = requests.get(url)
print(r.text)
answer = json.loads(r.text)
token = answer['access_token']
itchatmp.update_config(itchatmp.WechatConfig(
    token=token,
    appId=appId,
    appSecret=appSecret))


@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def reply(msg):
    print(msg)


itchatmp.run()
