import os
import dotenv
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dotenv.load_dotenv()

janela_info_turma = None
janela_menu_perfil = None

# Função para abrir a janela de informações da turma
def abrir_info_turma(titulo, dados_professor):
    global janela_info_turma
    if janela_info_turma and janela_info_turma.winfo_exists():
        janela_info_turma.destroy()
    
    if dados_professor is None:
        dados_professor = {'nome': 'N/A', 'carga_horaria': 'N/A', 'dias_semana': 'N/A'}
    
    janela_info_turma = ctk.CTkToplevel()
    janela_info_turma.title(f"Informações da turma - {titulo}")
    janela_info_turma.geometry("400x300")
    janela_info_turma.resizable(False, False)

    ctk.CTkLabel(janela_info_turma, text=f"Turma: {titulo}", font=("Arial", 18, "bold")).pack(pady=10)
    ctk.CTkLabel(janela_info_turma, text=f"Professor: {dados_professor.get('nome', 'N/A')}").pack(pady=5)
    ctk.CTkLabel(janela_info_turma, text=f"Carga Horária: {dados_professor.get('carga_horaria', 'N/A')}").pack(pady=5)
    ctk.CTkLabel(janela_info_turma, text=f"Dias da Semana: {dados_professor.get('dias_semana', 'N/A')}").pack(pady=5)

# Função para criar o mini menu do perfil
def abrir_menu_perfil():
    global janela_menu_perfil
    if janela_menu_perfil and janela_menu_perfil.winfo_exists():
        janela_menu_perfil.destroy()
    else:
        janela_menu_perfil = ctk.CTkToplevel()
        janela_menu_perfil.geometry("200x150")
        janela_menu_perfil.title("Menu Perfil")
        janela_menu_perfil.resizable(False, False)

        # Opções no menu
        ctk.CTkLabel(janela_menu_perfil, text="Perfil", font=("Arial", 16, "bold")).pack(pady=5)
        ctk.CTkButton(janela_menu_perfil, text="Configurações", command=lambda: print("Abrir configurações")).pack(pady=5)
        ctk.CTkButton(janela_menu_perfil, text="Sair", command=lambda: print("Sair do sistema")).pack(pady=5)

# Função para criar o layout das matérias
def criar_cartao_sala(frame, dados, labels, titulo, cor_fundo, dados_professor):
    titulo_label = ctk.CTkLabel(frame, text=titulo, font=("Arial", 16, "bold"), text_color="white", bg_color=cor_fundo)
    titulo_label.pack(pady=(10, 5))
    titulo_label.bind("<Button-1>", lambda e: abrir_info_turma(titulo, dados_professor))

    fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=100)
    cores = ['#F04747', '#7289DA', '#2C2F33', '#40444B']
    
    ax.pie(dados, colors=cores, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'white'})
    fig.patch.set_facecolor(cor_fundo)
    ax.set_facecolor(cor_fundo)
    ax.axis('equal')
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Função para ler usuário
def ler_usuario(arquivo):
    if not os.path.exists(arquivo):
        print(f"Arquivo {arquivo} não encontrado.")
        return None
    with open(arquivo, 'r') as file:
        return file.read().strip()

# Remover arquivo
def remover_arquivo(arquivo):
    if os.path.exists(arquivo):
        os.remove(arquivo)
        print(f'Arquivo {arquivo} excluído com sucesso.')

# Dados do usuário
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

# Conectar e buscar dados do usuário
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

# Interface principal
def criar_interface(dados_professor):
    janela_main = ctk.CTk()
    janela_main.title("Tela ADM")
    janela_main.geometry("1000x650")
    janela_main.resizable(False, False)
    ctk.set_appearance_mode("Dark")

    menu = ctk.CTkFrame(janela_main, width=990, height=35, corner_radius=10)
    menu.place(x=5, y=1)

    icon_path = os.getenv('ICON_PATH', "Desktop/FRONTEND/img/minerva.ico")
    if os.path.exists(icon_path):
        icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(25, 25))
        icon_label = ctk.CTkLabel(menu, text='', image=icon_image)
        icon_label.place(x=6, y=2)
    fonte = ctk.CTkFont(family="Cloister Black", size=14)
    text_label = ctk.CTkLabel(menu, text='Minerva', text_color='white', font=fonte)
    text_label.place(x=65, y=2)

    letra = dados_professor['nome'][0] if dados_professor else ""
    round_button = ctk.CTkButton(menu, text=letra, width=28, height=28, corner_radius=20, fg_color='#585858', font=fonte, command=abrir_menu_perfil)
    round_button.place(x=950, y=2)

    frame1 = ctk.CTkFrame(janela_main, width=225, height=595, bg_color='#40444B', corner_radius=10)
    frame1.place(x=10, y=40)
    ctk.CTkButton(frame1, text="Agenda", text_color="white", width=210, height=40, fg_color='#F04747', bg_color="#7289DA", corner_radius=5).place(x=8, y=10)

    dados_exemplo = [25, 35, 20, 20]
    labels_exemplo = ["Parte A", "Parte B", "Parte C", "Parte D"]
    titulos_salas = ["Matemática", "História", "Química", "Física", "Geografia", "Biologia", "Literatura", "Artes", "Educação Física"]
    cores_fundo = ['#7289DA', '#F04747', '#2C2F33', '#40444B', '#43B581', '#FAA61A', '#B9A9FE', '#FFD700', '#D69E2E']

    x, y = 250, 50
    for i, (titulo, cor_fundo) in enumerate(zip(titulos_salas, cores_fundo)):
        frame_sala = ctk.CTkFrame(janela_main, width=250, height=180, fg_color=cor_fundo, corner_radius=10)
        frame_sala.place(x=x, y=y)
        criar_cartao_sala(frame_sala, dados_exemplo, labels_exemplo, titulo, cor_fundo, dados_professor)

        if (i + 1) % 3 == 0:
            y += 200
            x = 250
        else:
            x += 260

    janela_main.mainloop()

dados_professor, dados_administrador = buscar_dados_usuario()
criar_interface(dados_professor)
