import pyautogui
from keyboard import write
from pyautogui import click
from util import loadUsers, loadUnidades, User, Unidade
from config import SPEED
# 10 Segundos para mudar para a pagina do sistema
pyautogui.time.sleep(3)

def cadastroUsuarios():
    userList : list[User] = loadUsers()    
    # Usuarios
    click(120,343, duration=SPEED)
    for user in userList:
        #Novo 
        click(109,373, duration=SPEED)
        pyautogui.time.sleep(1)
        # Orgão
        click(509,281, duration=SPEED)
        # PMFI
        click(425,321, duration=SPEED)
        # Sigla
        click(412,336, duration=SPEED)
        # Digitando sigla
        write(user.login)
        # Nome
        click(410,390, duration=SPEED)
        # Digitando nome
        write(user.name)
        # CPF
        click(413,571, duration=SPEED)
        # Preenchendo CPF
        write(user.cpf)
        # Email
        click(424,630, duration=SPEED)
        # Preenchendo email
        write(user.email)
        # Salvar
        click(1795,214, duration=SPEED)
        pyautogui.time.sleep(2)
        try:
            pyautogui.locateOnScreen('errormsg.png')
            # Cancelar
            click(1864,215, duration=SPEED)
            pyautogui.time.sleep(1)
        except pyautogui.ImageNotFoundException:
            pass
        click(120,343, duration=SPEED)

def cadastroUnidades():
    unidades : list[Unidade] = loadUnidades()
    # unidades
    click(151,307, duration=SPEED)
    for unidade in unidades:
        # nova
        click(141,342, duration=SPEED)
        pyautogui.time.sleep(1)
        # sigla
        click(422,334, duration=SPEED)
        write(unidade.sigla)
        # Nome
        click(427,392, duration=SPEED)
        write(unidade.nome)
        # salvar
        click(1795,214, duration=SPEED)
        pyautogui.time.sleep(2)
        try:
            pyautogui.locateOnScreen('errormsgunid.png')
            # Cancelar
            click(1864,215, duration=SPEED)
            pyautogui.time.sleep(1)
        except pyautogui.ImageNotFoundException:
            pass
        click(151,307, duration=SPEED)    

if __name__ == "__main__":
    cadastroUsuarios()