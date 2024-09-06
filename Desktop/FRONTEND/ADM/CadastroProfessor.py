import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random
from hashlib import sha256
comf = 0
janela = ctk.CTk()

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
        titulo_label = ctk.CTkLabel(master=janela, text="Cadastre-se como professor \n na plataforma",
                                    font=("Roboto", 20), text_color="#00B0F0")
        titulo_label.place(x=50, y=10)

        cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cadastro_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Professor", font=('Arial', 20, 'bold'),
                             text_color='white')
        label.place(x=25, y=5)

        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300,
                                  font=('Roboto', 14))
        nome_entry.place(x=25, y=45)

        usuario_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="usuario", width=300,
                                   font=('Roboto', 14))
        usuario_entry.place(x=25, y=103)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Disciplina", width=300,
                                   font=('Roboto', 14))
        curso_entry.place(x=25, y=161)

        CargH_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Carga Horária", width=145,
                                   font=('Roboto', 14))
        CargH_entry.place(x=25, y=219)

        DiaS_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Quantidade de dias de trabalho por semana", width=145,
                                  font=('Roboto', 14))
        DiaS_entry.place(x=180, y=219)

        checkbox_var = ctk.BooleanVar()

        def toggle_show_password():
            valor = checkbox_var.get()
            senha_entry.configure(show="" if valor else "*")

        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=315)

        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=275)

        global nome1, usuario, senha, Curso, RA, CargH, DiaS

        def get_dados():
            nome1 = nome_entry.get().strip()
            usuario = usuario_entry.get().strip()
            senha = senha_entry.get().strip()
            Curso = curso_entry.get().strip()
            CargH = CargH_entry.get().strip()
            DiaS = DiaS_entry.get().strip()
            return nome1, usuario, senha, Curso, CargH, DiaS

        def valida():
            nome, usuario, senha1, Curso, CargH, DiaS = get_dados()
            if not nome:
                label_errorNV.place(x=25, y=74)
                comf = 0
            else:
                label_errorNV.place(x=25, y=1007)
                nomeC = nome.split()
                contagem = len(nomeC)
                if contagem < 2:
                    label_errorSS.place(x=25, y=74)
                    comf = 0
                else:
                    label_errorSS.place(x=25, y=1007)
                    label_NAceito.place(x=25, y=74)
                    if not usuario:
                        label_EAceito.place(x=25, y=1300)
                        label_errorEV.place(x=25, y=130)
                        comf = 0
                    else:
                        label_errorEV.place(x=25, y=1620)
                        if "@gmail.com" not in usuario:
                            label_errorSAR.place(x=25, y=130)
                            comf = 0
                        else:
                            label_errorSAR.place(x=25, y=1620)
                            label_EAceito.place(x=25, y=130)
                            if not Curso:
                                label_errorCV.place(x=25, y=190)
                                comf = 0
                            else:
                                label_errorCV.place(x=25, y=1620)
                                if len(Curso) < 8:
                                    label_errorCM8.place(x=25, y=190)
                                    comf = 0
                                else:
                                    label_errorCM8.place(x=25, y=1620)
                                    label_CAceito.place(x=25, y=190)
                                    if not CargH:
                                        label_errorCHV.place(x=25, y=246)
                                        comf = 0
                                    else:
                                        label_errorCHV.place(x=25, y=1620)
                                        if len(CargH) > 2:
                                            label_errorCHMO.place(x=25, y=246)
                                            comf = 0
                                        else:
                                            label_errorCHMO.place(x=25, y=1620)
                                            label_CHAceito.place(x=25, y=246)
                                            if not DiaS:
                                                label_errorCHV.place(x=180, y=246)
                                                comf = 0
                                            else:
                                                label_errorCHV.place(x=25, y=1620)
                                                if len(DiaS) > 1:
                                                    label_errorCHMO.place(x=180, y=246)
                                                    comf = 0
                                                else:
                                                    label_errorCHMO.place(x=25, y=1620)
                                                    label_CHAceito.place(x=25, y=246)
                                                    if not senha1:
                                                        label_errorSV.place(x=150, y=315)
                                                        comf = 0
                                                    else:
                                                        label_errorSV.place(x=25, y=1620)
                                                        if len(senha1) < 8:
                                                            label_errorSM8.place(x=150, y=315)
                                                            comf = 0
                                                        else:
                                                            label_errorSM8.place(x=25, y=1620)
                                                            label_SAceito.place(x=150, y=315)
                                                            comf = 1
                                                            return comf
            return comf

        def on_login_button_click(event):
            valida()
            nome, usuario, senha1, Curso, CargH, DiaS = get_dados()
            comf = valida()
            matricula = random.randint(10000, 99999)
            if comf == 1:
                senha = sha256(senha1.encode()).hexdigest()
                def obter_informacoes_usuario():
                    return {'nome': nome, 'Disciplina': Curso, 'CargaHoraria': CargH, 'diaSemana': DiaS, 'usuario': usuario, 'senha': senha, 'matricula': matricula}

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
                        sql = "SELECT senha FROM Minerva_Professor WHERE usuario = %s"
                        cursor.execute(sql, (usuario,))
                        result = cursor.fetchone()
                        if result:
                            label_errorJE.place(x=25, y=162)
                        else:
                            sql = "INSERT INTO Minerva_Professor (Nome, Disciplina, CargaHoraria, diaSemana, usuario, senha, matricula) VALUES (%(nome)s, %(Disciplina)s, %(CargaHoraria)s, %(diaSemana)s, %(usuario)s, %(senha)s, %(matricula)s)"
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

        cadastro_button = ctk.CTkButton(master=cadastro_frame, text="Cadastro", width=300)
        cadastro_button.place(x=25, y=350)
        cadastro_button.bind("<Button-1>", on_login_button_click)

        global label_errorNV, label_errorSS, label_errorEV, label_errorSAR, label_errorJE
        global label_errorCV, label_errorCM8, label_errorCHV, label_errorCHMO
        global label_errorSV, label_errorSM8
        global label_NAceito, label_EAceito, label_CAceito, label_SAceito, label_DAceito, label_CHAceito

        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="Nome vazio, coloque um nome válido", font=('Arial', 9), text_color='red')
        label_errorSS = ctk.CTkLabel(master=cadastro_frame, text="Digite o sobrenome", font=('Arial', 9), text_color='red')
        label_errorEV = ctk.CTkLabel(master=cadastro_frame, text="usuario vazio, coloque um usuario válido", font=('Arial', 9), text_color='red')
        label_errorSAR = ctk.CTkLabel(master=cadastro_frame, text="usuario fora do padrão, use @gmail.com", font=('Arial', 9), text_color='red')
        label_errorJE = ctk.CTkLabel(master=cadastro_frame, text="O usuario inserido já foi registrado", font=('Arial', 9), text_color='red')

        label_errorCV = ctk.CTkLabel(master=cadastro_frame, text="Curso vazio, coloque um Curso válido", font=('Arial', 9), text_color='red')
        label_errorCM8 = ctk.CTkLabel(master=cadastro_frame, text="Coloque uma Curso maior", font=('Arial', 9), text_color='red')
        label_errorCHV = ctk.CTkLabel(master=cadastro_frame, text="vazia, inválida", font=('Arial', 9), text_color='red')
        label_errorCHMO = ctk.CTkLabel(master=cadastro_frame, text="Quantidade de caracter inválida", font=('Arial', 9), text_color='red')

        label_errorSV = ctk.CTkLabel(master=cadastro_frame, text="Senha vazia, coloque uma senha válida", font=('Arial', 9), text_color='red')
        label_errorSM8 = ctk.CTkLabel(master=cadastro_frame, text="Senha pequena, menor que 8 caracteres", font=('Arial', 9), text_color='red')

        label_NAceito = ctk.CTkLabel(master=cadastro_frame, text="Nome aceito", font=('Arial', 9), text_color='green')
        label_EAceito = ctk.CTkLabel(master=cadastro_frame, text="usuario aceito", font=('Arial', 9), text_color='green')
        label_CAceito = ctk.CTkLabel(master=cadastro_frame, text="Curso aceito", font=('Arial', 9), text_color='green')
        label_CHAceito = ctk.CTkLabel(master=cadastro_frame, text="dias aceito", font=('Arial', 9), text_color='green')
        label_SAceito = ctk.CTkLabel(master=cadastro_frame, text="Senha aceita", font=('Arial', 9), text_color='green')
        label_DAceito = ctk.CTkLabel(master=cadastro_frame, text="Carga horária aceita", font=('Arial', 9), text_color='green')

Application()
