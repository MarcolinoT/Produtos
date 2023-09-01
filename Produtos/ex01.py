import json

estoque = {}  # Dicionário
opcao = 1

while opcao != 3:
    print('=' * 10)
    print('=== MENU ===')
    print('1 - Adicionar')
    print('2 - Consultar')
    print('3 - Sair')
    opcao = int(input('>>>>'))

    if opcao == 1:
        codigo = input('Codigo: ')
        nome = input('Nome do produto: ')
        estoque[codigo] = nome
        print('Adicionado com sucesso!')
    elif opcao == 2:
        # Vou informar o código e ele me retornará o nome
        codigo = input('Codigo desejado: ')
        # Verificar se a chave está no estoque
        if codigo in estoque:
            registro = estoque[codigo]
            print(f'REGISTRO RECUPERADO: {registro}')
        else:
            print('Produto não encontrado')
    elif opcao == 3:
        print('Saindo...')