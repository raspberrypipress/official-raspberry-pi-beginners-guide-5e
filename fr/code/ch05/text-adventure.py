#!/bin/python3

# Une aventure textuelle simple que tu peux améliorer avec ton propre code

def showInstructions():
    # affiche un menu principal et les commandes
    print("""
Text Adventure
==============
Commandes:
  aller [direction]
  prendre [objet]
""")

def showStatus():
    # affiche l'état actuel du joueur
    print("---------------------------")
    print("Tu es dans le/la " + currentRoom)
    # affiche l'inventaire actuel
    print("Inventaire : " + str(inventory))
    # affiche un objet s'il y en a un
    if "objet" in rooms[currentRoom]:
        print("Tu vois un/une " + rooms[currentRoom]['objet'])
    print("---------------------------")

# un inventaire, qui est initialement vide
inventory = []

# un dictionnaire liant une pièce à d'autres pièces
rooms = {

    'Hall' : { 
        'sud' : 'Cuisine'
    },

    'Cuisine' : {
        'nord' : 'Hall'
    }

}

# démarre le joueur dans le Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:

    showStatus()

    # obtenir la prochaine action du joueur
    # .split() le divise en un tableau de liste
    # ex en tapant 'aller est' donnerait la liste:
    # ['aller','est']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    # si il tape 'aller' en premier
    if move[0] == 'go':
        # vérifie qu'ils sont autorisés peu importe où ils souhaitent aller
        if move[1] in rooms[currentRoom]:
            # définis la pièce actuelle à une autre pièce
            currentRoom = rooms[currentRoom][move[1]]
        # il n'y a pas de porte (lier) à une autre pièce
        else:
            print("Tu ne peux pas aller par là !")

    # s'ils tapent 'prendre' en premier
    if move[0] == 'get':
        # si la pièce contient un objet, et l'objet est celui qu'ils souhaitent obtenir
        if 'objet' in rooms[currentRoom] and move[1] in rooms[currentRoom]['objet']:
            # ajoute l'objet à leur inventaire
            inventory += [move[1]]
            # affiche un message utile
            print(move[1] + " got!")
            # supprime l'objet de la pièce
            del rooms[currentRoom]['objet']
        # sinon, si l'objet n'est pas là
        else:
            # leur indiquer qu'ils ne peuvent pas l'avoir
            print("Vous ne pouvez pas l avoir " + move[1] + " !")
