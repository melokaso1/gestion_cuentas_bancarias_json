import os

#Menus
def menu():
    os.system("cls")
    a = input('''
  SISTEMA DE GESTION BANCARIA
===============================

#1 Registro de cliente
#2 Solicitud Productos
#3 Deposito a cuentas
#4 Solicitud de creditos
#5 Retiros de cuentas
#6 Pagos a creditos
#7 Cerrar cuenta
#8 Historial de usuario
#9 Salir

Seleccione una opcion: ''')
    
    return a

def menu_solicitud_productos():
    os.system("cls")
    a = input('''
  SOLICITUD DE PRODUCTOS
==========================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 CDT
#4 salir

Seleccione una opcion: ''')
    return a

def menu_depositos():
    os.system('cls')
    a = input('''
  DEPOSITOS A CUENTAS
=======================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 CDT
#4 salir

Seleccione una opcion: ''')
    return a

def menu_creditos():
    os.system('cls')
    a = input('''
  SOLICITUD DE CREDITOS
=========================

#1 Credito de libre inversion
#2 Credito de vivienda
#3 Credito vehicular
#4 Salir

Seleccione una opcion: ''')
    return a

def menu_retiros():
    os.system('cls')
    a = input('''
  RETIROS
===========

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 salir

Seleccione una opcion: ''')
    return a

def menu_pago_creditos():
    os.system('cls')
    a = input('''
  PAGO DE CREDITOS
=====================

#1 Credito de libre inversion
#2 Credito de vivienda
#3 Credito vehicular
#4 Salir

Seleccione una opcion: ''')
    return a

def menu_cancelar():
    os.system('cls')
    a = input('''
  CANCELAR CUENTA O PRODUCTOS
===============================

#1 Cuenta de ahorros
#2 Cuenta corriente
#3 CDT
#4 salir

Seleccione una opcion: ''')
    return a

def menu_estadisticas():
    os.system('cls')
    a = input('''
  ESTADISTICAS
================
#1 Ingresos
#2 Gastos
#3 historial de movimientos
#4 salir

Seleccione una opcion: ''')
    return a