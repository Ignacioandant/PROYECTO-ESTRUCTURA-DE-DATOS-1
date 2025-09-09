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
import random

def estadisticas_pertenencias(matrizOC):
    resumen = [(fila[0], len(fila[1])) for fila in matrizOC] #lista=[x,y] x= entra a la lista de nombres y= la cantidad de objetos en la lista de objetos

    total_huespedes = len(resumen)
    total_objetos = sum(c for _, c in resumen)
    promedio = total_objetos / total_huespedes if total_huespedes > 0  else 0

    max_cantidad = max(c for _, c in resumen) #ignora el nombre y toma la cantidad
    min_cantidad = min(c for _, c in resumen)

    huespedes_max = [n for n, c in resumen if c == max_cantidad]
    huespedes_min = [n for n, c in resumen if c == min_cantidad]

    print("=== Estadísticas de pertenencias ===")
    print(f"Total de huéspedes: {total_huespedes}")
    print(f"Total de objetos registrados: {total_objetos}")
    print(f"Promedio de pertenencias por huésped: {promedio:.2f}\n")

    print(f"Máximo de pertenencias: {max_cantidad}")
    print("Huésped(es) con máximo de pertenencias:")
    for h in huespedes_max:
        print(" -", h)
    print()

    print(f"Mínimo de pertenencias: {min_cantidad}")
    print("Huésped(es) con mínimo de pertenencias:")
    for h in huespedes_min:
        print(" -", h)


#parte 1
listaHuesped=[]
listaPersonal=[]

Cpersonal=int(input("ingrese la cantidad de personal presente ")) #ingreso de cantidad de personal
for k in range(Cpersonal):
    personal=input(f"ingrese el nombre y apellido del personal registrado {k+1}: ")
    if personal in listaPersonal:                                            #verifica si el personal esta repetido
        aux=personal
        personal=input(f"el personal '{personal}' ya existe en el registro de empleados, ingrese nuevamente")
        if personal!=aux:
            listaPersonal.append(personal)
    else:
        listaPersonal.append(personal)

print("lista de personal del dia")
print(listaPersonal)


Chuesped = int(input("ingrese cuántos huéspedes: ")) #ingreso de cantidad de huespedes
for k in range(Chuesped):
    huesped = input(f"ingrese el nombre del huésped {k+1}: ")
    if huesped in listaHuesped:                      # Verifica si el huesped esta repetido
        aux=huesped
        huesped=input(f"el huésped '{huesped}' ya existe en el registro, ingrese nuevamente ")
        if huesped!=aux:
            listaHuesped.append(huesped)
    else:
        listaHuesped.append(huesped)

print("lista de huéspedes:")
print(listaHuesped)

#parte 2
matrizOC = []  #[nombre del huesped, [objetos]]

for k in range(len(listaHuesped)):
    listaObjetos_huesped = []
    question1 = input(f"¿Armar checklist para objetos del huésped {listaHuesped[k]}? (y/n): ")

    if question1.lower() == "y": #lower esta asi toma siempre la y incluso si esta mayuscula
        objetos = int(input(f"Ingrese la cantidad de objetos para {listaHuesped[k]} (máx 10): "))

        for x in range(min(objetos, 10)): #solidifica que si o si sea 10 el limite
            aux = input(f"Ingrese el objeto {x+1}: ")
            listaObjetos_huesped.append(aux)
    else:
        print(f"No se creó checklist para el huésped {listaHuesped[k]}")

    matrizOC.append([listaHuesped[k], listaObjetos_huesped]) #como cualquier otra lista

print("\n=== MATRIZ DE HUESPEDES Y OBJETOS ===")
for fila in matrizOC:
    print(f"Huésped: {fila[0]} - Objetos: {fila[1]}")

estadisticas_pertenencias(matrizOC) #llamada del def para la matrizOC para estadisticas

#parte 3
#LLave virtual
def generar_llave():
    llave = random.randint(1000, 9999)
    return llave


llave_virtual = str(input("Deseea solicitar su llave virtual? (si/no): "))
if llave_virtual.lower() == "si":
    print("Su llave virtual es: ", generar_llave())
