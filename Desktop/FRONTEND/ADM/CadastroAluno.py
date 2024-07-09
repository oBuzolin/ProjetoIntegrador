import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random
#imposts criptografia
from hashlib import sha256

comf = 0
janela = ctk.CTk()

# banco iniciar

class Application():
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

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Aluno", font=('Arial', 20, 'bold'),
                             text_color=('white'))
        label.place(x=25, y=20)

        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300,
                                  font=('Roboto', 14), corner_radius=10)
        nome_entry.place(x=25, y=80)

        email_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Email", width=300,
                                   font=('Roboto', 14), corner_radius=10)
        email_entry.place(x=25, y=135)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Curso", width=300,
                                   font=('Roboto', 14), corner_radius=10)
        curso_entry.place(x=25, y=190)

        checkbox_var = ctk.BooleanVar()
        def toggle_show_password():
            valor = checkbox_var.get()
            if valor:
                senha_entry.configure(show="")
            else:
                senha_entry.configure(show="*")
        
        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=310)

        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*", corner_radius=10)
        senha_entry.place(x=25, y=245)
        
        global nome1
        global email
        global senha
        global Curso
        global RA

        def get_dados():
            nome1 = nome_entry.get().strip()
            email = email_entry.get().strip()
            senha = senha_entry.get().strip()
            Curso = curso_entry.get().strip()
            return nome1, email, senha, Curso
        
        def valida():
            nome, email, senha1, Curso = get_dados()
            if not nome:
                label_errorSS.place(x=25,y=1007)
                label_NAceito.place(x=25,y=1007)
                label_errorNV.pack()  
                label_errorNV.place(x=25,y=107)
                comf = 0
            else:
                label_errorNV.place(x=25,y=1007)
                nomeC = nome.split()
                contagem = len(nomeC)
                if contagem < 2:
                    label_NAceito.place(x=25,y=1007)
                    label_errorSS.pack()  
                    label_errorSS.place(x=25,y=107)
                    comf = 0
                else:
                    label_errorSS.place(x=25,y=1007)
                    label_NAceito.pack()  
                    label_NAceito.place(x=25,y=107)
                    if not email:
                        label_errorSAR.place(x=25,y=1620)
                        label_EAceito.place(x=25,y=1620)
                        label_errorEV.pack()  
                        label_errorEV.place(x=25,y=162)
                        comf = 0
                    else:
                        label_EAceito.place(x=25,y=1620)
                        label_errorEV.place(x=25,y=1620)
                        if not "@gmail.com" in email:
                            label_errorSAR.pack()  
                            label_errorSAR.place(x=25,y=162)
                            comf = 0
                        else:
                            label_errorSAR.place(x=25,y=1620)
                            label_errorEV.place(x=25,y=1620)
                            label_EAceito.pack()  
                            label_EAceito.place(x=25,y=162)
                            if not Curso:
                                label_errorCM8.place(x=25,y=1620)
                                label_CAceito.place(x=25,y=1620)
                                label_errorCV.pack()  
                                label_errorCV.place(x=25,y=217)
                                comf = 0
                            else:
                                label_CAceito.place(x=25,y=1620)
                                label_errorCV.place(x=25,y=1620)
                                if len(Curso) < 8:
                                    label_errorCM8.pack()  
                                    label_errorCM8.place(x=25,y=217)
                                    comf = 0
                                else:
                                    label_errorCV.place(x=25,y=1620)
                                    label_errorCM8.place(x=25,y=1620)
                                    label_CAceito.pack()  
                                    label_CAceito.place(x=25,y=217)
                                    if not senha1:
                                        label_errorCM8.place(x=25,y=1620)
                                        label_SAceito.place(x=25,y=1620)
                                        label_errorSV.pack()  
                                        label_errorSV.place(x=25,y=272)
                                        comf = 0
                                    else:
                                        label_SAceito.place(x=25,y=1620)
                                        label_errorSV.place(x=25,y=1620)
                                        if len(senha1) < 8:
                                            label_errorSM8.pack()  
                                            label_errorSM8.place(x=25,y=272)
                                            comf = 0
                                        else:
                                            label_errorSV.place(x=25,y=1620)
                                            label_errorSM8.place(x=25,y=1620)
                                            label_SAceito.pack()  
                                            label_SAceito.place(x=25,y=272)
                                            comf = 1
                                            return comf

        def on_login_button_click(event):
            valida()
            nome, email, senha1, Curso = get_dados()
            RA = random.randint(10000, 99999)
            comf = valida()
            
            if comf == 1:
                senha = sha256(senha1.encode())
                senha = senha.hexdigest()
                def obter_informacoes_usuario():
                    return {'nome': nome, 'RA': RA, 'email': email, 'senha': senha, 'Curso': Curso}

                def inserir_dados_mysql(dados):
                    try:
                        conexao = mysql.connector.connect(
                            host="143.106.241.3",
                            port=3306,
                            user="cl201107",
                            password="cl*02032005",
                            database="cl201107"
                        )
                        cursor = conexao.cursor()
                        sql = "SELECT senha FROM Minerva_Aluno WHERE email = %s"
                        cursor.execute(sql, (email,))

                        result = cursor.fetchone()
                    
                        if result:
                            label_CAceito.place(x=25,y=1620)
                            label_errorJE.place(x=25,y=162)
                        else:
                            sql = "INSERT INTO Minerva_Aluno (Nome, RA, email, senha, Curso) VALUES (%(nome)s, %(RA)s, %(email)s, %(senha)s, %(Curso)s)"
                            cursor.execute(sql, dados)
                            conexao.commit()
                            print("Dados inseridos com sucesso!")
                            janela.destroy()
                    except mysql.connector.Error as erro:
                        print(f"Erro ao inserir dados no banco de dados: {erro}")
                        conexao.rollback()
                    finally:
                        cursor.close()
                        conexao.close()

                informacoes = obter_informacoes_usuario()
                inserir_dados_mysql(informacoes)
                comf += 1
            else:
                print("incompleto")

        cadastro_buttom = ctk.CTkButton(master=cadastro_frame, text="Cadastro", width=300, corner_radius=10)
        cadastro_buttom.place(x=25, y=350)
        cadastro_buttom.bind("<Button-1>", on_login_button_click)

        # Erros
        global label_errorNV  # nome vazio
        global label_errorSS  # sem sobrenome
        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="Nome vazio, coloque um nome válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSS = ctk.CTkLabel(master=cadastro_frame, text="Sem sobrenome, coloque um nome válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))

        # Email
        global label_errorEV  # email vazio
        global label_errorSAR  # sem @gmail.com
        global label_errorJE
        label_errorEV = ctk.CTkLabel(master=cadastro_frame, text="Email vazio, coloque um email válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSAR = ctk.CTkLabel(master=cadastro_frame, text="Sem @gmail, coloque um email válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorJE = ctk.CTkLabel(master=cadastro_frame, text="Email já existe", font=('Arial', 9, 'bold'),
                                     text_color=('red'))

        # Cursos
        global label_errorCV  # curso vazio
        global label_errorCM8  # menos de oito caracteres
        label_errorCV = ctk.CTkLabel(master=cadastro_frame, text="Curso vazio, coloque um curso válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorCM8 = ctk.CTkLabel(master=cadastro_frame, text="Curso com menos de 8 caracteres, coloque um curso válido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))

        # Senhas
        global label_errorSV  # senha vazia
        global label_errorSM8  # menos de oito caracteres
        label_errorSV = ctk.CTkLabel(master=cadastro_frame, text="Senha vazia, coloque um senha válida", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSM8 = ctk.CTkLabel(master=cadastro_frame, text="Senha com menos de 8 caracteres, coloque uma senha válida", font=('Arial', 9, 'bold'),
                                     text_color=('red'))

        # Aceito
        global label_NAceito  # nome
        global label_EAceito  # Email
        global label_CAceito  # Curso
        global label_SAceito  # senha
        label_NAceito = ctk.CTkLabel(master=cadastro_frame, text="Nome válido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_EAceito = ctk.CTkLabel(master=cadastro_frame, text="Email válido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_CAceito = ctk.CTkLabel(master=cadastro_frame, text="Curso válido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_SAceito = ctk.CTkLabel(master=cadastro_frame, text="Senha válida", font=('Arial', 9, 'bold'),
                                     text_color=('green'))

Application()
