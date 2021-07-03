#Programa para dividir los integrantes de un grupo
#En el grupo A estan las mujeres siempre y cuando la letra inicial de su nombre este antes de la m
#En el grupo A estan los hombres siempre y cuando la letra inicial de su nombre este despues de la n

#El resto esta en el grupo B
nameUsu=input("Ingresa Tu nombre: ")
sexUsu=input("Ingresa tu sexo M/F: ")

if(sexUsu=="F" and nameUsu.lower()< 'm') or (sexUsu== "M" and nameUsu.lower()>'n'):
    grupo="A"
else:
    grupo="B"
print("Tu grupo es: "+grupo)

#Fin del programa

#Condicional if
if 10>10:
    print("False")
elif 9==9:
    print("True")
else:
    print("Esta es la estructura de las condicionales")
#Condicionales

#Ciclos
#Ciclo for
for i in range(10):
    print("a")
#fin cilo for

#cilco for con incremento
edad=int(input("Cual es tu edad? "))
for i in range(edad):
    print("Has cumplido "+str(i+1)+" Años")
#Fin ciclo for con incremento
#Imprimir numeros impares
n=int(input("ingresa un numero positivo: "))
for i in range(1,n+1,2):
    print(i, end=", ")
#Final de ejercicio
#Ciclo for para calcular ganancias con porcentaje anual
inv=float(input("¿Cantidad a invertir? "))
inter=float(input("¿Interes porcentual anual? "))
years=int(input("¿Tiempo en años de la inversion? "))

for i in range(years):
   inv *= 1+inter/100
   print("Capital tras " +str(i+1)+ " años: "+str(round(inv,1)))
#fin del ejercicio
#imprimir un pino de un tamaño dado por el usuario
v=int(input("Tamaño de ciclo: "))
for i in range(v):
   print("*"*(i+1))
#fin del ejercicio
#Elabora un triangulo formado con los numeros inpares tomando un numero introducido por el usuario
n=int(input("Numero entero:"))
for i in range(1,n+1,2):
    for j in range(i,0,-2):
        print(j, end=" ")
    print("")
#Fin del ejercicio.
#Validar si las contraseñas coinciden, en base a una almacenada en una variable.
pas="Password"
val=str(input("Escriba la contraseña: "))
while val != pas:
    val=str(input("Contraseña incorrecta"))
print("Contraseña correcta")
#Fin del ejercicio.
#Valida si el numero ingresado es par o impar (si el numero ingresado es impar vuelve a solicitar un valor, hasta que se ingrese un valor par)
v=int(input(""))
i=2
while v%i!=0:
    print("El valor es impar")
    v=int(input(""))
print("El valor es par")
#Fin del ejercicio
#Lee una palabra ingresada por el usuario, para despues colocarla letra por letra de manera inversa.
p=input("Ingresa una palabra: ")
for i in range(len(p)-1,-1,-1):
    print(p[i])
#Fin del ejercicio.
#Lee una oracion ingresada por el usuario, para despues contar las veces que se repite una letra dada tambien dada por el usuario
f=input("Ingresa una frase")
l=input("Ingresa una letra:")
contador=0

for i in f:
    if i==l:
        contador+=1
print("La letra '%s' aparece '%2i' veces en la frase '%s'"%(l,contador,f))
#Fin del ejercicio.
#Le palabras de forma repetitiva hasta que el usuario escriba la palabra correcta para detenerse.
while True:
    f=input("Ingresa una palabra: ")
    if f=="salir":
        break
    print(f)
#Fin del ejercicio
#Creacion de listas
materias=["Español","Matematicas","Ciencias"]
print(Materias)
#Fin del Ejemplo
#Lista de materias, que mediante un ciclo for, escribe "yo estudio + mas la materia correspondiente dependiendo la posicion del ciclo"
m=["Español","Matematicas","Fisica"]
for m in m:
    print("Yo estudio " + m)
#Fin del ejercicio.
#Pregunta las calificaciones sacadas en las materias pre definidas, para despues imprimir la materia con su respectiva calificacion
materias= ["Español","Matematicas","Fisica","Quimica"]
notas=[]
for materia in materias:
    nota=input("Cual es tu calificacion en "+materia+ " ")
    notas,append(nota)
for i in range(len(materias)):
    print("En " +materias[i]+ " has sacado "+notas[i])
