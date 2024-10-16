import os
import modulos.mensajes as m_messg
import modulos.regEquipo as regE
import modulos.cuerpoTec as cTec
import modulos.nDorsal as nDor
import modulos.pJugador as pJug
import modulos.nJugador as nJug
import modulos.fPartido as fPar
isAllow = True

if(__name__ == '__main__'):
    Liga = []
    LigaProgAct = True
    opcMenu = 0
    while (LigaProgAct):
        os.system('clear')
        print(m_messg.MenuPrinPartes)
        try:
            opcMenu = int(input(':)_'))        
            match opcMenu:
                case 1:
                    MenuRegEquIs = True
                    while MenuRegEquIs:
                        os.system ('clear')
                        print(m_messg.MenuRegEqu)
                        opcMenu = int(input(':)_'))
                        match opcMenu:
                            case 1:
                                regE.addEquipo(Liga)
                            case 2:
                                cTec.addCtec(Liga)
                            case 3:
                                menuPlantel = True
                                while menuPlantel:
                                    os.system ('clear')
                                    print(m_messg.MenInInfoCJug)
                                    opcMenu = int(input(':)_'))
                                    match opcMenu:
                                        case 1:
                                            nDor.nDorsal(Liga)
                                        case 2:
                                            pJug.pJugador(Liga)
                                        case 3:
                                            nJug.nJugador(Liga)
                                        case 4:
                                            menuPlantel = False
                            case 4:
                                MenuRegEquIs = False
                case 2:
                    MenuReRrogPar = True
                    while MenuReRrogPar:
                        os.system ('clear')
                        print(m_messg.MenProgPart)
                        opcMenu = int(input(':)_'))
                        match opcMenu:
                            case 1:
                                fPar.progPart(Liga)
                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    LigaProgAct = False
        except:
            print ("La opcion ingresada no concuerda con las opciones dadas")
            x = input("De enter para continuar: ")