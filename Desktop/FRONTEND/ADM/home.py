import customtkinter as ctk
import os
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk

# Função para ler o email do arquivo
def ler_email(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return None

# Função para remover o arquivo
def remover_arquivo(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f'Arquivo {arquivo} excluído com sucesso.')
    else:
        print(f'O arquivo {arquivo} não existe.')

# Função para obter dados do professor
def obter_dados_professor(email, cursor):
    queries_professor = {
        'nome': "SELECT Nome FROM Minerva_Professor WHERE email = %s",
        'disciplina': "SELECT Disciplina FROM Minerva_Professor WHERE email = %s",
        'carga_horaria': "SELECT CargaHoraria FROM Minerva_Professor WHERE email = %s",
        'dias_semana': "SELECT DiasSemana FROM Minerva_Professor WHERE email = %s",
        'ra': "SELECT RA FROM Minerva_Professor WHERE email = %s"
    }

    dados_professor = {}
    for key, query in queries_professor.items():
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        dados_professor[key] = result[0] if result else None

    return dados_professor if dados_professor['nome'] else None

# Função para obter dados do administrador
def obter_dados_administrador(email, cursor):
    queries_administrador = {
        'nome': "SELECT Nome FROM Minerva_Administrador WHERE email = %s",
        'cargo': "SELECT Cargo FROM Minerva_Administrador WHERE email = %s"
    }

    dados_administrador = {}
    for key, query in queries_administrador.items():
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        dados_administrador[key] = result[0] if result else None

    return dados_administrador if dados_administrador['nome'] else None

# Configurações de conexão ao banco de dados
host = '143.106.241.3'
port = '3306'
user = 'cl201107'
password = 'cl*02032005'
database = 'cl201107'
arquivo_email = 'email.txt'

# Lê o email do arquivo e remove o arquivo
email = ler_email(arquivo_email)
if email:
    print(f"Email lido: {email}")
    remover_arquivo(arquivo_email)

    try:
        # Conecta ao banco de dados
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            cursor = conn.cursor()

            # Tenta obter os dados do professor
            dados_professor = obter_dados_professor(email, cursor)
            
            if dados_professor:
                # Imprime os dados do professor
                print(f'Nome: {dados_professor["nome"]}')
                print(f'Disciplina: {dados_professor["disciplina"]}')
                print(f'Carga Horária: {dados_professor["carga_horaria"]}')
                print(f'Dias da Semana: {dados_professor["dias_semana"]}')
                print(f'RA: {dados_professor["ra"]}')
            else:
                # Tenta obter os dados do administrador
                dados_administrador = obter_dados_administrador(email, cursor)

                if dados_administrador:
                    print(f'Nome: {dados_administrador["nome"]}')
                    print(f'Cargo: {dados_administrador["cargo"]}')
                else:
                    print(f"Nenhum resultado encontrado para o email {email}")

            cursor.close()

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexão ao MySQL foi fechada")
else:
    print("Não foi possível ler o email do arquivo.")

# Criação da janela principal
janela_main = ctk.CTk()
janela_main.title("Tela ADM")
janela_main.geometry("1000x650")
janela_main.maxsize(width=1100, height=700)
janela_main.minsize(width=800, height=600)
janela_main.resizable(width=False, height=False)
ctk.set_appearance_mode("Dark")  # Modo escuro para uma aparência moderna

# Menu superior
menu = ctk.CTkFrame(master=janela_main, width=990, height=35, corner_radius=10)
menu.place(x=5, y=1)

# Exemplos de submenus
submenus = [
    ctk.CTkFrame(master=menu, width=55, height=15, fg_color='#2C2F33', corner_radius=5),  # Cor cinza escuro
    ctk.CTkFrame(master=menu, width=140,height=15, fg_color='#2C2F33', corner_radius=5),  # Cor cinza escuro
    ctk.CTkFrame(master=menu, width=40, height=15, fg_color='#2C2F33', corner_radius=5)    # Cor cinza escuro
]
x_positions = [6, 65, 950]
for index, submenu in enumerate(submenus):
    submenu.place(x=x_positions[index], y=2)

# Carregar a imagem do ícone
icon_path = "Desktop/FRONTEND/img/minerva.ico"  # Substitua pelo caminho real do seu ícone
icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(25, 25))

# Adicionando ícone ao primeiro frame
icon_label = ctk.CTkLabel(submenus[0], text='', image=icon_image)
icon_label.pack(padx=0, pady=0)

# Adicionando texto ao segundo frame
font = ctk.CTkFont(family="Cloister Black", size=14)
text_label = ctk.CTkLabel(submenus[1], text='Minerva', text_color='white',font=font)
text_label.pack(padx=0, pady=0)

# Adicionando botão redondo ao terceiro frame
letra = dados_professor['nome'][0] if dados_professor else ""
round_button = ctk.CTkButton(submenus[2], text=letra, width=28, height=28, corner_radius=20, fg_color='#585858', font=font)
round_button.pack(padx=0, pady=0)

# Botão "Agenda"
frame1 = ctk.CTkFrame(master=janela_main, width=225, height=595, bg_color='#40444B', corner_radius=10)  # Cor de fundo mais escura
frame1.place(x=10, y=40)

button = ctk.CTkButton(master=frame1, text="Agenda", text_color="white", width=210, height=40, fg_color='#F04747', bg_color="#7289DA", corner_radius=5)  # Vermelho e azul do Discord
button.place(x=8, y=10)

# Exemplos de visualização de turmas
x_positions = [250, 485, 720]
y_positions = [45, 230, 415]

for x in x_positions:
    for y in y_positions:
        ctk.CTkFrame(master=janela_main, width=225, height=175, fg_color='#2C2F33', corner_radius=10).place(x=x, y=y)  # Cor cinza escuro

# Loop principal da janela
janela_main.mainloop()
