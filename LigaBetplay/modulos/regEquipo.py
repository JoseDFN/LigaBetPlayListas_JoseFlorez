# Importamos módulos personalizados para utilidades y mensajes
import modulos.utilcustoms as uc
import modulos.mensajes0_2 as msg

def addEquipo(src: list):
    # Variable que controla el bucle para agregar un nuevo equipo
    isAddEquipo = True
    while isAddEquipo:
        # Solicita al usuario el nombre del nuevo equipo
        nombre = input('Ingrese el nombre del equipo: ')
        
        # Verifica si el nombre ya está registrado en la lista de equipos
        if any(equipo[0] == nombre for equipo in src):
            print('El equipo ya está registrado. Intente con otro nombre.')
            continue  # Si el nombre ya existe, vuelve al inicio del bucle
        
        # Crea una nueva entrada de equipo con el nombre y listas vacías para otros datos
        equipo = [nombre, [], [], []]
        
        # Agrega el nuevo equipo a la lista de equipos
        src.append(equipo)
        
        # Verifica la validez de los datos usando una función del módulo utilcustoms
        isAddEquipo = bool(uc.validateData(msg.messagest))
