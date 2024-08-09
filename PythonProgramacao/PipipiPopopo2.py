import tkinter as tk
from tkinter import ttk

def adicionar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()

    if nome and idade:
        tree.insert("", "end", values=(nome, idade))
        entry_nome.delete(0, tk.END)
        entry_idade.delete(0, tk.END)

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo com tkinter")

# Criando um Frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Criando os campos de entrada
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade = tk.Label(frame, text="Idade:")
label_idade.grid(row=1, column=0, padx=5, pady=5)

entry_idade = tk.Entry(frame)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

# Botão para adicionar os dados na tabela
botao_adicionar = tk.Button(frame, text="Adicionar", command=adicionar_dados)
botao_adicionar.grid(row=2, columnspan=2, pady=10)

# Criando a Tabela
colunas = ("Nome", "Idade")
tree = ttk.Treeview(frame, columns=colunas, show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.grid(row=3, columnspan=2, pady=10)

# Iniciando o loop principal da interface
root.mainloop()
