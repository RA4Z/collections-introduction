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