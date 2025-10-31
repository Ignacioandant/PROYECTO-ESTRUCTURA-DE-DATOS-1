"""Una cadena hotelera desea desarrollar un sistema de seguridad interna para gestionar el registro de huéspedes, el control del personal y el inventario de pertenencias dentro de los hoteles. El sistema deberá simular el funcionamiento básico de la seguridad del hotel, utilizando listas, funciones y matrices como estructuras principales.
El objetivo es ofrecer un sistema sencillo pero completo, que permita llevar un control de las habitaciones, el personal, los huéspedes y sus accesos al hotel, además de realizar cálculos estadísticos sobre la ocupación y pertenencias.

Requerimientos del sistema

1. Registro de huéspedes y personal
Se ingresará la cantidad de huéspedes y la cantidad de personal disponible en el hotel.
Los nombres de cada huésped y cada miembro del personal se almacenarán en listas separadas.
No se permitirán nombres duplicados.

2. Gestión de pertenencias de huéspedes
Cada huésped podrá registrar una cierta cantidad de objetos personales, los cuales deberán almacenarse en una lista.
Se controlará que la cantidad de pertenencias sea razonable (ejemplo: máximo 10 objetos).

Se calcularán estadísticas:
Número promedio de pertenencias por huésped.
Huésped con máximo y mínimo de pertenencias.

3. Llaves virtuales de acceso
El sistema permitirá generar llaves virtuales de acceso (códigos aleatorios) mediante el módulo random.
Cada llave será temporal, con un tiempo de validez simulado.
Las llaves podrán invalidarse manualmente si el huésped se retira antes de tiempo.

4. Matriz de habitaciones
El hotel contará con una matriz de habitaciones (id) y pisos(ejemplo: 5x5, y representa los pisos en un rango de 1 a 8, x representa el id de habitación).
Cada posición representará el estado de la habitación:
L: Libre
O: Ocupada
M: En mantenimiento
Se va a registrar primero la cantidad de ingreso que va a haber en el hotel ( más información en la parte de máximos y mínimos), al registrar un huésped, el sistema deberá asignarle automáticamente la primera habitación libre.
Se deberá poder cambiar de habitación a un huésped si es necesario.
Se calcularán estadísticas de ocupación:
Porcentaje de habitaciones ocupadas y libres.
Número máximo y mínimo de cantidad de personas en cada piso.

5. Control de accesos
Se almacenará una lista de accesos realizados (entradas y salidas).
Cada acceso deberá registrar: huésped/persona, acción (entrada o salida), fecha y hora.
Si se intenta ingresar sin estar registrado, el sistema generará una alerta de acceso no autorizado.

6. Reportes finales
Al finalizar la ejecución, el sistema deberá mostrar:
El listado de huéspedes con sus pertenencias y número de habitación.
El listado del personal registrado.
El estado de la matriz de habitaciones (ocupadas o libres), indicando el total de cada tipo y los porcentajes.
El historial de accesos realizados con fecha y hora.
El listado de intentos de acceso no autorizados.
Estadísticas adicionales:
Porcentaje de ocupación de habitaciones.
Número máximo y mínimo de personas en cada habitación y pisos.
"""
"""
UADE - Programación I / Algoritmos y Estructura de Datos I
Proyecto - Segunda Etapa (versión sin POO, simple y legible)

FUNCIONALIDADES (6):
1) Registro de huéspedes y personal (ABM + login simple, sin POO, TXT plano)
2) Gestión de pertenencias de huéspedes (máx. 10; estadísticas: promedio, máx, mín)
3) Llaves virtuales de acceso (códigos aleatorios y estado/validez)
4) Matriz de habitaciones (L/O/M); asignación automática, cambio de habitación, estadísticas
5) Control de accesos (entradas/salidas, hora); alerta si no está registrado
6) Reportes finales (≥4 CSV + opcional JSON), con % y promedios + bitácora LOG

CONDICIONES DE LA CÁTEDRA (resumen):
- Listas obligatorias y matrices (usadas en todo el flujo)
- Funciones lambda, list comprehensions y slicing (marcadas con # LAMBDA / # LC / # SLICING)
- Programación modular (funciones en este archivo)
- Manejo de datos aleatorios (para demo/semillas)
- Cadenas (strings) en validaciones/parsing
- Manejo de excepciones (inputs/archivo/lógica)
- Diccionarios, tuplas y conjuntos (usados en índices/validaciones)
- Recursividad (función recursiva para contar celdas 'M')
- Archivos TXT/CSV plano (NO se usa el módulo csv). JSON opcional.
- Menú por consola con validaciones
- ≥ 3 archivos de entrada y ≥ 4 archivos de salida
- Archivo LOG/bitácora con fecha/hora/acción/resultado
- Restricciones: sin POO, sin librerías externas (solo stdlib), sin usar 'csv' lib

EJECUCIÓN:
- Ejecutar este archivo. Elegir "1. Cargar datos demo" para generar entradas mínimas.
- Luego usar el menú para ABM, llaves, accesos, reportes, etc.
"""

import os
import random
import json
from datetime import datetime

