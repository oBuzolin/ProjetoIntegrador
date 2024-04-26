# imports backend
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
#cripto
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

janela = ctk.CTk()

class Application():
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
        titulo_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha \n acesso a plataforma",
                                    font=("Roboto", 20), text_color="#00B0F0").place(x=50, y=10)

        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=('Arial', 20, 'bold'),
                              text_color=('white'))
        label.place(x=25, y=5)

        Email_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Email", width=300,
                                    font=('Roboto', 14))
        Email_entry.place(x=25, y=75)

        senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300,
                                    font=('Roboto', 14), show="*")
        senha_entry.place(x=25, y=135)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-se de mim sempre")
        checkbox.place(x=25, y=195)

        def on_login_button_click(event):
            # Gerar um par de chaves RSA (chave pública e privada)
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            public_key = private_key.public_key()

            # Preparar a senha digitada para criptografia
            senha = senha_entry.get()
            senha_bytes = senha.encode('utf-8')

            # Criptografar a senha usando a chave pública RSA
            encrypted_password = public_key.encrypt(
                senha_bytes,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            #email comparação
            
            # Simulação: Suponha que 'encrypted_password' é o valor criptografado armazenado no banco de dados
            stored_encrypted_password = encrypted_password

            # Simulação: Obtendo o email do campo de entrada
            email = Email_entry.get()

            # Verificar se o email e a senha correspondem
            if email == "usuario@example.com":
                
                
                
                if encrypted_password == stored_encrypted_password:
                    print("Login bem-sucedido!")
                else:
                    print("Senha incorreta!")
            else:
                print("Usuário não encontrado!")

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300)
        login_button.place(x=25, y=255)
        login_button.bind("<Button-1>", on_login_button_click)

Application()
