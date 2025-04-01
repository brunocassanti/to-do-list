def adicionando_tarefa(tarefas, nome_tarefa):
    tarefa = {'tarefa': nome_tarefa, 'completada': False}
    tarefas.append(tarefa)
    print(f'Tarefa "{nome_tarefa}" adicionada!')
    return

def ver_tarefas(tarefas):
    print('\nLista de tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        status = '✔' if tarefa['completada'] else 'Pendente'
        nome_tarefa = tarefa['tarefa']
        print(f'{i}. [{status}] {nome_tarefa}')

def atualiza_tarefa(tarefas, indice_tarefa, novo_nome):
    indice_atualizado = int(indice_tarefa) - 1
    if 0 <= indice_atualizado < len(tarefas):
        tarefas[indice_atualizado]['tarefa'] = novo_nome
        print(f'Tarefa {indice_tarefa} atualizada para "{novo_nome}".')
    else:
        print('Índice de tarefa inválido!')

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if 0 <= indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['completada'] = True
        print(f'Tarefa {indice_tarefa} marcada como completada!')
    else:
        print('Índice de tarefa inválido!')

def delete_tarefas(tarefas):
    for tarefa in tarefas:
        if tarefa['completada']:
            tarefas.remove(tarefa)
    print('Tarefas completadas foram deletadas')
    return

tarefas = []

while True:
    print('\nMenu de Lista de Tarefas:')
    print('1. Adicionar tarefa')
    print('2. Ver tarefas')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar tarefa completada')
    print('6. Sair')

    opcao = input('\nO que deseja fazer? ')

    if opcao == "1":
        nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ')
        adicionando_tarefa(tarefas, nome_tarefa)

    elif opcao == '2': 
        ver_tarefas(tarefas)

    elif opcao == '3':
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite a tarefa que deseja alterar: ')
        novo_nome = input('Digite o nome da nova tarefa: ')
        atualiza_tarefa(tarefas, indice_tarefa, novo_nome)

    elif opcao == '4':
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite a tarefa que deseja marcar como completa: ')
        completar_tarefa(tarefas, indice_tarefa)

    elif opcao == '5':
        delete_tarefas(tarefas)
        ver_tarefas(tarefas)

        
    elif opcao == '6':
        break

print('Programa finalizado!')