# ---------------------------- MAPEADO DE REQUISITOS (con líneas) ----------------------------
# REQ 1 - Control de versiones (GIT/GitHub): fuera del código (gestión con git en el repositorio)
# REQ 2 - Listas (obligatorio): implementado en funciones:
#     - cargar_lista_simple()      -> línea 276
#     - guardar_lista_simple()     -> línea 282
#     - cargar_pertenencias()      -> línea 307
#     - guardar_pertenencias()     -> línea 320
#     - uso de listas en llaves y asignaciones: menu_llaves() línea 563, asignaciones en menu_habitaciones() línea 704
# REQ 3 - Matrices (opcional pero obligatorio en enunciado):
#     - cargar_matriz()            -> línea 287
#     - guardar_matriz()           -> línea 299
#     - asignar_habitacion()       -> línea 600
#     - cambiar_habitacion()       -> línea 616
#     - estadisticas_ocupacion()   -> línea 646
# REQ 4 - Funciones LAMBDA (obligatorio):
#     - uso en main(): map(lambda ...) -> línea 1008  # LAMBDA
# REQ 5 - List comprehensions / SLICING (obligatorio uno):
#     - ejemplo de list comprehension en cargar_lista_simple() -> línea 276
#     - list comprehension para objetos en cargar_pertenencias() -> línea 310
# REQ 6 - Programación modular (funciones): todo el archivo (varias funciones: ver listados)
# REQ 7 - Manejo de datos aleatorios (random):
#     - generar_codigo()           -> línea 555
#     - registrar_acceso()         -> línea 746
# REQ 8 - Cadenas (strings) y parsing:
#     - leer_lineas()              -> línea 149
#     - cargar_pertenencias()      -> línea 307
#     - cargar_llaves()            -> línea 334
# REQ 9 - Manejo de excepciones (obligatorio):
#     - presente en leer_lineas() (149), escribir_lineas() (162), cargar_datos_demo() (196), generar_reportes() (797)
# REQ 10 - Archivos TXT/CSV plano (obligatorio):
#     - leer_lineas()              -> línea 149
#     - escribir_lineas()          -> línea 162
#     - escribir_csv_plano()       -> línea 172
# REQ 11 - Diccionarios (obligatorio):
#     - consolidado_dict en generar_reportes() -> línea 840
# REQ 12 - Recursividad (obligatorio):
#     - contar_M_recursivo()       -> línea 636
# REQ 13 - Archivos JSON (opcional):
#     - escritura del JSON en generar_reportes() (consolidado_dict) -> línea 846
# -------------------------------------------------------------------------------

# --- Config archivos ---
DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    try:
        os.makedirs(DATA_DIR)
    except Exception:
        # Si no se puede crear el directorio, informar al usuario (forma sencilla para principiantes)
        print(f"No se pudo crear el directorio '{DATA_DIR}'")

F_USUARIOS = DATA_DIR + "/" + "usuarios.txt"
F_HUESPEDES = DATA_DIR + "/" + "huespedes.csv"
F_PERSONAL = DATA_DIR + "/" + "personal.csv"
F_HABITACIONES = DATA_DIR + "/" + "habitaciones.csv"
F_PERTENENCIAS = DATA_DIR + "/" + "pertenencias.csv"
F_LLAVES = DATA_DIR + "/" + "llaves.csv"
F_ACCESOS = DATA_DIR + "/" + "accesos.csv"
F_ACCESOS_NO = DATA_DIR + "/" + "accesos_no.csv"
F_LOG = DATA_DIR + "/" + "log.txt"

R_OCUPACION = DATA_DIR + "/" + "reporte_ocupacion.csv"
R_ACCESOS = DATA_DIR + "/" + "reporte_accesos.csv"
R_PERTENENCIAS = DATA_DIR + "/" + "reporte_pertenencias.csv"
R_TOPS = DATA_DIR + "/" + "reporte_tops.csv"
R_JSON = DATA_DIR + "/" + "reporte_completo.json"

# --- Utilidades de archivos y logs ---

# Función: log(mensaje, estado="OK") -- escribe una línea en el archivo de log con timestamp y estado
# Versión para principiantes: el estado se pasa como texto "OK" o "ERR" en lugar de True/False
def log(mensaje, estado="OK"):
    # obtener timestamp en formato legible
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # `estado` ya es una cadena; validamos valores simples para evitar confusión
    if estado != "OK" and estado != "ERR":
        # si se recibió algo inesperado, lo convertimos a texto
        estado = str(estado)
    # construir la línea concatenando cadenas
    linea = "[" + ts + "] " + estado + ": " + str(mensaje) + "\n"
    try:
        f = open(F_LOG, "at")
        try:
            f.write(linea)
        finally:
            f.close()
    except Exception as e:
        # Mostrar un mensaje claro si no se pudo escribir en el log
        print("No se pudo escribir en el archivo de log (" + F_LOG + "): " + str(e))


