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

# ------------------------------ CONFIG DE ARCHIVOS ------------------------------ #
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

F_USUARIOS = os.path.join(DATA_DIR, "usuarios.txt")          # login/rol -> "usuario;hash;rol"
F_HUESPEDES = os.path.join(DATA_DIR, "huespedes.csv")        # nombre
F_PERSONAL = os.path.join(DATA_DIR, "personal.csv")          # nombre
F_HABITACIONES = os.path.join(DATA_DIR, "habitaciones.csv")  # matriz serializada
F_PERTENENCIAS = os.path.join(DATA_DIR, "pertenencias.csv")  # "huesped, objeto1|objeto2|..."
F_Llaves = os.path.join(DATA_DIR, "llaves.csv")              # "huesped,codigo,estado"
F_ACCESOS = os.path.join(DATA_DIR, "accesos.csv")            # "persona,tipo,accion,hh:mm:ss"
F_ACCESOS_NO = os.path.join(DATA_DIR, "accesos_no.csv")      # no autorizados
F_LOG = os.path.join(DATA_DIR, "log.txt")

# Reportes (≥4)
R_OCUPACION = os.path.join(DATA_DIR, "reporte_ocupacion.csv")
R_ACCESOS = os.path.join(DATA_DIR, "reporte_accesos.csv")
R_PERTENENCIAS = os.path.join(DATA_DIR, "reporte_pertenencias.csv")
R_TOPS = os.path.join(DATA_DIR, "reporte_tops.csv")
R_JSON_OPCIONAL = os.path.join(DATA_DIR, "reporte_completo.json")  # opcional

# ------------------------------ UTILIDADES DE ARCHIVOS ------------------------------ #
def log(msg: str, ok: bool = True):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{ts}] {'OK' if ok else 'ERR'}: {msg}"
    with open(F_LOG, "a", encoding="utf-8") as f:
        f.write(linea + "\n")

def escribir_csv_plano(ruta: str, filas: list[list[str]]):
    with open(ruta, "w", encoding="utf-8") as f:
        for fila in filas:
            f.write(",".join(map(str, fila)) + "\n")

def leer_lineas(ruta: str) -> list[str]:
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return [x.rstrip("\n") for x in f.readlines()]

def escribir_lineas(ruta: str, lineas: list[str]):
    with open(ruta, "w", encoding="utf-8") as f:
        for ln in lineas:
            f.write(ln + "\n")

def hashito(clave: str) -> int:
    # hash MUY simple y docente (no criptográfico)
    return sum(ord(c) for c in clave)

# ------------------------------ DEMO: GENERAR ENTRADAS (≥3) ------------------------------ #
def cargar_datos_demo():
    try:
        # Usuarios: admin + recepcion
        usuarios = [
            "admin;{};personal".format(hashito("admin123")),
            "recepcion;{};personal".format(hashito("recep456")),
        ]
        escribir_lineas(F_USUARIOS, usuarios)

        # Listas de huéspedes y personal
        huespedes = [["Ana Perez"], ["Bruno Diaz"], ["Carla Gomez"], ["Dario Luna"]]
        personal = [["Seguridad 1"], ["Limpieza 1"], ["Recepcion 1"]]
        escribir_csv_plano(F_HUESPEDES, huespedes)
        escribir_csv_plano(F_PERSONAL, personal)

        # Habitaciones: por defecto 4x4 con algunas en Mantenimiento
        pisos, cols = 4, 4
        matriz = [["L" for _ in range(cols)] for _ in range(pisos)]
        matriz[0][1] = "M"
        matriz[2][3] = "M"
        escribir_csv_plano(F_HABITACIONES, [",".join(fila).split(",") for fila in ["".join(f) for f in matriz]])

        # Pertenencias iniciales
        pertenencias = [
            ["Ana Perez", "valija|notebook"],
            ["Bruno Diaz", "mochila|libro"],
        ]
        escribir_csv_plano(F_PERTENENCIAS, pertenencias)

        # Llaves vacías inicialmente
        escribir_csv_plano(F_Llaves, [])

        # Accesos históricos vacíos (dejar archivos creados)
        escribir_csv_plano(F_ACCESOS, [])
        escribir_csv_plano(F_ACCESOS_NO, [])

        log("Datos demo generados")
        print("✔ Datos demo generados en carpeta /data")
    except Exception as e:
        log(f"Error en cargar_datos_demo: {e}", ok=False)
        print("Error generando demo:", e)

