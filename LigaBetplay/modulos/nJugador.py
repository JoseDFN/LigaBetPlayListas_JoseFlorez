def nJugador(src: list):
    nombre = input('Ingrese el nombre del equipo: ')
    for equipo in src:
        if equipo[0] == nombre:
            nDorsal = input('Ingrese el número de dorsal del jugador: ')
            # Buscar el jugador en el plantel
            for plantel in equipo[2]:  # Aquí accedes al plantel (índice 2)
                if plantel[0] == nDorsal:  # Verifica si el dorsal coincide
                    posJugador = input('Ingrese el nombre del jugador a agregar: ')
                    plantel[2] = posJugador  # Guardar la posición en el índice 1
                    print(f"Posición {posJugador} asignada al jugador con dorsal {nDorsal}")
                    break
            else:
                print(f"No se encontró un jugador con el dorsal {nDorsal} en el equipo {nombre}.")
            break
    else:
        print(f"Equipo {nombre} no encontrado.")
