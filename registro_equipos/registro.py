import tkinter as tk
import customtkinter as ctk
from usuarios.interfaz import Frame, barra_menu

ctk.set_default_color_theme("green")
ctk.set_default_color_theme("blue")

def main():
    root = tk.Tk()
    root.geometry("800x580+260+9")  
    root.title('Registro de Equipos de Computo')
    root.iconbitmap('img/nuevo_logo.ico')
    root.resizable(0,0)
    

    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()


if __name__ == '__main__':
    main()