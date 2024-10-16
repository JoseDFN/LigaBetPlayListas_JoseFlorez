def validateData(message:str):
    opciones = ('N','n','S','s')
    accion = (input(f'{message}'))
    # Si el usuario presiona enter sin ingresar nada
    if accion == '':
        return False
    
    # Si la acción ingresada no está en las opciones permitidas
    elif accion not in opciones:
        print('La opción que ingresó no está permitida...')
        return validateData(message)  # Volver a pedir la entrada
    
    # Si la acción ingresada es válida
    else:
        return True