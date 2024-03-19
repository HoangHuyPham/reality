import os, json
def retrieveJSON(type):
    res = None
    if (type == "setting"):
        with open(os.getcwd()+"/config/setting.json", "r+") as jfile:
            res = json.loads(jfile.read())
    return res

def saveJSON(data:str = None) -> int:
    if (str == None):
        return -1
    try:
        with open(os.getcwd()+"/config/setting.json", "rb+") as jfile:
            res = jfile.write(bytes(str, "utf-8"))
    except Exception:
        init_data:dict = {
            "account" : {
            "auto_login" : False,
            "nro_path" : None
            }
        }
        json_convert = json.dumps(init_data)
        with open(os.getcwd()+"/config/setting.json", "wb+") as jfile:
            res = jfile.write(bytes(json_convert, "utf-8"))
    return res