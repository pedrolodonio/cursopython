"""Crie uma classe ContaBancaria com os atributos titular e saldo.
Implemente os métodos:

depositar(valor) → adiciona dinheiro ao saldo.
sacar(valor) → retira dinheiro do saldo, se houver saldo suficiente.
exibir_saldo() → imprime o saldo atual.
📌 Dicas:

O saldo inicial deve ser zero.
Teste criando uma conta, depositando e sacando valores.
"""

class ContaBancária:
    def __init__(self,titular):
        self.titular = titular
        self.__saldo = 0
    
    def deposito(self,valor):
        self.__saldo += valor
        print(f"Depósito realizado com sucesso!! o novo saldo é R$ {self.__saldo}")
    
    def saque(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"saque realizado com sucesso !! Novo Saldo é de R$ {self.__saldo}")
        else:
            print("saldo insuficiente")
    
    """def exibirSaldo(self):
        print(f"Saldo atual de {self.titular}: R${self.__saldo:.2f}")"""
    
    def get_saldo(self):
        return self.__saldo
    
conta = ContaBancária("Pedro")
conta.deposito(50000)
conta.saque(26000)
print(f"Saldo disponível: R$ {conta.get_saldo():.2f}")