from core.kapp import Kapp


class Alarm(Kapp):
    name = "Alarm"

    def iconCallback(self):
        return {"code": 200, "content": self.getRes("icon.png")}
        

def register(appID, appPath, ctx):
    print("register " + Alarm.name)
    return Alarm(appID, appPath, ctx)
