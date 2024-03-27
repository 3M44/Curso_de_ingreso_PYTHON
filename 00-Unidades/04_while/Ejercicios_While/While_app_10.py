import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Emanuel
apellido:Mendoza
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        numero_suma_positivos = 0
        numero_suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_cero = 0
        
        while True:
            numero = prompt("","ingrese un numero")

            if numero == None:
                break
            
            numero = int(numero)

            if numero == 0 :
                contador_cero += 1

            elif numero > 0:
                contador_positivos += 1 
                numero_suma_positivos +=numero

            else:
                contador_negativos += 1 
                numero_suma_negativos +=numero

            
        if contador_negativos < contador_positivos:
            minuendo = contador_positivos
            sustraendo = contador_negativos

        else:
            minuendo = contador_negativos
            sustraendo = contador_positivos

        diferencia = minuendo - sustraendo

        msg = "La suma de los numeros positivos es {0} y su cantidad es de {1}\nLa suma de los numeros negativos es {2} y su cantidad es de {3}\nLa cantidad de ceros es {4}\nLa diferencia entre la cantidad de positivos y negativos es de {5}".format(numero_suma_positivos,contador_positivos,numero_suma_negativos,contador_negativos,contador_cero,diferencia)

        alert("", msg)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
