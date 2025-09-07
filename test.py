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
    if huesped in listaHuesped:                                              # Verifica si el huesped esta repetido
        aux=huesped
        huesped=input(f"el huésped '{huesped}' ya existe en el registro, ingrese nuevamente ")
        if huesped!=aux:
            listaHuesped.append(huesped)
    else:
        listaHuesped.append(huesped)

print("lista de huéspedes:")
print(listaHuesped)

# Gestión de pertenencias de huéspedes
listaobjetos = []  # Lista para almacenar las pertenencias de cada huésped

for k in range(len(listaHuesped)): #optimizar en el caso de que pongan n, asi solo skipea el huesped y no la lista entera
    question1=input(f"armar checklist para objetos para el huesped {k+1}?(y/n)")
    if question1=="y":
        objetos=int(input(f"ingrese la cantidad de objetos en la checklist del huesped {k+1}: "))
        for x in range(objetos):
            aux=input(f"ingrese el {x+1} objeto")
            listaobjetos.append(aux)
    else:
        print(f"no ha creado una checklist para el huesped {k+1}")

matrizOC=[ #roto, solo toma splits y cosas como [juan,toto,maria],[obj1,obj2,obj3],etc. no accepta listas como lo puse
    [listaHuesped]
    [listaobjetos]
]
for k in range(len(listaHuesped)):
    for x in range(len(listaobjetos)):
        print(f"huesped {listaHuesped[k]}, objetos {listaobjetos[x]}")
