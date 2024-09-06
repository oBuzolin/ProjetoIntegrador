import customtkinter as ctk
import os
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para gerar gráfico de pizza e inseri-lo em um frame com fundo escuro
def criar_grafico_pizza(frame, dados, labels):
    fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=100)  # Reduzi o tamanho do gráfico para 1.5x1.5
    cores = ['#F04747', '#7289DA', '#2C2F33', '#40444B']  # Cores que combinam com o layout
    ax.pie(dados, labels=None, colors=cores, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'white'})
    
    # Fundo escuro para o gráfico
    fig.patch.set_facecolor('#2C2F33')  # Cor do fundo da figura
    ax.set_facecolor('#2C2F33')  # Cor do fundo do gráfico
    ax.axis('equal')  # Assegura que o gráfico seja um círculo
    
    # Remover bordas e reduzir espaçamento
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Adicionar a legenda no lado direito e em branco
    ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5), facecolor='#2C2F33', labelcolor='white', fontsize=8)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Função para ler o usuario do arquivo
def ler_usuario(arquivo):
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
def obter_dados_professor(usuario, cursor):
    queries_professor = {
        'nome': "SELECT Nome FROM Minerva_Professor WHERE usuario = %s",
        'disciplina': "SELECT Disciplina FROM Minerva_Professor WHERE usuario = %s",
        'carga_horaria': "SELECT CargaHoraria FROM Minerva_Professor WHERE usuario = %s",
        'dias_semana': "SELECT DiaSemana FROM Minerva_Professor WHERE usuario = %s",
        'ra': "SELECT matricula FROM Minerva_Professor WHERE usuario = %s"
    }

    dados_professor = {}
    for key, query in queries_professor.items():
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        dados_professor[key] = result[0] if result else None

    return dados_professor if dados_professor['nome'] else None

# Função para obter dados do administrador
def obter_dados_administrador(usuario, cursor):
    queries_administrador = {
        'nome': "SELECT Nome FROM Minerva_Administrador WHERE usuario = %s",
        'cargo': "SELECT Cargo FROM Minerva_Administrador WHERE usuario = %s"
    }

    dados_administrador = {}
    for key, query in queries_administrador.items():
        cursor.execute(query, (usuario,))
        result = cursor.fetchone()
        dados_administrador[key] = result[0] if result else None

    return dados_administrador if dados_administrador['nome'] else None

# Configurações de conexão ao banco de dados
host = '143.106.241.3'
port = '3306'
user = 'cl201107'
password = 'cl*02032005'
database = 'cl201107'
arquivo_usuario = 'usuario.txt'

# Lê o email do arquivo e remove o arquivo
usuario = ler_usuario(arquivo_usuario)
if usuario:
    print(f"Email lido: {usuario}")
    remover_arquivo(arquivo_usuario)

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
            dados_professor = obter_dados_professor(usuario, cursor)
            
            if dados_professor:
                # Imprime os dados do professor
                print(f'Nome: {dados_professor["nome"]}')
                print(f'Disciplina: {dados_professor["disciplina"]}')
                print(f'Carga Horária: {dados_professor["carga_horaria"]}')
                print(f'Dias da Semana: {dados_professor["dias_semana"]}')
                print(f'RA: {dados_professor["ra"]}')
            else:
                # Tenta obter os dados do administrador
                dados_administrador = obter_dados_administrador(usuario, cursor)

                if dados_administrador:
                    print(f'Nome: {dados_administrador["nome"]}')
                    print(f'Cargo: {dados_administrador["cargo"]}')
                else:
                    print(f"Nenhum resultado encontrado para o email {usuario}")

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

# Dados fictícios para os gráficos de pizza
dados_exemplo = [25, 35, 20, 20]
labels_exemplo = ["Parte A", "Parte B", "Parte C", "Parte D"]

# Exemplos de visualização de turmas com gráficos de pizza
x_positions = [250, 485, 720]
y_positions = [45, 230, 415]

for x in x_positions:
    for y in y_positions:
        frame = ctk.CTkFrame(master=janela_main, width=225, height=175, fg_color='#2C2F33', corner_radius=10)
        frame.place(x=x, y=y)
        
        # Adiciona gráfico de pizza ao frame
        criar_grafico_pizza(frame, dados_exemplo, labels_exemplo)

# Loop principal da janela
janela_main.mainloop()
