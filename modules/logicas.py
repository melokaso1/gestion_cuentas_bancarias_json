#importes
import os 
import random
import time

db = { 
    7086 : {'cuentas' : {}, 'creditos' : {}, 'historial' : {} }
}

#funcion para obtener fecha y hora actual
def obtener_fecha_hora():
    tiempo_actual = time.localtime()
    dia = tiempo_actual.tm_mday
    mes = tiempo_actual.tm_mon
    anio = tiempo_actual.tm_year
    hora = tiempo_actual.tm_hour
    minuto = tiempo_actual.tm_min
    segundo = tiempo_actual.tm_sec
    return f"{dia:02d}/{mes:02d}/{anio} {hora:02d}:{minuto:02d}:{segundo:02d}"

#funcion para agregar al historial
def agregar_historial(accion, detalles):
    fecha_hora = obtener_fecha_hora()
    # Obtener el siguiente número de historial
    if len(db[numero_user]['historial']) == 0:
        siguiente_num = 1
    else:
        siguiente_num = max(db[numero_user]['historial'].keys()) + 1
    
    db[numero_user]['historial'][siguiente_num] = {
        'fecha': fecha_hora,
        'accion': accion,
        'detalles': detalles
    }

def registro_user():
    os.system('cls')
    acc = True
    nombre = input('Ingrese el nombre completo: ').upper().strip()
    dni = input('Ingrese el numero de documento: ').upper().strip()
    email = input('Ingrese el correo electronico: ').upper().strip()
    movil = input('Ingrese el numero de telefono: ').strip()
    fijo = input('Ingrese el numero de telefono fijo: ').strip()
    pais = input('Ingrese el pais de residencia: ').upper().strip()
    dep = input('Ingrese el departamento de residencia: ').upper().strip()
    ciudad = input('Ingrese la ciudad o municipio de residencia: ').upper().strip()
    dirc = input('Ingrese la direccion de residencia: ').upper().strip()
    
    while acc:
        acc_num = random.randint(0, 10000)

        if acc_num  in db.keys():
            acc = True
        else:
            acc = False
    
    db[acc_num] = {  # type: ignore
        'nombre': nombre,
        'dni': dni,
        'email': email,
        'contacto': {
            'movil': movil,
            'fijo': fijo
        },
        'ubicacion' : {
            'pais': pais,
            'departamento': dep,
            'ciudad': ciudad,
            'direccion': dirc
            },
        'cuentas' : {
        },
        'creditos' : {
        },
        
        'historial' : {
            
        }
        }
    print(f'Usuario creado con exito, su numero de usuario es: {acc_num}')
    input('oprima enter para continuar')

#filtro de usuarios
def filtro_user():    
    global numero_user
    os.system('cls')            
    numero_user = int(input('Ingrese el numero de usuario: '))
    
    while True:
        if numero_user in db.keys():
            print('Usuario encontrado')
            break
        else:
            print('Usuario no existe, intente de nuevo')
            time.sleep(1)
            numero_user = int(input('Ingrese el numero de usuario: '))


#agregar cuentas
def add_acc_ahorro():
    os.system('cls')
    while True:
        num_acc = random.randint(100, 199)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:   
            if len(db[numero_user]['cuentas'].keys()) == 0:
                db[numero_user]['cuentas'] = {num_acc : 0}
                print(f'Cuenta de ahorros creada con exito, el numero de cuenta es: {num_acc}')
                input('Precione enter para continuar...')
                break
            else:
                db[numero_user]['cuentas'][num_acc] = 0
                print(f'Cuenta de ahorros creada con exito, el numero de cuenta es: {num_acc}')
                input('Precione enter para continuar...')
                break
    
def add_acc_corriente():
    os.system('cls')
    
    while True:
        num_acc = random.randint(200, 299)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else: 
            if len(db[numero_user]['cuentas'].keys()) == 0:
                db[numero_user]['cuentas'] = {num_acc : 0}
                print(f'Cuenta corriente creada con exito, el numero de cuenta es: {num_acc}')
                input('Precione enter para continuar...')
                break
            else:
                db[numero_user]['cuentas'][num_acc] = 0
                print(f'Cuenta corriente creada con exito, el numero de cuenta es: {num_acc}')
                input('Precione enter para continuar...')
                break
        
def add_CDT():
    os.system('cls')
    inv = int(input('Ingrese el valor de la inversion: '))
    
    
    v_g = inv * 0.12
    v_t = inv + v_g
    
    while True:
        num_acc = random.randint(300, 399)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:
            if len(db[numero_user]['cuentas'].keys()) == 0:
                db[numero_user]['cuentas'] = {num_acc : v_t}
                print(f'''Cuenta de CDT creado con exito, el numero de cuenta es: {num_acc}
Su saldo del CDT estimado a 1 año al 12% anual es: {v_t}''')
                input('Precione enter para continuar...')
                break
            else:
                db[numero_user]['cuentas'][num_acc] = v_t
                print(f'''Cuenta de CDT creado con exito, el numero de cuenta es: {num_acc}
Su saldo del CDT estimado a 1 año al 12% anual es: {v_t}''')
                input('Precione enter para continuar...')
                break

