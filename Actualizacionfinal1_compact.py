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

FUNCIONALIDADES (6):
1) Registro de huéspedes y personal (ABM + login simple, sin POO, TXT plano)
2) Gestión de pertenencias de huéspedes (máx. 10; estadísticas: promedio, máx, mín)
3) Llaves virtuales de acceso (códigos aleatorios y estado/validez)
4) Matriz de habitaciones (L/O/M); asignación automática, cambio de habitación, estadísticas
5) Control de accesos (entradas/salidas, hora); alerta si no está registrado
6) Reportes finales (≥4 CSV + opcional JSON), con % y promedios

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
- Restricciones: sin POO, sin librerías externas (solo stdlib), sin usar 'csv' lib"""

import random 

def login(): 
    while True:
        usuario = input("Ingrese su nombre de usuario: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()

        if usuario == "" or contrasena == "":
            print("Usuario y contraseña no pueden estar vacíos, intente de nuevo.")
            continue

        return usuario, contrasena
    

def ipertenencias(listapertenencias):
    # validar cantidad de pertenencias
    while True:
        try:
            num_str = input("ingrese la cantidad de pertenencias (0-10): ").strip()
            if num_str == "":
                print("Entrada vacía, intente de nuevo.")
                continue

            num = int(num_str)

            if num < 0 or num > 10:
                print("Número inválido, intente de nuevo.")
                continue

            break
        except ValueError:
            print("valor no reconocido, ingrese un número entero")

    for i in range(num):
        while True:
            objeto = input(f"ingrese el nombre del objeto {i+1}: ").strip()
            if objeto == "":
                print("Nombre vacío, intente de nuevo.")
                continue
            if objeto in listapertenencias:
                print("Error, objeto ya existente. Ingrese otro objeto.")
                continue
            listapertenencias.append(objeto)
            break

    return listapertenencias


def llaves_virtuales():
    llave_resp = input("Desea generar una llave virtual? (s/n): ").strip().lower()
    if llave_resp == "s":
        llave_generada = random.randint(100000, 999999)
        print(f"Su llave virtual es: {llave_generada}")
    else:
        print("No se generará ninguna llave virtual.")
        llave_generada = None
    return llave_generada


def ihotel_1():
    print("======= MATRIZ HOTEL 1 =======")
    matriz = []
    for piso in range(10):
        habitaciones = []
        for habitacion in range(15):
            habitaciones.append("L")
        matriz.append(habitaciones)
    return matriz


def ihotel_2():
    print("======= MATRIZ HOTEL 2 =======")
    matriz = []
    for piso in range(10):
        habitaciones = []
        for habitacion in range(15):
            habitaciones.append("L")
        matriz.append(habitaciones)
    return matriz


def control_accesos():
    usuarios = {
        "admin": "1234",
        "recepcionista": "abcd",
        "cliente": "0000"
    }  # diccionario de usuarios y contraseñas

    intentos = 3
    while intentos > 0:
        print("\n=== CONTROL DE ACCESOS ===")
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuario in usuarios and usuarios[usuario] == contrasena:
            print(f"Acceso autorizado. Bienvenido, {usuario}.")
            return usuario  # acceso OK
        else:
            intentos -= 1
            print(f"Acceso denegado. Intentos restantes: {intentos}")

    print("Demasiados intentos. Acceso bloqueado.")
    return None  # acceso falló



# Generación de archivos de entrada (requisito del TP)

def generar_archivos_entrada():
    # 1) Lista de huéspedes simulada
    huespedes_fake = ["Juan Perez", "Ana Lopez", "Carlos Diaz", "Luisa Gomez", "Roberto Silva"]
    try:
        arch1 = open("entrada_huespedes.txt", "wt")
        for nombre in huespedes_fake:
            arch1.write(nombre + "\n")
        arch1.close()
    except IOError:
        print("No se pudo crear entrada_huespedes.txt")

    # 2) Lista de pertenencias simulada
    objetos_fake = ["valija", "notebook", "celular", "reloj", "billetera"]
    try:
        arch2 = open("entrada_pertenencias.txt", "wt")
        for obj in objetos_fake:
            arch2.write(obj + "\n")
        arch2.close()
    except IOError:
        print("No se pudo crear entrada_pertenencias.txt")

    # 3) Registros de accesos simulados
    # formato nombre;estado (OK o DENEGADO)
    try:
        arch3 = open("entrada_accesos.txt", "wt")
        for i in range(5):
            nombre_random = random.choice(["admin", "cliente", "intruso", "recepcionista"])
            estado = random.choice(["OK", "DENEGADO"])
            arch3.write(f"{nombre_random};{estado}\n")
        arch3.close()
    except IOError:
        print("No se pudo crear entrada_accesos.txt")

    print("Archivos de entrada generados: entrada_huespedes.txt, entrada_pertenencias.txt, entrada_accesos.txt")



# Generación de archivos de salida intermedios
# OJO: Vamos a generar 3 acá y el 4to es reportes_finales.txt

def generar_archivos_salida(total, listausuario, listapertenencias, llave_generada):
    # salida_resumen_usuarios.txt
    try:
        out1 = open("salida_resumen_usuarios.txt", "wt")
        out1.write("=== RESUMEN DE USUARIOS REGISTRADOS ===\n")
        out1.write(f"Cantidad total de usuarios declarada: {total}\n")
        out1.write(f"Nombres cargados manualmente: {listausuario}\n")
        out1.close()
    except IOError:
        print("No se pudo crear salida_resumen_usuarios.txt")

    # salida_resumen_pertenencias.txt
    try:
        out2 = open("salida_resumen_pertenencias.txt", "wt")
        out2.write("=== RESUMEN DE PERTENENCIAS ===\n")
        out2.write(f"Cantidad total de pertenencias declaradas: {len(listapertenencias)}\n")
        out2.write(f"Listado completo: {listapertenencias}\n")

        # usamos slicing otra vez para grabar solo las primeras 3 pertenencias
        primeras_tres = listapertenencias[:3]
        out2.write(f"Primeras tres pertenencias (slicing): {primeras_tres}\n")

        out2.close()
    except IOError:
        print("No se pudo crear salida_resumen_pertenencias.txt")

    # salida_llaves.txt
    try:
        out3 = open("salida_llaves.txt", "wt")
        out3.write("=== LLAVES VIRTUALES GENERADAS ===\n")
        out3.write(f"Llave activa en sesión: {llave_generada}\n")
        if llave_generada is None:
            out3.write("Nota: El usuario decidió no generar llave virtual.\n")
        else:
            out3.write("Nota: Llave aleatoria válida asignada.\n")
        out3.close()
    except IOError:
        print("No se pudo crear salida_llaves.txt")

    print("Archivos de salida generados: salida_resumen_usuarios.txt, salida_resumen_pertenencias.txt, salida_llaves.txt")


def reportes_finales(num_str, listausuario, listapertenencias, llave):
    try:
        arch = open("reportes_finales.txt", "wt")

        arch.write("Reportes Finales del Hotel\n")
        arch.write("============================\n")
        arch.write("1. Registro de huéspedes y personal:\n")
        arch.write(f"La cantidad de usuarios es: {num_str} y sus nombres son: {listausuario}\n")
        
        primeras_pertenencias = listapertenencias[:3]  # Esto es un ejemplo de SLICING que muestra solo las primeras 3 pertenencias si hay muchas
        
        arch.write("2. Gestión de pertenencias de huéspedes:\n")
        arch.write(f"La cantidad de pertenencias es: {len(listapertenencias)} y sus nombres son: {primeras_pertenencias}\n")
        arch.write("3. Llaves virtuales de acceso:\n")
        arch.write(f"La llave creada aleatoriamente es: {llave}\n")
        
        contar_total = lambda matriz: sum(len(fila) for fila in matriz) # cuenta total de habitaciones y es una función lambda
        total_habitaciones = contar_total(ihotel_1()) + contar_total(ihotel_2())
        
        arch.write("4. Matriz de habitaciones:\n")
        arch.write(f"Matriz Hotel 1:\n{ihotel_1()}\n")
        arch.write(f"Matriz Hotel 2:\n{ihotel_2()}\n")
        arch.write(f"Total de habitaciones entre ambos hoteles: {total_habitaciones}\n")

        arch.write("5. Control de accesos:\n")
        arch.write("El control de accesos se realizó antes de permitir el uso del sistema.\n")
        arch.write("============================\n")

        arch.close()
        print("Reportes generados en 'reportes_finales.txt'.")
    except IOError:
        print("Imposible crear archivo de reportes finales")


def menu_principal(num, listausuario, listapertenencias, llave_generada):
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registro de huéspedes y personal")
        print("2. Gestión de pertenencias de huéspedes")
        print("3. Llaves virtuales de acceso")
        print("4. Matriz de habitaciones")
        print("5. Reportes finales")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()
        if opcion not in {"1", "2", "3", "4", "5", "6"}:
            print("Opción no válida. Intente nuevamente.")
            continue

        try:
            if opcion == "1":
                crear_usuario()

            elif opcion == "2":
                listapertenencias.clear()
                ipertenencias(listapertenencias)
                print("Pertenencias registradas:", listapertenencias)

            elif opcion == "3":
                llave_generada = llaves_virtuales()

            elif opcion == "4":
                h1 = ihotel_1()
                print("Matriz Hotel 1 creada.")
                print(h1)
                h2 = ihotel_2()
                print("Matriz Hotel 2 creada.")
                print(h2)

            elif opcion == "5":
                print("Generando reportes finales...")
                reportes_finales(num, listausuario, listapertenencias, llave_generada)

            elif opcion == "6":
                print("Saliendo del sistema. Adiós.")
                break

        except Exception as e:
            print("Ocurrió un error, intente de nuevo.")


def crear_usuario():
    while True:
        try:
            user = input("Usted desea crear un usuario? (s/n): ").strip().lower()
            if user == "s":
                usuario, contrasena = login()
                if usuario and contrasena:
                    print(f"Usuario creado: {usuario}")
            elif user == "n":
                print("No se creará ningún usuario.")
            else:
                print("Opción no válida, intente de nuevo.")
            break
        except Exception as e:
            print(f"Error: {e}")


def ipersonas(listausuario):
    while True:
        try:
            num_str = input("Ingrese la cantidad de personas a registrar (0 para none): ").strip()
            if num_str == "":
                print("Entrada vacía, intente de nuevo.")
                continue

            num_str = int(num_str)
            if num_str < 0:
                print("Número inválido, intente de nuevo.")
                continue

            for k in range(num_str):
                while True:
                    usuario, contrasena = login()  # login solo valida campos no vacíos

                    if usuario == "":
                        print("Nombre vacío, intente de nuevo.")
                        continue
                    
                    if usuario in listausuario:
                        print("Error, usuario ya existente. Ingrese otro usuario.")
                        continue

                    listausuario.append(usuario)
                    break  # usuario agregado correctamente, pasar al siguiente

            return num_str, listausuario  # se completó el ingreso de personas sin errores

        except ValueError:
            print("valor no reconocido, ingrese un número entero")


def main(intentos = 3):
    # 1) Generamos los archivos de ENTRADA que pide la consigna
    generar_archivos_entrada()

    listausuario = []

    # preguntar creación de usuario inicial
    while True:
        crear = input("Usted desea crear un usuario? (s/n): ").strip().lower()
        if crear in ("s", "n"):
            break
        print("Opción no válida, intente de nuevo.")

    creado = False
    if crear == "s":
        usuario, contrasena = login()
        if usuario == "":
            print("Nombre vacío, no se creó usuario.")
        elif usuario in listausuario:
            print("Error, usuario ya existente. No se agregará.")
        else:
            listausuario.append(usuario)
            print(f"Usuario creado: {usuario}")
            creado = True

    # registrar el resto de personas
    num, listausuario = ipersonas(listausuario)

    # mostrar resultado total
    if creado:
        total = num + 1
        print(f"Se registraron {total} usuario(s).")
    else:
        total = num
        print(f"Se registraron {total} usuario(s).")

    # === CICLO PRINCIPAL DEL SISTEMA ===
    while True:
        acceso = control_accesos()

        if not acceso:
            print("No tiene permiso para continuar. Programa finalizado.")
            break  # salimos del while True y con eso termina main()

        else:
            print("Entrando al sistema...")

            listapertenencias = []
            ipertenencias(listapertenencias)

            llave_generada = llaves_virtuales()

            h1 = ihotel_1()
            opa = input("Desea ver la matriz del hotel 1? (s/n): ").strip().lower()
            if opa == "s":
                print(h1)
            
            h2 = ihotel_2()
            opa1 = input("Desea ver la matriz del hotel 2? (s/n): ").strip().lower()
            if opa1 == "s":
                print(h2)

            # 2) Generamos los archivos de SALIDA intermedios
            generar_archivos_salida(total, listausuario, listapertenencias, llave_generada)

            # 3) Menú y luego reporte final (4to archivo de salida)
            menu_principal(total, listausuario, listapertenencias, llave_generada)

            reportes_finales(total, listausuario, listapertenencias, llave_generada)

            # IMPORTANTE: agregamos esta pregunta para SALIR del while True
            salir = input("¿Desea salir del sistema? (s/n): ").strip().lower()
            if salir == "s":
                print("Saliendo del sistema. Adiós.")
                break
            else:
                print("Reiniciando sesión...\n")
                # vuelve a pedir control_accesos() al inicio del while


if __name__ == "__main__":
    main()
