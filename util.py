#encoding: utf-8
import csv
import json

class Usuario:
    def __init__(self, nome : str, email : str, sigla: str, cpf : str):
        self.nome = nome
        self.email = email
        self.sigla = sigla
        self.cpf = cpf



def carregarDados(arquivo : str):
    with open(arquivo, newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        resultado : list[Usuario] = []
        for row in spamreader:
            x = Usuario(row[0], row[1], row[2], row[3])
            resultado.append(x)
    return resultado     
                