# Función: leer_lineas(ruta) -- devuelve lista de líneas (sin '\n') de un archivo si existe
def leer_lineas(ruta):
    lineas = []
    try:
        if os.path.exists(ruta):
            f = open(ruta, "rt")
            try:
                for ln in f:
                    lineas.append(ln.rstrip("\n"))
            finally:
                f.close()
    except Exception as e:
        log("Error leyendo " + ruta + ": " + str(e), estado="ERR")
    return lineas


# Función: escribir_lineas(ruta, lista_lineas) -- sobrescribe un archivo con las líneas provistas
def escribir_lineas(ruta, lista_lineas):
    try:
        f = open(ruta, "wt")
        try:
            for ln in lista_lineas:
                f.write(str(ln) + "\n")
        finally:
            f.close()
    except Exception as e:
        log("Error escribiendo " + ruta + ": " + str(e), estado="ERR")


# Función: escribir_csv_plano(ruta, filas) -- escribe una lista de filas como CSV (separado por comas)
def escribir_csv_plano(ruta, filas):
    try:
        f = open(ruta, "wt")
        try:
            for fila in filas:
                # cada fila es lista; unir por comas
                s = ""
                for x in fila:
                    if s == "":
                        s = str(x)
                    else:
                        s = s + "," + str(x)
                f.write(s + "\n")
        finally:
            f.close()
    except Exception as e:
        log("Error escribiendo csv " + ruta + ": " + str(e), estado="ERR")

# --- Hash sencillo para usuarios (docente) ---
# Función: hashito(clave) -- hash sencillo (suma de códigos unicode) para claves de usuario
def hashito(clave):
    s = 0
    for c in clave:
        s += ord(c)
    return s

# ---------------- DEMO (carga mínima) ----------------

# Función: cargar_datos_demo() -- crea archivos de ejemplo mínimos en la carpeta data
def cargar_datos_demo():
    # escribimos ejemplos simples; control de excepciones
    try:
        usuarios = [f"admin;{hashito('admin123')};personal", f"recepcion;{hashito('recep456')};personal"]
        escribir_lineas(F_USUARIOS, usuarios)

        huespedes = ["Ana Perez", "Bruno Diaz", "Carla Gomez", "Dario Luna"]
        escribir_lineas(F_HUESPEDES, huespedes)

        personal = ["Seguridad 1", "Limpieza 1", "Recepcion 1"]
        escribir_lineas(F_PERSONAL, personal)

        # matriz 4x4
        matriz = []
        for _ in range(4):
            fila = ["L", "L", "L", "L"]
            matriz.append(fila)
        matriz[0][1] = "M"
        matriz[2][3] = "M"
        # guardar cada fila como string (sin comas internas)
        filas_h = []
        for fila in matriz:
            s = ""
            for ch in fila:
                s = s + ch
            filas_h.append(s)
        escribir_lineas(F_HABITACIONES, filas_h)

        # pertenencias: nombre, objeto1|objeto2
        perten = ["Ana Perez,valija|notebook", "Bruno Diaz,mochila|libro"]
        escribir_lineas(F_PERTENENCIAS, perten)

        # llaves vacías
        escribir_lineas(F_LLAVES, [])
        escribir_lineas(F_ACCESOS, [])
        escribir_lineas(F_ACCESOS_NO, [])

        log("Datos demo generados")
        print("Datos demo generados en carpeta /data")
    except Exception as e:
        log("Error demo: " + str(e), estado="ERR")
        print("Error generando demo:", e)

# ---------------- Utilitarios de entrada ----------------

# Función: pedir_int(mensaje, minimo (opcional), maximo (opcional)) -- solicita y valida un entero
def pedir_int(mensaje, minimo=-999999999, maximo=999999999):
    resultado = 0
    while True:
        try:
            texto = input(mensaje).strip()
            valor = int(texto)
            if minimo != -999999999 and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue
            if maximo != 999999999 and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue
            resultado = valor
            break
        except ValueError:
            print("Entrada inválida. Ingrese un entero.")
        except Exception:
            print("Error en entrada. Intente de nuevo.")
    return resultado


# Función: pedir_opcion(mensaje, opciones) -- pide una opción y la valida contra el conjunto dado
def pedir_opcion(mensaje, opciones):
    opciones_minus = []
    for o in opciones:
        opciones_minus.append(o.lower())
    while True:
        try:
            valor = input(mensaje).strip().lower()
            if valor in opciones_minus:
                resultado = valor
                break
            else:
                print("Opción inválida. Opciones:", opciones)
        except Exception:
            print("Error leyendo opción. Intente de nuevo.")
    return resultado

# ---------------- Cargas y guardados simples (listas en lugar de dicts) ----------------

# Función: cargar_lista_simple(ruta) -- lee un archivo y devuelve una lista de cadenas no vacías
def cargar_lista_simple(ruta):
    # devuelve lista de strings
    return [ln for ln in leer_lineas(ruta) if ln]


# Función: guardar_lista_simple(ruta, lista) -- guarda una lista de strings en un archivo (uno por línea)
def guardar_lista_simple(ruta, lista):
    escribir_lineas(ruta, lista)