elif llave_virtual.lower() == "no":
    print("No se generó ninguna llave virtual.")
else:
    print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
    llave_virtual = str(input("Deseea solicitar su llave virtual? (si/no): "))


#parte 4
print("\n=== Sistema de habitaciones ===")

pisos=int(input("Ingrese la cantidad de pisos del hotel (1-8): "))
habitaciones_por_piso=int(input("Ingrese la cantidad de habitaciones por piso:"))


matrizHabitaciones=[]
for i in range(pisos):
    fila=[]
    for j in range(habitaciones_por_piso):
        fila.append("L") #libre
    matrizHabitaciones.append(fila)


asignaciones=[] #lista para ver si ya se la asigno una habitacion al huesped


for k in range(len(listaHuesped)):
    huesped=listaHuesped[k]
    asignaciones_habitacion=[]  # vacía si no se asignó
    for i in range(pisos):
        for j in range(habitaciones_por_piso):
            if matrizHabitaciones[i][j]=="L" and len(asignaciones_habitacion)==0:
                matrizHabitaciones[i][j]="O"
                asignaciones_habitacion.append(i)
                asignaciones_habitacion.append(j)
                asignaciones.append([huesped, i, j])
                print(f"Huésped {huesped} asignado a Piso {i+1}, Habitación {j+1}")
    if len(asignaciones_habitacion)==0:
        print(f"No hay habitaciones libres para el huésped {huesped}")


print("\nEstado actual de las habitaciones (L=Libre, O=Ocupada):")
for i in range(pisos):
    print(f"Piso {i+1}: ",matrizHabitaciones[i])

# Estadísticas de ocupación
total_habitaciones=pisos*habitaciones_por_piso
ocupadas=0
libres=0

for i in range(pisos):
    for j in range(habitaciones_por_piso):
        if matrizHabitaciones[i][j]=="O":
            ocupadas=ocupadas+1
        elif matrizHabitaciones[i][j]=="L":
            libres=libres+1

print("\n=== Estadísticas de ocupación ===")
print(f"Total de habitaciones: {total_habitaciones}")
print(f"Libres: {libres} ({libres/total_habitaciones*100:.2f}%)")
print(f"Ocupadas: {ocupadas} ({ocupadas/total_habitaciones*100:.2f}%)")


# Número máximo y mínimo de ocupación por piso
ocupacion_por_piso = []

for i in range(pisos):
    contador=0
    for j in range(habitaciones_por_piso):
        if matrizHabitaciones[i][j]=="O":
            contador=contador+1
    ocupacion_por_piso.append(contador)

max_personas_piso=max(ocupacion_por_piso)
min_personas_piso=min(ocupacion_por_piso)

print("\n=== Personas por piso ===")
for i in range(pisos):
    print(f"Piso {i+1}: {ocupacion_por_piso[i]} personas")
print(f"Máximo de personas en un piso: {max_personas_piso}")
print(f"Mínimo de personas en un piso: {min_personas_piso}")


# parte 5 - Control de accesos

# Esta sección registra las entradas y salidas de huéspedes y personal, guardando quién realizó la acción, el tipo de persona (huésped/personal),
#la fecha y hora exacta. Si alguien intenta ingresar o salir sin estar previamente registrado, el sistema genera una alerta y guarda el intento como
#acceso no autorizado. Además, se muestra un historial completo de accesos válidos y de intentos rechazados.

accesos = []  # accesos válidos
intentos_no_autorizados = []  # intentos inválidos

