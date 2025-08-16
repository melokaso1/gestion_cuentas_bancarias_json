#importes
import os, time
import modules.logicas as lg
import modules.menu as mn

#inicio de programa
if __name__ == '__main__':
    while True:
        try:
            match int(mn.menu()):
                case 1:
                    lg.registro_user()
                case 2:
                    lg.filtro_user()
                    while True:    
                        match int(mn.menu_solicitud_productos()):
                            case 1:
                                lg.add_acc_ahorro()
                            case 2:
                                lg.add_acc_corriente()
                            case 3:
                                lg.add_CDT()
                            case 4:
                                break
                case 3:
                    lg.filtro_user()
                    while True: 
                        match int(mn.menu_depositos()):
                            case 1:
                                lg.deposito_ahorros()
                            case 2: 
                                lg.deposito_corriente()
                            case 3:
                                lg.deposito_CDT()
                            case 4:
                                break
                            
                case 4:
                    lg.filtro_user()
                    while True:
                        match int(mn.menu_creditos()):
                            case 1:
                                lg.credito_libre_inv()
                            case 2: 
                                lg.credito_vivienda()
                            case 3:
                                lg.credito_vehicular()
                            case 4:
                                break
                case 5:
                    lg.filtro_user()
                    while True:
                        match int(mn.menu_retiros()):
                            case 1:
                                lg.retiro_cuenta_ahorro()
                            case 2: 
                                lg.retiro_cuenta_corriente()
                            case 3:
                                break
                case 6:
                    lg.filtro_user()
                    while True:
                        match int(mn.menu_pago_creditos()):
                            case 1:
                                lg.pago_creditos(1000, 1999)
                            case 2: 
                                lg.pago_creditos(2000, 2999)
                            case 3:
                                lg.pago_creditos(3000, 3999)
                            case 4:
                                break
                case 7:
                    lg.filtro_user()
                    while True:
                        match int(mn.menu_cancelar()):
                            case 1:
                                lg.cancelar_cuenta(100, 199, 'CTA AHORROS')
                            case 2: 
                                lg.cancelar_cuenta(200, 299, 'CTA CORRIENTE')
                            case 3:
                                lg.cancelar_cuenta(300, 399, 'CDT')
                            case 4:
                                break
                case 8:
                    lg.filtro_user()
                    lg.historial_movimientos()
                
                case 9:
                    os.system('cls')
                    break
        except (ValueError, KeyboardInterrupt):
            print("Por favor ingrese un número válido.")
            time.sleep(1)
            continue
