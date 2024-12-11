# Imports
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from hashlib import sha256
import mysql.connector
import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

janela = ctk.CTk()

class Application:
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaLogin()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de Login")
        janela.resizable(False, False)

    def telaLogin(self):
        ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha \n acesso a plataforma",
                     font=("Roboto", 20), text_color="#00B0F0").place(x=50, y=10)

        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=ctk.RIGHT)

        ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=('Arial', 20, 'bold'),
                     text_color='white').place(x=25, y=5)

        usuario_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Email", width=300, font=('Roboto', 14))
        usuario_entry.place(x=25, y=75)

        senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=135)

        checkbox_var = tk.BooleanVar()

        def toggle_show_password():
            senha_entry.configure(show="" if checkbox_var.get() else "*")

        ctk.CTkCheckBox(master=login_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password).place(x=25, y=200)

        global label_error
        label_error = ctk.CTkLabel(master=login_frame, text="", font=('Arial', 9, 'bold'), text_color='red')

        def mostrar_erro(msg):
            label_error.configure(text=msg)
            label_error.pack()
            label_error.place(x=25, y=165)

        def on_login_button_click(event):
            senha = sha256(senha_entry.get().encode()).hexdigest()
            usuario = usuario_entry.get().strip()

            if not usuario or not senha:
                mostrar_erro("Email e senha são obrigatórios.")
                return

            def check_usuario_and_password(usuario, password):
                try:
                    conn = mysql.connector.connect(
                        host="143.106.241.3",
                        port=3306,
                        user="cl201107",
                        password="cl*02032005",
                        database="cl201107"
                    )
                    cursor = conn.cursor()

                    sql = "SELECT senha FROM Minerva_Administrador WHERE usuario = %s"
                    cursor.execute(sql, (usuario,))
                    result = cursor.fetchone()

                    if result:
                        if password == result[0]:
                            caminho = r'Desktop\codigos\arquivos\Administrador.txt'
                            with open(caminho, 'w') as file:
                                file.write(usuario)
                            self.janela.quit()
                            self.janela.destroy()
                            os.system('Desktop\codigos\ADM\homeAdm.py')
                        else:
                            mostrar_erro("Senha inválida.")
                    else:
                        mostrar_erro("Email inválido.")

                except mysql.connector.Error as err:
                    mostrar_erro(f"Erro ao conectar ao banco de dados: {err}")
                finally:
                    if conn.is_connected():
                        cursor.close()
                        conn.close()

            label_error.pack_forget()
            check_usuario_and_password(usuario, senha)

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300)
        login_button.place(x=25, y=235)
        login_button.bind("<Button-1>", on_login_button_click)

        esqueci_senha_button = ctk.CTkButton(master=login_frame, text="Esqueci minha senha", width=300, command=self.telaEsqueciSenha)
        esqueci_senha_button.place(x=25, y=280)

    def telaEsqueciSenha(self):
        self.esqueci_senha_toplevel = tk.Toplevel(self.janela)
        self.esqueci_senha_toplevel.geometry("450x200")
        self.esqueci_senha_toplevel.title("Esqueci minha senha")
        self.esqueci_senha_toplevel.configure(bg="#2b2b2b")

        ctk.CTkLabel(master=self.esqueci_senha_toplevel, text="Digite seu email para receber o código de verificação:",
                     font=('Roboto', 14)).pack(pady=20)

        self.usuario_recuperacao_entry = ctk.CTkEntry(master=self.esqueci_senha_toplevel, placeholder_text="Email", width=300, font=('Roboto', 14))
        self.usuario_recuperacao_entry.pack(pady=10)

        enviar_codigo_button = ctk.CTkButton(master=self.esqueci_senha_toplevel, text="Enviar código", command=self.enviar_codigo)
        enviar_codigo_button.pack(pady=10)

    def enviar_codigo(self):
        usuario = self.usuario_recuperacao_entry.get()
        codigo = random.randint(100000, 999999)

        try:
            conn = mysql.connector.connect(
                host="143.106.241.3",
                port=3306,
                user="cl201107",
                password="cl*02032005",
                database="cl201107"
            )
            cursor = conn.cursor()

            sql = "SELECT usuario FROM Minerva_Administrador WHERE usuario = %s"
            cursor.execute(sql, (usuario,))
            result = cursor.fetchone()

            if result:
                self.usuario_verificado = usuario  # Armazenar o email verificado
                self.enviar_usuario(usuario, codigo)
                self.tela_codigo_verificacao(codigo)
            else:
                label_erro_usuario = ctk.CTkLabel(master=self.esqueci_senha_toplevel, text="Email não encontrado", font=('Arial', 9, 'bold'), text_color='red')
                label_erro_usuario.pack(pady=5)
        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou executar consulta: {error}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def enviar_usuario(self, usuario, codigo):
        remetente = "minervaembv@gmail.com"
        senha = "a u z q y d f v a w a x m o h a"
        
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = usuario
        msg['Subject'] = "Código de Verificação"
        body = f"Seu código de verificação é: {codigo}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(remetente, senha)
            text = msg.as_string()
            server.sendmail(remetente, usuario, text)
            server.quit()
            print("Email enviado com sucesso")
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    def tela_codigo_verificacao(self, codigo_gerado):
        self.codigo_verificacao_toplevel = tk.Toplevel(self.janela)
        self.codigo_verificacao_toplevel.geometry("450x200")
        self.codigo_verificacao_toplevel.title("Verificação de Código")
        self.codigo_verificacao_toplevel.configure(bg="#2b2b2b")

        ctk.CTkLabel(master=self.codigo_verificacao_toplevel, text="Digite o código de verificação enviado para seu email:",
                     font=('Roboto', 14)).pack(pady=20)

        self.codigo_entry = ctk.CTkEntry(master=self.codigo_verificacao_toplevel, placeholder_text="Código", width=300, font=('Roboto', 14))
        self.codigo_entry.pack(pady=10)

        verificar_codigo_button = ctk.CTkButton(master=self.codigo_verificacao_toplevel, text="Verificar", command=lambda: self.verificar_codigo(codigo_gerado))
        verificar_codigo_button.pack(pady=10)

    def verificar_codigo(self, codigo_gerado):
        codigo_digitado = self.codigo_entry.get().strip()

        if str(codigo_gerado) == codigo_digitado:
            self.tela_alterar_senha()
        else:
            mostrar_erro_codigo("Código incorreto.")

    def tela_alterar_senha(self):
        self.alterar_senha_toplevel = tk.Toplevel(self.janela)
        self.alterar_senha_toplevel.geometry("450x250")
        self.alterar_senha_toplevel.title("Alterar Senha")
        self.alterar_senha_toplevel.configure(bg="#2b2b2b")

        ctk.CTkLabel(master=self.alterar_senha_toplevel, text="Digite sua nova senha:",
                     font=('Roboto', 14)).pack(pady=20)

        self.nova_senha_entry = ctk.CTkEntry(master=self.alterar_senha_toplevel, placeholder_text="Nova Senha", width=300, font=('Roboto', 14), show="*")
        self.nova_senha_entry.pack(pady=10)

        confirmar_senha_button = ctk.CTkButton(master=self.alterar_senha_toplevel, text="Alterar Senha", command=self.alterar_senha)
        confirmar_senha_button.pack(pady=10)

    def alterar_senha(self):
        nova_senha = sha256(self.nova_senha_entry.get().encode()).hexdigest()

        try:
            conn = mysql.connector.connect(
                host="143.106.241.3",
                port=3306,
                user="cl201107",
                password="cl*02032005",
                database="cl201107"
            )
            cursor = conn.cursor()

            sql = "UPDATE Minerva_Administrador SET senha = %s WHERE usuario = %s"
            cursor.execute(sql, (nova_senha, self.usuario_verificado))
            conn.commit()
            print("Senha alterada com sucesso")
            self.alterar_senha_toplevel.destroy()
            self.codigo_verificacao_toplevel.destroy()
            self.esqueci_senha_toplevel.destroy()
        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou executar consulta: {error}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

# Inicializando a aplicação
if __name__ == "__main__":
    Application()
