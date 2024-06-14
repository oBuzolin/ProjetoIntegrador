# imports backend
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
#cripto
from hashlib import sha256
#banco
import mysql.connector
import os
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
        
        checkbox_var = ctk.BooleanVar()
        def toggle_show_password():
            valor = checkbox_var.get()
            if valor == True:
                senha_entry.configure(show="")
            else:
                senha_entry.configure(show="*")
        # Criar a CTkCheckBox e associar com a variável de controle
        checkbox = ctk.CTkCheckBox(master=login_frame, text="Mostrar senha", variable=checkbox_var, command=toggle_show_password)
        checkbox.place(x=25, y=200)

        def on_login_button_click(event):
            # Gerar um par de chaves RSA (chave pública e privada)
            
            #email comparação
            
            # Simulação: Suponha que 'encrypted_password' é o valor criptografado armazenado no banco de dados
            senha = senha_entry.get()
            senha = sha256(senha.encode())
            senha = senha.hexdigest()
            # Simulação: Obtendo o email do campo de entrada
            email = Email_entry.get()
            
            # Verificar se o email e a senha correspondem
            def check_email_and_password(email, password):
                try:
                    # Estabelecer conexão com o banco de dados MySQL
                    conn = mysql.connector.connect(
                        host="143.106.241.3",
                        port=3306,
                        user="cl201107",
                        password="cl*02032005",
                        database="cl201107"
                    )

                    # Criar um cursor para executar comandos SQL
                    cursor = conn.cursor()

                    # Consulta SQL para verificar se o email existe
                    sql = "SELECT senha FROM Minerva_Professor WHERE email = %s"
                    cursor.execute(sql, (email,))
                    # Obter o resultado da consulta
                    result = cursor.fetchone()  # Retorna uma única linha se encontrar

                    if result:
                        # Email encontrado, verificar a senha
                        hashed_password_from_db = result[0]

                        # Verificar se a senha fornecida corresponde à senha no banco de dados
                        if check_password(password, hashed_password_from_db):
                            with open('Desktop\FRONTEND\ADM\home.py', 'r') as f:
                                adm = f.read()
                                exec(adm)
                                janela.quit() 
                                janela.destroy()
                        else:
                            label_errorE.place(x=25,y=1300)
                            label_errorSV.pack()  
                            label_errorSV.place(x=25,y=165)
                    else:
                        sql2 = "SELECT senha FROM Minerva_Administrador WHERE email = %s"
                        cursor.execute(sql2, (email,))
                        result = cursor.fetchone()
                        if result:
                            # Email encontrado, verificar a senha
                            hashed_password_from_db = result[0]

                            # Verificar se a senha fornecida corresponde à senha no banco de dados
                            if check_password(password, hashed_password_from_db):
                                print(f"Email '{email}' encontrado e a senha está correta.")
                            else:
                                label_errorE.place(x=25,y=1300)
                                label_errorSV.pack()  
                                label_errorSV.place(x=25,y=165)
                        else:
                            label_errorSV.place(x=25,y=1300)
                            label_errorE.pack()  
                            label_errorE.place(x=25,y=105)
                            
                except mysql.connector.Error as error:
                    print(f"Erro ao conectar ou executar consulta: {error}")

                finally:
                    # Fechar cursor e conexão com o banco de dados
                    if 'cursor' in locals():
                        cursor.close()
                    if 'conn' in locals() and conn.is_connected():
                        conn.close()

            def check_password(input_password, hashed_password):
                # Neste exemplo simulado, verificamos a senha sem hash (por motivos educacionais)
                # Em produção, você deve verificar usando um método seguro, como bcrypt, pbkdf2, etc.
                return input_password == hashed_password
            check_email_and_password(email, senha)

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300)
        login_button.place(x=25, y=235)
        login_button.bind("<Button-1>", on_login_button_click)
        #senha errado
        global label_errorSV
        label_errorSV = ctk.CTkLabel(master=login_frame, text="senha invalida", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
        #email errado
        global label_errorE
        label_errorE = ctk.CTkLabel(master=login_frame, text="email invalido", font=('Arial', 9, 'bold'),
                                     text_color=('red'))
Application()
