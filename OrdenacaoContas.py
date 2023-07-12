from operator import attrgetter
from functools import total_ordering    #ADICIONANDO FUNCIONALIDADE DE VERIFICAR SE É MENOR OU IGUAL

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return '[>>Codigo {} Saldo {}<<]'.format(self._codigo, self._saldo)
    
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo # ADICIONANDO SEGUNDA FORMA DE COMPARAÇÃO ENTRE CONTAS

    #COMPARAÇÃO PARA VER SE OS DOIS OBJETOS SÃO IGUAIS
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo
    
conta_raz = ContaSalario(1700)
conta_raz.deposita(500)

conta_karol = ContaSalario(3)
conta_karol.deposita(1000)

conta_outro = ContaSalario(133)
conta_outro.deposita(500)

contas = [conta_raz, conta_karol, conta_outro]

for conta in contas:
    print(conta)

print(conta_karol <= conta_raz)

# USANDO MÉTODO attrgetter PARA TER MAIS UMA FORMA DE COMPARAÇÃO
#for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
#    print(conta)

print('------------------------------------')
for conta in sorted(contas):
    print(conta)