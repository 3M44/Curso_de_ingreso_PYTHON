import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        bandera_primero = True
        contador_postulantes_primer_punto = 0
        edad_minima = 0
        contador_masculinos = 0
        contador_femenino = 0
        contador_no_binario = 0
        acumulador_edad_masculino = 0
        acumulador_edad_femenino = 0
        acumulador_edad_no_binario = 0
        contador_asp_net = 0
        contador_js = 0
        contador_python = 0

        for i in range(1,11):
            nombre = prompt("","Ingrese nombre")

            edad = int(prompt("","Ingrese edad"))

            while edad < 18:
                edad = int(prompt("","Reingrese una edad valida"))
            

            genero = prompt("","Ingrese genero")

            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("","Reingrese un genero valido")
        
            tecnologia = prompt("","Ingrese tecnología")

            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("","Reingrese una tecnologia valida")

            puesto = prompt("","Ingrese puesto")

            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("","Reingrese un puesto valido")

            if (edad > 24 and edad < 41) and genero == "NB" and (tecnologia == "ASP.NET" or tecnologia == "JS") and puesto == "Ssr":
                contador_postulantes_primer_punto += 1


            if bandera_primero == True:
                edad_minima = edad
                nombre_edad_minima_jr = nombre
                bandera_primero = False

            if puesto == "Jr" and edad < edad_minima:
                nombre_edad_minima_jr = nombre
                edad_minima = edad

            match genero:
                case "M":
                    contador_masculinos += 1
                    acumulador_edad_masculino += edad
                case "F":
                    contador_femenino += 1
                    acumulador_edad_femenino += edad
                case "NB":
                    contador_no_binario += 1
                    acumulador_edad_no_binario += edad

            match tecnologia:
                case "ASP.NET":
                    contador_asp_net += 1
                case "JS":
                    contador_js += 1
                case "PYTHON":
                    contador_python += 1

        if contador_masculinos != 0:
            promedio_m = acumulador_edad_masculino / contador_masculinos
        else:
            promedio_m = "0"

        if contador_femenino != 0:
            promedio_f = acumulador_edad_femenino / contador_femenino
        else:
            promedio_f = "0"
        
        if contador_no_binario != 0:
            promedio_nb = acumulador_edad_no_binario / contador_no_binario
        else:
            promedio_nb = "0"


        if contador_python > contador_js and contador_python > contador_asp_net:
            tecnologia_mas_postulantes = "PYTHON"

        elif contador_js > contador_asp_net:
            tecnologia_mas_postulantes = "JS"

        else:
            tecnologia_mas_postulantes = "ASP.NET"

        postulantes_totales = contador_no_binario + contador_femenino + contador_masculinos
        porcentaje_postulantes_masculinos = (contador_masculinos * 100) / postulantes_totales 
        porcentaje_postulantes_femenino = (contador_femenino * 100) / postulantes_totales
        porcentaje_postulantes_no_binario = (contador_no_binario * 100) / postulantes_totales


        print(f"La cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr son {contador_postulantes_primer_punto}")
        print(f"El nombre del postulante a jr con menor edad es {nombre_edad_minima_jr}")
        print(f"El promedio de edades son: \n\tMasculino: {promedio_m}\n\tFemenino: {promedio_f}\n\tNB: {promedio_nb}")
        print(f"La tecnología con mas postulantes es {tecnologia_mas_postulantes}")
        print(f"El porcentaje de hombres es {porcentaje_postulantes_masculinos}, el de mujeres es {porcentaje_postulantes_femenino} y el de no binario es {porcentaje_postulantes_no_binario}")



if __name__ == "__main__":

    app = App()
    app.geometry("300x300")
    app.mainloop()
