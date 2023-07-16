import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Martin
apellido: Morales
---
Ejercicio: instrucion_if_10
---
Enunciado:
Al presionar el botón  'Calcular', se deberá calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
    6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
    4 y 5           ---> Aprobado, la nota es ...
    1, 2 y 3        ---> Desaprobado, la nota es ...

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # numero=random.randint(1, 10)  

        # mensaje_desaprobado="Desaprobado, la nota es {0}".format(numero) 
        # mensaje_aprobado="Aprobado, la nota es {0}".format(numero)
        # mensaje_promocion="Promoción directa, la nota es {0}".format(numero)

        # if(numero<=3):
        #     print(mensaje_desaprobado)
        # elif(numero>3 and numero<=7):
        #     print(mensaje_aprobado)
        # elif(numero>7 and numero<=10) :
        #     print(mensaje_promocion) 

        nota = random.randint(0,10)
        str_nota = str(nota)

        if (nota >= 6):
            alert(title="Nota aleatoria", message="Promoción directa, la nota es " + str_nota)
        elif (nota >= 4 and nota >= 5):
            alert(title="Nota aleatoria", message="Aprobado, la nota es " + str_nota)
        else:
            alert(title="Nota aleatoria", message="Desaprobado, la nota es " + str_nota)

            

if __name__ == "__main__":
    app = App()
    app.mainloop()