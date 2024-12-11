import mysql.connector
import customtkinter as ctk
from tkinter import ttk

# Configuração da conexão com o banco de dados
conexao = mysql.connector.connect(
    host="143.106.241.3",
    port=3306,
    user="cl201107",
    password="cl*02032005",
    database="cl201107"
)

def fetch_alunos():
    """Busca todos os alunos no banco de dados."""
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT nome, RA FROM Minerva_Aluno")
    alunos = cursor.fetchall()
    cursor.close()
    return alunos

# Interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração inicial
        self.title("Lista de Alunos")
        self.geometry("950x600")
        self.resizable(False, False)  # Desabilitar redimensionamento
        ctk.set_appearance_mode("dark")  # Tema escuro
        ctk.set_default_color_theme("blue")  # Tema com predominância azul
        
        # Container principal com barra de rolagem
        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.canvas = ctk.CTkCanvas(self.main_frame, highlightthickness=0, bg="black")
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color="black")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Preencher a lista de alunos
        self.populate_alunos()

    def populate_alunos(self):
        """Adiciona os alunos em uma grade 3x3 na interface."""
        alunos = fetch_alunos()
        
        # Configurar o número de colunas
        num_cols = 3
        row = 0
        col = 0
        
        for aluno in alunos:
            frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=15, fg_color="#1e1e2e")
            frame.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            
            aluno_label = ctk.CTkLabel(
                frame,
                text=f"Nome: {aluno['nome']}\nRA: {aluno['RA']}",
                justify="center",
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color="#1E90FF"  # Azul vibrante
            )
            aluno_label.pack(pady=20, padx=20)
            
            # Avançar na grade
            col += 1
            if col >= num_cols:
                col = 0
                row += 1

        # Ajustar colunas para tomar espaço uniformemente
        for i in range(num_cols):
            self.scrollable_frame.grid_columnconfigure(i, weight=1)

# Executar a aplicação
if __name__ == "__main__":
    app = App()
    app.mainloop()