# Función: cargar_matriz() -- carga la matriz de habitaciones desde el archivo
def cargar_matriz():
    lineas = leer_lineas(F_HABITACIONES)
    matriz = []
    for linea in lineas:
        fila = []
        for caracter in linea:
            fila.append(caracter)
        matriz.append(fila)
    return matriz


# Función: guardar_matriz(m) -- guarda la matriz de habitaciones en el archivo
def guardar_matriz(m):
    filas = []
    for fila in m:
        s = ""
        for ch in fila:
            s = s + ch
        filas.append(s)
    escribir_lineas(F_HABITACIONES, filas)


# Función: cargar_pertenencias() -- lee pertenencias y devuelve lista de [nombre, [objetos]]
def cargar_pertenencias():
    # devuelve lista de [nombre, [obj1,obj2,...]]
    res = []
    lineas = leer_lineas(F_PERTENENCIAS)
    for linea in lineas:
        if not linea:
            continue
        partes = linea.split(",")
        nombre = partes[0].strip()
        objetos = []
        if len(partes) > 1:
            objetos = [obj for obj in partes[1].split("|") if obj]
        res.append([nombre, objetos])
    return res


# Función: guardar_pertenencias(lista) -- guarda la lista de pertenencias en formato nombre,obj1|obj2
def guardar_pertenencias(lista):
    filas = []
    for item in lista:
        nombre = item[0]
        objs = item[1]
        # construir la cadena de objetos de forma explícita (más claro para principiantes)
        objstr = ""
        for o in objs:
            if o:
                if objstr == "":
                    objstr = o
                else:
                    objstr = objstr + "|" + o
        filas.append(nombre + "," + objstr)
    escribir_lineas(F_PERTENENCIAS, filas)


# Función: cargar_llaves() -- lee las llaves virtuales y devuelve lista de [nombre,codigo,estado]
def cargar_llaves():
    # devuelve lista de [nombre, codigo, estado]
    res = []
    for linea in leer_lineas(F_LLAVES):
        if not linea:
            continue
        partes = linea.split(",")
        if len(partes) >= 3:
            res.append([partes[0].strip(), partes[1].strip(), partes[2].strip()])
    return res


# Función: guardar_llaves(lista) -- guarda la lista de llaves en el archivo correspondiente
def guardar_llaves(lista):
    filas = []
    for item in lista:
        # concatenar elementos con comas (forma explícita para principiantes)
        s = ""
        s = item[0] + "," + item[1] + "," + item[2]
        filas.append(s)
    escribir_lineas(F_LLAVES, filas)


# Función: cargar_accesos() -- retorna (accesos_validos, accesos_no) como listas de líneas
def cargar_accesos():
    # accesos y accesos no autorizados son listas de string CSV
    return leer_lineas(F_ACCESOS), leer_lineas(F_ACCESOS_NO)


# Función: guardar_acceso_valido(entry) -- añade una entrada de acceso válido al archivo
def guardar_acceso_valido(entry):
    # entry: [persona,tipo,accion,hh:mm:ss]
    try:
        f = open(F_ACCESOS, "at")
        try:
            s = ""
            for e in entry:
                if s == "":
                    s = str(e)
                else:
                    s = s + "," + str(e)
            f.write(s + "\n")
        finally:
            f.close()
    except Exception as e:
        log("Error escribiendo acceso: " + str(e), estado="ERR")


# Función: guardar_acceso_no(entry) -- añade una entrada de acceso no autorizado al archivo
def guardar_acceso_no(entry):
    try:
        f = open(F_ACCESOS_NO, "at")
        try:
            s = ""
            for e in entry:
                if s == "":
                    s = str(e)
                else:
                    s = s + "," + str(e)
            f.write(s + "\n")
        finally:
            f.close()
    except Exception as e:
        log("Error escribiendo acceso_no: " + str(e), estado="ERR")

# ---------------- Login simple (como antes) ----------------

# Función: login() -- maneja login simple (lee usuarios, valida hash, permite 'skip')
def login():
    lineas = leer_lineas(F_USUARIOS)
    usuarios = []  # lista de [usuario,hash,rol]
    for ln in lineas:
        if not ln:
            continue
        partes = ln.split(";")
        if len(partes) >= 3:
            usuarios.append([partes[0], partes[1], partes[2]])

    print("\n== Login (o 'skip' para saltar) ==")
    try:
        nombre = input("Usuario: ").strip()
    except Exception:
        nombre = ""
    if nombre.lower() == "skip":
        return "skip", "visitante"

    clave = input("Clave: ").strip()
    rol = ""
    for u in usuarios:
        try:
            if u[0] == nombre and int(u[1]) == hashito(clave):
                rol = u[2]
                break
        except Exception:
            continue
    if rol != "":
        print("Login exitoso. Rol:", rol)
        log("Login ok: " + nombre)
        return nombre, rol
    else:
        print("Login fallido.")
        log("Login fallido: " + nombre, estado="ERR")
        return "", ""

# ---------------- ABM simples ----------------

