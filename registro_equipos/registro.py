import tkinter as tk
import ttkbootstrap as tb
from usuarios.interfaz import Frame, barra_menu

def main():
    root = tb.Window(themename="morph")
    #root = tk.Tk()
    root.geometry("1100x700+400+150")  
    root.title('Registro de Equipos de Computo')
    root.iconbitmap('img/nuevo_logo.ico')
    #root.resizable(0,0)
    
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()


if __name__ == '__main__':
    main()