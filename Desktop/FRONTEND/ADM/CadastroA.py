import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

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
                                    font=('Robot', 14)).place(x=25, y=105)

    senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Email", width=300,
                                font=('Robot', 14), show="*").place(x=25, y=175)

    username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="senha", width=300,
                                    font=('Robot', 14)).place(x=25, y=245)

    checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-se de mim sempre").place(x=25, y=305)

    login_buttom = ctk.CTkButton(master=login_frame, text="LOGIN", width=300).place
Application()