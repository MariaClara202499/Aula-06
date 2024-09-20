# cria o dicionário
alunos = {'Maria':99,'Clovis':88,'Ana':77,'Dio':66}
# alterar um valor
alunos['Clovis'] = 55 # modificação
print(alunos)
alunos.pop('Clovis') # remoção
print(alunos)
alunos['Kiko'] = 44 # adição de valor
for nome, mat in alunos.items(): # iterando no dicionário
    print(f'matricula {mat} Nome {nome}')
alunosCopia = alunos.copy()
alunosCopia['Ana'] = 33
print('Alunos ',alunos)
print('Alunos Copia ',alunosCopia)