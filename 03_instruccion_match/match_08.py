import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Martín
apellido: Morales

Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el botón 
"Informar" indicar mediante alert si en el destino hace frío o calor la mayoría 
de las estaciones del año.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destino = self.combobox_destino.get()
        mensaje_calor = "Hace calor la mayoria de las estaciones del año"
        mensaje_frio = "Hace frio la mayoria de las estaciones del año" 

        # match destino:
        #     case "Ushuaia":
        #         alert(title=destino, message=mensaje_frio)
        #     case "Cataratas":
        #         alert(title=destino, message= mensaje_calor)
        #     case "Bariloche":
        #         alert(title=destino, message=mensaje_frio)
        #     case "Mar del plata":
        #         alert(title=destino, message= mensaje_calor)
        
        match destino:
            case "Cataratas" | "Mar del plata":
                alert(title=destino, message= mensaje_calor)
            case _:
                alert(title=destino, message=mensaje_frio)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()