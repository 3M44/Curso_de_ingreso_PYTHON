import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        max = 0
        min = 0
        contador = 0
        acumulador = 0
        edad_candidatos = 0
        bandera_del_primero = True

        while True:

            cantidad_candidatos = prompt("","Ingrese la cantidad de candidatos")
            
            if cantidad_candidatos == None:
                break
            
            cantidad_candidatos = int(cantidad_candidatos)

            while cantidad_candidatos > contador:
                nombre = prompt("","Ingrese un nombre")
                
                edad = prompt("","Ingrese edad")
                edad = int(edad)
            
                while edad < 25:
                    edad = prompt("", "Ingrese una edad valida")
                    edad = int(edad)

                edad_candidatos += edad

                votos = prompt("","Ingrese cantidad de votos")
                votos = int(votos)

                while votos < 0:
                    votos = prompt("","Ingrese una cantidad de votos valida")
                    votos = int(votos)

                if bandera_del_primero == True :
                    max = votos
                    min = votos
                    mas_votos_nombre = nombre
                    menos_votos_edad = edad
                    menos_votos_nombre = nombre
                    bandera_del_primero = False

                else:
                    if votos > max:
                        max = votos
                        mas_votos_nombre = nombre
            
                    elif votos < min:
                        min = votos
                        menos_votos_edad = edad
                        menos_votos_nombre = nombre

                contador += 1
                acumulador += votos

            promedio = edad_candidatos / cantidad_candidatos

        msg = "La persona con mas votos es {0}\nLa persona con menos votos es {1} y su edad es {2}\nEl promedio de edades es de {3}\nEl total de votos es de {4}".format(mas_votos_nombre,menos_votos_nombre,menos_votos_edad,promedio,acumulador)
        
        alert("",msg)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
