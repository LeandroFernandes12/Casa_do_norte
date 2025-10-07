import tkinter as tk  # Importa o módulo principal do tkinter para criar janelas e widgets GUI.
from tkinter import ttk  # Importa os widgets temáticos do tkinter (visualmente mais modernos).
from db import ensuredb  # Importa função para garantir que o banco de dados exista e esteja inicializado.
from utils import centralizarjanela  # Importa função utilitária para centralizar janela na tela.
from login import showlogin  # Importa a função responsável por exibir a tela de login.
from comidas import showcomidas  # Importa a função de cadastro/consulta/edição de comidas.
from estoque import showgestaoestoque  # Importa função para tela de gestão de estoque.

class App(tk.Tk):
    """Classe principal - Controle de Estoque de Comidas Nordestinas."""

    def __init__(self):
        super().__init__()  # Inicializa objeto Tk (janela principal).
        self.title("Controle de Estoque de Comidas Nordestinas")  # Determina título da janela.
        ensuredb()  # Garante que o banco foi criado e está pronto.
        self.currentuser = None  # Armazena dados do usuário logado.
        centralizarjanela(self, 400, 250)  # Centraliza janela no início.
        showlogin(self)  # Mostra tela de login no lançamento do app.

    def showmain(self):
        """Exibe a tela principal do sistema após o login."""
        # Limpa a tela de widgets antigos.
        for w in self.winfo_children():
            w.destroy()
        # Centraliza e expande janela para modo principal.
        centralizarjanela(self, 1000, 550)

        # Frame superior com dados do usuário e botões de navegação.
        top = ttk.Frame(self, padding=2)
        top.pack(fill="x")
        # Exibe quem está logado (usa 'nome_completo' do banco).
        ttk.Label(top, text=f"Usuário logado: {self.currentuser.get('nome_completo','')}").pack(side="left")
        # Botão para deslogar.
        ttk.Button(top, text="Sair", command=lambda: showlogin(self)).pack(side="right")
        # Botão para acessar cadastro de comidas.
        ttk.Button(top, text="Cadastro de Comidas", command=lambda: showcomidas(self)).pack(side="right", padx=6)
        # Botão para acessar tela de gestão de estoque.
        ttk.Button(top, text="Gestão de Estoque", command=lambda: showgestaoestoque(self)).pack(side="right", padx=6)

        # Frame central para mensagem de boas-vindas e instruções.
        center = ttk.Frame(self, padding=40)
        center.pack(expand=True)
        msg = (
            "Bem-vindo ao Controle de Estoque de Comidas Nordestinas.\n"
            "Aqui você pode:\n"
            " - Cadastrar novos pratos e comidas típicas\n"
            " - Consultar e editar o estoque\n"
            " - Registrar entradas e saídas"
            "\nEscolha uma das opções no menu acima para começar."
        )
        tk.Label(center, text=msg, font=("TkDefaultFont", 18), fg="blue", justify="left").pack()

if __name__ == "__main__":
    # Inicia o programa chamando a classe principal.
    app = App()
    app.mainloop()  # Executa o loop principal da interface gráfica.
