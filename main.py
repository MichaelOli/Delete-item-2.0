import time
#lista
cidades = ['Brasilia', 'Taguatinga', 'Gama', 'Ceilandia', 'Sobradinho', 'Taguatinga',]
print('Vou te apresentar algumas cidades e logo em seguida voce poderá deletar um item')
print(f'{'='*10}{cidades}{'='*10}')

#usuario informa o nome que deseja deletar
cidade_deletada = input('Nome da cidade a ser deletada: ')
time.sleep(2)
print('\n')

#deleta a cidade informada
try:
    cidades.remove(cidade_deletada)
except:
    print('Não foi possível remover a cidade.')

#exibe a lista na tela
for cidade in cidades:
    print(cidade)