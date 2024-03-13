#!/bin/python3

# Una semplice avventura testuale che può essere migliorata con il proprio codice.

def showInstructions():
    # stampa un menu principale e i comandi
    print('''
Text Adventure
==============
Commandi:
  vai [direzione]
  prendi [oggetto]
''')

def showStatus():
    # stampa la posizione corrente del giocatore
    print('---------------------------')
    print('Sei in ' + currentRoom)
    # stampa il contenuto dell'inventario
    print('inventario : ' + str(inventory))
    # stampa un oggetto se presente nell'inventario
    if 'oggetto' in rooms[currentRoom]:
        print('Vedi quest\'oggetto: ' + rooms[currentRoom]['oggetto'])
    print('---------------------------')

# un inventario inizialmente vuoto
inventory = []

# un dizionario collega una stanza alle altre
rooms = {

    'Ingresso': {
        'sud': 'Cucina'
    },

    'Cucina': {
        'nord': 'Ingresso'
    }

}

# all'inizio il giocatore si trova nell'ingresso
currentRoom = 'Ingresso'

showInstructions()

# ciclo infinito
while True:

    showStatus()

    # prende la prossima 'istruzione' del giocatore
    # e .split() la divide in una lista
    # per esempio digitando 'vai est' si ottiene la seguente lista:
    # ['vai','est']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # se la prima parola digitata è 'vai'
    if move[0] == 'vai':
        # verifica se la direzione inserita è consentita
        if move[1] in rooms[currentRoom]:
            # imposta la stanza corrente alla nuova inserita
            currentRoom = rooms[currentRoom][move[1]]
        # altrimenti, se non c'è nessuna porta (collegamento) in quella direzione
        else:
            print('Non puoi andare da quella parte!')

    # se la prima parola digitata è 'prendi'
    if move[0] == 'prendi':
        # se la stanza contiene un oggetto ed è quello che si vuole raccogliere
        if 'oggetto' in rooms[currentRoom] and move[1] in rooms[currentRoom]['oggetto']:
            # aggiungi l'oggetto all'inventario
            inventory += [move[1]]
            # visualizza un messaggio di conferma
            print('Ho raccolto: ' + move[1])
            # cancella l'oggetto dalla stanza
            del rooms[currentRoom]['oggetto']
        # altrimenti se non c'è nessun oggetto da prendere
        else:
            # informa che non si può prendere
            print('Impossibile prendere ' + move[1] + '!')