#depositos 
def deposito_ahorros():
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas de ahorro disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= cuenta <= 199:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
    
    a = int(input('\nIngrese el numero de cuenta: '))
    
    if a >= 100 and a <= 199:
        if a in db[numero_user]['cuentas'].keys():
            monto = int(input('Ingrese el monto a depositar: $'))
            if monto > 0:
                db[numero_user]['cuentas'][a] += monto
                agregar_historial("DEPOSITO AHORROS", f"Depósito de ${monto} en cuenta {a}")
                print(f'Deposito exitoso de ${monto}')
                print(f'Nuevo saldo en cuenta {a}: ${db[numero_user]["cuentas"][a]}')
                input("Presione enter para continuar...")
            else:
                print("El monto debe ser mayor a 0")
                input("Presione enter para continuar...")
        else:
            print(f'La cuenta de ahorros {a} no esta asociada a {numero_user}')
            input("Presione enter para continuar...")
    else:
        print(f'La cuenta de ahorros {a} no existe (debe ser entre 100-199)')
        input("Presione enter para continuar...")

def deposito_corriente():
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas corrientes disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 200 <= cuenta <= 299:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
    
    a = int(input('\nIngrese el numero de cuenta: '))
    
    if a >= 200 and a <= 299:
        if a in db[numero_user]['cuentas'].keys():
            monto = int(input('Ingrese el monto a depositar: $'))
            if monto > 0:
                db[numero_user]['cuentas'][a] += monto
                agregar_historial("DEPOSITO CORRIENTE", f"Depósito de ${monto} en cuenta {a}")
                print(f'Deposito exitoso de ${monto}')
                print(f'Nuevo saldo en cuenta {a}: ${db[numero_user]["cuentas"][a]}')
                input("Presione enter para continuar...")
            else:
                print("El monto debe ser mayor a 0")
                input("Presione enter para continuar...")
        else:
            print(f'La cuenta corriente {a} no esta asociada a {numero_user}')
            input("Presione enter para continuar...")
    else:
        print(f'La cuenta corriente {a} no existe (debe ser entre 200-299)')
        input("Presione enter para continuar...")

def deposito_CDT():
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas CDT disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 300 <= cuenta <= 399:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
    
    a = int(input('\nIngrese el numero de cuenta: '))
    
    if a >= 300 and a <= 399:
        if a in db[numero_user]['cuentas'].keys():
            inv = int(input('Ingrese el valor de la inversion: $'))
            if inv > 0:
                v_g = inv * 0.12
                v_t = inv + v_g
                
                db[numero_user]['cuentas'][a] += v_t
                agregar_historial("DEPOSITO CDT", f"Depósito de ${v_t} en cuenta {a}")
                
                print(f'''Deposito exitoso 
Su saldo del CDT estimado a 1 año al 12% anual es: {db[numero_user]['cuentas'][a]}''')
                input("Presione enter para continuar...")
            else:
                print("El monto debe ser mayor a 0")
                input("Presione enter para continuar...")
        else:
            print(f'La cuenta CDT {a} no esta asociada a {numero_user}')
            input("Presione enter para continuar...")
    else:
        print(f'La cuenta CDT {a} no existe (debe ser entre 300-399)')
        input("Presione enter para continuar...")

