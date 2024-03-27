import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = 50

        for i in range(1,8):
            numero = int(prompt("","Ingrese un numero"))
            

            if numero == numero_secreto:
                break

            elif numero < numero_secreto:
                alert("","Falta…")

            else:
                alert("","Se pasó…")
        
        if i == 1:
            alert("","Usted es un psíquico")
        
        elif i == 2: 
            alert("","Excelente percepción")
        
        elif i == 3:
            alert("","Esto es suerte")
        
        elif i == 4 or i == 5:
            alert("","Excelente técnica")
        
        else:
            alert("","Perdiste, suerte para la próxima")


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()