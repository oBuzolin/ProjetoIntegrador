import customtkinter as ctk
from cryptography.fernet import Fernet

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela=janela
        self.tema()
        self.tela()
        self.telaCadastroProfessor()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Cadastro de Professor")
        janela.resizable(False, False)

    def telaCadastroProfessor(self):
        label_img = ctk.CTkLabel(master=janela, text='').place(x=20, y=100)

        titulo_label = ctk.CTkLabel(master=janela, text="Cadastre-se como professor \n na plataforma",
                               font=("Roboto", 20), text_color="#00B0F0").place(x=50, y=10)

        cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        cadastro_frame.pack(side=ctk.RIGHT)

        label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro de Professor", font=('Arial',20,'bold'), text_color=('white'))
        label.place(x=25, y=5)

        nome_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome", width=300,
                                            font=('Roboto', 14)).place(x=25, y=105)

        email_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Email", width=300,
                                            font=('Roboto', 14)).place(x=25, y=175)
        
        senha_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha", width=300,
                                            font=('Roboto', 14), show="*").place(x=25, y=245)

        checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Lembre-se de mim sempre").place(x=25, y=305)

        cadastro_button = ctk.CTkButton(master=cadastro_frame, text="CADASTRAR", width=300).place(x=25, y=355)

Application()
