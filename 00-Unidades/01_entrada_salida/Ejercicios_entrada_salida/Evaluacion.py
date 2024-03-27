import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Emanuel
apellido: Mendoza
---
Ejercicio: entrada_salida_02
---
Enunciado:
De los 50 participantes del torneodeUTN-TETRIS,se debe ingresar los siguientes datos: 
Nombre 
Categoría(Principiante-Intermedio-Avanzado) 
Edad(entre 18 y 99 inclusive) 
Score(mayor que 0) 
Nivel alcanzado(1,2o3) 

Pedir datos por prompt y mostrar por print , se debe informar:
InformeA-Cuál es el nivel más alcanzado de los jugadores 
InformeB-El Porcentaje de jugadores de la categoría principiante sobre el total 
InformeC-La categoría del participante de mayor edad 
InformeD-El score y nombre del principiante con mayor score 
InformeE-Promedio de score de los participantes intermedios.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        bandera_primera = True
        bandera_segunda = True
        contador_nivel_alcanzado_uno = 0
        contador_nivel_alcanzado_dos = 0
        contador_nivel_alcanzado_tres = 0
        contador_categoria_principiante = 0
        contador_categoria_intermedio = 0
        contador_categoria_avanzado = 0
        acumulador_score_intermedios = 0


        for i in range(1,51):
            
            nombre = prompt("","Ingrese nombre")

            edad = int(prompt("","Ingrese edad"))
            while edad > 99 or edad < 18:
                edad = int(prompt("","Reingrese una edad valida"))

            categoria = prompt("","Ingrese categoria")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = prompt("","Reingrese una categoría valida")

            score = int(prompt("","Ingrese score"))
            while score < 1:
                score = int(prompt("","Reingrese un score valido"))

            nivel_alcanzado = prompt("","Ingrese nivel alcanzado")
            while nivel_alcanzado != "1" and nivel_alcanzado != "2" and nivel_alcanzado != "3":
                nivel_alcanzado = prompt("","Reingrese un nivel valido")

            match nivel_alcanzado:
                case "1":
                    contador_nivel_alcanzado_uno += 1
                case "2":
                    contador_nivel_alcanzado_dos += 1
                case "3":
                    contador_nivel_alcanzado_tres += 1

            match categoria:
                case "Principiante":
                    contador_categoria_principiante += 1

                    if bandera_segunda:
                        score_max = score
                        nombre_score_max = nombre
                        bandera_segunda = False
                    elif score > score_max:
                        score_max = score
                        nombre_score_max = nombre

                case "Intermedio":
                    contador_categoria_intermedio += 1
                    acumulador_score_intermedios += score

                case "Avanzado":
                    contador_categoria_avanzado += 1

            if bandera_primera :
                edad_max = edad
                categoria_edad_max = categoria
                bandera_primera = False
            elif edad > edad_max:
                edad_max = edad
                categoria_edad_max = categoria


        if contador_nivel_alcanzado_uno > contador_nivel_alcanzado_dos and contador_nivel_alcanzado_uno > contador_nivel_alcanzado_tres:
            mayor_nivel = "1"
        elif contador_nivel_alcanzado_dos > contador_nivel_alcanzado_tres:
            mayor_nivel = "2"
        else:
            mayor_nivel = "3"

        if contador_categoria_principiante != 0:
            categoria_totales = contador_categoria_intermedio + contador_categoria_avanzado + contador_categoria_principiante
            porcentaje_categoria_principiante = (contador_categoria_principiante * 100) / categoria_totales
        else:
            porcentaje_categoria_principiante = 0
            nombre_score_max = "Nadie"
            score_max = "0"

        if contador_categoria_intermedio != 0:
            promedio_score_intermedio = acumulador_score_intermedios / contador_categoria_intermedio
        else:
            promedio_score_intermedio = 0

        print(f"El nivel mas alcanzado es el {mayor_nivel}")
        print(f"El porcentaje de personas de la categoria principiantes es de {porcentaje_categoria_principiante}%")
        print(f"La persona de mayor edad pertenece a la categoria {categoria_edad_max}")
        print(f"La persona con mayor score de los principiantes es {nombre_score_max} y su score es de {score_max}")
        print(f"El promedio del score de las personas de nivel intermedio es de {promedio_score_intermedio}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()