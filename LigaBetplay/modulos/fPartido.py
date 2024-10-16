# Importamos módulos personalizados para utilidades y mensajes
import modulos.utilcustoms as uc
import modulos.mensajes0_2 as msg

def progPart(src: list):
# Variable que controla el bucle para agregar un nuevo equipo
    isAddPart = True
    i=int(0)
    while isAddPart:
        i+=1
        # Solicita al usuario el nombre del nuevo equipo
        Fecha = input('Ingrese la fecha del partido: ')
        
        # Crea una nueva entrada de equipo con el nombre y listas vacías para otros datos
        fePartido = [i, Fecha, [], [], [[],[],[],[],[],[]]]
        
        # Agrega el nuevo equipo a la lista de equipos
        src.append(fePartido)
        
        # Verifica la validez de los datos usando una función del módulo utilcustoms
        isAddPart = bool(uc.validateData(msg.messagefPartido))