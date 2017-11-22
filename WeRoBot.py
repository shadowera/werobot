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


@robot.voice
def voi(message):
    print(message.type)
    print(message.recognition)
    return message.recognition


@robot.subscribe
def onsubscribe():
    return 'hello world'


@robot.location
def location(message):
    return message.label


robot.config['APP_ID'] = 'wxe31287e98a274894'
robot.config['APP_SECRET'] = '3d8b928b3263ad3fc88e497a5f494abc'
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
client = robot.client

robot.run()
