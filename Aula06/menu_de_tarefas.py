from adicionar_tarefas import adicionar, listar, remover

def menu():
    print('Escolha uma das opções abaixo:')
    print('1 - Adicionar Tarefa')
    print('2 - Listar Tarefas')
    print('3 - Remover Tarefa')
    print('4 - Sair')

    index = 0
    tarefas = "lista"
    index_tarefas =(tarefas)

    escolha = input('Escolha sua opção: ')

    if escolha == '1':
        adicionar()
        print('Tarefa adicionada')

    elif escolha == '2':
        listar()
        print(f'Você tem uma nova  :{adicionar(tarefas)}')

    elif escolha == '3':
        print('Tarefa removida')
        remover()

    elif escolha == '4':
        print('Obrigado por usar a lista de tarefas')

    else:
        print('Escolha uma das opções válidas: ')

    if escolha != '4':
        return menu()
       
   
print('Seja bem vindo a lista de tarefas')
menu()