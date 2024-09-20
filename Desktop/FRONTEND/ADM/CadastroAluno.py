import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random
from hashlib import sha256

janela = ctk.CTk()

# Banco iniciar
class Application:
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaCadastroAluno()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x450")
        janela.title("Cadastro de Aluno")
        janela.resizable(False, False)

    def telaCadastroAluno(self):
        titulo_label = ctk.CTkLabel(master=janela, text="Cadastre-se como aluno \n na plataforma",
                                    font=("Roboto", 20, 'bold'), text_color="#00B0F0")
        titulo_label.place(x=50, y=20)

        cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=420, corner_radius=15)
        cadastro_frame.pack(side=ctk.RIGHT, padx=20, pady=20)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Aluno", font=('Arial', 20, 'bold'), text_color=('white'))
        label.place(x=25, y=20)

        # Entradas
        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300, font=('Roboto', 14), corner_radius=10)
        nome_entry.place(x=25, y=80)

        usuario_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Usuário", width=300, font=('Roboto', 14), corner_radius=10)
        usuario_entry.place(x=25, y=135)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Curso", width=300, font=('Roboto', 14), corner_radius=10)
        curso_entry.place(x=25, y=190)

        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*", corner_radius=10)
        senha_entry.place(x=25, y=245)

        # Checkbox mostrar senha
        checkbox_var = ctk.BooleanVar()
        def toggle_show_password():
            senha_entry.configure(show="" if checkbox_var.get() else "*")
        
        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=310)

        # Erros e mensagens de sucesso
        global label_errorNV, label_errorSS, label_errorEV, label_errorSAR, label_errorJE
        global label_errorCV, label_errorCM8, label_errorSV, label_errorSM8
        global label_NAceito, label_EAceito, label_CAceito, label_SAceito

        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="Nome vazio, coloque um nome válido", font=('Arial', 9, 'bold'), text_color='red')
        label_errorSS = ctk.CTkLabel(master=cadastro_frame, text="Sem sobrenome, coloque um nome válido", font=('Arial', 9, 'bold'), text_color='red')
        label_errorEV = ctk.CTkLabel(master=cadastro_frame, text="Usuário vazio, coloque um usuário válido", font=('Arial', 9, 'bold'), text_color='red')
        label_errorSAR = ctk.CTkLabel(master=cadastro_frame, text="Usuário deve conter '@gmail.com'", font=('Arial', 9, 'bold'), text_color='red')
        label_errorJE = ctk.CTkLabel(master=cadastro_frame, text="Usuário já existe", font=('Arial', 9, 'bold'), text_color='red')

        label_errorCV = ctk.CTkLabel(master=cadastro_frame, text="Curso vazio, coloque um curso válido", font=('Arial', 9, 'bold'), text_color='red')
        label_errorCM8 = ctk.CTkLabel(master=cadastro_frame, text="Curso com menos de 8 caracteres", font=('Arial', 9, 'bold'), text_color='red')

        label_errorSV = ctk.CTkLabel(master=cadastro_frame, text="Senha vazia, coloque uma senha válida", font=('Arial', 9, 'bold'), text_color='red')
        label_errorSM8 = ctk.CTkLabel(master=cadastro_frame, text="Senha com menos de 8 caracteres", font=('Arial', 9, 'bold'), text_color='red')

        # Mensagens de aceitação
        label_NAceito = ctk.CTkLabel(master=cadastro_frame, text="Nome válido", font=('Arial', 9, 'bold'), text_color='green')
        label_EAceito = ctk.CTkLabel(master=cadastro_frame, text="Usuário válido", font=('Arial', 9, 'bold'), text_color='green')
        label_CAceito = ctk.CTkLabel(master=cadastro_frame, text="Curso válido", font=('Arial', 9, 'bold'), text_color='green')
        label_SAceito = ctk.CTkLabel(master=cadastro_frame, text="Senha válida", font=('Arial', 9, 'bold'), text_color='green')

        def get_dados():
            return {
                "nome": nome_entry.get().strip(),
                "usuario": usuario_entry.get().strip(),
                "senha": senha_entry.get().strip(),
                "curso": curso_entry.get().strip(),
            }

        def exibe_erros(erros):
            # Limpa as mensagens anteriores
            label_errorNV.place_forget()
            label_errorSS.place_forget()
            label_errorEV.place_forget()
            label_errorSAR.place_forget()
            label_errorJE.place_forget()
            label_errorCV.place_forget()
            label_errorCM8.place_forget()
            label_errorSV.place_forget()
            label_errorSM8.place_forget()

            # Exibe os erros conforme a chave
            for erro in erros:
                if erro == "Nome vazio":
                    label_errorNV.place(x=25, y=107)
                elif erro == "Sem sobrenome":
                    label_errorSS.place(x=25, y=107)
                elif erro == "Usuário vazio":
                    label_errorEV.place(x=25, y=162)
                elif erro == "Usuário deve conter '@gmail.com'":
                    label_errorSAR.place(x=25, y=162)
                elif erro == "Usuário já existe":
                    label_errorJE.place(x=25, y=162)
                elif erro == "Curso vazio":
                    label_errorCV.place(x=25, y=217)
                elif erro == "Curso com menos de 8 caracteres":
                    label_errorCM8.place(x=25, y=217)
                elif erro == "Senha vazia":
                    label_errorSV.place(x=25, y=272)
                elif erro == "Senha com menos de 8 caracteres":
                    label_errorSM8.place(x=25, y=272)

        def valida():
            dados = get_dados()
            erros = []

            # Validação nome
            if not dados["nome"]:
                erros.append("Nome vazio")
            elif len(dados["nome"].split()) < 2:
                erros.append("Sem sobrenome")

            # Validação usuário
            if not dados["usuario"]:
                erros.append("Usuário vazio")
            elif "@gmail.com" not in dados["usuario"]:
                erros.append("Usuário deve conter '@gmail.com'")

            # Validação curso
            if not dados["curso"]:
                erros.append("Curso vazio")
            elif len(dados["curso"]) < 8:
                erros.append("Curso com menos de 8 caracteres")

            # Validação senha
            if not dados["senha"]:
                erros.append("Senha vazia")
            elif len(dados["senha"]) < 8:
                erros.append("Senha com menos de 8 caracteres")

            return erros

        def on_login_button_click(event):
            erros = valida()
            if erros:
                exibe_erros(erros)
                return

            dados = get_dados()
            RA = random.randint(10000, 99999)
            senha_hash = sha256(dados["senha"].encode()).hexdigest()

            dados_atualizados = {
                "nome": dados["nome"],
                "RA": RA,
                "usuario": dados["usuario"],
                "senha": senha_hash,
                "Curso": dados["curso"],
            }

            try:
                conexao = mysql.connector.connect(
                    host="143.106.241.3",
                    port=3306,
                    user="cl201107",
                    password="cl*02032005",
                    database="cl201107"
                )
                cursor = conexao.cursor()
                sql = "SELECT senha FROM Minerva_Aluno WHERE usuario = %s"
                cursor.execute(sql, (dados["usuario"],))

                result = cursor.fetchone()
                if result:
                    exibe_erros(["Usuário já existe"])
                else:
                    sql = "INSERT INTO Minerva_Aluno (Nome, RA, usuario, senha, Curso) VALUES (%(nome)s, %(RA)s, %(usuario)s, %(senha)s, %(Curso)s)"
                    cursor.execute(sql, dados_atualizados)
                    conexao.commit()
                    print("Dados inseridos com sucesso!")
                    janela.destroy()

            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no banco de dados: {erro}")
                conexao.rollback()

            finally:
                cursor.close()
                conexao.close()

        cadastro_button = ctk.CTkButton(master=cadastro_frame, text="Cadastro", width=300, corner_radius=10)
        cadastro_button.place(x=25, y=350)
        cadastro_button.bind("<Button-1>", on_login_button_click)

Application()
