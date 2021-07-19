class Pessoa():

    def __init__(self, nome, endereco, cpf):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
    
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco
        
    def getCPF(self):
        return self.cpf
        
    def setCPF(self, cpf):
        self.cpf = cpf

class ContaCorrente():
    def __init__(self, contaC):
        self.contaC = contaC
    
    def getContaC(self):
        return self.contaC

    def setContaC(self, contaC):
        self.contaC = contaC

    def taxa(self):
        return self.contaC - 10

class ContaPoupanca():
    def __init__(self, contaP):
        self.contaP = contaP
    
    def getContaP(self):
        return self.contaP

    def setContaP(self, contaP):
        self.contaP = contaP

    def rendimento(self):
        return self.contaP * 1.03

class Conta(Pessoa, ContaCorrente, ContaPoupanca):

    def __init__(self, nome, endereco, cpf, contaC, contaP):
        Pessoa.__init__(self, nome, endereco, cpf)
        ContaCorrente.__init__(self, contaC)
        ContaPoupanca.__init__(self, contaP)


    def criarConta(self):
        self.setNome("Ediglebison")
        self.setEndereco("Rua bla bla bla")
        self.setCPF(12345678910)
        self.setContaC(21390)
        self.setContaP(30000)
        print("Conta criada!")

    def operacao(self):
        menu = Menu()
        while menu.getOpcao() != "3":
            print ("Você deseja efetuar a operação em qual conta:")
            print ("1 - Conta corrente")
            print ("2 - Conta Poupança")
            print ("3 - Sair")
            menu.setOpcao(input(">"))
            if menu.getOpcao() == "1":
                saldo = 21390
            elif menu.getOpcao() == "2":
                saldo = 30000
            elif menu.getOpcao() == "3":
                print("Saindo...")
            else: 
                print ("erro")

    def confirmaOp(self):
        menu = Menu()
        if menu.getOpcao == "1":
            Conta.saldoC = Conta.operacao().saldo
        elif menu.getOpcao == "2":
            Conta.saldoP = Conta.operacao().saldo

    def depositoConta(self):
        deposito = float(input("Informe o valor a ser depositado na conta: "))
        while deposito < 0:
            print ("Valor incorreto!!")
            deposito = float(input("Informe o valor a ser depositado na conta: "))
        conta = Conta("Ediglebison", "Rua bla bla bla", "12345678910", 21390, 30000) 
        menu = Menu()
        conta.operacao()
        if menu.getOpcao() != "3":
            conta.operacao().saldo += deposito
            print(conta.operacao().saldo)
        Conta.confirmaOp()
        
    def saqueConta(self):
        saque = float(input("Informe o valor a ser retirado na conta: "))
        while saque < 0:
            print ("Valor incorreto!!")
            saque = float(input("Informe o valor a ser retirado da conta: "))
        conta = Conta("Ediglebison", "Rua bla bla bla", "12345678910", 21390, 30000) 
        menu = Menu()
        conta.operacao()
        if menu.getOpcao() != "3":
            conta.operacao().saldo += saque
            print(conta.operacao().saldo)
        conta.operacao().saldo += saque
        Conta.confirmaOp()

    def listar(criarConta):
        acc = Conta("Ediglebison", "Rua bla bla bla", "12345678910", 21390, 30000)
        print("Nome: "+ acc.getNome())
        print("Endereço: "+ acc.getEndereco())
        print("CPF: "+ acc.getCPF())
        print("Saldo C. Corrente: "+ str(acc.getContaC()))
        print("Saldo C. Poupança: "+ str(acc.getContaP()))

class Menu():
	
    def __init__(self):
        self._opcao = None

    def getOpcao(self): 
        return self._opcao

    def setOpcao(self, opcao): 
        self._opcao = opcao

    def painel(self):
        banco = Conta("Ediglebison", "Rua bla bla bla", "12345678910", 21390, 30000)
        contaCorrente = ContaCorrente(21070)
        contaPoupanca = ContaPoupanca(300)
        while self.getOpcao() != 7:
            print("Selecione uma opção abaixo:")
            print("1 - Criar Conta")
            print("2 - Mostrar contas")
            print("3 - Efetuar um deposito")
            print("4 - Efetuar um Saque")
            print("5 - Cobrar tarifa")
            print("6 - Pagar rendimento")
            print("7 - Sair do programa")
            self.setOpcao(int((input (">"))))
            if self.getOpcao() == 1:
                banco.criarConta()
            elif self.getOpcao() == 2:
                banco.listar()
            elif self.getOpcao() == 3:
                banco.depositoConta()
            elif self.getOpcao() == 4:
                banco.saqueConta()
            elif self.getOpcao() == 5:
                contaCorrente.taxa()
                print("Taxa paga!")
            elif self.getOpcao() == 6:
                contaPoupanca.rendimento()
                print("Rendimento pago!")
            elif self.getOpcao() == 7:
                print("Tchau!! :)")
            else:
            	print("Opção invalida! Tente novamente")

menuPainel = Menu()
menuPainel.painel()