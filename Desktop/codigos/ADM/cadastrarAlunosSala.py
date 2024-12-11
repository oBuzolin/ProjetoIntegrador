import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Configuração do CustomTkinter
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Função para validar o ID da turma e os RAs
def validar_dados():
    turma_id = entry_turma_id.get()
    ra_list = entry_ra.get().split(',')
    
    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="143.106.241.3", 
        port=3306, 
        user="cl201107", 
        password="cl*02032005", 
        database="cl201107"
    )
    cursor = conexao.cursor()
    
    # Validação do ID da turma
    cursor.execute("SELECT COUNT(*) FROM Minerva_Turma WHERE id_Turma = %s", (turma_id,))
    turma_existe = cursor.fetchone()[0] > 0
    if not turma_existe:
        messagebox.showerror("Erro", "ID de turma não encontrado.")
        cursor.close()
        conexao.close()
        return
    
    # Validação dos RAs dos alunos e checagem de duplicatas
    ra_validos = []
    ra_duplicados = []
    for ra in ra_list:
        ra = ra.strip()
        
        # Verifica se o RA existe na tabela de alunos
        cursor.execute("SELECT COUNT(*) FROM Minerva_Aluno WHERE RA = %s", (ra,))
        if cursor.fetchone()[0] > 0:
            # Verifica se o RA já está cadastrado na turma
            cursor.execute("""
                SELECT COUNT(*) FROM Minerva_MatriculaTurma
                WHERE ra_id = %s AND id_Turma_id = %s
            """, (ra, turma_id))
            if cursor.fetchone()[0] == 0:
                ra_validos.append(ra)
            else:
                ra_duplicados.append(ra)
        else:
            messagebox.showerror("Erro", f"RA {ra} não encontrado.")
            cursor.close()
            conexao.close()
            return
    
    # Inserção dos dados na tabela Minerva_MatriculaTurma
    data_matricula = datetime.now().date()
    try:
        for ra in ra_validos:
            cursor.execute("""
                INSERT INTO Minerva_MatriculaTurma (ra_id, id_Turma_id, dataMatricula)
                VALUES (%s, %s, %s)
            """, (ra, turma_id, data_matricula))
        conexao.commit()
        
        # Mensagem de sucesso
        if ra_duplicados:
            messagebox.showinfo("Aviso", f"Alunos cadastrados com sucesso, exceto os seguintes RAs que já estavam matriculados: {', '.join(ra_duplicados)}.")
        else:
            messagebox.showinfo("Sucesso", "Alunos matriculados com sucesso.")
        
        # Fechar a janela após inserção bem-sucedida
        app.destroy()
        
    except mysql.connector.Error as err:
        conexao.rollback()
        messagebox.showerror("Erro", f"Erro ao inserir dados: {err}")
    finally:
        # Fechando a conexão com o banco de dados
        cursor.close()
        conexao.close()

# Interface gráfica aprimorada
app = ctk.CTk()
app.title("Cadastro de Matrículas")
app.geometry("400x350")
app.configure(bg="#1c1c1c")  # Cor de fundo mais escura

# Layout Centralizado
container = ctk.CTkFrame(app, width=350, height=300, corner_radius=10)
container.pack(pady=20, padx=20)

# Título
label_title = ctk.CTkLabel(container, text="Cadastro de Matrículas", font=("Arial", 18, "bold"))
label_title.pack(pady=(15, 20))

# Campo para ID da turma
label_turma_id = ctk.CTkLabel(container, text="ID da Turma:", font=("Arial", 12))
label_turma_id.pack(pady=(0, 5))
entry_turma_id = ctk.CTkEntry(container, width=250)
entry_turma_id.pack(pady=(0, 15))

# Campo para RAs dos alunos
label_ra = ctk.CTkLabel(container, text="RAs dos Alunos (separados por vírgula):", font=("Arial", 12))
label_ra.pack(pady=(0, 5))
entry_ra = ctk.CTkEntry(container, width=250)
entry_ra.pack(pady=(0, 15))

# Botão de envio
button_enviar = ctk.CTkButton(container, text="Enviar", command=validar_dados, width=150, height=40, font=("Arial", 12))
button_enviar.pack(pady=(10, 20))

app.mainloop()