# Función: abm_lista(ruta, etiqueta) -- ABM simple (Agregar/Borrar/Listar) para listas
def abm_lista(ruta, etiqueta):
    lista = cargar_lista_simple(ruta)
    while True:
        print(f"\nABM {etiqueta}: [A]gregar [B]orrar [L]istar [S]alir")
        op = pedir_opcion("> ", {"a", "b", "l", "s"})
        if op == "a":
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Nombre vacío.")
                continue
            # no permitimos duplicados
            existe = False
            for n in lista:
                if n == nombre:
                    existe = True
                    break
            if existe:
                print("Ya existe.")
                continue
            lista.append(nombre)
            print("Agregado.")
        elif op == "b":
            nombre = input("Nombre a borrar: ").strip()
            encontrado = False
            for i, n in enumerate(lista):
                if n == nombre:
                    del lista[i]
                    encontrado = True
                    break
            if encontrado:
                print("Borrado.")
            else:
                print("No encontrado.")
        elif op == "l":
            for i, n in enumerate(lista, 1):
                print(f"{i}. {n}")
        else:
            guardar_lista_simple(ruta, lista)
            log(f"ABM {etiqueta} guardado ({len(lista)} items)")
            break

# ---------------- Pertenencias (lista de listas) ----------------

# Función: estadisticas_pertenencias(lista_perten) -- calcula y muestra estadísticas de pertenencias
def estadisticas_pertenencias(lista_perten):
    if not lista_perten:
        print("Sin pertenencias registradas.")
        return
    cantidades = []  # lista de [nombre, cantidad]
    for item in lista_perten:
        cantidades.append([item[0], len(item[1])])
    total_huespedes = len(cantidades)
    total_obj = 0
    for c in cantidades:
        total_obj += c[1]

    promedio = 0
    if total_huespedes > 0:
        promedio = total_obj / total_huespedes

    max_c = cantidades[0][1]
    min_c = cantidades[0][1]
    for c in cantidades:
        if c[1] > max_c:
            max_c = c[1]
        if c[1] < min_c:
            min_c = c[1]

    max_h = []
    min_h = []
    for c in cantidades:
        if c[1] == max_c:
            max_h.append(c[0])
        if c[1] == min_c:
            min_h.append(c[0])

    print("\n=== Estadísticas de pertenencias ===")
    print(f"Total huéspedes: {total_huespedes} | Total objetos: {total_obj} | Promedio/h: {promedio:.2f}")
    # construir cadenas de nombres separadas por coma y espacio
    max_h_str = ""
    for nombre in max_h:
        if max_h_str == "":
            max_h_str = nombre
        else:
            max_h_str = max_h_str + ", " + nombre
    min_h_str = ""
    for nombre in min_h:
        if min_h_str == "":
            min_h_str = nombre
        else:
            min_h_str = min_h_str + ", " + nombre
    print("Máximo " + str(max_c) + ": " + max_h_str)
    print("Mínimo " + str(min_c) + ": " + min_h_str)


# Función: menu_pertenencias() -- menú interactivo para gestionar pertenencias de huéspedes
def menu_pertenencias():
    perten = cargar_pertenencias()
    while True:
        print("\nPertenencias: [A]gregar [Q]uitar [L]istar [E]stadísticas [S]alir")
        op = pedir_opcion("> ", {"a", "q", "l", "e", "s"})
        if op == "a":
            h = input("Huésped: ").strip()
            found = False
            for item in perten:
                if item[0] == h:
                    found = True
                    objs = item[1]
                    break
            if not found:
                objs = []
                perten.append([h, objs])
            n = pedir_int("¿Cuántos objetos? (máx 10): ", 0, 10)
            for i in range(n):
                obj = input(f"  Objeto {i+1}: ").strip()
                if obj:
                    objs.append(obj)
            print("OK.")
        elif op == "q":
            h = input("Huésped: ").strip()
            quien = []
            for item in perten:
                if item[0] == h:
                    quien = item
                    break
            if not quien or not quien[1]:
                print("No hay objetos.")
                continue
            objs_str = ""
            for o in quien[1]:
                if objs_str == "":
                    objs_str = o
                else:
                    objs_str = objs_str + ", " + o
            print("Objetos: " + objs_str)
            obj = input("  Quitar: ").strip()
            if obj in quien[1]:
                quien[1].remove(obj)
                print("Quitado.")
            else:
                print("No existe.")
        elif op == "l":
            for h, objs in perten:
                print(f"- {h}: {objs}")
        elif op == "e":
            estadisticas_pertenencias(perten)
        else:
            guardar_pertenencias(perten)
            log("Pertenencias guardadas")
            break

# ---------------- Llaves virtuales (lista) ----------------

# Función: generar_codigo() -- genera un código aleatorio de 4 dígitos para llaves
def generar_codigo():
    return str(random.randint(1000, 9999))


