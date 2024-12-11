import customtkinter as ctk
import subprocess

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("Dark")  # Define o tema escuro
ctk.set_default_color_theme("blue")  # Define o tema de cores azul

# Funções para abrir os scripts de login e fechar a janela principal
def abrir_login_professor():
    caminho_prof = r"Desktop\codigos\PROF\Login.py"
    subprocess.Popen(["python", caminho_prof])
    janela.destroy()  # Fecha a janela principal

def abrir_login_administrador():
    caminho_adm = r"Desktop\codigos\ADM\Login.py"
    subprocess.Popen(["python", caminho_adm])
    janela.destroy()  # Fecha a janela principal

# Configuração da janela principal
janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("400x300")
janela.configure(bg="#1a1a1a")  # Fundo da janela principal

# Estilização do título
titulo = ctk.CTkLabel(janela, text="Bem-vindo ao Sistema", font=("Arial", 24, "bold"), text_color="#00aaff")
titulo.pack(pady=(20, 10))

# Subtítulo para orientação
subtitulo = ctk.CTkLabel(janela, text="Escolha o tipo de login abaixo:", font=("Arial", 16), text_color="white")
subtitulo.pack(pady=(0, 20))

# Botão para login do professor
botao_professor = ctk.CTkButton(janela, text="Login Professor", 
                                font=("Arial", 14), 
                                fg_color="#0e4da4", hover_color="#073f7a", 
                                text_color="white", width=200, height=40, 
                                corner_radius=10, 
                                command=abrir_login_professor)
botao_professor.pack(pady=10)

# Botão para login do administrador
botao_administrador = ctk.CTkButton(janela, text="Login Administrador", 
                                    font=("Arial", 14), 
                                    fg_color="#0e4da4", hover_color="#073f7a", 
                                    text_color="white", width=200, height=40, 
                                    corner_radius=10, 
                                    command=abrir_login_administrador)
botao_administrador.pack(pady=10)

# Barra inferior com mensagem de boas-vindas
barra_inferior = ctk.CTkLabel(janela, text="© 2024 Sistema de Login | Todos os direitos reservados", 
                              font=("Arial", 10), text_color="gray")
barra_inferior.pack(side="bottom", pady=10)

# Iniciar a aplicação
janela.mainloop()
