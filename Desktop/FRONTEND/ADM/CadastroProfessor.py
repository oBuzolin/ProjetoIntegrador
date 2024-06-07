
import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random
#imposts criptografia
from hashlib import sha256
comf = 0;
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
        janela.geometry("700x400")
        janela.title("Cadastro de Aluno")
        janela.resizable(False, False)

    def telaCadastroAluno(self):
        titulo_label = ctk.CTkLabel(master=janela, text="Cadastre-se como professor \n na plataforma",
                                    font=("Roboto", 20), text_color="#00B0F0")
        titulo_label.place(x=50, y=10)

        cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cadastro_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Professor", font=('Arial', 20, 'bold'),
                             text_color=('white'))
        label.place(x=25, y=5)

        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300,
                                  font=('Roboto', 14))
        nome_entry.place(x=25, y=45)

        email_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Email", width=300,
                                   font=('Roboto', 14))
        email_entry.place(x=25, y=103)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="diciplina", width=300,
                                   font=('Roboto', 14))
        curso_entry.place(x=25, y=161)

        CargH_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="carga horaria", width=145,
                                   font=('Roboto', 14))
        CargH_entry.place(x=25, y=219)
        
        DiaS_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="quantidade de dias de trabalho por semana", width=145,
                                   font=('Roboto', 14))
        DiaS_entry.place(x=180, y=219)

        checkbox_var = ctk.BooleanVar()
        def toggle_show_password():
            valor = checkbox_var.get()
            if valor == True:
                senha_entry.configure(show="")
            else:
                senha_entry.configure(show="*")
        # Criar a CTkCheckBox e associar com a variável de controle
        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=315)

        # Criar a CTkEntry para a senha
        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=275)
        
        
        global nome1
        global email
        global senha
        global Curso
        global RA
        global CargH
        global DiaS
        def get_dados():
            nome1 = nome_entry.get().strip()
            email = email_entry.get().strip()
            senha = senha_entry.get().strip()
            Curso = curso_entry.get().strip()
            CargH = CargH_entry.get().strip()
            DiaS = DiaS_entry.get().strip()

            return(nome1,email,senha,Curso,DiaS,CargH)
        
        
        def valida():
            nome, email, senha1, Curso,CargH,DiaS = get_dados()
            if not nome:
                label_errorSS.place(x=25,y=1007)
                label_NAceito.place(x=25,y=1007)
                label_errorNV.pack()  
                label_errorNV.place(x=25,y=74)
                comf = 0

            else:  # Esconde mensagem de erro se nome for válido
                #label_errorNV.destroy()
                #label_errorNV.pack_forget()
                label_errorNV.place(x=25,y=1007)
                nomeC = nome.split()
                contagem = len(nomeC)
                if contagem < 2:
                    label_NAceito.place(x=25,y=1007)
                    label_errorSS.pack()  
                    label_errorSS.place(x=25,y=74)
                    comf = 0
                else:
                    label_errorSS.place(x=25,y=1007)
                    label_NAceito.pack()  
                    label_NAceito.place(x=25,y=74)
                    if not email:
                        label_errorSAR.place(x=25,y=1620)
                        label_EAceito.place(x=25,y=1620)
                        label_errorEV.pack()  
                        label_errorEV.place(x=25,y=130)
                        comf = 0
                    else:
                        label_EAceito.place(x=25,y=1620)
                        label_errorEV.place(x=25,y=1620)
                        if not "@gmail.com" in email:
                            label_errorSAR.pack()  
                            label_errorSAR.place(x=25,y=130)
                            comf = 0
                        else:
                            label_errorSAR.place(x=25,y=1620)
                            label_errorEV.place(x=25,y=1620)
                            label_EAceito.pack()  
                            label_EAceito.place(x=25,y=130)
                            if not Curso:
                                label_errorCM8.place(x=25,y=1620)
                                label_CAceito.place(x=25,y=1620)
                                label_errorCV.pack()  
                                label_errorCV.place(x=25,y=190)
                                comf = 0
                            else:
                                label_CAceito.place(x=25,y=1620)
                                label_errorCV.place(x=25,y=1620)
                                if len(Curso) < 8:
                                    label_errorCM8.pack()  
                                    label_errorCM8.place(x=25,y=190)
                                    comf = 0
                                else:
                                    label_errorCM8.place(x=25,y=1620)
                                    label_errorCV.place(x=25,y=1620)
                                    label_CAceito.pack()  
                                    label_CAceito.place(x=25,y=190)
                                    if not CargH:
                                      label_errorCHMO.place(x=25,y=1620)
                                      label_CHAceito.place(x=25,y=1620)
                                      label_errorCHV.pack()  
                                      label_errorCHV.place(x=25,y=246)
                                      comf = 0
                                    else:
                                      label_CHAceito.place(x=25,y=1620)
                                      label_errorCHV.place(x=25,y=1620)
                                      if len(CargH) < 8:
                                          label_errorCM8.pack()  
                                          label_errorCM8.place(x=25,y=250)
                                          comf = 0
                                      else:
                                        label_errorCHMO.place(x=25,y=1620)
                                        label_errorCHV.place(x=25,y=1620)
                                        label_CHAceito.pack()  
                                        label_CHAceito.place(x=25,y=250)
                                        if not DiaS:
                                          label_errorCHMO.place(x=25,y=1620)
                                          label_CHAceito.place(x=25,y=1620)
                                          label_errorCHV.pack()  
                                          label_errorCHV.place(x=180,y=217)
                                          comf = 0
                                        else:
                                            label_errorCHV.place(x=25,y=1620)
                                            label_CHAceito.place(x=25,y=1620)
                                            if len(DiaS) < 8:
                                                label_errorCHMO.pack()  
                                                label_errorCHMO.place(x=180,y=217)
                                                comf = 0
                                            else:
                                                label_errorCHMO.place(x=25,y=1620)
                                                label_errorCHV.place(x=25,y=1620)
                                                label_CHAceito.pack()  
                                                label_CHAceito.place(x=25,y=250)
                                                if not senha1:
                                                    label_errorSM8.place(x=25,y=1620)
                                                    label_SAceito.place(x=25,y=1620)
                                                    label_errorSV.pack()  
                                                    label_errorSV.place(x=150,y=315)
                                                    comf = 0
                                                else:
                                                    label_SAceito.place(x=25,y=1620)
                                                    label_errorSV.place(x=25,y=1620)
                                                    if len(senha1) < 8:
                                                        label_errorSM8.pack()  
                                                        label_errorSM8.place(x=150,y=315)
                                                        comf = 0
                                                    else:
                                                        label_errorSV.place(x=25,y=1620)
                                                        label_errorSM8.place(x=25,y=1620)
                                                        label_SAceito.pack()  
                                                        label_SAceito.place(x=150,y=315)
                                                        comf = 1
                                                        return comf
    # função de cadastro
        def on_login_button_click(event):
            valida()
            nome, email, senha1, Curso, CargH, DiaS = get_dados()
            comf = valida()
            RA = random.randint(10000, 99999)
            if comf == 1:
                senha = sha256(senha1.encode())
                senha = senha.hexdigest()
                def obter_informacoes_usuario():
                    return {'nome': nome, 'Diciplina': Curso,'CargaHoraria': CargH, 'DiasSemana': DiaS,'email': email, 'senha': senha,'RA':RA}

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
                        sql = "SELECT senha FROM Minerva_Professor WHERE email = %s"
                        cursor.execute(sql, (email,))

                        # Obter o resultado da consulta
                        result = cursor.fetchone()  # Retorna uma única linha se encontrar
                    
                        if result:
                            label_CAceito.place(x=25,y=1620)
                            label_errorJE.place(x=25,y=162)

                        else:
                            sql = "INSERT INTO Minerva_Professor (Nome, Disciplina, CargaHoraria, DiasSemana, email, senha, RA) VALUES (%(nome)s, %(Diciplina)s, %(CargaHoraria)s, %(DiasSemana)s, %(email)s, %(senha)s, %(RA)s)"

                            cursor.execute(sql, dados)

                            conexao.commit()
                            print("Dados inseridos com sucesso!")
                            print(senha)
                            janela.destroy()
                    except mysql.connector.Error as erro:
                        print(f"Erro ao inserir dados no banco de dados: {erro}")
                        conexao.rollback()

                    finally:
                        cursor.close()
                        conexao.close()
                informacoes = obter_informacoes_usuario()
                inserir_dados_mysql(informacoes)
                comf = comf+1
            else:
                print("incompleto")



        cadastro_buttom = ctk.CTkButton(master=cadastro_frame, text="cadastro", width=300)
        cadastro_buttom.place(x=25, y=350)
        cadastro_buttom.bind("<Button-1>", on_login_button_click,)
        #
        #
        #erros
        #NOME
        global label_errorNV#nome vazio
        global label_errorSS#sem sobrenome
        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="nome vazio, coloque um nome valido", font=('Arial', 9, ),
                                     text_color=('red'),fg_color=None)
        label_errorSS = ctk.CTkLabel(master=cadastro_frame, text="sem sobrenome, coloque um nome valido", font=('Arial', 9, ),
                                     text_color=('red'))
        #
        #EMAIL
        global label_errorEV#email vazio
        global label_errorSAR#sem @gmail.com
        global label_errorJE
        label_errorEV = ctk.CTkLabel(master=cadastro_frame, text="Email vazio, coloque um email valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSAR = ctk.CTkLabel(master=cadastro_frame, text="sem @gmail, coloque um email valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorJE = ctk.CTkLabel(master=cadastro_frame, text="email já existe", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #
        #Cursos
        global label_errorCV#curso vazio
        global label_errorCM8# menos de oito caracter
        label_errorCV = ctk.CTkLabel(master=cadastro_frame, text="curso vazio, coloque um curso valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorCM8 = ctk.CTkLabel(master=cadastro_frame, text="curso com menos de 8 caracteres, coloque um Curso valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #
        
        #carga horaria/ dias por semana
        global label_errorCHV#curso vazio
        global label_errorCHMO# menos de oito caracter
        label_errorCHV = ctk.CTkLabel(master=cadastro_frame, text="vazio, coloque um valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorCHMO = ctk.CTkLabel(master=cadastro_frame, text="menos de 8 caracteres, coloque um valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #
        #
        #senhas
        global label_errorSV#curso vazio
        global label_errorSM8# menos de oito caracter
        label_errorSV = ctk.CTkLabel(master=cadastro_frame, text="senha vazio, coloque um senha valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        label_errorSM8 = ctk.CTkLabel(master=cadastro_frame, text="senha com menos de 8 caracteres, coloque um senha valido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #
        #aceito
        global label_NAceito#nome
        global label_EAceito#Email
        global label_CAceito#Curso
        global label_SAceito#senha
        global label_DAceito#DIas
        global label_CHAceito#Carga
        label_CHAceito = ctk.CTkLabel(master=cadastro_frame, text="Carga horaria valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_DAceito = ctk.CTkLabel(master=cadastro_frame, text="Dias de semana valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_NAceito = ctk.CTkLabel(master=cadastro_frame, text="Nome valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_EAceito = ctk.CTkLabel(master=cadastro_frame, text="email valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_CAceito = ctk.CTkLabel(master=cadastro_frame, text="Curso valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))
        label_SAceito = ctk.CTkLabel(master=cadastro_frame, text="senha valido", font=('Arial', 9, 'bold'),
                                     text_color=('green'))

        
        

Application()

