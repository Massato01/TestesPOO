# HERANÇA MÚLTIPLA

class Funcionario:

    def trabalhar(self):
        print('Trabalhando...')


class FrontEnd(Funcionario):

    def front_end(self):
        super().trabalhar()


class BackEnd(Funcionario):
    
    def back_end(self):
        super().trabalhar()


class FullStack(FrontEnd, BackEnd):
    pass


ana = FullStack()
raul = FrontEnd()
masato = BackEnd()

ana.trabalhar()
ana.back_end()
ana.front_end()

raul.trabalhar()
masato.trabalhar()
