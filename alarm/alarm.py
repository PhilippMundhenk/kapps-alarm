from core import kapp


class Alarm(kapp.Kapp):
    icon = "res/icon.png"
    name = "Alarm"

    def handleGet(self, path):
        if "/res" in path:
            # app resource requested
            return {"code": 200, "content": self.getRes(self.urlToAppPath(path))}
        elif path.split(self.getAppURL())[1] == "":
            # app is started
            return {"code": 200, "content": "<html><h1>Alarm App</h1></html>"}
        else:
            return {"code": 404, "content": "<html><h1>Not Found</h1></html>"}


def register(appID, appPath, ctx):
    print("register " + Alarm.name)
    return Alarm(appID, appPath, ctx)
