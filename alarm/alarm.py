import os

appFolder = None


def register():
    global appFolder
    print("register Alarm")
    path = os.path.dirname(os.path.realpath(__file__))
    appFolder = path.split("kapps")[1]
    return {"icon": "res/icon.png", "name": "Alarm"}


def handle(path):
    if "/res" in path:
        # app resource requested
        return {"code": 200, "content": getRes(path.replace("/", "", 1))}
    elif path.split(appFolder)[1] == "":
        # app is started
        return {"code": 200, "content": "<html><h1>Alarm App</h1></html>"}
    else:
        return {"code": 404, "content": "<html><h1>Not Found</h1></html>"}


def getRes(path):
    with open(path, 'r') as file:
        return file.read()
