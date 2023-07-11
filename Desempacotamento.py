idades = [15, 87, 32, 65, 56, 32, 49, 37]

#print(list(enumerate(idades)))

for i in range(len(idades)):
    pass
    #print(f'A idade do índice {i} é {idades[i]}')

for valor in enumerate(idades):
    pass
    #print(valor)
    
for indice, idade in enumerate(idades):
    pass
    #print(indice, 'x', idade)

# - - - - - DESEMPACOTANDO DADOS - - - - - #

usuarios = [
    ('Robert', 19, 2003),
    ('Karol', 20, 2002)
]

#LEVANDO TODOS OS DADOS PARA O FOR
for nome, idade, nascimento in usuarios:
    print(nome)

#IGNORANDO RESTO
for nome, _, _ in usuarios:
    print(nome)

#ORDENAR DE FORMA CRESCENTE
print(sorted(idades))

#ORDENAR DE FORMA DECRESCENTE
print(sorted(idades, reverse=True))

#ALTERAR A LISTA EM ORDEM CRESCENTE
idades.sort()

print(idades)