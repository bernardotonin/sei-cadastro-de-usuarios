from config import USER_FILE_NAME, UNIDADES_FILE_NAME
import csv

class User:
    def __init__(self, name : str, email : str, login: str, cpf : str):
        self.name = name
        self.email = email
        self.login = login
        self.cpf = cpf

class Unidade:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome

def loadUsers() -> list[User]:
    with open(USER_FILE_NAME, newline='', encoding="utf8") as dataFile:
        data = csv.reader(dataFile, delimiter=',')
        users : list[User] = []
        for row in data:
            x = User(row[0].title(), row[1], row[2], row[3])
            users.append(x)
    return users

def loadUnidades() -> list[Unidade]:
    with open(UNIDADES_FILE_NAME, newline='', encoding="utf8") as dataFile:
        data = csv.reader(dataFile, delimiter=',')
        unidades : list[Unidade] = []
        for row in data:
           x = Unidade(row[0].upper(), row[1].title())
           unidades.append(x)
    return unidades