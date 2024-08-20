#!/bin/python3

# Substitua o projeto inicial de RPG por este código quando novas instruções estiverem ativas

def showInstructions():
    # imprime um menu principal e os comandos
    print('''
Jogo RPG
========
Comandos:
  vai [direçāo]
  apanha [item]
''')

def showStatus():
    # imprime o estado corrente do jogador
    print('---------------------------')
    print('Estás na ' + currentRoom)
    # imprime o inventário currente
    print('Inventário : ' + str(inventory))
    # imprime um item se houver um
    if 'item' in rooms[currentRoom]:
        print('Estás a ver uma ' + rooms[currentRoom]['item'])
    print('---------------------------')

# um inventário, que inicialmente está vazio
inventory = []

# um dicionário a ligar uma divisão a outras divisões
rooms = {

    'Entrada' : { 
        'sul' : 'Cozinha'
    },

    'Cozinha' : {
        'norte' : 'Entrada'
    }

}

# começa com o jogador na Entrada
currentRoom = 'Entrada'

showInstructions()

# ciclo perpétuo
while True:

    showStatus()

    # recebe a próxima 'move'
    # .split() divide-a numa matriz de listas
    # por exemplo digitar 'vai este' resulta na lista:
    # ['vai', 'este']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # se digitarem 'vai' primeiro
    if move[0] == 'vai':
        # verifica que o jogador pode ir na direção que está a pedir
        if move[1] in rooms[currentRoom]:
            # altera a divisão actual para a nova divisāo
            currentRoom = rooms[currentRoom][move[1]]
        # nāo há porta (ligaçāo) para a nova divisão
        else:
            print('Nāo podes ir nessa direçāo!')

    # se digitarem 'apanha' primeiro
    if move[0] == 'apanha':
        # se a divisāo tiver um item, e o jogador quiser apanhar esse item
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # adicionar o item ao inventário
            inventory += [move[1]]
            # mostra uma mensagem informativa
            print('Apanhaste uma ' + move[1] + '!')
            # apaga o item da divisão
            del rooms[currentRoom]['item']
        # senāo, se não houver item para apanhar
        else:
            # diz ao jogador que não pode apanhar o item
            print('Nāo podes apanhar uma ' + move[1] + '!')
