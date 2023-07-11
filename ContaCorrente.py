from Conta import Conta

# LISTAS SÃO MUTÁVEIS
class ContaCorrente(Conta):
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} Slado {}<<]'.format(self.codigo, self.saldo)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

conta_raz = ContaCorrente(15)
conta_raz.deposita(900)
conta_karol = ContaCorrente(47685)
conta_karol.deposita(1000)

contas = [conta_raz, conta_karol]
deposita_para_todas(contas)

for conta in contas:
    print(conta)
    
#TUPLAS SÃO IMUTÁVEIS
raz = ('Robert', 19, 2003)
karol = ('Karoline', 20, 2002)
print('------------------------\n')

usuarios = [raz, karol]
usuarios.append(('Paulo', 39, 1979))
print(usuarios)