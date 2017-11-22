import werobot

robot = werobot.WeRoBot(token='guishuai')


@robot.text
def first(message, session):
    if 'first' in session:
        return '你之前给我发过消息'
    session['first'] = True
    return '你之前没给我发过消息'


@robot.image
def img(message):
    return message.img


robot.config['APP_ID'] = 'wxe31287e98a274894'
robot.config['APP_SECRET'] = '3d8b928b3263ad3fc88e497a5f494abc'
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
client = robot.client
client.create_menu({
    "button": [{
        "type": "click",
        "name": "今日歌曲",
        "key": "music"
    }]
})


@robot.key_click("music")
def music(message):
    return '你点击了“今日歌曲”按钮'


robot.run()
