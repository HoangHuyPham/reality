import drawgui, utils, time

        

def main():
    setting:dict = dict(utils.retrieveJSON("setting"))
    is_auto_login:str = setting.get("account").get("auto_login")
    nro_path:str = setting.get("account").get("nro_path")
    init_data:dict = {"auto_login": is_auto_login, "nro_path": nro_path}
    select:int = -1
 
    while(select != 2):
        select = drawgui.drawMenu(auto_login= is_auto_login, nro_path=nro_path)
        handle(select)
    print("bye")
    
def handle(select:int):
    init_data:dict = utils.retrieveJSON("setting")
    if (select == 2):
        init_data["account"]["auto_login"] = not init_data["account"]["auto_login"]
        utils.saveJSON(init_data)
        time.sleep(5)
    
if __name__ == "__main__":
    main()