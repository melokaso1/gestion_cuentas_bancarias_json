# Sistema de Gestión Bancaria - README

## 📋 Descripción General

**Sistema de Gestión Bancaria** es una aplicación de consola desarrollada en Python que permite gestionar operaciones bancarias completas para clientes. El sistema ofrece funcionalidades para registro de clientes, administración de cuentas, solicitud de productos financieros, créditos, y seguimiento de transacciones con almacenamiento persistente en formato JSON.

## 👨‍💻 Autor

**Jhon Alejandro Escobar Lozada**

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.12.0
- **Sistema Operativo:** Windows
- **Tipo:** Aplicación de consola/terminal
- **Almacenamiento:** Archivos JSON locales
- **Librerías estándar:** json, os, random, time, typing

## 📁 Estructura de Archivos

```
├── README.md               # Documentación del proyecto
├── main.py                # Código principal del sistema (menú principal)
├── data/
│   └── db.json            # Base de datos JSON persistente
├── modules/
│   ├── json_logic.py      # Manejo de operaciones JSON (CRUD)
│   ├── logicas.py         # Lógica de negocio y operaciones bancarias
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

### Rangos de Números de Cuenta y Créditos
- **Cuentas de Ahorros**: 100-199
- **Cuentas Corrientes**: 200-299
- **CDTs (Certificados de Depósito a Término)**: 300-399
- **Créditos de Libre Inversión**: 1000-1999
- **Créditos de Vivienda**: 2000-2999
- **Créditos Vehiculares**: 3000-3999

## 🎯 Funcionalidades Principales

### 1. **Registro de Clientes**
- Registro completo con información personal y de contacto
- Generación automática de número de usuario único (0-10000)
- Almacenamiento de datos de ubicación geográfica
- Validación de duplicados

### 2. **Gestión de Cuentas**
- **Cuentas de Ahorros** (100-199): Sin restricciones especiales
- **Cuentas Corrientes** (200-299): Sin restricciones especiales
- **CDTs** (300-399): Inversión con rendimiento del 12% anual
- Depósitos y retiros por cuenta
- Cancelación de cuentas (solo si saldo es 0)

### 3. **Sistema de Créditos**
- **Crédito de Libre Inversión** (1000-1999)
- **Crédito de Vivienda** (2000-2999)
- **Crédito Vehicular** (3000-3999)
- Límite máximo de 5 créditos por cliente
- Sistema de pagos parciales o totales
- Cancelación automática cuando el saldo llega a 0

### 4. **Operaciones Disponibles**
- ✅ Registro de nuevos clientes
- ✅ Solicitud de productos bancarios (cuentas y CDT)
- ✅ Depósitos a cuentas (ahorros, corriente, CDT)
- ✅ Solicitud de créditos (3 tipos)
- ✅ Retiros de cuentas (ahorros y corriente)
- ✅ Pagos a créditos (parciales o totales)
- ✅ Cierre de cuentas/productos
- ✅ Visualización de historial completo de transacciones

### 5. **Sistema de Auditoría**
- Registro automático de todas las transacciones
- Timestamp preciso para cada operación
- Detalles completos de cada movimiento
- Historial por usuario

## 🎮 Cómo Usar el Sistema

### Instalación y Ejecución
1. Asegúrese de tener Python 3.12.0 o superior instalado
2. Descargue todos los archivos del proyecto manteniendo la estructura de carpetas
3. Ejecute desde la terminal: `python main.py`
4. El sistema creará automáticamente el archivo `data/db.json` si no existe

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

### Flujo de Uso Recomendado
1. **Primer Uso**: Registre un nuevo cliente con todos sus datos
2. **Solicitud de Productos**: Abra cuentas de ahorro/corriente o solicite CDT
3. **Operaciones**: Realice depósitos, retiros, solicite créditos según necesite
4. **Seguimiento**: Consulte regularmente su historial de transacciones
5. **Gestión**: Realice pagos de créditos o cierre cuentas según corresponda

## 🔧 Características Técnicas

### Módulos del Sistema

#### **main.py**
- Punto de entrada principal
- Control de flujo mediante estructura match-case
- Manejo de errores con try-except
- Limpieza de pantalla entre operaciones

#### **modules/logicas.py**
- **Funciones principales**:
  - `registro_user()`: Registro completo de nuevos clientes
  - `filtro_user()`: Validación de usuarios existentes
  - Operaciones de cuenta: depósitos, retiros, cancelaciones
  - Operaciones de crédito: solicitud, pagos, cancelaciones
  - `historial_movimientos()`: Visualización de transacciones
  - `agregar_historial()`: Registro automático de auditoría

#### **modules/menu.py**
- Interfaces de usuario para cada sección
- Menús anidados para operaciones específicas
- Validación de entrada de datos

#### **modules/json_logic.py**
- **Funciones de persistencia**:
  - `read_json()`: Lectura de datos desde archivo
  - `write_json()`: Escritura de datos al archivo
  - `rewrite_json()`: Actualización parcial de datos
  - `delete_data_json()`: Eliminación de registros
  - `initialize_json()`: Inicialización de estructura

### Validaciones Implementadas
- Verificación de rangos de números de cuenta/crédito
- Límite de 5 créditos por cliente
- Validación de saldos antes de retiros/pagos
- Verificación de existencia de cuentas/créditos
- Control de entrada de datos numéricos
- Prevención de duplicados en números de usuario

### Seguridad y Auditoría
- Números de cuenta/crédito generados automáticamente
- Validación de existencia antes de cada operación
- Registro completo de auditoría con timestamps
- Prevención de cancelación de cuentas con saldo
- Validación de rangos para tipos específicos de productos

## 🚀 Requisitos del Sistema

- **Python:** 3.12.0 o superior
- **Sistema Operativo:** Windows (compatible con versiones recientes)
- **Espacio en Disco:** Mínimo 1MB para datos
- **RAM:** 128MB mínimo
- **Permisos:** Lectura/escritura en directorio del proyecto

## 📝 Notas Importantes

- **Persistencia de Datos**: Todos los datos se almacenan localmente en `data/db.json`
- **Generación Automática**: Los números de cuenta y crédito se generan automáticamente según rangos predefinidos
- **CDTs**: Los Certificados de Depósito a Término generan rendimiento del 12% anual automáticamente
- **Límites**: Máximo 5 créditos por cliente
- **Cancelaciones**: Solo se pueden cancelar cuentas con saldo 0
- **Historial**: Todas las operaciones quedan registradas automáticamente
- **Uso Educativo**: Sistema diseñado para propósitos educativos y demostrativos

## 📊 Ejemplo de Uso

```bash
# Ejecutar el sistema
python main.py

# Flujo típico:
# 1. Registro de cliente → Obtiene número de usuario
# 2. Solicitud de productos → Crea cuenta de ahorros
# 3. Depósito a cuentas → Agrega saldo a la cuenta
# 4. Solicitud de créditos → Solicita crédito de libre inversión
# 5. Pagos a créditos → Realiza pagos desde cuenta
# 6. Historial → Revisa todas las operaciones realizadas
