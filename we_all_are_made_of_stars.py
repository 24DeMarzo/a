#“We all are made of stars (WAAMOS)”
#Interfaz 80 caracteres de Largo y 20 de Ancho
import random 
my_list = [" "," "," ","´"," ","*"," "," "] #Lista 0,1,2,3,4,5,6,7
for i in range (20):
    for i in range (80):
        x=random.randint(0,7) #Funcion que elige un numero aleatorio entre 0 y 6
        print (my_list[x],end="")
    print ("\n",end="")