def registrar_acceso(persona: str, accion: str):
    """ Registra un acceso (entrada/salida) con hora, minuto y segundo aleatorios. """
    global accesos, intentos_no_autorizados
    accion = accion.strip().lower()
    if accion not in ("entrada", "salida"):
        print("Acción inválida. Use 'entrada' o 'salida'.")
        return

    # Hora aleatoria
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)

    if persona in listaHuesped:
        accesos.append({
            "persona": persona,
            "tipo": "Huésped",
            "accion": accion,
            "hora": hora,
            "minuto": minuto,
            "segundo": segundo
        })
        print(f"Acceso registrado: {persona} (Huésped) -> {accion} | {hora:02d}:{minuto:02d}:{segundo:02d}") #02 es para que sean 2 digitos y la d es para que sean numeros redondos
    elif persona in listaPersonal:
        accesos.append({
            "persona": persona,
            "tipo": "Personal",
            "accion": accion,
            "hora": hora,
            "minuto": minuto,
            "segundo": segundo
        })
        print(f"Acceso registrado: {persona} (Personal) -> {accion} | {hora:02d}:{minuto:02d}:{segundo:02d}")
    else:
        intentos_no_autorizados.append({
            "persona": persona,
            "accion": accion,
            "hora": hora,
            "minuto": minuto,
            "segundo": segundo
        })
        print(f"ALERTA: acceso no autorizado para '{persona}' | {hora:02d}:{minuto:02d}:{segundo:02d}")
        
while True:
    registrar = input("\n¿Desea registrar un acceso? (si/no): ").strip().lower()
    if registrar != "si":
        break
    persona = input("Nombre y apellido de la persona: ").strip()
    accion = input("Acción (entrada/salida): ").strip()
    registrar_acceso(persona, accion)

# Reportes finales
print("\n=== Historial de accesos válidos ===")
if not accesos:
    print("No se registraron accesos válidos.")
else:
    for i, a in enumerate(accesos, start=1):
        print(f"{i}. {a['hora']:02d}:{a['minuto']:02d}:{a['segundo']:02d} - {a['tipo']}: {a['persona']} - {a['accion']}")

print("\n=== Intentos de acceso no autorizados ===")
if not intentos_no_autorizados:
    print("No hubo intentos no autorizados.")
else:
    for i, a in enumerate(intentos_no_autorizados, start=1):
        print(f"{i}. {a['hora']:02d}:{a['minuto']:02d}:{a['segundo']:02d} - Persona: {a['persona']} - Intento: {a['accion']}")
#punto 6


def reportes_finales(listaHuesped, listaPersonal, matrizHabitaciones, matrizOC, accesos, accesos_no_autorizados):
    print("\n========== REPORTES FINALES ==========\n")

    # Listado de huéspedes con sus pertenencias
    print("Huéspedes, sus pertenencias y número de habitación:")
    for i, (huesped, objetos) in enumerate(matrizOC):
        hab_asignada = None
        for piso in range(len(matrizHabitaciones)):
            for hab in range(len(matrizHabitaciones[piso])):
                if matrizHabitaciones[piso][hab] == "O":  # ocupada
                    hab_asignada = f"Piso {piso+1}, Habitación {hab+1}"
                    break
            if hab_asignada:
                break
        print(f"- {huesped}: {objetos} | Habitación: {hab_asignada}")
    print()

    # Listado de personal
    print("Personal registrado:")
    for p in listaPersonal:
        print("-", p)
    print()

    # Estado de habitaciones
    total = sum(len(fila) for fila in matrizHabitaciones)
    ocupadas = sum(fila.count("O") for fila in matrizHabitaciones)
    libres = sum(fila.count("L") for fila in matrizHabitaciones)
    mantenimiento = sum(fila.count("M") for fila in matrizHabitaciones)

    print("Estado de habitaciones:")
    print(f"Ocupadas: {ocupadas} ({ocupadas/total*100:.2f}%)")
    print(f"Libres: {libres} ({libres/total*100:.2f}%)")
    print(f"En mantenimiento: {mantenimiento} ({mantenimiento/total*100:.2f}%)")
    print()

    # Historial de accesos
    print("Historial de accesos:")
    for acc in accesos:
        print("-", acc)
    print()

    # Intentos no autorizados
    print("Intentos de acceso no autorizados:")
    for intento in accesos_no_autorizados:
        print("-", intento)
    print()

    # Estadísticas adicionales (ejemplo: ocupación y personas por piso)
    print("Estadísticas adicionales:")
    print(f"Porcentaje de ocupación: {(ocupadas/total*100):.2f}%")

    for piso, fila in enumerate(matrizHabitaciones):
        personas = fila.count("O")  # suponiendo 1 persona por habitación ocupada
        print(f"Piso {piso+1}: {personas} personas")
    print("=====================================\n")