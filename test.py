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
Porcentaje de habitaciones ocupadas, libres y en mantenimiento.
Número máximo y mínimo de cantidad de personas en cada habitación y pisos.

5. Control de accesos
Se almacenará una lista de accesos realizados (entradas y salidas).
Cada acceso deberá registrar: huésped/persona, acción (entrada o salida), fecha y hora.
Si se intenta ingresar sin estar registrado, el sistema generará una alerta de acceso no autorizado.

6. Reportes finales
Al finalizar la ejecución, el sistema deberá mostrar:
El listado de huéspedes con sus pertenencias y número de habitación.
El listado del personal registrado.
El estado de la matriz de habitaciones (ocupadas, libres y en mantenimiento), indicando el total de cada tipo y los porcentajes.
El historial de accesos realizados con fecha y hora.
El listado de intentos de acceso no autorizados.
Estadísticas adicionales:
Porcentaje de ocupación de habitaciones.
Número máximo y mínimo de personas en cada habitación y pisos.
"""
import random

def estadisticas_pertenencias(matrizOC):
    resumen = [(fila[0], len(fila[1])) for fila in matrizOC]

    total_huespedes = len(resumen)
    total_objetos = sum(c for _, c in resumen)
    promedio = total_objetos / total_huespedes if total_huespedes > 0 else 0

    max_cantidad = max(c for _, c in resumen)
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

    matrizOC.append([listaHuesped[k], listaObjetos_huesped])

print("\n=== MATRIZ DE HUESPEDES Y OBJETOS ===")
for fila in matrizOC:
    print(f"Huésped: {fila[0]} - Objetos: {fila[1]}")

estadisticas_pertenencias(matrizOC) #llamada del def para la matrizOC

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
