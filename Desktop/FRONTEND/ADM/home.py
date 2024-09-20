import os
import dotenv
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carregar variáveis de ambiente para informações sensíveis
dotenv.load_dotenv()

# Função para gerar gráfico de pizza e inseri-lo em um frame com fundo escuro
def criar_grafico_pizza(frame, dados, labels):
    fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=100)  # Gráfico pequeno
    cores = ['#F04747', '#7289DA', '#2C2F33', '#40444B']  # Cores compatíveis com layout
    
    ax.pie(dados, labels=None, colors=cores, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'white'})
    
    # Configuração do fundo escuro
    fig.patch.set_facecolor('#2C2F33')  # Cor do fundo da figura
    ax.set_facecolor('#2C2F33')  # Cor do fundo do gráfico
    ax.axis('equal')  # Mantém o gráfico circular
    
    # Remover bordas e ajustar espaçamento
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # Adicionar legenda com estilo
    ax.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5), facecolor='#2C2F33', labelcolor='white', fontsize=8)
    
    # Inserir gráfico no frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Função para ler o usuário de um arquivo de texto
def ler_usuario(arquivo):
    if not os.path.exists(arquivo):
        print(f"Arquivo {arquivo} não encontrado.")
        return None
    with open(arquivo, 'r') as file:
        return file.read().strip()

# Função para remover arquivo
def remover_arquivo(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f'Arquivo {arquivo} excluído com sucesso.')

# Função para obter dados do professor a partir do banco de dados
def obter_dados_professor(usuario, cursor):
    queries = {
        'nome': "SELECT Nome FROM Minerva_Professor WHERE usuario = %s",
        'disciplina': "SELECT Disciplina FROM Minerva_Professor WHERE usuario = %s",
        'carga_horaria': "SELECT CargaHoraria FROM Minerva_Professor WHERE usuario = %s",
        'dias_semana': "SELECT DiaSemana FROM Minerva_Professor WHERE usuario = %s",
        'ra': "SELECT matricula FROM Minerva_Professor WHERE usuario = %s"
    }
    dados = {key: cursor.execute(query, (usuario,)) or cursor.fetchone()[0] for key, query in queries.items() if cursor.fetchone()}
    return dados if dados.get('nome') else None

# Função para obter dados do administrador a partir do banco de dados
def obter_dados_administrador(usuario, cursor):
    queries = {
        'nome': "SELECT Nome FROM Minerva_Administrador WHERE usuario = %s",
        'cargo': "SELECT Cargo FROM Minerva_Administrador WHERE usuario = %s"
    }
    dados = {key: cursor.execute(query, (usuario,)) or cursor.fetchone()[0] for key, query in queries.items() if cursor.fetchone()}
    return dados if dados.get('nome') else None

# Configuração do banco de dados
def conectar_bd():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', '143.106.241.3'),
        port=os.getenv('DB_PORT', '3306'),
        user=os.getenv('DB_USER', 'cl201107'),
        password=os.getenv('DB_PASSWORD', 'cl*02032005'),
        database=os.getenv('DB_NAME', 'cl201107')
    )

# Lê o usuário do arquivo e tenta conectar ao banco de dados
def buscar_dados_usuario():
    usuario = ler_usuario('usuario.txt')
    if not usuario:
        print("Não foi possível ler o email do arquivo.")
        return None, None

    print(f"Email lido: {usuario}")
    remover_arquivo('usuario.txt')

    try:
        conn = conectar_bd()
        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            cursor = conn.cursor()
            dados_professor = obter_dados_professor(usuario, cursor)
            if dados_professor:
                print(f'Dados do Professor: {dados_professor}')
                return dados_professor, None
            else:
                dados_administrador = obter_dados_administrador(usuario, cursor)
                if dados_administrador:
                    print(f'Dados do Administrador: {dados_administrador}')
                    return None, dados_administrador
            cursor.close()
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            print("Conexão ao MySQL foi fechada")
    return None, None

# Criação da interface principal
def criar_interface(dados_professor):
    janela_main = ctk.CTk()
    janela_main.title("Tela ADM")
    janela_main.geometry("1000x650")
    janela_main.maxsize(width=1100, height=700)
    janela_main.minsize(width=800, height=600)
    janela_main.resizable(False, False)
    ctk.set_appearance_mode("Dark")  # Modo escuro para estilo moderno

    # Menu superior
    menu = ctk.CTkFrame(janela_main, width=990, height=35, corner_radius=10)
    menu.place(x=5, y=1)

    # Submenus
    submenus = [ctk.CTkFrame(menu, width=55, height=15, fg_color='#2C2F33', corner_radius=5) for _ in range(3)]
    submenus[0].place(x=6, y=2)
    submenus[1].place(x=65, y=2)
    submenus[2].place(x=950, y=2)

    # Ícone
    icon_path = os.getenv('ICON_PATH', "Desktop/FRONTEND/img/minerva.ico")
    if os.path.exists(icon_path):
        icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(25, 25))
        icon_label = ctk.CTkLabel(submenus[0], text='', image=icon_image)
        icon_label.pack()

    # Texto Minerva
    fonte = ctk.CTkFont(family="Cloister Black", size=14)
    text_label = ctk.CTkLabel(submenus[1], text='Minerva', text_color='white', font=fonte)
    text_label.pack()

    # Botão redondo
    letra = dados_professor['nome'][0] if dados_professor else ""
    round_button = ctk.CTkButton(submenus[2], text=letra, width=28, height=28, corner_radius=20, fg_color='#585858', font=fonte)
    round_button.pack()

    # Frame e botão "Agenda"
    frame1 = ctk.CTkFrame(janela_main, width=225, height=595, bg_color='#40444B', corner_radius=10)
    frame1.place(x=10, y=40)
    ctk.CTkButton(frame1, text="Agenda", text_color="white", width=210, height=40, fg_color='#F04747', bg_color="#7289DA", corner_radius=5).place(x=8, y=10)

    # Gráficos de pizza
    dados_exemplo = [25, 35, 20, 20]
    labels_exemplo = ["Parte A", "Parte B", "Parte C", "Parte D"]
    for x in [250, 485, 720]:
        for y in [45, 230, 415]:
            frame = ctk.CTkFrame(janela_main, width=225, height=175, fg_color='#2C2F33', corner_radius=10)
            frame.place(x=x, y=y)
            criar_grafico_pizza(frame, dados_exemplo, labels_exemplo)

    janela_main.mainloop()

# Execução principal
dados_professor, dados_administrador = buscar_dados_usuario()
criar_interface(dados_professor)
