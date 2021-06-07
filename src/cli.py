from os import PRIO_PGRP
from .dll.List import List
import traceback

MESSAGE = """
    _      ___   ___   _  _   ___      _   
   /_\    / __| | __| | \| | |   \    /_\  
  / _ \  | (_ | | _|  | .` | | |) |  / _ \ 
 /_/ \_\  \___| |___| |_|\_| |___/  /_/ \_\

1. Ingresar nuevo contacto
2. Buscar contacto
3. Visualizar agenda
4. Salir
    """

agenda = List()

def new_contact(number = None):
    try:
        phone_number = number
        name = input("Ingrese nombre: ")
        lastname = input("Ingrese apellido: ")
        if phone_number == None:            
            phone_number = int(input("Ingrese número de teléfono: "))
        else:
            print("Número de teléfono: ", phone_number)
        if agenda.search(phone_number) == None:            
            agenda.add(name, lastname, phone_number)
            print("El contacto se ha agregado exitosamente")
        else:
            print("El contacto ya existe")
    except ValueError:
        print("Error al ingresar los datos")
        print(ValueError)
        



def search_contact():
    try:
        phone_number = int(input("Ingrese el número por buscar: "))
        contact = agenda.search(phone_number)
        if contact != None:
            print("Nombre: ", contact.name)
            print("Apellido: ", contact.lastname)
            print("Número de teléfono: ", contact.phone_number)
        else:
            option = input("   El número de teléfono no existe ¿Desea agregarlo? (y/n)")
            if option.lower() == 'y':
                new_contact(phone_number)
    except:
        print("Error al ingresar los datos")


def view_agenda():
    agenda.show()

def main_menu():
    option = ""
    while option != '4':
        print(MESSAGE)        
        option = input("Ingrese la opción de desea => ")
        if option == '1':
            new_contact()
        elif option == '2':
            search_contact()
        elif option == '3':
            view_agenda()
        elif option == '4':
            print("Bye")
        else:
            print("La opción no es correcta")
        input()