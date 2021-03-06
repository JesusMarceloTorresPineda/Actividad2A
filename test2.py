from random import randint
from tkinter import *
import random
import math 
import matplotlib.pyplot as plt
import numpy as np


paquete1=[]
paquete2=[]
paquete3=[]
paquete4=[]
paquete5=[]
initial_population=[]
aux=[]
packages=[]
paquetesElegidos=0
choosenPackages=[]
all_fitness=[]
mejorfit_gen=[]
peorfit_gen=[]
promfit_gen=[]
prob_wheel_roulette=[]
aux_fitness=[]
paquetes_a_enviar=[]
send_package=[]
requerido=[]
losMejoresGen=[]
envio=[]
Send_to=[]

def seleccion(initial_population):
    global aux_fitness
    aux_fitness=[]
    retorno_gen=[]
    suma_fitness = 0
    prom_fitness= 0
    evaluar_esto=[]
    z=0

    for x in initial_population:
        auxiliar= initial_population[z]
        sumaCostos=0
        for y in auxiliar:
            sumaCostos += y[0]
        z+=1
        aux_fitness.append(sumaCostos)
        evaluar_esto.append([x, sumaCostos])

    
    suma_fitness=sum(aux_fitness)
    prom_fitness=suma_fitness/(len(initial_population))
    print("suma fitness " ,suma_fitness)
    print("promedio fitness " , prom_fitness)
    print("maximo fitness " , max(aux_fitness))
    the_best=[]
    for chin in evaluar_esto:
        if len(the_best)==0 or len(the_best) == 1:
            the_best.append(chin)
        else:
            for sc in range(len(the_best)):
                if(the_best[sc][1]<chin[1]):
                    the_best[sc] = chin
                    break
    retorno_gen.append(the_best[0][0])
    retorno_gen.append(the_best[1][0])
    
    

    if(the_best[0][1]>the_best[1][1]):
        send_package.append(the_best[0][1])
        envio.append(the_best[0][0])
    else:
        send_package.append(the_best[1][1])
        envio.append(the_best[1][0])

    minimo_gen=min(aux_fitness)
    peorfit_gen.append(minimo_gen)
    promfit_gen.append(prom_fitness)
    send_package.sort()
    
    return retorno_gen

def crossover(datos):
    puntoCorte1=randint(1,len(datos[0])-1)
    puntoCorte2=randint(1,len(datos[1])-1)
    valor1 = datos[0]
    valor2 = datos[1]
    entran = datos
    mitaduno1 = valor1[:puntoCorte1]
    mitaduno2 = valor1[puntoCorte1:]

    mitadDos1 = valor2[:puntoCorte2]
    mitadDos2 = valor2[puntoCorte2:]

    hijo1=[]
    hijo2=[]
    hijitos=[]

    hijo1.extend(mitaduno1)
    hijo1.extend(mitadDos2)

    hijo2.extend(mitadDos1)
    hijo2.extend(mitaduno2)

    hijitos.append(hijo1)
    hijitos.append(hijo2)
    data_returned = validate_weight(hijitos, entran)

    return data_returned

def mutation(datos):
    indice=0
    for a in datos:
        ans = bool(random.getrandbits(1))
        if ans:
            for y in range(len(a)):
                if bool(random.getrandbits(1)):
                    peso = datos[indice][y][1]
                    indexPackage = random.randint(1, peso)
                    newPackage = obtener_Paquete(indexPackage)
                    datos[indice][y] = newPackage   
                else:
                    pass
        indice+=1
    return datos

def obtener_Paquete(indice):
    global requerido
    value=0
    for i in packages:
        peso=i[1]
        if(indice == peso):
            requerido=i
        else:
            value+=1
    return requerido

def validate_weight(hijitos, datos):
    hijos_returned=[]
    valor1=hijitos[0]
    valor2=hijitos[1]
    sumValor1=0
    sumValor2=0
    for d in valor1:
        sumValor1+=d[1]
    for e in valor2:
        sumValor2+=e[1]
    if sumValor1 > tamanioContenedor:
        while sumValor1 > tamanioContenedor:

            puntoCorte1=randint(1,len(datos[0])-1)
            puntoCorte2=randint(1,len(datos[1])-1)
            valor1 = datos[0]
            valor2 = datos[1]

            mitaduno1 = valor1[:puntoCorte1]
            mitaduno2 = valor1[puntoCorte1:]

            mitadDos1 = valor2[:puntoCorte2]
            mitadDos2 = valor2[puntoCorte2:]

            hijo1=[]
            hijo2=[]

            hijo1.extend(mitaduno1)
            hijo1.extend(mitadDos2)

            auxvalor1=0
            for d in hijo1:
                auxvalor1+=d[1]
            if auxvalor1 <= tamanioContenedor:
                sumValor1=auxvalor1
                hijos_returned.append(hijo1)
            else: 
                pass
    else:
        hijos_returned.append(valor1)

    if sumValor2 > tamanioContenedor:
        while sumValor2 > tamanioContenedor:

            puntoCorte1=randint(1,len(datos[0])-1)
            puntoCorte2=randint(1,len(datos[1])-1)
            valor1 = datos[0]
            valor2 = datos[1]

            mitaduno1 = valor1[:puntoCorte1]
            mitaduno2 = valor1[puntoCorte1:]

            mitadDos1 = valor2[:puntoCorte2]
            mitadDos2 = valor2[puntoCorte2:]


            hijo1=[]
            hijo2=[]

            hijo1.extend(mitaduno1)
            hijo1.extend(mitadDos2)

            hijo2.extend(mitadDos1)
            hijo2.extend(mitaduno2)

            auxvalor2=0
            for e in hijo2:
                auxvalor2+=e[1]
            if auxvalor2 <= tamanioContenedor:
                sumValor2=auxvalor2
                hijos_returned.append(hijo2)
            else:
                pass     
    else:
        hijos_returned.append(valor2)
    return hijos_returned
    
