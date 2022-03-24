from abc import ABC


dados = dict()
pessoas = list()

class Todos:

    def mostrar_pessoas(self):
        print(pessoas)


class Pessoa:
    
    def __init__(self, nome=None, idade=None):
        dados['Nome'] = nome
        dados['Idade'] = idade
        pessoas.append(dados.copy())


    def mostrar_dados(self):
        print(dados)


class Funcionario(Pessoa):

    def mostrar_dados(self):
        super().mostrar_dados()
    

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return f'{nome_classe} trabalhando...'


class Visitante(Pessoa):

    def mostrar_dados(self):
        super().mostrar_dados()

    def expecionar(self):
        nome_classe = self.__class__.__name__
        return f'{nome_classe} expecionando...'


todos = Todos()

maria = Funcionario('Maria', 31)
joao = Visitante('João', 20)

print(maria.trabalhar())
print(joao.expecionar())

todos.mostrar_pessoas()