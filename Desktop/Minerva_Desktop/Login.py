import customtkinter as ctk
from _tkinter import *
from PIL import *
from mysql.connector import connect
import PyQt5
#import psycopg2
import mysql.connector
#import pandas.io.sql as sqlio

from tkinter import RIGHT, PhotoImage
#from PIL import Image, ImageTk
janela = ctk.CTk()
class BackEnd():
    def conexao_mysql(self):
        try:
            conexao = mysql.connector.connect(
                host='143.106.241.3',
                user='cl201107',
                password='cl*02032005',
                database='cl201107'
            )
            self.cursor = conexao.cursor()
        except mysql.connector.Error as err:
            if err.errno == err.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user name or')
            else:
                print(err)
        else:
            print("Conexão bem sucedida")

    def desconecta_bd(self):
        self.conn.close()
        print("Banco de dado desconectado")

    def verifica_login(self):
        self.username = self.username_entry
        self.senha = self.senha_entry

        self.conexao_mysql()
        self.cursor.execute("""SELECT * FROM Minerva_Login WHERE(usuário =? AND senha=?)""",
                            (self.username_login, self.password_login))
        self.verifica_dados = self.cursor.fetchone()
        self.limpa_entry_login()

class Application(BackEnd):
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
            # janela.iconbitmap('icon.ico')
            janela.resizable(False, False)

        def telaLogin(self):
            img = ctk.CTkImage(Image.open("Minerva_Desktop/foto2.png"), size=(300, 300))

            label_img = ctk.CTkLabel(master=janela, text='', image=img)
            label_img.place(x=40, y=70)

            self.titulo_label = ctk.CTkLabel(master=janela, text="Entre na sua conta e tenha \n acesso a plataforma",
                                       font=("Roboto", 20), text_color="#00B0F0").place(x=50, y=10)

            #frame
            login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            login_frame.pack(side=RIGHT)

            #frame widgets
            label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=('Arial',20,'bold'), text_color=('white'))
            label.place(x=25, y=5)

            #frame
            self.username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username", width=300,
                                                font=('Robot', 14)).place(x=25, y=90)
            #self.username_label = ctk.CTkLabel(master=login_frame, text="*O campo de username é obrigatorio.", text_color='green',
            #                                    font=('Roboto', 8)).place(x=25, y=135)

            self.senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300,
                                                font=('Robot', 14), show="*").place(x=25, y=150)
            #self.senha_label = ctk.CTkLabel(master=login_frame, text="*O campo de senha é obrigatorio.", text_color='green',
            #                                    font=('Roboto', 8)).place(x=25, y=205)

            self.checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-se de mim sempre").place(x=25, y=200)

            self.login_buttom = ctk.CTkButton(master=login_frame, text="LOGIN", width=300, command=self.verifica_login, fg_color="black", hover_color="#401a1e").place(x=25, y=255)
            self.loginGoogle_buttom = ctk.CTkButton(master=login_frame, text="Conecte ao Google", width=300, fg_color="#FF6347", hover_color="#FF6347", text_color="black").place(x=25, y=300)
            self.salvarsenha_label = ctk.CTkLabel(master=login_frame, text="Esqueceu a senha?", text_color='white',
                                              font=('Roboto', 15)).place(x=110, y=350)
        def limpa_entry_login(self):
            self.username_entry.delete(0, END)
            self.senha_entry.delete(0, END)


Application()