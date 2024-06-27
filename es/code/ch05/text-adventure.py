#!/bin/python3

# Reemplaza el proyecto inicial RPG con este codigo cuando aparezcan nuevas intrucciones

def showInstructions():
    # imprime un menu principal y los comandos
    print("""
Juego RPG
========
Comandos:
  ir [dirección]
  coger [objeto]
""")

def showStatus():
    # imprime el estado actual del jugador
    print("---------------------------")
    print("Estas en el / la " + currentRoom)
    # imprime el inventario actual
    print("Inventario: " + str(inventory))
    # imprime un objeto si hay uno
    if "objeto" in rooms[currentRoom]:
        print('Puedes ver un/una ' + rooms[currentRoom]['objeto'])
    print("---------------------------")

# un inventario, que esta vacio al principio
inventory = []

# un diccionario que une una habitacion a las posiciones de las otras habitaciones
rooms = {

    'Sala' : { 
        'sur' : 'Cocina'
    },

    'Cocina' : {
        'norte' : 'Sala'
    }

}

# comienza con el jugador en la Sala
currentRoom = 'Sala'

showInstructions()

# repetir indefinidamente
while True:

    showStatus()

    # obtiene el siguiente movimiento del jugador
    # .split() lo separa en una lista
    # por ejemplo escribir 'ir este' va a dar la lista:
    # ['ir','este']
    move = ''
    while move == '':  
        move = input('>')
    
    move = move.lower().split()

    # si escriben 'ir' primero
    if move[0] == 'ir':
        # verifica que esta permitido ir a donde quieren ir
        if move[1] in rooms[currentRoom]:
            # haz que la habitacion en la que esta el jugador sea la nueva habitacion
            currentRoom = rooms[currentRoom][move[1]]
        # si no hay una puerta (conectando) hacia donde quieren ir
        else:
            print('¡No puedes ir en esa direccion!')

    # si escriben 'coger' primero
    if move[0] == 'coger' :
        # si la habitacion contiene un objeto y ese objeto es el que el jugador quiere coger
        if 'objeto' in rooms[currentRoom] and move[1] in rooms[currentRoom]['objeto']:
            # añade el objeto al inventario
            inventory += [move[1]]
            # muestra un mensaje de ayuda
            print('¡Ahora tienes un/una ' + move[1] + '!')
            # borra el objeto de la habitacion
            del rooms[currentRoom]['objeto']
        # si el objeto que se quiere no esta en la habitacion
        else:
            # diles que no pueden cogerlo
            print('¡No puedes coger el/la ' + move[1] + '!')
