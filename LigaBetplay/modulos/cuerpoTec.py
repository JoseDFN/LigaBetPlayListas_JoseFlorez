def addCtec(src:list):
    nombre = input('Ingrese el nombre del equipo a ingresar el cuerpo tecnico: ')
    for equipo in src:
        if equipo[0] == nombre:
            i = 1
            while True:
                cuerpoTec = input(f'Ingrese el nombre del cuerpo técnico {i}(deje vacío para terminar): ')
                if cuerpoTec == '':
                    break
                cuerpoTecRol = input(f'Ingrese el rol del cuerpo técnico {i}: ')
                equipo[1].append([cuerpoTec, cuerpoTecRol])
                i += 1
            break
    else:
        print("Equipo no encontrado.")