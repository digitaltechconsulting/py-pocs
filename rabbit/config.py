import json

appsettings = '''
{
    "rabbitServer": "localhost",
    "queue": "hello"

}
'''

class AppSettings:
    def __init__(self):
        data = json.loads(appsettings)
        self.rabbitServer = data['rabbitServer']
        self.queue = data['queue']