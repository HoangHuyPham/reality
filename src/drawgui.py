import os
from termcolor import cprint, colored
def drawMenu(auto_login=False, nro_path=None) -> int:
    os.system("cls")
    print(f'{"="*30}Reality application{"="*30}')
    cprint(f'1. Run program', "green")
    cprint(f'2. Auto login ({"on" if auto_login else "off"})', "green")
    print(colored(f'3. Change path ', "green")+colored("(", "green")+colored(f'{nro_path}', "light_magenta")+colored(")", "green"))
    cprint(f'4. Exit', "green")
    select = int(input("Select: "))
    return select