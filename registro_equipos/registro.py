import tkinter as tk
import ttkbootstrap as tb
from usuarios.interfaz3 import Frame3, barra_menu

def main():
    root = tb.Window(themename="morph")
    #root = tk.Tk()
    root.geometry("1100x700+80+0")  
    root.title('Registro de Equipos de Computo')
    root.iconbitmap('img/nuevo_logo.ico')
    root.resizable(0,0)
    
    barra_menu(root)

    app = Frame3(root = root)

    app.grid(row=2, column=0, padx=150, pady=20, sticky='nsew')
    
    
    
    app.mainloop()


if __name__ == '__main__':
    main()