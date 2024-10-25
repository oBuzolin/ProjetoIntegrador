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

# Função para gerar gráfico de pizza e inseri-lo em um frame estilizado como um cartão de sala de aula
def criar_cartao_sala(frame, dados, labels, titulo, cor_fundo):
    # Adicionar título da sala de aula
    titulo_label = ctk.CTkLabel(frame, text=titulo, font=("Arial", 16, "bold"), text_color="white", bg_color=cor_fundo)
    titulo_label.pack(pady=(10, 5))

    # Criar gráfico de pizza no centro do cartão
    fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=100)
    cores = ['#F04747', '#7289DA', '#2C2F33', '#40444B']
    
    ax.pie(dados, colors=cores, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'white'})
    fig.patch.set_facecolor(cor_fundo)
    ax.set_facecolor(cor_fundo)
    ax.axis('equal')
    
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

# Função para obter dados do usuário a partir do banco de dados
def obter_dados_usuario(tabela, usuario, cursor):
    queries = {
        'professor': {
            'nome': "SELECT Nome FROM Minerva_Professor WHERE usuario = %s",
            'disciplina': "SELECT Disciplina FROM Minerva_Professor WHERE usuario = %s",
            'carga_horaria': "SELECT CargaHoraria FROM Minerva_Professor WHERE usuario = %s",
            'dias_semana': "SELECT DiaSemana FROM Minerva_Professor WHERE usuario = %s",
            'ra': "SELECT matricula FROM Minerva_Professor WHERE usuario = %s"
        },
        'administrador': {
            'nome': "SELECT Nome FROM Minerva_Administrador WHERE usuario = %s",
            'cargo': "SELECT Cargo FROM Minerva_Administrador WHERE usuario = %s"
        }
    }

    dados = {key: cursor.execute(query, (usuario,)) or cursor.fetchone()[0] for key, query in queries[tabela].items() if cursor.fetchone()}
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
            dados_professor = obter_dados_usuario('professor', usuario, cursor)
            if dados_professor:
                print(f'Dados do Professor: {dados_professor}')
                return dados_professor, None
            else:
                dados_administrador = obter_dados_usuario('administrador', usuario, cursor)
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

# Função para criar e alternar a visibilidade do menu do usuário
menu_usuario = None
def toggle_menu_usuario(master, event):
    global menu_usuario
    if menu_usuario is not None and menu_usuario.winfo_exists():
        menu_usuario.destroy()
        menu_usuario = None
    else:
        menu_usuario = ctk.CTkToplevel(master)
        menu_usuario.geometry("150x100")
        menu_usuario.title("Opções do Usuário")
        menu_usuario.transient(master)
        menu_usuario.overrideredirect(True)

        botao_perfil = ctk.CTkButton(menu_usuario, text="Perfil", width=140, fg_color="#7289DA")
        botao_perfil.pack(pady=5)

        botao_config = ctk.CTkButton(menu_usuario, text="Configurações", width=140, fg_color="#7289DA")
        botao_config.pack(pady=5)

        botao_sair = ctk.CTkButton(menu_usuario, text="Sair", width=140, fg_color="#F04747", command=master.quit)
        botao_sair.pack(pady=5)

        menu_usuario.geometry(f"+{event.x_root}+{event.y_root}")

# Criação da interface principal
def criar_interface(dados_professor):
    janela_main = ctk.CTk()
    janela_main.title("Tela ADM")
    janela_main.geometry("1000x650")
    janela_main.resizable(False, False)
    ctk.set_appearance_mode("Dark")

    # Menu superior
    menu = ctk.CTkFrame(janela_main, width=990, height=35, corner_radius=10)
    menu.place(x=5, y=1)

    # Ícone e texto "Minerva"
    icon_path = os.getenv('ICON_PATH', "Desktop/FRONTEND/img/minerva.ico")
    if os.path.exists(icon_path):
        icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(25, 25))
        icon_label = ctk.CTkLabel(menu, text='', image=icon_image)
        icon_label.place(x=6, y=2)
    fonte = ctk.CTkFont(family="Cloister Black", size=14)
    text_label = ctk.CTkLabel(menu, text='Minerva', text_color='white', font=fonte)
    text_label.place(x=65, y=2)

    # Botão redondo para abrir o menu do usuário
    letra = dados_professor['nome'][0] if dados_professor else ""
    round_button = ctk.CTkButton(menu, text=letra, width=28, height=28, corner_radius=20, fg_color='#585858', font=fonte)
    round_button.place(x=950, y=2)
    round_button.bind("<Button-1>", lambda event: toggle_menu_usuario(janela_main, event))

    # Frame lateral e botão "Agenda"
    frame1 = ctk.CTkFrame(janela_main, width=225, height=595, bg_color='#40444B', corner_radius=10)
    frame1.place(x=10, y=40)
    ctk.CTkButton(frame1, text="Agenda", text_color="white", width=210, height=40, fg_color='#F04747', bg_color="#7289DA", corner_radius=5).place(x=8, y=10)

    # Criar cartões de sala de aula com layout estilizado
    dados_exemplo = [25, 35, 20, 20]
    labels_exemplo = ["Parte A", "Parte B", "Parte C", "Parte D"]
    titulos_salas = ["Matemática", "História", "Química", "Física"]
    cores_fundo = ['#7289DA', '#F04747', '#2C2F33', '#40444B']

    x, y = 250, 50
    for titulo, cor_fundo in zip(titulos_salas, cores_fundo):
        frame_sala = ctk.CTkFrame(janela_main, width=250, height=180, fg_color=cor_fundo, corner_radius=10)
        frame_sala.place(x=x, y=y)
        criar_cartao_sala(frame_sala, dados_exemplo, labels_exemplo, titulo, cor_fundo)
        y += 200
        if y > 500:
            y = 50
            x += 260

   


    janela_main.mainloop()

# Execução principal
dados_professor, dados_administrador = buscar_dados_usuario()
criar_interface(dados_professor)
