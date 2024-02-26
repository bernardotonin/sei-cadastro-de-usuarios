from config import FILE_NAME
import csv

class User:
    def __init__(self, name : str, email : str, login: str, cpf : str):
        self.name = name
        self.email = email
        self.login = login
        self.cpf = cpf

def loadData() -> list[User]:
    with open(FILE_NAME, newline='', encoding="utf8") as dataFile:
        data = csv.reader(dataFile, delimiter=',')
        userList : list[User] = []
        for row in data:
            x = User(row[0].title(), row[1], row[2], row[3])
            userList.append(x)
    return userList