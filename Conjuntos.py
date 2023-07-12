usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

assistiram = usuarios_data_science | usuarios_machine_learning
assistiramOsDois = usuarios_data_science & usuarios_machine_learning
assistiramSomenteDataScience = usuarios_data_science - usuarios_machine_learning
assistiuSomenteUm = usuarios_data_science ^ usuarios_machine_learning

print(f'Alunos que fizeram qualquer curso: {assistiram}')
print(f'Alunos que fizeram os dois cursos: {assistiramOsDois}')
print(f'Alunos que fizeram somente Data Science: {assistiramSomenteDataScience}')
print(f'Alunos que fizeram somente um curso: {assistiuSomenteUm}')

usuarios = {1,5,76,34,52,13,17}     #CRIAÇÃO DE CONJUNTO
usuarios.add(765)   #ADICIONANDO UM NÚMERO A UM CONJUNTO

usuarios = frozenset(usuarios)  #CONGELANDO UM CONJUNTO IMPEDINDO SUA MUTABILIDADE

print('\n-----------------------------------------\n')

texto = 'Meu nome é Robert e eu sou um ser humano muito divertido que trabalha todo dia porque sou muito trabalhador'
print(set(texto.split()))   #COLOCANDO EM UM CONJUNTO CADA PALAVRA INDIVIDUAL QUE EXISTE NA STRING

#CRIANDO DICIONÁRIO
aparicoes = {
    'Robert': 1,
    'sou': 2,
    'muito': 2,
    'nome': 1
}

print(type(aparicoes))
print(aparicoes.get('Robert', 0))
aparicoes['Carlos'] = 1

print(aparicoes)
del aparicoes['Carlos'] #DELETAR ALGO NO DICIONÁRIO
print(aparicoes)

#MOSTRAR CHAVES (NOMES)
for elemento in aparicoes.keys():
    print(elemento)

#MOSTRAR VALORES (NÚMEROS)
for elemento in aparicoes.values():
    print(elemento)
    
#MOSTRAR AMBOS DE FORMA INTELIGENTE
for elemento in aparicoes:
    print(elemento, aparicoes[elemento])

#MOSTRAR A LINHA INTEIRA DE FORMA BRUTA
for elemento in aparicoes.items():
    print(elemento)

#MOSTRAR A LINHA INTEIRA DESEMPACOTANDO OS VALORES
for chave, valor in aparicoes.items():
    print(f'{chave} : {valor}')

#CONCATENANDO DIRETAMENTE NO FOR E MOSTRANDO OS VALORES
print([f'palavra {chave}' for chave in aparicoes.keys()])
