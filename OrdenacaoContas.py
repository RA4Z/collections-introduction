class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)
    
    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
conta_raz = ContaSalario(17)
conta_raz.deposita(500)

conta_karol = ContaSalario(3)
conta_karol.deposita(1000)

contas = [conta_raz, conta_karol]

for conta in contas:
    print(conta)

print(conta_karol > conta_raz)

for conta in sorted(contas, reverse=True):
    print(conta)