import json


class Configuration:
    def __init__(self, environment):
        self.environment = environment
        properties = open('/home/rafael/projects/FirstPyProject/Properties.json')
        environmentList = json.load(properties)

        for env in environmentList:
            if environment == env.get('environment'):
                self.url = env.get('url')
                self.user = env.get('user')
                self.password = env.get('pass')
                return