# Función: menu_llaves() -- menú para generar, invalidar y listar llaves virtuales
def menu_llaves():
    llaves = cargar_llaves()
    while True:
        print("\nLlaves: [G]enerar/renovar [I]nvalidar [L]istar [S]alir")
        op = pedir_opcion("> ", {"g", "i", "l", "s"})
        if op == "g":
            h = input("Huésped: ").strip()
            encontrado = False
            for item in llaves:
                if item[0] == h:
                    item[1] = generar_codigo()
                    item[2] = "valida"
                    encontrado = True
                    break
            if not encontrado:
                llaves.append([h, generar_codigo(), "valida"])
            print("Llave generada.")
        elif op == "i":
            h = input("Huésped: ").strip()
            encontrado = False
            for item in llaves:
                if item[0] == h:
                    item[2] = "invalida"
                    encontrado = True
                    break
            if encontrado:
                print("Invalidadada.")
            else:
                print("No existe.")
        elif op == "l":
            for item in llaves:
                print(f"- {item[0]}: {item[1]} ({item[2]})")
        else:
            guardar_llaves(llaves)
            log("Llaves guardadas")
            break

# ---------------- Habitaciones: matriz L/O/M y asignaciones (lista de asignaciones) ----------------

# Función: asignar_habitacion(matriz, huesped, asignaciones) -- asigna la primera habitación libre
def asignar_habitacion(matriz, huesped, asignaciones):
    # asignaciones es lista de [huesped, i, j]
    asignado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "L":
                matriz[i][j] = "O"
                asignaciones.append([huesped, i, j])
                asignado = True
                break
        if asignado:
            break
    return asignado


# Función: cambiar_habitacion(matriz, huesped, asignaciones) -- cambia la habitación de un huésped
def cambiar_habitacion(matriz, huesped, asignaciones):
    indice = -1
    for k in range(len(asignaciones)):
        if asignaciones[k][0] == huesped:
            indice = k
            break
    if indice == -1:
        return False
    pi = asignaciones[indice][1]
    pj = asignaciones[indice][2]
    # liberar actual
    if 0 <= pi < len(matriz) and 0 <= pj < len(matriz[pi]):
        matriz[pi][pj] = "L"
    # eliminar asignación vieja
    del asignaciones[indice]
    # asignar nueva
    return asignar_habitacion(matriz, huesped, asignaciones)


# Función: contar_M_recursivo(m, i=0, j=0) -- cuenta recursivamente celdas en mantenimiento 'M'
def contar_M_recursivo(m, i=0, j=0):
    # sencillo: recorrer recursivamente
    if i >= len(m):
        return 0
    if j >= len(m[i]):
        return contar_M_recursivo(m, i+1, 0)
    suma = 0
    if m[i][j] == "M":
        suma = 1
    return suma + contar_M_recursivo(m, i, j+1)


# Función: estadisticas_ocupacion(m) -- muestra estadísticas y porcentajes de ocupación por piso
def estadisticas_ocupacion(m):
    total = 0
    for fila in m:
        total += len(fila)
    occ = 0
    libres = 0
    mant = 0
    for fila in m:
        for c in fila:
            if c == "O":
                occ += 1
            elif c == "L":
                libres += 1
            elif c == "M":
                mant += 1
    print("\n=== Estadísticas de ocupación ===")
    pct_occ = 0
    if total > 0:
        pct_occ = occ / total * 100
    print(f"Total: {total} | Ocupadas: {occ} ({pct_occ:.2f}%) | Libres: {libres} | M: {mant}")
    por_piso = []
    for fila in m:
        cont = 0
        for c in fila:
            if c == "O":
                cont += 1
        por_piso.append(cont)
    print("\nPersonas por piso:")
    max_p = 0
    min_p = 0
    if por_piso:
        max_p = por_piso[0]
        min_p = por_piso[0]
        for c in por_piso:
            if c > max_p:
                max_p = c
            if c < min_p:
                min_p = c
    for i, c in enumerate(por_piso, 1):
        print(f"Piso {i}: {c} personas")
    print("Máximo piso:", max_p, "| Mínimo piso:", min_p)
    print("Celdas en mantenimiento (recursivo):", contar_M_recursivo(m))


# Función: menu_habitaciones() -- menú para gestionar matriz de habitaciones y asignaciones
def menu_habitaciones():
    m = cargar_matriz()
    if not m:
        pisos = pedir_int("Cantidad de pisos (1-8): ", 1, 8)
        cols = pedir_int("Habitaciones por piso: ", 1, 20)
        for _ in range(pisos):
            fila = []
            for _ in range(cols):
                fila.append("L")
            m.append(fila)
    asignaciones = []  # lista de [huesped, i, j]
    while True:
        print("\nHabitaciones: [A]signar [C]ambiar [M]antenimiento toggle [V]er [E]stadísticas [S]alir")
        op = pedir_opcion("> ", {"a", "c", "m", "v", "e", "s"})
        if op == "a":
            h = input("Huésped: ").strip()
            ok = asignar_habitacion(m, h, asignaciones)
            if ok:
                print("Asignado.")
            else:
                print("No hay libres.")
        elif op == "c":
            h = input("Huésped: ").strip()
            ok = cambiar_habitacion(m, h, asignaciones)
            if ok:
                print("Cambiado.")
            else:
                print("No asignado o sin libres.")
        elif op == "m":
            i = pedir_int("Piso (1..): ", 1) - 1
            j = pedir_int("Hab (1..): ", 1) - 1
            try:
                if m[i][j] != "M":
                    m[i][j] = "M"
                else:
                    m[i][j] = "L"
                print("OK.")
            except Exception:
                print("Posición inválida.")
        elif op == "v":
            for idx, fila in enumerate(m, 1):
                print(f"Piso {idx}: {fila}")
        elif op == "e":
            estadisticas_ocupacion(m)
        else:
            guardar_matriz(m)
            log("Matriz de habitaciones guardada")
            break

