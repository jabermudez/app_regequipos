import tkinter as tk
import ttkbootstrap as tb
from usuarios.interfaz import Frame
from usuarios.interfaz2 import Frame1
from usuarios.interfaz3 import Frame3


def main():
    root = tb.Window(themename="morph")
    root.geometry("1100x800+80+0")  
    root.title('Registro de Equipos de Computo')
    root.iconbitmap('img/nuevo_logo.ico')   
    root.resizable(0,0)
        
    
    barra_menu(root)

    app = Frame1(root = root)    
   
    app.mainloop()



def mostrar_registro_usuarios():
    
    root = tk.Toplevel()
    root.title("Registro de Usuarios")    
    root.geometry("1100x800+80+0")      
    root.iconbitmap('img/nuevo_logo.ico')   
    root.resizable(0,0)
            

    app = Frame(root = root)          
    app.grid(row=2, column=0, padx=55, pady=20, sticky='nsew')

# Función para crear y mostrar la ventana de préstamos de equipos
def mostrar_prestamos_equipos():
    root = tk.Toplevel()
    root.title("Registro Prestamos")    
    root.geometry("1100x800+80+0")      
    root.iconbitmap('img/nuevo_logo.ico')   
    root.resizable(0,0)
           
    
    app = Frame3(root = root)  
    app.grid(row=2, column=0, padx=150, pady=10, sticky='nsew')

def barra_menu(root):
    barra_menu = tb.Menu(root)
    root.config(menu = barra_menu)

    menu_inicio = tb.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu = menu_inicio)
    menu_inicio.add_command(label='Salir', command=root.quit)

    # Menú de consultas
    menu_consultas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Consultas', menu=menu_consultas)
    menu_consultas.add_command(label='Registro de Usuarios', command=mostrar_registro_usuarios)
    menu_consultas.add_command(label='Préstamos de Equipos', command=mostrar_prestamos_equipos)



if __name__ == '__main__':
    main()