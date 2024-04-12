from tkinter import *
from tkinter.ttk import *
import customtkinter as ctk
from PIL import Image
from mysql.connector import connect
import psycopg2
import mysql.connector
import pandas.io.sql as sqlio
from tkinter import PhotoImage
# icone = PhotoImage (file= '/run/media/eduardo/800694AB0694A426/Documents and Settings/Busolin/Documents/Escola/TCC/TCC/Desktop/FRONTEND/icon.png')
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
                            (self.username, self.password_login))
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
            # janela.iconphoto(FALSE, icone)
            janela.resizable(False, False)

        def telaLogin(self):
            img = ctk.CTkImage(Image.open("FRONTEND/foto2.png"), size=(150, 300))

            label_img = ctk.CTkLabel(master=janela, text='', image=img)
            label_img.place(x=20, y=100)

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
                                                font=('Robot', 14)).place(x=25, y=105)
            #self.username_label = ctk.CTkLabel(master=login_frame, text="*O campo de username é obrigatorio.", text_color='green',
            #                                    font=('Roboto', 8)).place(x=25, y=135)

            self.senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300,
                                                font=('Robot', 14), show="*").place(x=25, y=175)
            #self.senha_label = ctk.CTkLabel(master=login_frame, text="*O campo de senha é obrigatorio.", text_color='green',
            #                                    font=('Roboto', 8)).place(x=25, y=205)

            self.checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-se de mim sempre").place(x=25, y=235)

            self.login_buttom = ctk.CTkButton(master=login_frame, text="LOGIN", width=300, command=self.verifica_login).place(x=25, y=285)

        def limpa_entry_login(self):
            self.username_entry.delete(0, END)
            self.senha_entry.delete(0, END)

Application()