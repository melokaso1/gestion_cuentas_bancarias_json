#importes
import os 
import random
import time
import modules.json_logic as json

RUTA = 'data/db.json'

# cargar datos 
db = json.read_json(RUTA)


#Funcion desembolso de creditos
def desembolso_creditos(deposito):
    db = json.read_json(RUTA)
    os.system('cls')
    print("Cuentas disponibles para el desembolso:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= int(cuenta) <= 299:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
            
    a = input('\nIngrese el numero de cuenta: ')
    
    if int(a)  >= 100 and int(a) <= 299:
        if a in db[numero_user]['cuentas'].keys():
            monto = deposito
            if monto > 0:
                db[numero_user]['cuentas'][a] += monto
                json.write_json(RUTA, db)
                print(f'Desembolso exitoso de ${monto} a la cuenta {a}')
                print(f'Nuevo saldo en cuenta {a}: ${db[numero_user]["cuentas"][a]}')
                input("Presione enter para continuar...")
                return a
            else:
                print("El monto debe ser mayor a 0")
                input("Presione enter para continuar...")
        else:
            print(f'La cuenta de ahorros {a} no esta asociada a {numero_user}')
            input("Presione enter para continuar...")

#funcion para obtener fecha y hora actuaL
def obtener_fecha_hora():
    tiempo_actual = time.localtime()
    dia = tiempo_actual.tm_mday
    mes = tiempo_actual.tm_mon
    año = tiempo_actual.tm_year
    hora = tiempo_actual.tm_hour
    minuto = tiempo_actual.tm_min
    segundo = tiempo_actual.tm_sec
    return f"{dia:02d}/{mes:02d}/{año} {hora:02d}:{minuto:02d}:{segundo:02d}"

#funcion para agregar al historial
def agregar_historial(accion, cuenta, monto, origen):
    db = json.read_json(RUTA)
    fecha_hora = obtener_fecha_hora()
    if len(db[numero_user]['historial']) == 0:
        siguiente_num = 1
    else:
        claves_enteros = [int(k) for k in db[numero_user]['historial'].keys()]
        siguiente_num = max(claves_enteros) + 1
    
    db[numero_user]['historial'][siguiente_num] = {
        'fecha': fecha_hora,
        'accion': accion,
        'cuenta': cuenta,
        'monto': monto,
        'origen': origen
    }
    json.write_json(RUTA, db)
    
def registro_user():
    db = json.read_json(RUTA)
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
        acc_num = str(acc_num)

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
        
    json.rewrite_json(RUTA, db)
    
    os.system('cls')
    print(f'Usuario creado con exito, su numero de usuario es: {acc_num}')
    input('oprima enter para continuar...')

#filtro de usuarios
def filtro_user():    
    global numero_user
    os.system('cls')            
    numero_user = input('Ingrese el numero de usuario: ')
    
    while True:
        
        data = json.read_json(RUTA)
        
        if numero_user in data.keys():
            print('Usuario encontrado')
            break
        else:
            print('Usuario no existe, intente de nuevo')
            time.sleep(1)
            numero_user = input('Ingrese el numero de usuario: ')
    


#agregar cuentas
def add_acc_ahorro():
    db = json.read_json(RUTA)
    os.system('cls')
    while True:
        num_acc = random.randint(100, 199)
        num_acc = str(num_acc)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:   
            db[numero_user]['cuentas'][num_acc] = 0
            json.write_json(RUTA, db)
            print(f'Cuenta de ahorros creada con exito, el numero de cuenta es: {num_acc}')
            input('Precione enter para continuar...')
            break
    
def add_acc_corriente():
    db = json.read_json(RUTA)
    os.system('cls')
    
    while True:
        num_acc = random.randint(200, 299)
        num_acc = str(num_acc)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:
            db[numero_user]['cuentas'][num_acc] = 0
            json.write_json(RUTA, db)
            print(f'Cuenta corriente creada con exito, el numero de cuenta es: {num_acc}')
            input('Precione enter para continuar...')
            break
        
def add_CDT():
    db = json.read_json(RUTA)
    os.system('cls')
    inv = int(input('Ingrese el valor de la inversion: '))
    
    v_g = inv * 0.12
    v_t = inv + v_g
    
    while True:
        num_acc = random.randint(300, 399)
        num_acc = str(num_acc)
        if num_acc in db[numero_user]['cuentas'].keys():
            continue
        else:
            db[numero_user]['cuentas'][num_acc] = v_t
            json.write_json(RUTA, db)
            print(f'''Cuenta de CDT creado con exito, el numero de cuenta es: {num_acc}
Su saldo del CDT estimado a 1 año al 12% anual es: {v_t}''')
            input('Precione enter para continuar...')
            break

#depositos 
def deposito_ahorros():
    db = json.read_json(RUTA)
    os.system('cls')
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas de ahorro disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= int(cuenta) <= 199:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
            
    a = input('\nIngrese el numero de cuenta: ')
    
    if int(a) >= 100 and int(a) <= 199:
        if a in db[numero_user]['cuentas'].keys():
            monto = int(input('Ingrese el monto a depositar: $'))
            if monto > 0:
                db[numero_user]['cuentas'][a] += monto
                json.write_json(RUTA, db)
                agregar_historial("DEPOSITO AHORROS", a, monto, 'BANCO')
                os.system('cls')
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
    db = json.read_json(RUTA)
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas corrientes disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 200 <= int(cuenta) <= 299:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
    
    a = input('\nIngrese el numero de cuenta: ')
    
    if int(a) >= 200 and int(a) <= 299:
        if a in db[numero_user]['cuentas'].keys():
            monto = int(input('Ingrese el monto a depositar: $'))
            if monto > 0:
                db[numero_user]['cuentas'][a] += monto
                json.write_json(RUTA, db)
                agregar_historial("DEPOSITO CORRIENTE", a, monto, 'BANCO')
                os.system('cls')
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
    db = json.read_json(RUTA)
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas CDT disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 300 <= cuenta <= 399:
            print(f"Cuenta: {cuenta} - Saldo actual: ${saldo}")
    
    a = input('\nIngrese el numero de cuenta: ')
    
    if int(a) >= 300 and int(a) <= 399:
        if a in db[numero_user]['cuentas'].keys():
            inv = int(input('Ingrese el valor de la inversion: $'))
            if inv > 0:
                v_g = inv * 0.12
                v_t = inv + v_g
                
                db[numero_user]['cuentas'][a] += v_t
                json.write_json(RUTA, db)
                agregar_historial("DEPOSITO CDT", a, v_t, 'BANCO')
                os.system('cls')
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
    db = json.read_json(RUTA)
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(1000, 1999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
            else:
                db[numero_user]['creditos'][num_acc] = cant
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break

def credito_vivienda():
    db = json.read_json(RUTA)
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(2000, 2999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
            
            else:
                db[numero_user]['creditos'][num_acc] = cant
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
            
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break

def credito_vehicular():
    db = json.read_json(RUTA)
    os.system('cls')
    cant = int(input(f'Ingresa el valor del credito solicitado: '))
    
    while True:
        num_acc = random.randint(3000, 3999)
        
        if num_acc in db[numero_user]['creditos'].keys():
            continue
        elif len(db[numero_user]['creditos']) < 5:
            if len(db[numero_user]['creditos']) == 0:
                db[numero_user]['creditos'] = {num_acc : cant}
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
            else:
                db[numero_user]['creditos'][num_acc] = cant
                json.write_json(RUTA, db)
                print(f'El credito fue aprobado, numero de credito: {num_acc}')
                input('Precione enter para continuar...')
                time.sleep(1)
                a = desembolso_creditos(cant)
                agregar_historial("DESEMBOLSO CREDITO", a, cant, f'Credito: {num_acc}')
                break
        else:
            print('No se puede solicitar mas de 5 creditos')
            time.sleep(1)
            break
        
#retiros cuentas
def retiro_cuenta_ahorro():
    db = json.read_json(RUTA)
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas de ahorro disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= int(cuenta) <= 199:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_num = input('\nIngrese el numero de cuenta de ahorros: ')
    
    if int(acc_num) < 100 or int(acc_num) > 199:
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
    json.write_json(RUTA, db)
    agregar_historial("RETIRO AHORROS", numero_user, monto, acc_num)
    print(f'Retiro exitoso de ${monto}')
    print(f'Nuevo saldo en cuenta {acc_num}: ${db[numero_user]["cuentas"][acc_num]}')
    input("Presione enter para continuar...")
        
def retiro_cuenta_corriente():
    db = json.read_json(RUTA)
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print("No tiene cuentas registradas")
        input("Presione enter para continuar...")
        return
    
    print("Cuentas corrientes disponibles:")
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 200 <= cuenta <= 299:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_num = input('\nIngrese el numero de cuenta de ahorros: ')
    
    if int(acc_num) < 200 or int(acc_num) > 299:
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
    json.write_json(RUTA, db)
    agregar_historial("RETIRO AHORROS", numero_user, monto, acc_num)
    print(f'Retiro exitoso de ${monto}')
    print(f'Nuevo saldo en cuenta {acc_num}: ${db[numero_user]["cuentas"][acc_num]}')
    input("Presione enter para continuar...")

#pago credito
def pago_creditos(a, b):
    db = json.read_json(RUTA)
    os.system('cls')
    if len(db[numero_user]['creditos']) == 0:
        print("No tiene creditos registrados")
        input("Presione enter para continuar...")
        return
    
    print("Creditos a pagar:")
    for credito, saldo in db[numero_user]['creditos'].items():
        if a <= int(credito) <= b:
            print(f"Credito: {credito} - Saldo: ${saldo}")
    
    credito = input('\n Ingrese el numero de credito a pagar: ')
    
    os.system('cls')
    
    for cuenta, saldo in db[numero_user]['cuentas'].items():
        if 100 <= int(cuenta) <= 299:
            print(f"Cuenta: {cuenta} - Saldo: ${saldo}")
    
    acc_pago = input('Ingrese su numero de cuenta para pagar el credito (Cta ahorros / Cta corriente): ')
    
    if int(acc_pago) < 100 or int(acc_pago) > 299:
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
    json.write_json(RUTA, db)
    db[numero_user]['creditos'][credito] -= monto
    json.write_json(RUTA, db)
    agregar_historial("PAGO CREDITO", f"Credito: {credito}", monto, acc_pago)
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
    db = json.read_json(RUTA)
    os.system('cls')
    
    if len(db[numero_user]['cuentas']) == 0:
        print('No tiene cuentas asociadas')
        input("Presione enter para continuar...")
        return
    
    cont = 0
    
    print('Cuentas Disponibles:\n')
    for cuenta in db[numero_user]['cuentas'].keys():
        if a <= int(cuenta) <= b:
            cont += 1
            print(f'#{cont} | {acc}: {cuenta}')
    
    acc_canc = input(f'\nIngrese su numero de cuenta para cancelar ({acc}): ')
    
    if acc_canc not in db[numero_user]['cuentas'].keys():
        print(f'El número de cuenta {acc_canc} no es válido')
        input("Presione enter para continuar...")
        return
    
    if not a <= int(acc_canc) <= b:
        print(f'El número de cuenta {acc_canc} no es válido para {acc}')
        input("Presione enter para continuar...")
        return
    
    if db[numero_user]['cuentas'][acc_canc] == 0:
        del db[numero_user]['cuentas'][acc_canc] 
        json.write_json(RUTA, db)
        print(f'Cuenta {acc_canc} cancelada con exito')
        input('Presione enter para continuar...')
    
    else:
        print(f'La cuenta {acc_canc} no se puede cancelar ya que tiene un saldo de ${db[numero_user]["cuentas"][acc_canc]}')
        input('Presione enter para continuar...')

#historial de movimientos
def historial_movimientos():
    db = json.read_json(RUTA)
    os.system('cls')
    print('''
         HISTORIAL
===========================

  CUENTAS DE AHORROS
=======================''')
    for cuenta in db[numero_user]['cuentas'].keys():
        if 100 <= int(cuenta) <= 199: 
            print(f'Cuenta: {cuenta} | Saldo: ${db[numero_user]["cuentas"][cuenta]}')
            
    print('''

  CUENTAS CORRIENTES
======================''')
    for cuenta in db[numero_user]['cuentas'].keys():
        if 200 <= int(cuenta) <= 299: 
            print(f'Cuenta: {cuenta} | Saldo: ${db[numero_user]["cuentas"][cuenta]}')

    print('''

  CUENTAS CDT'S
======================''')
    for cuenta in db[numero_user]['cuentas'].keys():
        if 300 <= int(cuenta) <= 399: 
            print(f'Cuenta: {cuenta} | Saldo: ${db[numero_user]["cuentas"][cuenta]}')
    
    print(f'''

                                                                 HISTORIAL DE MOVIMIENTOS''')
    
    for history in db[numero_user]['historial'].keys():
        print(f'''      
============================================================================================================================================
|        Movimiento: {db[numero_user]['historial'][history]['accion']}      |       Origen: {db[numero_user]['historial'][history]['origen']}      |       Cantidad: {db[numero_user]['historial'][history]['monto']}        |       Destino: {db[numero_user]['historial'][history]['cuenta']}     |
============================================================================================================================================''')
    
    input('\nPresione enter para continuar...')

