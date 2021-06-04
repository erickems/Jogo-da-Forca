from typing import Type

class Usuario:
    
    def __init__(self):
        self.login = ''
        self.senha = ''

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def __iter__(self):
        yield 'login', self.login
        yield 'senha', self.senha