import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Martín
apellido: Morales

Enunciado:
Al presionar el botón "Mostrar Iteración", mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        # ingreso = 1
        # ingreso = int(ingreso)

        # alert("Inicio", "Inicio")
        # while ingreso != 10:
        #     alert("Ingresado", ingreso)
        #     ingreso += 1
        
        # alert("Fin", "Fin")


        # respuesta = True

        # acumulador_precios = 0 
        # alert("Incio", "Inicio")

        # while respuesta:
        #     precio = float(prompt("Ingreso", "Ingrese un numero"))
        #     contador_arg += 1
        #     acumulador_precios += precio
        #     respuesta = question("Pregunta", "Dese repetir?")

        # alert("Fin", "Precio total: " + str(acumulador_precios))

        # ingreso_numero = 1

        # while ingreso_numero != 10:
        #     alert(title="Ingreso num", message=ingreso_numero)
        #     ingreso_numero +=1
        
        # alert("Fin", "FIn")

        # contador = 1

        # while contador <= 10:
        #     alert(title="Número", message=contador)
        #     contador = contador + 1
    

        #Clase Lune 17
        #ejemplo de prmedio de notas, etc
        contador = 0
        acumulador = 0
        numero = 1
        numero = int(prompt("Numero", "Ingrese un numero"))
        #op1 != op2

        #not True = False
        #not False =  True

        # "Algo" .isdigit() => True 0-9, de lo contrario false
        # str.isalpha() => True a-z A-Z, de lo contrario false
        # str.alnum() => True a-zA-Z

        while contador < 5 and numero != 0:
            
            acumulador += numero
            contador += 1
        
        print("La sumatoria es: ", str(acumulador))




    
if __name__ == "__main__":
    app = App()
    app.mainloop()