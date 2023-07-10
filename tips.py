# CRIAR UMA LISTA
idades = [15, 32, 60, 30]

# ADICIONAR INFORMAÇÃO NOVA AO FINAL DA LISTA
idades.append(19)

# PERCORRER A LISTA
for idade in idades:
    print(idade)

# ADICIONAR INFORMAÇÃO EM UM ÍNDICE ESPECÍFICO DA LISTA
idades.insert(0,17)

# REMOVER DADO ESPECÍFICO DA LISTA
idades.remove(32)
print(idades)

# LIMPAR DADOS DE TODA A LISTA
idades.clear()
print(idades)

# ADICIONAR INFORMAÇÕES EM MASSA NA LISTA
idades = [50, 13, 23]
idades.extend([29,11])
print(idades)

# CRIANDO UMA NOVA LISTA CUJA IDADE SEJA UM ANO A MAIS QUE O ATUAL
idades_ano_que_vem = [(idade + 1) for idade in idades]
print(idades_ano_que_vem)

# INSERINDO EM UMA NOVA LISTA TODOS QUE FOREM MAIOR DE IDADE
maior_idade = [(idade) for idade in idades if idade > 18]
print(maior_idade)