#se te encargo programar un contador que permita recibir una cantidad ejemplo: 10 y restar hasta que llegue a 0 
#debe ser capaz de reiniciarse sin tener que volver a ejecutarse 
#no debe recibir numeros igual o menor que 0
#debe utilizar un while (adicional intentar hacer que los numeros aparezcan de uno en uno)
#mostrar las cantidades en pantalla

#el import time es para el time.sleep()
import time

#inicio de while para auto reinicio
opcion=1
while opcion==1:
    cantidad = int(input("ingrese una cantidad para empezar el contador: "))

    if cantidad >0:
     while cantidad > -1 :
        print(cantidad)
        time.sleep(1)
        cantidad = cantidad -1      
   
    else: 
        print("no puedes poner cantidad iguales o menor que cero")
       
    print("quieres intentar nuevamente? 1 = si 2 = no: ")
    opcion=int(input())

print("cerrando contador, adioss")