#logica creditos
def credito_libre_inv():
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(1000, 1999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                agregar_historial("APROBACION CREDITO", f"Crédito de libre inversión aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
            else:
                db[numero_user]['creditos'][num_acc] = cant
                agregar_historial("APROBACION CREDITO", f"Crédito de libre inversión aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break

def credito_vivienda():
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(2000, 2999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                agregar_historial("APROBACION CREDITO", f"Crédito de vivienda aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
            else:
                db[numero_user]['creditos'][num_acc] = cant
                agregar_historial("APROBACION CREDITO", f"Crédito de vivienda aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break
def credito_vehicular():
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(3000, 3999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                agregar_historial("APROBACION CREDITO", f"Crédito vehicular aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
            else:
                db[numero_user]['creditos'][num_acc] = cant
                agregar_historial("APROBACION CREDITO", f"Crédito vehicular aprobado por ${cant} , número {num_acc}")
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                break
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break
        
#retiros cuentas
def retiro_cuenta_ahorro():
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas de ahorro disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= cuenta <= 199:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_num = int(input('\nIngrese el numero de cuenta de ahorros: '))
    
    if acc_num < 100 or acc_num > 199:
        print("Numero de cuenta invalido. Las cuentas de ahorro son del 100 al 199")
        input("Presione enter para continuar...")
        
    
        
    if acc_num not in db[numero_user]['cuentas'].keys():
        print(f'La cuenta de ahorros {acc_num} no existe')
        input("Presione enter para continuar...")
        return
        
    monto = int(input('Ingrese el monto a retirar: $'))
        
    if monto > db[numero_user]['cuentas'][acc_num]:
        print(f'Saldo insuficiente. Saldo actual: ${db[numero_user]["cuentas"][acc_num]}')
        input("Presione enter para continuar...")
        return
        
    db[numero_user]['cuentas'][acc_num] -= monto
    agregar_historial("RETIRO AHORROS", f"Retiro de ${monto} desde cuenta {acc_num}")
    print(f'Retiro exitoso de ${monto}')
    print(f'Nuevo saldo en cuenta {acc_num}: ${db[numero_user]["cuentas"][acc_num]}')
    input("Presione enter para continuar...")
        
def retiro_cuenta_corriente():
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas corrientes disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 200 <= cuenta <= 299:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_num = int(input('\nIngrese el numero de cuenta de ahorros: '))
    
    if acc_num < 200 or acc_num > 299:
        print("Numero de cuenta invalido. Las cuentas corrientes son del 200 al 299")
        input("Presione enter para continuar...")
        return
    
        
    if acc_num not in db[numero_user]['cuentas'].keys():
        print(f'La cuenta corriente {acc_num} no existe')
        input("Presione enter para continuar...")
        return
        
    monto = int(input('Ingrese el monto a retirar: $'))
        
    if monto > db[numero_user]['cuentas'][acc_num]:
        print(f'Saldo insuficiente. Saldo actual: ${db[numero_user]["cuentas"][acc_num]}')
        input("Presione enter para continuar...")
        return
        
    db[numero_user]['cuentas'][acc_num] -= monto
    agregar_historial("RETIRO CORRIENTE", f"Retiro de ${monto} desde cuenta corriente {acc_num}")
    print(f'Retiro exitoso de ${monto}')
    print(f'Nuevo saldo en cuenta {acc_num}: ${db[numero_user]["cuentas"][acc_num]}')
    input("Presione enter para continuar...")

#pago credito
def pago_creditos(a, b):
    os.system('cls')
    if len(db[numero_user]['creditos']) == 0:
        print("No tiene creditos registrados")
        input("Presione enter para continuar...")
        return
    
    print("Creditos a pagar:")
    for credito, saldo in db[numero_user]['creditos'].items():
        if a <= credito <= b:
            print(f"Credito: {credito} - Saldo: ${saldo}")
    
    credito = int(input('\n Ingrese el numero de credito a pagar: '))
    
    os.system('cls')
    
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= cuenta <= 299:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_pago = int(input('Ingrese su numero de cuenta para pagar el credito (Cta ahorros / Cta corriente): '))
    
    if acc_pago < 100 or acc_pago > 299:
        print("Numero de cuenta invalido. Las cuentas de ahorro son del 100 al 199 / Numero de cuenta de corriente son del 200 al 299")
        input("Presione enter para continuar...")
        return
    
        
    if acc_pago not in db[numero_user]['cuentas'].keys():
        print(f'La cuenta de ahorros {acc_pago} no existe')
        input("Presione enter para continuar...")
        return
    
    monto = int(input('Ingrese el monto a pagar: $'))
    
    if monto > db[numero_user]['cuentas'][acc_pago]:
        print(f'Saldo insuficiente. Saldo actual de la cuenta: ${db[numero_user]["cuentas"][acc_pago]}')
        input("Presione enter para continuar...")
        return
    elif monto > db[numero_user]['creditos'][credito]:
        print(f' El credito a pagar es menor que el monto ingresado')
        input("Presione enter para continuar...")
        return
    
    db[numero_user]['cuentas'][acc_pago] -= monto
    db[numero_user]['creditos'][credito] -= monto
    agregar_historial("PAGO CREDITO", f"Pago de ${monto} al crédito {credito}")
    print(f'Pago realizado por valor de ${monto}')
    print(f'Saldo en cuenta {acc_pago}: ${db[numero_user]["cuentas"][acc_pago]}')
    
    if db[numero_user]['creditos'][credito] == 0:
        print(f'Credito {credito} cancelado en su totalidad')
        del db[numero_user]['creditos'][credito]
        input('Presione enter para continuar...')
    else:
        print(f'Saldo de credito {credito}: ${db[numero_user]["creditos"][credito]}')
        input('Presione enter para continuar...')

#cancelar una cuenta
def cancelar_cuenta(a, b, acc):
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print('No tiene cuentas asociadas')
        input("Presione enter para continuar...")
        return
    
    acc_canc = int(input(f'Ingrese su numero de cuenta para cancelar ({acc}): '))
    
    if acc_canc not in db[numero_user]['cuentas'].keys():
        print(f'El número de cuenta {acc_canc} no es válido')
        input("Presione enter para continuar...")
        return
    
    if not (a <= acc_canc <= b):
        print(f'El número de cuenta {acc_canc} no es válido para {acc}')
        input("Presione enter para continuar...")
        return
    
    if db[numero_user]['cuentas'][acc_canc] == 0:
        del db[numero_user]['cuentas'][acc_canc] 
        print(f'Cuenta {acc_canc} cancelada con exito')
        input('Presione enter para continuar...')
    
    else:
        print(f'La cuenta {acc_canc} no se puede cancelar ya que tiene un saldo de ${db[numero_user]["cuentas"][acc_canc]}')
        input('Presione enter para continuar...')

#historial de movimientos
def historial_movimientos():
    print(f'''
  HISTORIAL DE MOVIMIENTOS - USUARIO: {numero_user}
==================================================''')
    
    print('\n--- CUENTAS ---')
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
    else:
        print("Cuentas de ahorro:")
        for cuenta, saldo in db[numero_user]['cuentas'].items():
            if 100 <= cuenta <= 199:
                print(f"  Cuenta #{cuenta} - Saldo: ${saldo}")
        
        print("\nCuentas corrientes:")
        for cuenta, saldo in db[numero_user]['cuentas'].items():
            if 200 <= cuenta <= 299:
                print(f"  Cuenta #{cuenta} - Saldo: ${saldo}")
        
        print("\nCDTs:")
        for cuenta, saldo in db[numero_user]['cuentas'].items():
            if 300 <= cuenta <= 399:
                print(f"  CDT #{cuenta} - Valor: ${saldo}")
    
    print('\n--- CRÉDITOS ---')
    if len(db[numero_user]['creditos']) == 0:
        print("No tiene créditos registrados")
    else:
        print("Créditos de libre inversión:")
        for credito, saldo in db[numero_user]['creditos'].items():
            if 1000 <= credito <= 1999:
                print(f"  Crédito #{credito} - Saldo: ${saldo}")
        
        print("\nCréditos de vivienda:")
        for credito, saldo in db[numero_user]['creditos'].items():
            if 2000 <= credito <= 2999:
                print(f"  Crédito #{credito} - Saldo: ${saldo}")
        
        print("\nCréditos vehiculares:")
        for credito, saldo in db[numero_user]['creditos'].items():
            if 3000 <= credito <= 3999:
                print(f"  Crédito #{credito} - Saldo: ${saldo}")
    
    print('\n--- HISTORIAL DE TRANSACCIONES ---')
    if len(db[numero_user]['historial']) == 0:
        print("No hay transacciones registradas")
    else:
        print(f"{'Fecha/Hora':<20} {'Acción':<25} {'Monto':<10} {'Origen':<15} {'Destino':<15}")
        print("=" * 85)
        
        for num_trans, transaccion in db[numero_user]['historial'].items():
            fecha = transaccion['fecha']
            accion = transaccion['accion']
            detalles = transaccion['detalles']
            
            # Extraer información del detalle
            monto = "$0"
            origen = "N/A"
            destino = "N/A"
            
            if "$" in detalles:
                # Buscar monto después del $
                partes = detalles.split("$")
                if len(partes) > 1:
                    monto_parte = partes[1].split()[0]
                    monto = f"${monto_parte}"
            
            if "cuenta" in detalles.lower():
                if "en cuenta" in detalles.lower():
                    # Para depósitos
                    partes = detalles.split("cuenta")
                    if len(partes) > 1:
                        destino = f"Cuenta {partes[1].strip()}"
                        origen = "Depósito"
                elif "de cuenta" in detalles.lower():
                    # Para retiros
                    partes = detalles.split("de cuenta")
                    if len(partes) > 1:
                        origen = f"Cuenta {partes[1].strip()}"
                        destino = "Retiro"
            elif "crédito" in detalles.lower() or "credito" in detalles.lower():
                if "pago" in detalles.lower():
                    origen = "Pago desde cuenta"
                    destino = "Crédito"
                else:
                    origen = "Aprobación"
                    destino = "Crédito"
            
            print(f"{fecha:<20} {accion:<25} {monto:<10} {origen:<15} {destino:<15}")
    
    print(f"\nTotal en cuentas: ${sum(db[numero_user]['cuentas'].values())}")
    print(f"Total en créditos: ${sum(db[numero_user]['creditos'].values())}")
    input("\nPresione enter para continuar...")