# ---------------- Control de accesos ----------------

# Función: registrar_acceso(persona, tipo, accion) -- registra accesos válidos o no autorizados
def registrar_acceso(persona, tipo, accion):
    hh = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
    entry = [persona, tipo, accion, hh]
    if tipo == "Huesped" or tipo == "Personal":
        guardar_acceso_valido(entry)
        log(f"Acceso ok: {persona}-{accion} {hh}")
    else:
        guardar_acceso_no(entry)
        log("Acceso NO AUT: " + persona + "-" + accion + " " + hh, estado="ERR")


# Función: menu_accesos() -- menú para registrar y listar accesos
def menu_accesos():
    huespedes = cargar_lista_simple(F_HUESPEDES)
    personal = cargar_lista_simple(F_PERSONAL)
    while True:
        print("\nAccesos: [R]egistrar [L]istar válidos [N]o autorizados [S]alir")
        opcion = pedir_opcion("> ", {"r", "l", "n", "s"})
        if opcion == "r":
            persona = input("Persona: ").strip()
            accion = pedir_opcion("Acción (entrada/salida): ", {"entrada", "salida"})
            tipo = "NoAut"
            encontrado = False
            for nombre_h in huespedes:
                if nombre_h == persona:
                    tipo = "Huesped"
                    encontrado = True
                    break
            if not encontrado:
                for nombre_p in personal:
                    if nombre_p == persona:
                        tipo = "Personal"
                        encontrado = True
                        break
            registrar_acceso(persona, tipo, accion)
            if tipo == "NoAut":
                print("ALERTA: acceso no autorizado.")
            else:
                print(f"Registrado ({tipo}).")
        elif opcion == "l":
            for linea in leer_lineas(F_ACCESOS):
                print(linea)
        elif opcion == "n":
            for linea in leer_lineas(F_ACCESOS_NO):
                print(linea)
        else:
            break

# ---------------- Generar reportes (CSV + JSON opcional) ----------------

