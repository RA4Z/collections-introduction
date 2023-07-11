class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>Codigo {} Slado {}<<]'.format(self.codigo, self.saldo)
    
conta_raz = ContaCorrente(15)
conta_raz.deposita(500)

conta_karol = ContaCorrente(47685)
conta_karol.deposita(1000)

contas = [conta_raz, conta_karol]
for conta in contas:
    print(conta)
    