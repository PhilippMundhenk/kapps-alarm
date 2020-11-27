class Kapp():
    icon = "res/icon.png"
    name = "Alarm"

    def __init__(self, appID, appPath, ctx):
        self.appID = appID
        self.appPath = appPath
        self.ctx = ctx

    def getAppPythonPath(self):
        return self.appPath

    def getAppFSPath(self):
        return self.appPath.replace(".", "/") + "/"

    def getAppURL(self):
        return "/apps/" + str(self.appID)

    def urlToAppPath(self, url):
        return url.replace(self.getAppURL(), self.getAppFSPath())

    def getRes(self, path):
        with open(path, 'r') as file:
            return file.read()

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
    print("register " + Kapp.name)
    return Kapp(appID, appPath, ctx)
