import customtkinter as ctk
from hashlib import sha256
import mysql.connector
import random

class Application:
    def __init__(self):
        self.janela = ctk.CTk()
        self.setup_interface()
        self.setup_cadastro()
        self.janela.mainloop()

    def setup_interface(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.janela.geometry("700x450")
        self.janela.title("Cadastro de Administrador")
        self.janela.resizable(False, False)

    def setup_cadastro(self):
        ctk.CTkLabel(
            self.janela, 
            text="Cadastre-se como Administrador \nna plataforma", 
            font=("Roboto", 20), 
            text_color="#00B0F0"
        ).place(x=50, y=10)

        cadastro_frame = ctk.CTkFrame(self.janela, width=350, height=396)
        cadastro_frame.pack(side=ctk.RIGHT)

        ctk.CTkLabel(
            cadastro_frame, 
            text="Cadastro de Administrador", 
            font=('Arial', 20, 'bold'), 
            text_color='white'
        ).place(x=25, y=5)

        entries = {
            'nome': ctk.CTkEntry(cadastro_frame, placeholder_text="Nome", width=300, font=('Roboto', 14)),
            'usuario': ctk.CTkEntry(cadastro_frame, placeholder_text="E-mail", width=300, font=('Roboto', 14)),
            'cargo': ctk.CTkEntry(cadastro_frame, placeholder_text="Cargo", width=300, font=('Roboto', 14)),
            'senha': ctk.CTkEntry(cadastro_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*")
        }
        labels_erro = {key: ctk.CTkLabel(cadastro_frame, text="", font=('Arial', 9), text_color='red') for key in entries}

        entries['nome'].place(x=25, y=45)
        labels_erro['nome'].place(x=25, y=75)
        entries['usuario'].place(x=25, y=103)
        labels_erro['usuario'].place(x=25, y=133)
        entries['cargo'].place(x=25, y=161)
        labels_erro['cargo'].place(x=25, y=191)
        entries['senha'].place(x=25, y=219)
        labels_erro['senha'].place(x=25, y=249)

        checkbox_var = ctk.BooleanVar()
        ctk.CTkCheckBox(
            cadastro_frame, 
            text="Mostrar senha", 
            variable=checkbox_var, 
            command=lambda: entries['senha'].configure(show="" if checkbox_var.get() else "*")
        ).place(x=25, y=275)

        ctk.CTkButton(
            cadastro_frame, 
            text="Cadastrar", 
            width=300, 
            command=lambda: self.cadastrar_administrador(entries, labels_erro)
        ).place(x=25, y=305)

    def validar_entradas(self, entries, labels_erro):
        nome = entries['nome'].get().strip()
        usuario = entries['usuario'].get().strip()
        cargo = entries['cargo'].get().strip()
        senha = entries['senha'].get().strip()

        erros = {
            'nome': "Nome incompleto" if not nome or len(nome.split()) < 2 else "",
            'usuario': "E-mail inválido" if not usuario or "@gmail.com" not in usuario else "",
            'cargo': "Cargo não informado" if not cargo else "",
            'senha': "Senha curta (mín 8 caracteres)" if not senha or len(senha) < 8 else ""
        }

        for key, error_label in labels_erro.items():
            error_label.configure(text=erros[key])

        return all(not erro for erro in erros.values())

    def email_existe(self, usuario):
        """Verifica se o e-mail já existe em qualquer tabela relevante."""
        try:
            conexao = mysql.connector.connect(
                host="143.106.241.3", port=3306, user="cl201107", password="cl*02032005", database="cl201107"
            )
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT usuario FROM Minerva_Administrador WHERE usuario = %s "
                "UNION SELECT usuario FROM Minerva_Professor WHERE usuario = %s "
                "UNION SELECT usuario FROM Minerva_Aluno WHERE usuario = %s",
                (usuario, usuario, usuario)
            )
            return cursor.fetchone() is not None
        except mysql.connector.Error as erro:
            print(f"Erro na verificação de e-mail: {erro}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def cadastrar_administrador(self, entries, labels_erro):
        if not self.validar_entradas(entries, labels_erro):
            return

        usuario = entries['usuario'].get().strip()

        if self.email_existe(usuario):
            labels_erro['usuario'].configure(text="E-mail já cadastrado")
            return

        # Corrigido aqui: usando .get() para obter o texto da entrada
        primeira_letra = entries['nome'].get()[0].upper()
        valor_letra = ord(primeira_letra) - ord('A') + 1  # 'A' = 1, 'B' = 2, ..., 'Z' = 26

        # Escolhendo um dos dígitos para colocar no final
        digito_final = random.choice([int(d) for d in str(valor_letra)])
        
        dados_usuario = {
            'nome': entries['nome'].get().strip(),
            'usuario': usuario,
            'cargo': entries['cargo'].get().strip(),
            'senha': sha256(entries['senha'].get().strip().encode()).hexdigest(),
            'matricula': random.randint(10000, 99999) // 10 * 10 + digito_final
        }

        try:
            conexao = mysql.connector.connect(
                host="143.106.241.3", port=3306, user="cl201107", password="cl*02032005", database="cl201107"
            )
            cursor = conexao.cursor()
            cursor.execute(""" 
                INSERT INTO Minerva_Administrador (nome, usuario, cargo, senha, matricula) 
                VALUES (%(nome)s, %(usuario)s, %(cargo)s, %(senha)s, %(matricula)s)
            """, dados_usuario)
            conexao.commit()
            print("Cadastro realizado com sucesso!")
            self.janela.destroy()

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir dados no banco de dados: {erro}")
        finally:
            cursor.close()
            conexao.close()

Application()
