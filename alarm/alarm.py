from core.kapp import Kapp
from core.httpResponse import HTTPResponse


class Alarm(Kapp):
    name = "Alarm"

    def iconCallback(self, kcommand):
        return HTTPResponse(content=self.getRes("icon.png"))


def register(appID, appPath, ctx):
    print("register " + Alarm.name)
    return Alarm(appID, appPath, ctx)
