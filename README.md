# Sistema de Gestión Bancaria - README

## 📋 Descripción General

**Sistema de Gestión Bancaria** es una aplicación de consola desarrollada en Python que permite gestionar operaciones bancarias completas para clientes. El sistema ofrece funcionalidades para registro de clientes, administración de cuentas, solicitud de productos financieros, créditos, y seguimiento de transacciones.

## 👨‍💻 Autor

**Jhon Alejandro Escobar Lozada**

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.12.0
- **Sistema Operativo:** Windows
- **Tipo:** Aplicación de consola/terminal

## 📁 Estructura de Archivos

```
├── README.md               # Documentación del proyecto
├── main.py                # Código principal del sistema
├── data/
│   └── database.json      # Base de datos JSON persistente
├── modules/
│   ├── json_logic.py      # Manejo de operaciones JSON
│   ├── logicas.py         # Lógica de negocio y operaciones
│   └── menu.py            # Interfaces de menú y navegación
```

## 🗃️ Estructura de Datos

### Base de Datos JSON (`data/db.json`)
```json
{
  "numero_usuario": {
    "nombre": "string",
    "dni": "string",
    "email": "string",
    "contacto": {
      "movil": "string",
      "fijo": "string"
    },
    "ubicacion": {
      "pais": "string",
      "departamento": "string",
      "ciudad": "string",
      "direccion": "string"
    },
    "cuentas": {
      "numero_cuenta": "saldo"
    },
    "creditos": {
      "numero_credito": "monto"
    },
    "historial": {
      "id_transaccion": {
        "fecha": "DD/MM/YYYY HH:MM:SS",
        "accion": "string",
        "detalles": "string"
      }
    }
  }
}
```

### Rangos de Números de Cuenta
- **Cuentas de Ahorros**: 100-199
- **Cuentas Corrientes**: 200-299
- **CDTs**: 300-399
- **Créditos de Libre Inversión**: 1000-1999
- **Créditos de Vivienda**: 2000-2999
- **Créditos Vehiculares**: 3000-3999

## 🎯 Funcionalidades Principales

### 1. **Registro de Clientes**
- Registro completo con información personal
- Generación automática de número de usuario único
- Almacenamiento de datos de contacto y ubicación

### 2. **Gestión de Cuentas**
- **Cuentas de Ahorros** (100-199)
- **Cuentas Corrientes** (200-299)
- **CDTs (Certificados de Depósito a Término)** (300-399)
- Depósitos y retiros por cuenta
- Cancelación de cuentas

### 3. **Sistema de Créditos**
- **Crédito de Libre Inversión** (1000-1999)
- **Crédito de Vivienda** (2000-2999)
- **Crédito Vehicular** (3000-3999)
- Máximo 5 créditos por cliente
- Sistema de pagos y amortización

### 4. **Historial y Reportes**
- Registro completo de transacciones
- Historial detallado por usuario
- Reportes de movimientos
- Estadísticas de ingresos/gastos

### 5. **Operaciones Disponibles**
- ✅ Registro de nuevos clientes
- ✅ Solicitud de productos bancarios
- ✅ Depósitos a cuentas
- ✅ Solicitud de créditos
- ✅ Retiros de cuentas
- ✅ Pagos a créditos
- ✅ Cierre de cuentas/productos
- ✅ Visualización de historial completo

## 🎮 Cómo Usar el Sistema

### Instalación
1. Asegúrese de tener Python 3.12.0 instalado
2. Descargue todos los archivos del proyecto
3. Ejecute desde la terminal: `python main.py`

### Navegación del Menú Principal
```
1. Registro de cliente
2. Solicitud Productos
3. Deposito a cuentas
4. Solicitud de creditos
5. Retiros de cuentas
6. Pagos a creditos
7. Cerrar cuenta
8. Historial de usuario
9. Salir
```

### Ejemplo de Flujo de Uso
1. **Registro**: Ingrese sus datos personales para crear un usuario
2. **Solicitud de Productos**: Abra cuentas de ahorro/corriente o solicite CDT
3. **Operaciones**: Realice depósitos, retiros, solicite créditos
4. **Seguimiento**: Consulte su historial completo de transacciones

## 🔧 Características Técnicas

### Estructura de Datos
- **Diccionario principal (`db`)**: Almacena todos los usuarios y sus datos
- **Organización por número de usuario único**
- **Sistema de historial con timestamps**
- **Validación de rangos para tipos de cuentas/créditos**

### Validaciones Implementadas
- Verificación de rangos de números de cuenta
- Límite de 5 créditos por cliente
- Validación de saldos antes de retiros/pagos
- Control de errores en entrada de datos

### Seguridad
- Números de cuenta/crédito generados automáticamente
- Validación de existencia antes de operaciones
- Registro completo de auditoría

## 🚀 Requisitos del Sistema

- **Python:** 3.12.0 o superior
- **Sistema Operativo:** Windows (compatible con versiones recientes)
- **Espacio en Disco:** Mínimo 10MB
- **RAM:** 512MB mínimo

## 📝 Notas Importantes

- El sistema almacena datos en memoria (se pierden al cerrar el programa)
- Los números de cuenta y crédito se generan automáticamente
- Se recomienda respaldar información importante externamente
- El sistema es para propósitos educativos/demostrativos