#Fin del ejercicio
#Capturar numeros ganadores de la loteria en un arreglo y despues de terminar de capturar ordenarlos de menor a mayor
num=[]
while True:
   nums=input("What is the winning number: ")
   num.append(nums)
   f=input("¿Finished Y/N")
   if f=="Y":
      break
   num.sort()
   
print("The winning numbers are:")
print(num)
#Fin del ejercicio
#Capturar 10 numeros y colocarlos en una lista para mostrarlos de mayor a menor 
num=[]
fin=10
for i in range(fin):
    nums=input("Insert a list of ten numbers: ")
    num.append(nums)

num.sort(reverse=True)
print("The list of numbers order by reverse: ")
print(num)
#Fin del ejercicio
#Capturar la calificacion obtenida en una lista de materias predefinidas y sacar de la lista la materia aprobada
#Para despues mostrar solo las materias reprobadas
materia=["Español","Matematicas","Fisica","Ingles"]
aprobadas=[]

for materia in materias:
    nota=float(input("¿Que nota sacaste en "+mateira+" ? "))
    if nota >=5:
        aprobadas.append(materia)
for materia in aprobadas:
    materias.remove(materia)
print("Tienes que repetir "+str(materias))
#Fin del ejercicio
#Colocar todas las letras del abecedario en una lista, para eliminar de la lista
#las letras que ocupen una posicion multiple de 3 y al final mostrar la lista final
letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=3
for letra in range(len(letras),1,-1):
    if letra%i==0:
        letras.pop(letra-1)
print(letras)
#Fin del ejercicio 
#Ingresar una palabra, para luego comparar si escrita al reves dice lo mismo
pa=input("Ingresa una palabra ")
def reverse(pa):
    return ' '.joind(list(map(lambda x: x[::-1], pa.split())))
if(reverse(pa)!=pa):
    print("Esta palabra no es polindromo")
else:
    print("Esta palabra es polindromo")
#Fin del ejercicio
#Ingresar una palabra y contar las veces que se repite las vocales dentro de ella
#Primera opcion
palabra=input("Ingresa una palabra: ")
voa=palabra.count("a")
voA=palabra.count("A")
suma=voa+voA
voe=palabra.count("e")
voE=palabra.count("E")
sume=voe+voE
voi=palabra.count("i")
voI=palabra.count("I")
sumi=voi+voI
voo=palabra.count("o")
voO=palabra.count("O")
sumo=voo+voO
vou=palabra.count("u")
voU=palabra.count("U")
sumu=vou+voU

if voa!=0:
   print("La palabra repite: "+str(suma)+" la letra a")
if voe!=0:
   print("La palabra repite: "+str(sume)+" la letra e")
if voi!=0:
   print("La palabra repite: "+str(sumi)+" la letra i")
if voo!=0:
   print("La palabra repite: "+str(sumo)+" la letra o")
if vou!=0:
   print("La palabra repite: "+str(sumu)+" la letra u")
#Nota: Cuentas todas las vocales repetidas sin importar si es mayuscula o minuscula
#Fin del ejercicio 
#Ingresar una palabra y contar las veces que se repite las vocales dentro de ella
#Segunda ocpion
palabra=input("Ingresa una pabalra: ")
vocales=["a","e","i","o","u"]

for vocal in vocales:
    cant=0
    for letra in palabra:
        if letra == vocal:
            cant+=1
    print ("La vocal "+vocal+" aparece "+ str(cant)+" veces")
#Nota: Cuenta todad las letras vocales repetidas solo minusculas
#Fin del ejercicio
#De un arreglo con precios extraer el menor y mayor para despues imprimirlos
numeros=['50','75','46','22','80','65','08']
menor=min(numeros)
print("El preciio menor es: "+str(menor))
mayor=max(numeros)
print("El precio mayor es: "+str(mayor))
#Fin del ejercicio
#Sacar el producto de los matrices predefinidas.
a=(1,2,3)
b=(-1,0,2)
res=0
for i in range(len(a)):
    res+= a[i]*b[i]
print("El producto de los vectores: "+str(a)+" y "+str(b)+" es: "+str(res))
#Fin del ejercicio
#Sacar el producto de matrices anidadas
a=((1,2,3),
   (4,5,6))

b=((-1,0),
   (0,1),
   (1,1))

res=[[0,0],
     [0,0]]
for i in range(len(a)):
    
    for n in range(len(b[0])):

        for j in range(len(b)):
            res[i][n]+=a[i][j]*b[j][n]

for i in range(len(res)):
    res[i]=tuple(res[i])

res=tuple(res)

for i in range(len(res)):
    print(res[i])
#Fin del ejercicio