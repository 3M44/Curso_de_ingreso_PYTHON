import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Emanuel
apellido: Mendoza
---
Ejercicio: entrada_salida_01
---
Simulacro Turno Tarde
Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre
Edad (debe ser mayor a 12)
Altura (no debe ser negativa)
Días que asiste a la semana (1, 3, 5)
Kilos que levanta en peso muerto (no debe ser cero, ni negativo)


No sabemos cuántos clientes serán consultados.
Se debe informar al usuario:
El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
El porcentaje de clientes que asiste solo 1 día a la semana.
Nombre y edad del cliente con más altura.
Determinar si los clientes eligen más ir 1, 3 o 5 días
Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        clientes = True
        bandera_primero = True
        bandera_segunda = True
        contador_dias_uno = 0
        contador_dias_tres = 0
        contador_dias_cinco = 0
        acumulador_kilos = 0
        altura_maxima = 0
        edad_minima = 0


        while clientes:
            nombre = prompt("","Ingrese nombre")

            edad = int(prompt("","Ingrese edad"))
            while edad < 12:
                edad = int(prompt("","Reingrese una edad valida"))

            altura = float(prompt("","Ingrese altura"))
            while altura < 0:
                altura = float(prompt("","Reingrese una altura valida"))

            dias_semana = int(prompt("","Ingrese los dias que asistira en la semana"))
            while dias_semana != 1 and dias_semana != 3 and dias_semana != 5:
                dias_semana = int(prompt("","Reingrese unos dias validos"))

            kilos_peso_muerto = int(prompt("","Ingrese los kilos que levanta en peso muerto"))
            while kilos_peso_muerto < 1:
                kilos_peso_muerto = int(prompt("","Reingrese una cantidad de kilos valida"))

            match dias_semana:
                case 1:
                    contador_dias_uno += 1 
                case 3:
                    contador_dias_tres += 1
                    acumulador_kilos += kilos_peso_muerto
                case 5:
                    contador_dias_cinco += 1

                    if bandera_segunda:
                        edad_minima = edad
                        nombre_edad_minima_cinco_dias = nombre
                        kilos_edad_minima_cinco_dias = kilos_peso_muerto
                        bandera_segunda = False

                    if edad < edad_minima:
                        altura_maxima = altura
                        nombre_edad_minima_cinco_dias = nombre
                        kilos_edad_minima_cinco_dias = kilos_peso_muerto


            if bandera_primero:
                altura_maxima = altura
                nombre_altura_max = nombre
                edad_altura_max = edad
                bandera_primero = False

            if altura > altura_maxima:
                altura_maxima = altura
                nombre_altura_max = nombre
                edad_altura_max = edad

            clientes = question("","quiere ingresar un nuevo cliente")

        if contador_dias_tres != 0:
            promedio_kilos_tres_dias = acumulador_kilos / contador_dias_tres
        else:
            promedio_kilos_tres_dias = "0"

        dias_totales = contador_dias_tres + contador_dias_uno + contador_dias_cinco
        porcentaje_dia_uno = (contador_dias_uno * 100) / dias_totales

        if contador_dias_uno > contador_dias_tres and contador_dias_uno > contador_dias_cinco:
            dia_mas = "1"
        elif contador_dias_tres > contador_dias_cinco:
            dia_mas = "3"
        else:
            dia_mas = "5"

        print(f"El promedio de kilos que levantan las personas que van 3 dias es {promedio_kilos_tres_dias}")

        print(f"El porcentaje de gente que va el dia uno es {porcentaje_dia_uno}")

        print(f"El  nombre de la persona mas alta es {nombre_altura_max} y su edad es {edad_altura_max}")

        print(f"El dia mas elegido es el {dia_mas}")
        
        if contador_dias_cinco != 0:
            print(f"La persona mas joven que va 5 dias es {nombre_edad_minima_cinco_dias} y la cantidad de kilos que levanta es {kilos_edad_minima_cinco_dias}")
        else:
            print(f"No hay nadie que va el dia 5")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
