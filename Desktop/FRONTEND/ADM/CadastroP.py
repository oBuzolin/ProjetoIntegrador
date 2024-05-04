import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random

janela = ctk.CTk()

# banco iniciar

class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaCadastroProfessor()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Cadastro de Aluno")
        janela.resizable(False, False)

    def telaCadastroProfessor(self):
        titulo_label = ctk.CTkLabel(master=janela, text="Cadastre-se como aluno \n na plataforma",
                                    font=("Roboto", 20), text_color="#00B0F0")
        titulo_label.place(x=50, y=10)

        cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cadastro_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Aluno", font=('Arial', 20, 'bold'),
                             text_color=('white'))
        label.place(x=25, y=5)

        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300,
                                  font=('Roboto', 14))
        nome_entry.place(x=25, y=80)

        email_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Email", width=300,
                                   font=('Roboto', 14))
        email_entry.place(x=25, y=135)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="curso", width=300,
                                   font=('Roboto', 14))
        curso_entry.place(x=25, y=190)

        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300,
                                   font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=245)
        
        global nome
        global email
        global senha
        global Curso
        global RA
        def get_dados():
            nome = nome_entry.get().strip()
            email = email_entry.get().strip()
            senha = senha_entry.get().strip()
            Curso = curso_entry.get().strip()
            return(nome,email,senha,Curso)
        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Lembre-se de mim sempre")
        checkbox.place(x=25, y=285)
        
        def valida():
            nome, email, senha, Curso = get_dados()
            if not nome:
                label_errorSS.place(x=25,y=1007)
                label_NAceito.place(x=25,y=1007)
                label_errorNV.pack()  
                label_errorNV.place(x=25,y=107)
                

            else:  # Esconde mensagem de erro se nome for válido
                #label_errorNV.destroy()
                #label_errorNV.pack_forget()
                label_errorNV.place(x=25,y=1007)
                nomeC = nome.split()
                contagem = len(nomeC)
                if contagem < 2:
                    label_NAceito.place(x=25,y=1007)
                    label_errorSS.pack()  
                    label_errorSS.place(x=25,y=107)
                else:
                    label_errorSS.place(x=25,y=1007)
                    label_NAceito.pack()  
                    label_NAceito.place(x=25,y=107)
                    


    # função de cadastro
        def on_login_button_click(event):
            valida()
            nome, email, senha, Curso = get_dados()
            RA = random.randint(10000, 99999)
            def obter_informacoes_usuario():
                return {'nome': nome, 'RA': RA, 'email': email, 'senha': senha,'Curso':Curso}

            # def inserir_dados_mysql(dados):
                # try:
                    # conexao = mysql.connector.connect(
                        # host="143.106.241.3",
                        # port=3306,
                        # user="cl201107",
                        # password="cl*02032005",
                        # database="cl201107"
                    # )
            # 
                    # cursor = conexao.cursor()
            # 
                    # sql = "INSERT INTO Minerva_Aluno (Nome, RA, email, senha, Curso) VALUES (%(nome)s, %(RA)s, %(email)s, %(senha)s, %(Curso)s)"
            # 
                    # cursor.execute(sql, dados)
            # 
                    # conexao.commit()
                    # print("Dados inseridos com sucesso!")
            # 
                # except mysql.connector.Error as erro:
                    # print(f"Erro ao inserir dados no banco de dados: {erro}")
                    # conexao.rollback()
            # 
                # finally:
                    # cursor.close()
                    # conexao.close()
            # informacoes = obter_informacoes_usuario()
            # inserir_dados_mysql(informacoes)




        cadastro_buttom = ctk.CTkButton(master=cadastro_frame, text="cadastro", width=300)
        cadastro_buttom.place(x=25, y=325)
        cadastro_buttom.bind("<Button-1>", on_login_button_click,)
        #
        #
        #erros
        global label_errorNV#nome vazio
        global label_errorSS#sem sobrenome
        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="nome vazio, coloque um nome valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSS = ctk.CTkLabel(master=cadastro_frame, text="sem sobrenome, coloque um nome valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #
        #
        #
        #aceito
        global label_NAceito#nome vazio
        global label_EAceito#sem sobrenome
        label_NAceito = ctk.CTkLabel(master=cadastro_frame, text="nome valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_EAceito = ctk.CTkLabel(master=cadastro_frame, text="nome vazio, coloque um nome valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        

        
        

Application()

