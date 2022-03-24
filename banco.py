class ContaBanco:

    # Atributos de Classe
    taxa = 0.50 # Taxa a ser cobrada por operação

    @staticmethod
    def retornarCodigoBanco():
        return 'Código: 777'

    # Atributos de Instâncias
    def __init__(self, numero=None, titular='<unknown>', saldo=0):
        self._numero = numero   # Visibilidade protegida
        self.titular = titular  # Visibilidade pública
        self.__saldo = saldo    # Visibilidade privada
        self.__historico = [saldo]


    def saldo(self):
        print(f'Saldo: R${self.__saldo}')


    def transacao(self, saldo):
        self.__historico.append(saldo)


    def extrato(self):
        # Custo de R$0.50 para realizar extrato!
        print('----Extrato----')
        print(f'Conta: {self.titular}')
        for saldo in self.__historico:
            print(f'Saldo: R${saldo}')


    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)


    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)



conta1 = ContaBanco(123, 'Mona Lisa', 2300)
conta2 = ContaBanco(456, 'Albert')

conta1.transferir(300, conta2)
conta1.extrato()
