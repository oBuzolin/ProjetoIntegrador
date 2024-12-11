import customtkinter as ctk
import mysql.connector
import random
from tkinter import messagebox

# Conectar ao banco de dados MySQL
db_connection = mysql.connector.connect(
    host="143.106.241.3", port=3306, user="cl201107", password="cl*02032005", database="cl201107"
)
cursor = db_connection.cursor()

# Função para criar ID único aleatório de 5 dígitos
def generate_unique_id():
    while True:
        random_id = random.randint(10000, 99999)
        cursor.execute("SELECT id_Turma FROM Minerva_Turma WHERE id_Turma = %s", (random_id,))
        if not cursor.fetchone():  # Confirma se o ID não existe
            return random_id

# Função para adicionar turma ao banco de dados
def add_turma():
    nome_turma = entry_nome_turma.get().strip()
    matricula_professor = entry_matricula_professor.get().strip()
    
    # Verificar se o nome da turma já existe
    cursor.execute("SELECT nomeTurma FROM Minerva_Turma WHERE nomeTurma = %s", (nome_turma,))
    if cursor.fetchone():
        messagebox.showerror("Erro", "Nome da turma já existe.")
        return
    
    # Verificar se a matrícula do professor existe
    cursor.execute("SELECT matricula FROM Minerva_Professor WHERE matricula = %s", (matricula_professor,))
    if not cursor.fetchone():
        messagebox.showerror("Erro", "Matrícula de professor não encontrada.")
        return
    
    # Criar ID único para a turma
    unique_id = generate_unique_id()
    
    # Inserir na tabela Minerva_Turma
    cursor.execute(
        "INSERT INTO Minerva_Turma (id_Turma, nomeTurma) VALUES (%s, %s)",
        (unique_id, nome_turma)
    )
    db_connection.commit()
    
    # Inserir na tabela Minerva_ProfessorTurma
    cursor.execute(
        "INSERT INTO Minerva_ProfessorTurma (id_Turma, matricula) VALUES (%s, %s)",
        (unique_id, matricula_professor)
    )
    db_connection.commit()
    
    messagebox.showinfo("Sucesso", f"Turma '{nome_turma}' criada com sucesso!")
    app.destroy()  # Fechar a janela após o uso

# Configuração da interface em customtkinter com tema escuro
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Cadastro de Turmas")
app.geometry("400x350")  # Aumenta a altura da janela
app.resizable(False, False)

# Layout e Estilo
frame = ctk.CTkFrame(app, width=350, height=300)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Título
label_title = ctk.CTkLabel(frame, text="Cadastrar Nova Turma", font=("Arial", 18, "bold"))
label_title.pack(pady=(10, 20))

# Campo de entrada para Nome da Turma
label_nome_turma = ctk.CTkLabel(frame, text="Nome da Turma:", font=("Arial", 14))
label_nome_turma.pack(pady=(10, 5))
entry_nome_turma = ctk.CTkEntry(frame, width=300, font=("Arial", 12))
entry_nome_turma.pack(pady=5)

# Campo de entrada para Matrícula do Professor
label_matricula_professor = ctk.CTkLabel(frame, text="Matrícula do Professor:", font=("Arial", 14))
label_matricula_professor.pack(pady=(10, 5))
entry_matricula_professor = ctk.CTkEntry(frame, width=300, font=("Arial", 12))
entry_matricula_professor.pack(pady=5)

# Botão para adicionar turma
button_add_turma = ctk.CTkButton(frame, text="Adicionar Turma", command=add_turma, font=("Arial", 14), width=200)
button_add_turma.pack(pady=(20, 30))  # Aumenta o espaço abaixo do botão

app.mainloop()

# Fechar conexão com o banco de dados ao sair
cursor.close()
db_connection.close()
