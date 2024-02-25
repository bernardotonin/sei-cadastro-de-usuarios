import pyautogui
from keyboard import write
from pyautogui import click
from util import loadData, User
from config import SPEED, FILE_NAME
# 10 Segundos para mudar para a pagina do sistema
pyautogui.time.sleep(10)
pyautogui.PAUSE = 0.2
def cadastro():
    userList : list[User] = loadData(FILE_NAME)    
    # Usuarios
    click(164,369, duration=SPEED)

    for user in userList:
        #Novo 
        click(130,405, duration=SPEED)
        pyautogui.time.sleep(4)
        # Orgão
        click(470,309, duration=SPEED)
        # PMFI
        click(463,351, duration=SPEED)
        # Sigla
        click(460,366, duration=SPEED)
        # Digitando sigla
        write(user.login)
        # Nome
        click(458,424, duration=SPEED)
        # Digitando nome
        write(user.name)
        # CPF
        click(453,602, duration=SPEED)
        # Preenchendo CPF
        write(user.cpf)
        # Email
        click(452,662, duration=SPEED)
        # Preenchendo email
        write(user.email)
        # Salvar
        click(1795,244, duration=SPEED)
        pyautogui.time.sleep(6)
        try:
            pyautogui.locateOnScreen('errormsg.png')
            # Cancelar
            click(1867,245, duration=SPEED)
            pyautogui.time.sleep(7)
        except pyautogui.ImageNotFoundException:
            pass
        click(164,371, duration=SPEED)

      
    

if __name__ == "__main__":
    cadastro()