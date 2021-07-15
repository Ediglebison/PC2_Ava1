class Menu():
	
    def __init__(self):
        self._opcao = None #atributo

    def getOpcao(self): #pega/retornar o valor do atributo
        return self._opcao

    def setOpcao(self, opcao): # atribuir um valor ao atributo
        self._opcao = opcao

    def painel(self):
        banco = Conta()
        contaCorrente = ContaCorrente()
        contaPoupanca = ContaPoupanca()
        print("Selecione uma opção abaixo:")
        print("1 - Criar Conta")
        print("2 - Mostrar contas")
        print("3 - Efetuar um deposito")
        print("4 - Efetuar um Saque")
        print("5 - Cobrar tarifa")
        print("6 - Pagar rendimento")
        print("7 - Sair do programa")
        opcao = int((input (">")))
        while opcao != 7:
            if opcao == 1:
                banco.criarConta()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                banco.depositoConta()
            elif opcao == 4:
                banco.saqueConta()
            elif opcao == 5:
                contaCorrente.taxa()
            elif opcao == 6:
                contaPoupanca.rendimento()
            elif self.getOpcao() == 7:
                print("Tchau!! :)")
                break
            elif 1 < opcao > 7:
            	print("Opção invalida! Tente novamente")
            	opcao = int((input (">")))

class Pessoa():
    
    #O programa deve ter uma classe Pessoa com os atributos Nome, Endereço e CPF:

    def init(self, nome, endereco, cpf):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
    
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEndereco(self):
        return self._endereco

    def setEndereco(self, endereco):
        self._endereco = endereco

    def getCPF(self):
        return self._cpf

    def setCPF(self, cpf):
        self._cpf = cpf

class Conta(Pessoa):
	
    def init(self, nome, endereco, cpf, contaC, contaP, conta):
        super().init(nome, endereco, cpf)
        self._contaC = contaC
        self._contaP = contaP
        self._conta = 

    def getConta(self):
        return self._conta

    def setConta(self, conta):
        self._conta = conta

    def getContaC(self):
        return self._contaC

    def setContaC(self, contaC):
        self._contaC = contaC

    def getContaP(self):
        return self._contaP

    def setContaP(self, contaP):
        self._contaP = contaP

    def criarConta(self):
        nome = input("Digite o Nome: ")
        endereco = input("Digite o Endereço: ")
        cpf = input("Digite o CPF: ")
        contaC = float(input("Informe o Saldo inicial da conta Corrente: "))
        contaP = float(input("Informe o Saldo inicial da conta Poupança: "))
        saldo = contaC + contaP
        #contas = Conta(contaC, contaP, conta)
        #usuario = Pessoa(nome, endereco, cpf)
        #pessoa = usuario, contas
        conta = nome, endereco, cpf, contaC, contaP, saldo
        self.getConta().append(conta)

    def operacao(self):
        print ("Você deseja efetuar a operação em qual conta:")
        print ("1 - Conta corrente")
        print ("2 - Conta Poupança")
        while True:
            opcao = input(">")
            if opcao == "1":
                Conta.saldo = Conta.saldoC
            elif opcao == "2":
                Conta.saldo = Conta.saldoP
            else: 
                print ("erro")

    def confirmaOp(self, operacao):
        if operacao.opcao == "1":
            Conta.saldoC = Conta.saldo
        elif operacao.opcao == "2":
            Conta.saldoP = Conta.saldo

    def depositoConta(self):
        listar()
        i_conta = int(input("ID do contato: "))
        Conta.operacao()[i_conta]
        deposito = float(input("Informe o valor a ser depositado na conta: "))
        while deposito < 0:
            print ("Valor incorreto!!")
            deposito = float(input("Informe o valor a ser depositado na conta: "))
        Conta.saldo[i_conta] += deposito
        Conta.confirmaOp()[i_conta]

    def saqueConta(self):
        listar()
        i_conta = int(input("ID do contato: "))
        Conta.operacao()[i_conta]
        saque = float(input("Informe o valor a ser retirado na conta: "))
        while saque < 0:
            print ("Valor incorreto!!")
            saque = float(input("Informe o valor a ser retirado da conta: "))
        Conta.saldo[i_conta] += saque
        Conta.confirmaOp()[i_conta]

    '''
    O programa deve ter uma classe Conta com os atributos Pessoa (objeto da classe
    Pessoa) e Saldo, e os métodos para fazer o depósito e retirada da conta (ambos
    fazem mudança no saldo da conta):
    '''
    
class ContaCorrente():
    def __init__(self):
        self._contaC = []

    def getContaC(self):
        return self._contaC

    def setContaC(self, contaC):
        self._contaC = contaC

    def taxa(self):
        listar()
        i_conta = int(input("ID do contato: "))
        tarifa = 10
        ContaCorrente.contaC[i_conta] -= tarifa

    """
    O programa deve ter uma classe ContaCorrente que é uma Conta (herança) e deve
    possuir o método para pagar a taxa da conta corrente (diminuir o saldo):
    """
    
class ContaPoupanca():

    def __init__(self):
        self._contaP = []

    def getContaP(self):
        return self._contaP

    def setContaP(self, contaP):
        self._contaP = contaP

    def rendimento(self):
        listar()
        i_conta = int(input("ID do contato: "))
        rende = 1.03
        ContaPoupanca.contaP[i_conta] *= rende

def listar(self):
    
    for i, pessoa in enumerate(self.getConta()):
        print("Contato ", i)
        print("Nome: "+pessoa.getNome())
        print("Endereco: "+pessoa.getEndereco())
        print("CPF: "+pessoa.getCPF())
        print("Saldo - C: "+pessoa.saldoC)
        print("Saldo - P: "+pessoa.saldoP)
        print("Saldo Total: "+pessoa.conta)
        

    '''
    O programa deve ter uma classe ContaPoupanca que é uma Conta (herança) e deve
    possuir o método para adicionar o rendimento da poupança (aumentar o saldo):
    '''
menuPainel = Menu()
menuPainel.painel()

""" 
1 – Criar um objeto do tipo pessoa e mostrar os detalhes desse objeto:
2 – Criar um objeto do tipo conta corrente e um objeto do tipo conta poupança e
ligar esses objetos uma pessoa:
3 – Fazer depósitos e saques na conta corrente, mostrar o saldo, assim como poder
pagar a taxa da conta corrente:
4 – Fazer depósitos e saques na conta poupança, mostrar o saldo, assim como
poder adicionar o rendimento da conta poupança:
Você pode adicionar todas as informações diretamente no código (ou solicitar que
o usuário as digite) para demonstrar todas as funcionalidades:
 """
