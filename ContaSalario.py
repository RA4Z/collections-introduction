class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)
    
    def __eq__(self, outro):
        #isinstance(ContaSalario(34), ContaSalario)
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
class ContaMultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta3 = ContaSalario(23)
conta4 = ContaSalario(37)
contas = [conta1, conta2, conta3, conta4]

print(conta1 == conta2)
print(contas.count(conta1))
