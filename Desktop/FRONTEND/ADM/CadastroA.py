#imports backend
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
#----------------------------------------------------------------------------------------------------------------------------------------
#imposts criptografia
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

janela = ctk.CTk()

class Application():
  def __init__(self):
    self.janela=janela
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

    # colocar imagem

    login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
    login_frame.pack(side=ctk.RIGHT)

    label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=('Arial',20,'bold'), text_color=('white'))
    label.place(x=25, y=5)

    username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome", width=300,
                                    font=('Robot', 14))
    username_entry.place(x=25, y=75)

    Email_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Email", width=300,
                                    font=('Robot', 14))
    Email_entry.place(x=25, y=135)

    senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300,
                                font=('Robot', 14), show="*")
    senha_entry.place(x=25, y=205)

    checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-se de mim sempre")
    checkbox.place(x=25, y=265)
    
    def on_login_button_click(event):
        #gerando chave de criptografia
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        
        #preparando email
        email = Email_entry.get()
        print(f'Email: {email}')
        
        #preparando senha
        # senha = str(senha_entry.get())
        # senha_bytes = senha.encode('utf-8')
        # cipher_text = cipher_suite.encrypt(senha_bytes)
        # print(f'Senha: {cipher_text}')
        #teste 2 cripto
        
        
    login_buttom = ctk.CTkButton(master=login_frame, text="LOGIN", width=300)
    login_buttom.place(x=25, y=325)
    login_buttom.bind("<Button-1>", on_login_button_click)

Application()