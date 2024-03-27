import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
Ejercicio: Ejemplo
---

UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''



class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True
        contador_masculino_IOT_IA = 0
        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0
        contador_maculino = 0
        contador_femenino = 0
        contador_otros = 0
        contador_IOT_edad = 0
        acumulador_femenino_IA = 0
        contador_femenino_IA = 0

        bandero_primer_rv_ra = False
        edad_minima = 0

        while seguir == True:
            nombre = input("Ingrese el nombre")

            edad = input("Ingrese la edad")
            edad = int(edad)
            while edad < 18 :
                edad = input("Reingrese edad")
                edad = int(edad)

            genero = input("Ingrese genero")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otros":
                genero = input("Reingrese genero")

            tecnologia = input("Ingrese tecnologia")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = input("Reingrese tecnologia")

            #if tecnologia == "IOT":
            #    contador_IOT += 1

            #elif tecnologia == "IA":
            #    contador_IA += 1

            #else:
            #    contador_RV_RA += 1

            match tecnologia:
                case "IOT":
                    contador_IOT += 1

                    if (edad > 17 and edad < 26) or (edad >32 and edad < 43):
                        contador_IOT_edad += 1
                case "IA":
                    contador_IA += 1
                case "RV/RA":
                    contador_IA += 1
                    if contador_IA == 1 or edad < edad_minima:
                        nombre_minimo = nombre
                        genero_minimo = genero
                        edad_minima = edad

            match genero:
                case "Masculino":
                    contador_maculino += 1
                case "Femenino":
                    contador_femenino += 1
                    if tecnologia == "IA":
                        acumulador_femenino_IA += 1
                        contador_femenino_IA += edad
                case "Otros":
                    contador_otros += 1
            

            if genero == "Masculino" and tecnologia == "IOT" or tecnologia == "IA" and edad >= 25 and edad <= 50:
                contador_masculino_IOT_IA += 1


            seguir = question("","Quiere continuar ingresando personas")



        if contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            print("2. Se voto mas a IOT")

        elif contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
            print("2. Se voto mas a IOT")

        elif contador_IA > contador_RV_RA:
            print("2. Se voto mas a IA")

        elif contador_IA > contador_RV_RA:
            print("2. Se voto mas a IA")

        elif contador_RV_RA > contador_IA:
            print("2. Se voto mas a RV/RA")

        elif contador_IA == contador_IOT and contador_IA == contador_RV_RA:
            print("2. Se empato")

        elif contador_IA == contador_IOT:
            print("2. Se empato entre IA y IOT")

        elif contador_IA == contador_RV_RA:
            print("2. Se empato entre IA y RV/RA")
        
        elif contador_RV_RA == contador_IOT:
            print("2. Se empato entre RV/RA y IOT")

        else:
            print("2. Se voto mas a RV/RA")


        total_empleados = contador_otros + contador_femenino + contador_maculino
        porcentaje_femenino = (contador_femenino * 100)/ total_empleados
        porcentaje_masculino = (contador_maculino * 100)/ total_empleados
        porcentaje_otros = total_empleados - (porcentaje_femenino + porcentaje_masculino)

        porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados

        if contador_femenino_IA > 0:
            promedio_femenino_IA = acumulador_femenino_IA / contador_femenino_IA
        else:
            promedio_femenino_IA = "0"


        print(F"1. cantidad masculina que votaron IOT/IA en el rango de edad: {contador_masculino_IOT_IA}")
        print(F"3. Porcentaje:\n\tMasculino: {porcentaje_masculino}%\n\tFemenino: {porcentaje_femenino}%\n\tOtros: {porcentaje_otros}%")
        print(F"4. La cantidad de personas que votaron a IOT y ademas esta en el intervalo de edad es de {porcentaje_IOT_edad}")
        print(F"5. El porcentaje de empleados femeninos que votaron a IA es {promedio_femenino_IA}")
        print(F"6. La persona con menor edad que voto a RV/RA es {nombre_minimo} y su genero es {genero_minimo}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()