def generate_population(paquetesIniciales):
    while len(initial_population) < paquetesIniciales:
        seleccionado=[]
        suma=0
        packInContainer=random.randint(4,20)
        control=0
        while control < packInContainer:
            randomPackage= random.randint(0,4)
            n = packages[randomPackage]
            suma += n[1]
            seleccionado.append(n)
            control+=1
        if suma > tamanioContenedor:
            pass
        else:
            initial_population.extend([seleccionado])
        
def generate_packages():
    while len(aux) < 5:
        i=0
        indice = random.randint(1, 20)
        if len(aux) == 0:
            aux.extend([indice])
        else:
            if indice in aux:
                pass
            else:
                aux.extend([indice])
    aux.sort()
    for i in range(len(aux)):
        packages.extend([[aux[i], i+1]])

def mostrar_Poblacion():
    f=0
    costos=0
    for i in initial_population:
        costos = initial_population[f] 
        sumaCostos=0
        sumaPeso=0
        for x in costos:
            sumaCostos += x[0]
            sumaPeso += x[1]
        f+=1
        print("individuo",f,".-", i, "pesa = ", sumaPeso," ---- suma de costos= ", sumaCostos)

def mostrar_Paquetes_a_enviar():
    f=0
    costos=0
    for i in envio:
        costos = envio[f] 
        sumaCostos=0
        sumaPeso=0
        for x in costos:
            sumaCostos += x[0]
            sumaPeso += x[1]
        f+=1
        print("individuo a enviar ",f,".-", i, "pesa = ", sumaPeso," ---- suma de costos= ", sumaCostos)

def ordenar_Packa_enviar():
    global envio, losMejoresGen
    x=0
    evaluar=[]
    for a in envio:
        aux = envio[x]
        sumaValor=0
        for b in aux:
            sumaValor+= b[0]
        x+=1
        evaluar.append([a, sumaValor])
    losMejoresGen = sorted(evaluar, key = lambda x : x[1])



def generateGraphic(x,y,z):
   plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
   plt.xlabel("abscisa")   # Inserta el título del eje X
   plt.ylabel("ordenada")   # Inserta el título del eje Y
   plt.ioff()   # Desactiva modo interactivo de dibujo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(y, label = "Peor Caso")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(z, label = "Caso promedio")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   # plt.plot(lista3)   # No dibuja datos de lista3
   plt.legend()
   plt.show()   # Fuerza dibujo de datos de lista3

def genereteGraphicPackages():
    paquete1=packages[0]
    paquete2=packages[1]
    paquete3=packages[2]
    paquete4=packages[3]
    paquete5=packages[4]
    valor1="1 Valor: " + str(paquete1[0]) + " - Peso: " + str(paquete1[1])
    valor2="2 Valor: " + str(paquete2[0]) + " - Peso: " + str(paquete2[1])
    valor3="3 Valor: " + str(paquete3[0]) + " - Peso: " + str(paquete3[1])
    valor4="4 Valor: " + str(paquete4[0]) + " - Peso: " + str(paquete4[1])
    valor5="5 Valor: " + str(paquete5[0]) + " - Peso: " + str(paquete5[1])

    root=Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill =Y)

    miFrame=Frame(root, width=1300, height=550)
    miFrame.pack()

    Label(miFrame, text="Valores de paquetes").place(x = 5, y =5)
    Label(miFrame, text=valor1+"\n"+valor2+"\n"+valor3+"\n"+valor4+"\n"+valor5+"\n").place(x=5, y=25)

    equis= 10
    ye = 120
    indice=0
    texto=""
    valor=0
    peso=0
    print("graficando packs")
    for i in Send_to:
        aux = i
        auxv2 = aux[0]
        #print(auxv2)
        for j in auxv2:
            #print(j)
            valor+=j[0]
            peso+=j[1]
            texto += "["+str(j)+"], "  
        Label(miFrame, text="Paquete "+ str(indice+1)+" = " +texto + " Pesa: "+ str(peso) +" Valor: " + str(valor), font=("Comic Sans MS", 8)).place(x= equis, y=ye)
        ye+=25
        indice+=1
        texto=""
        valor=0
        peso=0
    root.mainloop()

if __name__ == "__main__":
    tamanioContenedor = int (input("Tamano del contenedor: "))
    numPaquetes = int (input("Numero de paquetes a enviar:"))
    paquetesIniciales = int (input("Numero de paquetes iniciales: "))
    generate_packages()
    print("PAQUETES GENERADOS: ",packages)
    generate_population(paquetesIniciales)
    mostrar_Poblacion()
    poblation = initial_population
    i=0
    for i in range(50):
        i+=1
        print("Generacion no. ",i)
        poblation = seleccion(poblation)
        crossover_data=crossover(poblation)
        mutation_data=mutation(crossover_data)
        poblation.extend(mutation_data)
        paquetesElegidos+=1
    s=0
    to_Send=50-numPaquetes
    ordenar_Packa_enviar()
    Send_to=losMejoresGen[to_Send:]
    for sf in Send_to:
        print(sf)
    generateGraphic(send_package, peorfit_gen, promfit_gen)
    genereteGraphicPackages()