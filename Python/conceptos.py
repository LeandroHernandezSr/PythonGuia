print("Hola mundo!")
#For
for x in range(101):
    print(x)
#While
x=0
while x<100:
    print(x)
    x=x+1
#Ingreso de datos
z=input("Ingrese su nombre:")
print("Su nombre es: "+z)
#Estructuras condicionales simples y compuestas
edad=input("Ingrese su edad: ")
if int(edad)<18:
    print("Es menor,no puede pasar")
else:
    print("Puede pasar")
#Listas
meses=["Enero","Febrero","Marzo","Abril"]
print(meses[1])
#Ingreso por teclado en lista
lista=[]
for x in range (5):
    valor=int(input("Ingrese un numero"))
    lista.append(valor)
#Recorrer una lista con for
for x in lista:
    print(x)
    
    
    