# Función: generar_reportes() -- genera 4 CSV y un JSON opcional con las métricas del sistema
def generar_reportes():
    # Cargar insumos
    m = cargar_matriz()
    huespedes = cargar_lista_simple(F_HUESPEDES)
    personal = cargar_lista_simple(F_PERSONAL)
    perten = cargar_pertenencias()
    llaves = cargar_llaves()
    accesos = leer_lineas(F_ACCESOS)
    accesos_no = leer_lineas(F_ACCESOS_NO)

    # Reporte 1: ocupacion
    total = 0
    for fila in m:
        total += len(fila)
    if total == 0:
        total = 1
    occ = 0
    libres = 0
    for fila in m:
        for c in fila:
            if c == "O":
                occ += 1
            if c == "L":
                libres += 1
    por_piso = []
    for fila in m:
        cont = 0
        for c in fila:
            if c == "O":
                cont += 1
        por_piso.append(cont)
    filas1 = [["total", total], ["ocupadas", occ, f"{occ/total*100:.2f}%"], ["libres", libres, f"{libres/total*100:.2f}%"]]
    for i, c in enumerate(por_piso):
        filas1.append([f"Piso {i+1}", c])
    escribir_csv_plano(R_OCUPACION, filas1)

    # Reporte 2: accesos
    def parse_acc(ln):
        partes = (ln.split(",") + ["", "", "", ""])[:4]
        return partes
    acc_val = []
    for ln in accesos:
        acc_val.append(parse_acc(ln))
    acc_no = []
    for ln in accesos_no:
        acc_no.append(parse_acc(ln))
    filas_acc = [["Válidos"]]
    for a in acc_val:
        filas_acc.append(a)
    filas_acc.append(["NoAut"])
    for a in acc_no:
        filas_acc.append(a)
    escribir_csv_plano(R_ACCESOS, filas_acc)

    # Reporte 3: pertenencias (orden simple por cantidad)
    orden = []  # lista de [nombre, cantidad]
    for item in perten:
        orden.append([item[0], len(item[1])])
    # ordenar burbuja (para ser muy didáctico)
    n = len(orden)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if orden[j][1] < orden[j+1][1]:
                tmp = orden[j]
                orden[j] = orden[j+1]
                orden[j+1] = tmp
            j += 1
        i += 1
    filas3 = [["Huesped", "CantObjetos"]]
    for o in orden:
        filas3.append([o[0], o[1]])
    if orden:
        suma = 0
        for o in orden:
            suma += o[1]
        prom = suma / len(orden)
        max_c = orden[0][1]
        min_c = orden[-1][1]
        max_h = []
        min_h = []
        for o in orden:
            if o[1] == max_c:
                max_h.append(o[0])
            if o[1] == min_c:
                min_h.append(o[0])
        filas3.append(["Promedio", f"{prom:.2f}"])
        # construir cadenas con '|' explícitamente
        max_h_pipe = ""
        for nombre in max_h:
            if max_h_pipe == "":
                max_h_pipe = nombre
            else:
                max_h_pipe = max_h_pipe + "|" + nombre
        min_h_pipe = ""
        for nombre in min_h:
            if min_h_pipe == "":
                min_h_pipe = nombre
            else:
                min_h_pipe = min_h_pipe + "|" + nombre
        filas3.append(["Max", max_c, max_h_pipe])
        filas3.append(["Min", min_c, min_h_pipe])
    escribir_csv_plano(R_PERTENENCIAS, filas3)

    # Reporte 4: tops y metadatos
    filas4 = []
    pisos_top = 0
    pisos_min = 0
    if por_piso:
        pisos_top = por_piso[0]
        pisos_min = por_piso[0]
        for c in por_piso:
            if c > pisos_top:
                pisos_top = c
            if c < pisos_min:
                pisos_min = c
    filas4.append(["Piso con más ocupación", pisos_top])
    filas4.append(["Piso con menos ocupación", pisos_min])

    vals = 0
    invs = 0
    for it in llaves:
        if it[2] == "valida":
            vals += 1
        elif it[2] == "invalida":
            invs += 1
    filas4.append(["Llaves válidas", vals])
    filas4.append(["Llaves inválidas", invs])

    cont_no = []  # lista de [persona, count]
    for ln in accesos_no:
        if not ln:
            continue
        p = ln.split(",")[0].strip()
        encontrado = False
        for item in cont_no:
            if item[0] == p:
                item[1] += 1
                encontrado = True
                break
        if not encontrado:
            cont_no.append([p, 1])
    for it in cont_no:
        filas4.append([f"NoAut - {it[0]}", it[1]])

    escribir_csv_plano(R_TOPS, filas4)

    # JSON opcional (usamos listas para ser simples)
    consolidado = [
        ["huespedes", huespedes],
        ["personal", personal],
        ["pertenencias", perten],
        ["llaves", llaves],
        ["ocupacion", [total, occ, libres, por_piso]],
        ["accesos_validos", acc_val[:50]],
        ["accesos_no_aut", acc_no[:50]]
    ]
    # Además del listado en listas, generamos un diccionario consolidado
    # REQ: Diccionarios (obligatorio) - consolidado_dict se usa para JSON
    consolidado_dict = {
        "huespedes": huespedes,
        "personal": personal,
        "pertenencias": perten,
        "llaves": llaves,
        "ocupacion": {"total": total, "ocupadas": occ, "libres": libres, "por_piso": por_piso},
        "accesos_validos": acc_val[:50],
        "accesos_no_aut": acc_no[:50],
    }
    try:
        f = open(R_JSON, "wt")
        try:
            json.dump(consolidado_dict, f, ensure_ascii=False, indent=2)
        finally:
            f.close()
    except Exception as e:
        log("Error creando JSON: " + str(e), estado="ERR")

    log("Reportes generados")
    print("✔ Reportes generados en /data (4 CSV + JSON opcional)")

# ---------------- Menu principal y main ----------------

# Función: menu_principal() -- menú principal que enlaza todas las funcionalidades
def menu_principal():
    while True:
        print("""
================= HOTEL SEGURIDAD - MENU =================
1) Cargar datos DEMO (genera entradas mínimas)
2) ABM Huespedes
3) ABM Personal
4) Pertenencias de huéspedes
5) Llaves virtuales
6) Habitaciones (matriz L/O/M)
7) Registrar/Listar accesos
8) Generar reportes finales (CSV + JSON)
9) Salir
==========================================================
""")
        op = pedir_opcion("> ", {"1","2","3","4","5","6","7","8","9"})
        if op == "1":
            cargar_datos_demo()
        elif op == "2":
            abm_lista(F_HUESPEDES, "Huéspedes")
        elif op == "3":
            abm_lista(F_PERSONAL, "Personal")
        elif op == "4":
            menu_pertenencias()
        elif op == "5":
            menu_llaves()
        elif op == "6":
            menu_habitaciones()
        elif op == "7":
            menu_accesos()
        elif op == "8":
            generar_reportes()
        else:
            print("¡Hasta luego!")
            break


# Función: main() -- punto de entrada; realiza login opcional y lanza el menú principal
def main():
    # Login opcional
    try:
        u, rol = login()
    except Exception:
        u, rol = "", ""
    # mostramos un ejemplo sencillo con longitudes de nombres
    try:
        lista_h = cargar_lista_simple(F_HUESPEDES)
        # LAMBDA: usamos una lambda para obtener longitudes (requisito: funciones lambda)
        longs = list(map(lambda nombre: len(nombre), lista_h))
        if longs:
            print("Longitudes de nombres de huéspedes:", longs)
    except Exception:
        log("Error calculando longitudes", ok=False)

    menu_principal()


if __name__ == "__main__":
    main()
    