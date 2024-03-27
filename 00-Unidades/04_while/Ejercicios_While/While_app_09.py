import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):

        max = 0
        min = 0
        bandera_del_primero = True

        while True:
            numero = prompt("","Ingrese un numero")
            
            if numero == None:
                break

            
            numero = int(numero)
            
            if bandera_del_primero == True :
                max = numero
                min = numero
                bandera_del_primero = False

            else:
                if numero > max:
                    max = numero
            
                elif numero < min:
                    min = numero

            

            self.txt_minimo.delete(0,20)
            self.txt_minimo.insert(0,min)

            self.txt_maximo.delete(0,20)
            self.txt_maximo.insert(0,max)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
