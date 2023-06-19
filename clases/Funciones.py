from pyswip import Prolog
p = Prolog()
p.consult("./prolog/BobBH.pl")
from tkinter import *
from tkinter import messagebox as MessageBox

import numpy as np
array = []
fondo = ["bob"]

#se lo envio con un setter
cont = 0     
def fondoF(X):
    global cont,fondo
    cont += 1
    if cont == 0:
        #print(fondo)
        return fondo
    fondo.clear()
    fondo.append(X)
    Solution(fondo)
def Solution(X):
    
    if X[0] == "ram":
        MessageBox.showinfo("Tu memoria RAM está fallando", "Asegúratede que esté bien conectada")
    if X[0] == "grafica":
        MessageBox.showinfo("Tu tarjeta gráfica está fallando", "Asegúrate de que esté bien conectada")
    if X[0] == "tecnico":
        MessageBox.showinfo("No se ha encontrado solución", "Asegúrate de ir con un técnico en tu localidad")
    if X[0] == "problemascpu":
        MessageBox.showinfo("Tu procesador está fallando", "Asegúrate de que esté bien conectado o este limpió")
    if X[0] == "cortocircuito":
        MessageBox.showinfo("Hay un cortocircuito en tu equipo", "Asegúrate de examinar todas las conexiones")
    if X[0] == "fuentedepoder":
        MessageBox.showinfo("Tu fuente de poder está fallando", "Asegúrate de desconectar y conectarla de nuevo para reiniciarla")
    if X[0] == "suciedadypolvo":
        MessageBox.showinfo("Tu equipo necesita una limpieza", "Asegúrate de desempolvar todos los componentes y cambiar pasta térmica")
    if X[0] == "driversysoftware":
        MessageBox.showinfo("Tu equipo puede tener virus", "Asegúrate reinstalar el SO y los drivers o poner una vacuna")
        
def QuestionOrFactSi (X):#Problema para Si
    array.clear()
    for BH in p.query("es_problema(" + X + ",Y)"):
        array.append(BH["Y"])
    
    if len(array) == 2:
        return array[0]
    else:
        for valor in p.query("solucionsi(" + X + ")"):
            return valor  

def QuestionOrFactNo (X):#Problema para Si
    array.clear()
    cont = 0
    for BH in p.query("es_problema(" + X + ",Y)"):
        cont += 1
        array.append(BH["Y"])
    if cont > 1:
        return array[1]
    elif cont == 1:
        return array[0] 
    else:
        for valor in p.query("solucionno(" + X + ")"):
            return valor
      