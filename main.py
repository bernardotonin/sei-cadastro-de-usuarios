import pyautogui
from keyboard import write
from pyautogui import click
from util import loadData, User, searchErrorMsg
from config import SPEED, FILE_NAME
# 10 Segundos para mudar para a pagina do sistema
pyautogui.time.sleep(5)

def cadastro():
    userList : list[User] = loadData(FILE_NAME)    
    # Usuarios
    click(130,371, duration=SPEED)

    for user in userList:
    #Novo 
        click(150,400, duration=SPEED)
        # Orgão
        click(455,315, duration=SPEED)
        # PMFI
        click(455,350, duration=SPEED)
        # Sigla
        click(455,370, duration=SPEED)
        # Digitando sigla
        write(user.login)
        # Nome
        click(455,430, duration=SPEED)
        # Digitando nome
        write(user.name)
        # CPF
        click(455,600, duration=SPEED)
        # Preenchendo CPF
        write(user.cpf)
        # Email
        click(455,660, duration=SPEED)
        # Preenchendo email
        write(user.email)
        # Salvar
        click(1793,244, duration=SPEED)
        pyautogui.time.sleep(2)
        errorMsgExists = searchErrorMsg()
        if errorMsgExists:
            click(1867,245, duration=SPEED)
        click(130,371, duration=SPEED)
    

if __name__ == "__main__":
    cadastro()