def register():
    print("register Alarm")
    return {"icon": "res/icon.png", "name": "Alarm"}


def handle(path):
    if "/res" in path:
        return {"code": 200, "content": getRes(path.replace("/", "", 1))}


def getRes(path):
    with open(path, 'r') as file:
        return file.read()
