from abc import ABC, abstractclassmethod

# Classe Abstrata
class Pessoa(ABC):

    # (Superclasse) - classe mãe, classe pai
    
    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg

    def imprimir_nome(self):
        return self.nome

    @abstractclassmethod
    def trabalhar(self):
        pass

# Classe concreta
class Administrador(Pessoa):

    # (Subclasse) - classe filha, classe filha
    
    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Organizando Planilhas...')


class Professor(Pessoa):

    # (Subclasse) - classe filha, classe filha

    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []

    def trabalhar(self):
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Ensinando...')


class Aluno():

    # (Subclasse) - classe filha, classe filha

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []
    
    def estudar(self):
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Estudando...')


# professor1 = Professor('Marcos')
# admin = Administrador()
# aluno1 = Aluno('Joao')

# professor1.trabalhar()
# admin.trabalhar()
# aluno1.estudar()

# professor1 = Professor('Joseph')
# admin = Administrador()
# professor1.trabalhar()
# admin.trabalhar()