import os
from termcolor import cprint 
def drawMenu(autologin=False):
    os.system("cls")
    print(f'{"="*30}Reality application{"="*30}')
    cprint(f'1. Run program', "blue")
    cprint(f'2. Auto login ({"on" if autologin else "off"})', "blue")
    cprint(f'3. Change path', "blue")
    cprint(f'4. Exit', "blue")
    print(f'{"="*79}')