#SafeStay AR


import random

objetos=[]
habitantes=[]
cant=int(input("Ingrese la cantidad de habitantes"))

if cant>0:
    for k in range(cant):
        x=input("Ingrese el nombre del habitante")
        habitantes.append(x)
        print(habitantes)
else:
    print("error, debe haber por lo menos 1 habitante")

obj=int(input("Ingrese la cantidad de objetos para el checklist"))
if obj>0:
    for k in range(obj):
        y=input("Que objeto quiere añadir a la lista?")
        objetos.append(y)
        print(objetos)
        print("El checklist ha sido actualizado")
else:
    print("No se ha confeccionado una checklist")
        

llaveV=input("Desea generar una llave virtual? Tenga en cuenta que es valida por 1 minuto")

if llaveV=="si" or llaveV=="y":
    z=random.randint(1000,1000000)
else:
    print("Entendido, que tenga un buen dia!")
print("Su codigo es: ",z)