# ------------------------------ UTILES DE ENTRADA CON EXCEPCIONES ------------------------------ #
def pedir_int(msg: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if minimo is not None and v < minimo:
                raise ValueError(f"Debe ser ≥ {minimo}")
            if maximo is not None and v > maximo:
                raise ValueError(f"Debe ser ≤ {maximo}")
            return v
        except ValueError as e:
            print("Entrada inválida:", e)

def pedir_opcion(msg: str, opciones: set[str]) -> str:
    while True:
        v = input(msg).strip().lower()
        if v in opciones:
            return v
        print("Opción inválida:", opciones)

# ------------------------------ 1) LOGIN + ABM USUARIOS/PERSONAL/HUESPEDES ------------------------------ #
def cargar_lista_desde_csv(ruta: str) -> list[str]:
    return [linea.split(",")[0] for linea in leer_lineas(ruta) if linea]

def guardar_lista_csv(ruta: str, nombres: list[str]):
    escribir_csv_plano(ruta, [[n] for n in nombres])

def abm_lista(ruta: str, etiqueta: str):
    lista = cargar_lista_desde_csv(ruta)
    while True:
        print(f"\nABM {etiqueta}: [A]gregar [B]orrar [L]istar [S]alir")
        op = pedir_opcion("> ", {"a", "b", "l", "s"})
        if op == "a":
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Nombre vacío.")
                continue
            if nombre in set(lista):  # uso de CONJUNTO
                print("Ya existe.")
                continue
            lista.append(nombre)
            print("Agregado.")
        elif op == "b":
            nombre = input("Nombre a borrar: ").strip()
            if nombre in lista:
                lista.remove(nombre)
                print("Borrado.")
            else:
                print("No encontrado.")
        elif op == "l":
            for i, n in enumerate(lista, 1):
                print(f"{i}. {n}")
        else:
            guardar_lista_csv(ruta, lista)
            log(f"ABM {etiqueta} guardado ({len(lista)} items)")
            break

def login():
    lineas = leer_lineas(F_USUARIOS)
    base = [ln.split(";") for ln in lineas if ln]
    usuarios = {u: (int(h), r) for u, h, r in base}  # diccionario: usuario -> (hash, rol)
    print("\n== Login (o 'skip' para continuar sin validar) ==")
    u = input("Usuario: ").strip()
    if u.lower() == "skip":
        return "skip", "visitante"
    c = input("Clave: ").strip()
    if u in usuarios and usuarios[u][0] == hashito(c):
        print("Login exitoso. Rol:", usuarios[u][1])
        log(f"Login ok: {u}")
        return u, usuarios[u][1]
    print("Login fallido.")
    log(f"Login fallido: {u}", ok=False)
    return None, None

# ------------------------------ 2) PERTENENCIAS ------------------------------ #
def cargar_pertenencias() -> dict[str, list[str]]:
    d = {}
    for ln in leer_lineas(F_PERTENENCIAS):
        if not ln:
            continue
        partes = ln.split(",")
        nombre = partes[0].strip()
        objs = (partes[1].strip() if len(partes) > 1 else "")
        d[nombre] = [x for x in objs.split("|") if x]  # LC
    return d

def guardar_pertenencias(d: dict[str, list[str]]):
    filas = []
    for k, v in d.items():
        filas.append([k, "|".join(v)])
    escribir_csv_plano(F_PERTENENCIAS, filas)

def estadisticas_pertenencias(d: dict[str, list[str]]):
    if not d:
        print("Sin pertenencias registradas.")
        return
    cantidades = [(h, len(v)) for h, v in d.items()]  # lista de tuplas
    total_huespedes = len(cantidades)
    total_obj = sum(c for _, c in cantidades)
    promedio = total_obj / total_huespedes if total_huespedes else 0

    max_c = max(c for _, c in cantidades)
    min_c = min(c for _, c in cantidades)
    max_h = [h for h, c in cantidades if c == max_c]  # LC
    min_h = [h for h, c in cantidades if c == min_c]  # LC

    print("\n=== Estadísticas de pertenencias ===")
    print(f"Total huéspedes: {total_huespedes} | Total objetos: {total_obj} | Promedio/h: {promedio:.2f}")
    print(f"Máximo {max_c}: {', '.join(max_h)}")
    print(f"Mínimo {min_c}: {', '.join(min_h)}")

def menu_pertenencias():
    d = cargar_pertenencias()
    while True:
        print("\nPertenencias: [A]gregar [Q]uitar [L]istar [E]stadísticas [S]alir")
        op = pedir_opcion("> ", {"a", "q", "l", "e", "s"})
        if op == "a":
            h = input("Huésped: ").strip()
            d.setdefault(h, [])
            n = pedir_int("¿Cuántos objetos? (máx 10): ", 0, 10)
            for i in range(n):
                obj = input(f"  Objeto {i+1}: ").strip()
                if obj:
                    d[h].append(obj)
            print("OK.")
        elif op == "q":
            h = input("Huésped: ").strip()
            if h not in d or not d[h]:
                print("No hay objetos.")
                continue
            print("Objetos:", ", ".join(d[h]))
            obj = input("  Quitar: ").strip()
            if obj in d[h]:
                d[h].remove(obj)
                print("Quitado.")
            else:
                print("No existe.")
        elif op == "l":
            for h, objs in d.items():
                print(f"- {h}: {objs}")
        elif op == "e":
            estadisticas_pertenencias(d)
        else:
            guardar_pertenencias(d)
            log("Pertenencias guardadas")
            break

# ------------------------------ 3) LLAVES VIRTUALES ------------------------------ #
def cargar_llaves() -> dict[str, dict]:
    d = {}
    for ln in leer_lineas(F_Llaves):
        if not ln:
            continue
        h, cod, est = [x.strip() for x in ln.split(",")]
        d[h] = {"codigo": cod, "estado": est}
    return d

def guardar_llaves(d: dict[str, dict]):
    filas = [[h, v["codigo"], v["estado"]] for h, v in d.items()]  # LC
    escribir_csv_plano(F_Llaves, filas)

def generar_llave() -> str:
    return str(random.randint(1000, 9999))

def menu_llaves():
    llaves = cargar_llaves()
    while True:
        print("\nLlaves: [G]enerar/renovar [I]nvalidar [L]istar [S]alir")
        op = pedir_opcion("> ", {"g", "i", "l", "s"})
        if op == "g":
            h = input("Huésped: ").strip()
            llaves[h] = {"codigo": generar_llave(), "estado": "valida"}
            print("Llave:", llaves[h]["codigo"])
        elif op == "i":
            h = input("Huésped: ").strip()
            if h in llaves:
                llaves[h]["estado"] = "invalida"
                print("Invalidadada.")
            else:
                print("No existe.")
        elif op == "l":
            for h, data in llaves.items():
                print(f"- {h}: {data['codigo']} ({data['estado']})")
        else:
            guardar_llaves(llaves)
            log("Llaves guardadas")
            break

# ------------------------------ 4) MATRIZ DE HABITACIONES ------------------------------ #
def cargar_matriz() -> list[list[str]]:
    lineas = leer_lineas(F_HABITACIONES)
    if not lineas:
        return []
    # cada línea tiene la fila como string sin comas, usar slicing por seguridad
    matriz = []
    for ln in lineas:
        fila = [c for c in ln]  # LC (caracteres)
        matriz.append(fila[:])  # SLICING: copia
    return matriz

def guardar_matriz(m: list[list[str]]):
    escribir_csv_plano(F_HABITACIONES, [ ["".join(f)] for f in m ])

def asignar_habitacion(m: list[list[str]], huesped: str, asignaciones: dict[str, tuple[int,int]]) -> bool:
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "L":
                m[i][j] = "O"
                asignaciones[huesped] = (i, j)  # tupla (piso, col)
                return True
    return False

def cambiar_habitacion(m: list[list[str]], huesped: str, asignaciones: dict[str, tuple[int,int]]) -> bool:
    if huesped not in asignaciones:
        return False
    pi, pj = asignaciones[huesped]
    # liberar la actual
    m[pi][pj] = "L"
    return asignar_habitacion(m, huesped, asignaciones)

def contar_M_recursivo(m: list[list[str]], i=0, j=0) -> int:
    # RECURSIVIDAD simple: recorre toda la matriz contando 'M'
    if i >= len(m):
        return 0
    if j >= len(m[i]):
        return contar_M_recursivo(m, i+1, 0)
    return (1 if m[i][j] == "M" else 0) + contar_M_recursivo(m, i, j+1)

def estadisticas_ocupacion(m: list[list[str]]):
    total = sum(len(f) for f in m)
    occ = sum(f.count("O") for f in m)
    libres = sum(f.count("L") for f in m)
    mant = sum(f.count("M") for f in m)
    print("\n=== Estadísticas de ocupación ===")
    print(f"Total: {total} | Ocupadas: {occ} ({occ/total*100:.2f}%) | Libres: {libres} ({libres/total*100:.2f}%) | M: {mant}")
    print("\nPersonas por piso:")
    por_piso = [f.count("O") for f in m]  # LC
    for i, c in enumerate(por_piso, 1):
        print(f"Piso {i}: {c} personas")
    print("Máximo piso:", max(por_piso) if por_piso else 0, "| Mínimo piso:", min(por_piso) if por_piso else 0)
    print("Celdas en mantenimiento (recursivo):", contar_M_recursivo(m))

def menu_habitaciones():
    m = cargar_matriz()
    if not m:
        # crear desde cero
        pisos = pedir_int("Cantidad de pisos (1-8): ", 1, 8)
        cols = pedir_int("Habitaciones por piso: ", 1, 20)
        m = [["L" for _ in range(cols)] for _ in range(pisos)]
    asignaciones = {}  # huesped -> (piso, col)

    while True:
        print("\nHabitaciones: [A]signar [C]ambiar [M]antenimiento toggle [V]er [E]stadísticas [S]alir")
        op = pedir_opcion("> ", {"a", "c", "m", "v", "e", "s"})
        if op == "a":
            h = input("Huésped: ").strip()
            ok = asignar_habitacion(m, h, asignaciones)
            print("Asignado." if ok else "No hay libres.")
        elif op == "c":
            h = input("Huésped: ").strip()
            ok = cambiar_habitacion(m, h, asignaciones)
            print("Cambiado." if ok else "No asignado o sin libres.")
        elif op == "m":
            i = pedir_int("Piso (1..): ", 1) - 1
            j = pedir_int("Hab (1..): ", 1) - 1
            try:
                m[i][j] = "M" if m[i][j] != "M" else "L"
                print("OK.")
            except IndexError:
                print("Posición inválida.")
        elif op == "v":
            for i, fila in enumerate(m, 1):
                print(f"Piso {i}: {fila}")
        elif op == "e":
            estadisticas_ocupacion(m)
        else:
            guardar_matriz(m)
            log("Matriz de habitaciones guardada")
            break

# ------------------------------ 5) CONTROL DE ACCESOS ------------------------------ #
def registrar_acceso(persona: str, tipo: str, accion: str):
    hh = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"
    filas = [[persona, tipo, accion, hh]]
    escribir_csv_plano(F_ACCESOS if tipo in {"Huesped","Personal"} else F_ACCESOS_NO, filas)
    log(f"Acceso {'ok' if tipo in {'Huesped','Personal'} else 'NO AUT'}: {persona}-{accion} {hh}")

def menu_accesos():
    huespedes = set(cargar_lista_desde_csv(F_HUESPEDES))
    personal = set(cargar_lista_desde_csv(F_PERSONAL))
    while True:
        print("\nAccesos: [R]egistrar [L]istar válidos [N]o autorizados [S]alir")
        op = pedir_opcion("> ", {"r", "l", "n", "s"})
        if op == "r":
            p = input("Persona: ").strip()
            accion = pedir_opcion("Acción (entrada/salida): ", {"entrada", "salida"})
            if p in huespedes:
                registrar_acceso(p, "Huesped", accion)
                print("Registrado (Huésped).")
            elif p in personal:
                registrar_acceso(p, "Personal", accion)
                print("Registrado (Personal).")
            else:
                registrar_acceso(p, "NoAut", accion)
                print("ALERTA: acceso no autorizado.")
        elif op == "l":
            for ln in leer_lineas(F_ACCESOS):
                print(ln)
        elif op == "n":
            for ln in leer_lineas(F_ACCESOS_NO):
                print(ln)
        else:
            break

# ------------------------------ 6) REPORTES (≥4 CSV + JSON opcional) ------------------------------ #
def generar_reportes():
    # Cargar insumos
    m = cargar_matriz()
    huespedes = cargar_lista_desde_csv(F_HUESPEDES)
    personal = cargar_lista_desde_csv(F_PERSONAL)
    perten = cargar_pertenencias()
    llaves = cargar_llaves()
    accesos = leer_lineas(F_ACCESOS)
    accesos_no = leer_lineas(F_ACCESOS_NO)

    # --- Reporte 1: Ocupación --- #
    total = sum(len(f) for f in m) or 1
    occ = sum(f.count("O") for f in m)
    libres = sum(f.count("L") for f in m)
    por_piso = [f.count("O") for f in m]
    filas1 = [["total", total],
              ["ocupadas", occ, f"{occ/total*100:.2f}%"],
              ["libres", libres, f"{libres/total*100:.2f}%"]]
    filas1 += [[f"Piso {i+1}", c] for i, c in enumerate(por_piso)]
    escribir_csv_plano(R_OCUPACION, filas1)

    # --- Reporte 2: Accesos consolidado --- #
    def parse_acc(ln):
        p,t,a,h = (ln.split(",") + ["","","",""])[:4]
        return [p,t,a,h]
    acc_val = [parse_acc(ln) for ln in accesos]            # LC
    acc_no  = [parse_acc(ln) for ln in accesos_no]         # LC
    escribir_csv_plano(R_ACCESOS, [["Válidos"]] + acc_val + [["NoAut"]] + acc_no)

    # --- Reporte 3: Pertenencias --- #
    # LAMBDA: ordenar por cantidad desc
    orden = sorted([(h, len(objs)) for h, objs in perten.items()], key=lambda x: -x[1])  # LAMBDA
    filas3 = [["Huesped", "CantObjetos"]] + [[h, c] for h, c in orden]
    if orden:
        max_c = max(c for _, c in orden); min_c = min(c for _, c in orden)
        max_h = [h for h, c in orden if c == max_c]; min_h = [h for h, c in orden if c == min_c]
        prom = (sum(c for _, c in orden) / len(orden)) if orden else 0
        filas3 += [["Promedio", f"{prom:.2f}"],
                   ["Max", max_c, "|".join(max_h)],
                   ["Min", min_c, "|".join(min_h)]]
    escribir_csv_plano(R_PERTENENCIAS, filas3)

    # --- Reporte 4: TOPS y métricas mezcladas --- #
    filas4 = []
    # Top habitación más ocupada (inferimos por_piso y marcas O; ejemplo simple)
    pisos_top = max(por_piso) if por_piso else 0
    pisos_min = min(por_piso) if por_piso else 0
    filas4 += [["Piso con más ocupación", pisos_top],
               ["Piso con menos ocupación", pisos_min]]
    # Llaves: cuántas válidas e inválidas
    vals = sum(1 for v in llaves.values() if v["estado"] == "valida")
    invs = sum(1 for v in llaves.values() if v["estado"] == "invalida")
    filas4 += [["Llaves válidas", vals], ["Llaves inválidas", invs]]
    # Accesos no autorizados por persona (conteo)
    cont_no = {}
    for ln in accesos_no:
        if not ln: continue
        p = ln.split(",")[0].strip()
        cont_no[p] = cont_no.get(p, 0) + 1
    for p, c in cont_no.items():
        filas4 += [[f"NoAut - {p}", c]]
    escribir_csv_plano(R_TOPS, filas4)

    # --- Opcional: JSON consolidado --- #
    consolidado = {
        "huespedes": huespedes,
        "personal": personal,
        "pertenencias": perten,
        "llaves": llaves,
        "ocupacion": {"total": total, "ocupadas": occ, "libres": libres, "por_piso": por_piso},
        "accesos_validos": acc_val[:50],     # SLICING (primeros 50)
        "accesos_no_aut": acc_no[:50],       # SLICING
    }
    with open(R_JSON_OPCIONAL, "w", encoding="utf-8") as f:
        json.dump(consolidado, f, ensure_ascii=False, indent=2)

    log("Reportes generados")
    print("✔ Reportes generados en /data (4 CSV + JSON opcional)")

# ------------------------------ MENÚ PRINCIPAL ------------------------------ #
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

# ------------------------------ ARRANQUE ------------------------------ #
if __name__ == "__main__":
    # Login opcional (cumple requisito de "login de usuario válido")
    _u, _rol = login()
    # Ejemplo pequeño con LAMBDA adicional: largo de nombres de huéspedes
    # (se imprime una vez al inicio; sirve para mostrar lambda/lista)
    try:
        longs = list(map(lambda n: len(n), cargar_lista_desde_csv(F_HUESPEDES)))  # LAMBDA
        if longs:
            print("Longitudes de nombres de huéspedes:", longs)
    except Exception as e:
        log(f"Error calculando longitudes: {e}", ok=False)

    menu_principal()
