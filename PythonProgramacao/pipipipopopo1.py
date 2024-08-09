import tkinter as tk

def criar_moldura():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Moldura com tkinter")

    # Configurações do Frame (Moldura)
    moldura = tk.Frame(root, bg="white", bd=5, relief="solid")
    
    # Dimensões da Moldura
    moldura.config(width=200, height=200)

    # Colocando o Frame na tela
    moldura.pack(padx=10, pady=10)

    # Inicializa a janela
    root.mainloop()

# Chama a função para criar a moldura
criar_moldura()
