import customtkinter as ctk
from cryptography.fernet import Fernet
import mysql.connector
import random
from hashlib import sha256

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
        janela.title("Cadastro de Professor")
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

        label_errorNV = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorNV.place(x=25, y=75)

        usuario_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="E-mail", width=300,
                                   font=('Roboto', 14))
        usuario_entry.place(x=25, y=103)

        label_errorEV = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorEV.place(x=25, y=133)

        curso_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Disciplina", width=300,
                                   font=('Roboto', 14))
        curso_entry.place(x=25, y=161)

        label_errorCV = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorCV.place(x=25, y=191)

        CargH_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Carga Horária", width=145,
                                   font=('Roboto', 14))
        CargH_entry.place(x=25, y=219)

        label_errorCHV = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorCHV.place(x=25, y=249)

        DiaS_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Dias de Trabalho/semana", width=145,
                                  font=('Roboto', 14))
        DiaS_entry.place(x=180, y=219)

        label_errorCHMO = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorCHMO.place(x=180, y=249)

        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=275)

        label_errorSV = ctk.CTkLabel(master=cadastro_frame, text="", font=('Arial', 9), text_color='red')
        label_errorSV.place(x=25, y=305)

        checkbox_var = ctk.BooleanVar()

        def toggle_show_password():
            senha_entry.configure(show="" if checkbox_var.get() else "*")

        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=335)

        # Função de validação otimizada
        def validar_entradas():
            nome = nome_entry.get().strip()
            usuario = usuario_entry.get().strip()
            curso = curso_entry.get().strip()
            carga_horaria = int(CargH_entry.get().strip())
            dias_semana = int(DiaS_entry.get().strip())
            senha = senha_entry.get().strip()

            erros = {
                'nome': "",
                'usuario': "",
                'curso': "",
                'carga_horaria': "",
                'senha': "",
                'dias_semana': ""
            }

            # Validações e mensagens de erro
            if not nome or len(nome.split()) < 2:
                erros['nome'] = "Nome incompleto"
            if not usuario:
                erros['usuario'] = "E-mail vazio"
            elif "@gmail.com" not in usuario:
                erros['usuario'] = "E-mail inválido"
            if not curso:
                erros['curso'] = "Disciplina vazia"
            if not 0 < carga_horaria < 61:
                erros['carga_horaria'] = "Carga horária inválida"
            if not senha:
                erros['senha'] = "Senha vazia"
            elif not 0< dias_semana < 8:
                erros['senha'] = "Dias por semana invalido"
            elif len(senha) < 8:
                erros['senha'] = "Senha curta (mín 8 caracteres)"

            # Exibir mensagens de erro
            label_errorNV.configure(text=erros['nome'])
            label_errorEV.configure(text=erros['usuario'])
            label_errorCV.configure(text=erros['curso'])
            label_errorCHV.configure(text=erros['carga_horaria'])
            label_errorSV.configure(text=erros['senha'])

            return all(not msg for msg in erros.values())

        # Função de cadastro no banco de dados
        def cadastrar_professor():
            if not validar_entradas():
                return

            nome = nome_entry.get().strip()
            usuario = usuario_entry.get().strip()
            curso = curso_entry.get().strip()
            carga_horaria = CargH_entry.get().strip()
            dias_semana = DiaS_entry.get().strip()
            senha = senha_entry.get().strip()

            senha_hash = sha256(senha.encode()).hexdigest()
            matricula = random.randint(10000, 99999)

            dados_usuario = {
                'nome': nome,
                'disciplina': curso,
                'carga_horaria': carga_horaria,
                'dias_semana': dias_semana,
                'usuario': usuario,
                'senha': senha_hash,
                'matricula': matricula
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
                cursor.execute("SELECT senha FROM Minerva_Professor WHERE usuario = %s", (usuario,))
                resultado = cursor.fetchone()

                if resultado:
                    label_errorEV.configure(text="E-mail já cadastrado")
                else:
                    # Inserir professor no banco de dados
                    sql = """
                        INSERT INTO Minerva_Professor 
                        (Nome, Disciplina, CargaHoraria, diaSemana, usuario, senha, matricula)
                        VALUES (%(nome)s, %(disciplina)s, %(carga_horaria)s, %(dias_semana)s, %(usuario)s, %(senha)s, %(matricula)s)
                    """
                    cursor.execute(sql, dados_usuario)
                    conexao.commit()

                    # Criar o login associado ao professor
                    # login_sql = """
                    #     INSERT INTO Minerva_Login (professor_matricula_id, status)
                    #     VALUES (%s, %s)
                    # """
                    # cursor.execute(login_sql, (matricula, 'ativo'))
                    # conexao.commit()

                    print("Cadastro realizado com sucesso!")
                    
                    janela.destroy()
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados no banco de dados: {erro}")
            finally:
                cursor.close()
                conexao.close()

        cadastro_button = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", width=300, command=cadastrar_professor)
        cadastro_button.place(x=25, y=365)

Application()
