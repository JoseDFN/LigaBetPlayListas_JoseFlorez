def nDorsal(src:list):
    nombre = input('Ingrese el nombre del equipo: ')
    for equipo in src:
        if equipo[0] == nombre:
            while True:
                nDorsal = input('Ingrese el numero del dorsal (deje vacío para terminar): ')
                if nDorsal == '':
                    break
                plantel = [nDorsal,[],[]]
                equipo[2].append(plantel)
            break
    else:
        print("Equipo no encontrado.")