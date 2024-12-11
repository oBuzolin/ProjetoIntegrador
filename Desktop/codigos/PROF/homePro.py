import os
import dotenv
import mysql.connector
from mysql.connector import Error
from PIL import Image
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Patch
import subprocess

dotenv.load_dotenv()

janela_info_turma = None
janela_menu_perfil = None

def abrir_info_turma(titulo, id_turma, dados_Professor):
    global janela_info_turma

    # Verifica se a janela ainda existe e destrói se necessário
    if janela_info_turma is not None and janela_info_turma.winfo_exists():
        janela_info_turma.destroy()

    # Criação da nova janela
    janela_info_turma = ctk.CTkToplevel()
    janela_info_turma.title(f"Informações da turma - {titulo}")
    janela_info_turma.geometry("800x600")
    janela_info_turma.resizable(False, False)

    # Adiciona um CTkScrollableFrame
    scroll_frame = ctk.CTkScrollableFrame(janela_info_turma, width=780, height=580)
    scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Conteúdo dentro do scroll frame
    ctk.CTkLabel(scroll_frame, text=f"Turma: {titulo}", font=("Arial", 18, "bold")).pack(pady=10)

    try:
        conn = conectar_bd()
        if conn.is_connected():

            cursor = conn.cursor()

            # Obter professor e disciplina
            cursor.execute("""
                SELECT p.nome, p.disciplina, p.cargaHoraria, p.diaSemana 
                FROM Minerva_Professor p
                JOIN Minerva_ProfessorTurma pt ON p.matricula = pt.matricula
                WHERE pt.id_Turma = %s
            """, (id_turma,))
            professor_data = cursor.fetchone()
            if professor_data:
                professor, disciplina, carga_horaria, dia_semana = professor_data
                ctk.CTkLabel(scroll_frame, text=f"Professor: {professor}").pack(pady=5)
                ctk.CTkLabel(scroll_frame, text=f"Disciplina: {disciplina}").pack(pady=5)
                ctk.CTkLabel(scroll_frame, text=f"Carga Horária: {carga_horaria}h").pack(pady=5)
                ctk.CTkLabel(scroll_frame, text=f"Dia da Semana: {dia_semana}").pack(pady=5)
            else:
                ctk.CTkLabel(scroll_frame, text="Professor: N/A").pack(pady=5)


            

            # Obter alunos e distribuição por curso
            cursor.execute("""
                SELECT a.nome, a.curso
                FROM Minerva_Aluno a
                JOIN Minerva_MatriculaTurma mt ON a.RA = mt.ra_id
                WHERE mt.id_Turma_id = %s
            """, (id_turma,))
            alunos = cursor.fetchall()
            ctk.CTkLabel(scroll_frame, text="Alunos:").pack(pady=5)
            alunos_inner_frame = ctk.CTkScrollableFrame(scroll_frame, width=400, height=150)
            alunos_inner_frame.pack()
            cursos = {}
            for aluno, curso in alunos:
                ctk.CTkLabel(alunos_inner_frame, text=aluno).pack(anchor="w", padx=10)
                cursos[curso] = cursos.get(curso, 0) + 1

            # Estatísticas de cursos
            if cursos:
                cursos_texto = "\n".join([f"{curso}: {quantidade}" for curso, quantidade in cursos.items()])
                ctk.CTkLabel(scroll_frame, text=f"Distribuição por Curso:\n{cursos_texto}").pack(pady=5)

            # Estatísticas de atividades
            cursor.execute("""
                SELECT titulo, envio, entrega
                FROM Minerva_Atividades
                WHERE turma_id = %s
            """, (id_turma,))
            atividades = cursor.fetchall()
            total_atividades = len(atividades)
            entregues = sum(1 for _, envio, entrega in atividades if envio is not None and entrega is not None and envio <= entrega)
            atrasadas = total_atividades - entregues
            ctk.CTkLabel(scroll_frame, text=f"Atividades Registradas: {total_atividades}").pack(pady=5)
            ctk.CTkLabel(scroll_frame, text=f"Entregues no Prazo: {entregues}").pack(pady=5)
            ctk.CTkLabel(scroll_frame, text=f"Atrasadas: {atrasadas}").pack(pady=5)

            # Gráfico da distribuição de notas
            cursor.execute("""
                SELECT nota
                FROM Minerva_Atividades
                WHERE turma_id = %s
            """, (id_turma,))
            notas = [float(nota[0]) for nota in cursor.fetchall() if nota[0] and nota[0].replace('.', '', 1).isdigit()]
            if notas:
                abaixo = sum(1 for n in notas if 1 <= n <= 4)
                na_media = sum(1 for n in notas if 5 <= n <= 7)
                acima = sum(1 for n in notas if 8 <= n <= 10)
                dados = [abaixo, na_media, acima]
                categorias = ["Abaixo (1-4)", "Na média (5-7)", "Acima (8-10)"]

                fig, ax = plt.subplots(figsize=(6, 4))
                ax.bar(categorias, dados, color=['#F04747', '#7289DA', '#43B581'])
                ax.set_title("Distribuição das Notas")
                ax.set_ylabel("Número de Estudantes")
                canvas = FigureCanvasTkAgg(fig, master=scroll_frame)
                canvas.draw()
                canvas.get_tk_widget().pack()
    except Error as e:
        print(f"Erro ao buscar informações da turma: {e}")
    finally:
        if conn.is_connected():
            conn.close()



def criar_cartao_sala(frame, dados, labels, titulo, cor_fundo, id_turma, dados_Professor):
    titulo_label = ctk.CTkLabel(frame, text=titulo, font=("Arial", 20, "bold"), text_color="white", bg_color=cor_fundo)
    titulo_label.pack(pady=(10, 5))
    titulo_label.bind("<Button-1>", lambda e: abrir_info_turma(titulo, id_turma, dados_Professor))

    # Ajustando tamanho para visualização correta
    fig, ax = plt.subplots(figsize=(2.4, 2.4), dpi=95)
    cores = ['#F04747', '#7289DA', '#43B581']  # Cores para as categorias: abaixo, na média, acima
    
    if not any(dados):  # Garantir gráfico mesmo sem dados
        dados = [1, 1, 1]
        labels = ["Sem dados", "Sem dados", "Sem dados"]

    wedges, texts, autotexts = ax.pie(
        dados, 
        labels=None, 
        colors=cores, 
        startangle=80, 
        autopct='%1.1f%%', 
        wedgeprops={'edgecolor': 'white'}
    )
    ax.axis('equal')
    fig.patch.set_facecolor(cor_fundo)
    ax.set_facecolor(cor_fundo)

    # Posicionando a legenda acima do gráfico
    legend_labels = ["Abaixo da média (1-4)", "Na média (5-7)", "Acima da média (8-10)"]
    legend_handles = [Patch(color=cores[i], label=legend_labels[i]) for i in range(len(legend_labels))]
    fig.legend(
        handles=legend_handles, 
        loc="upper center",  # Posição da legenda: acima do gráfico
        bbox_to_anchor=(0.5, 0.9),  # Ajuste fino para colocar a legenda acima e centralizada
        fontsize=7
    )

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()



global_usuario = None

def ler_usuario(arquivo="Desktop\\codigos\\arquivos\\professor.txt"):
    global global_usuario  # Declarando que vamos usar a variável global

    if not os.path.exists(arquivo):
        print(f"Arquivo {arquivo} não encontrado.")
        return None

    with open(arquivo, 'r') as file:
        usuario = file.read().strip()

    global_usuario = usuario  # Salvando o valor na variável global

    os.remove(arquivo)  # Excluir o arquivo após a leitura
    print(f"Arquivo {arquivo} excluído após a leitura.")
    return usuario


def obter_dados_professor(usuario, cursor):
    cursor.execute("""
        SELECT matricula, nome, disciplina, cargaHoraria, diaSemana 
        FROM Minerva_Professor WHERE usuario = %s
    """, (usuario,))
    dados = cursor.fetchone()
    if dados:
        return {
            'matricula': dados[0],
            'nome': dados[1],
            'disciplina': dados[2],
            'carga_horaria': dados[3],
            'dias_semana': dados[4]
        }
    return None

def conectar_bd():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', '143.106.241.3'),
        port=os.getenv('DB_PORT', '3306'),
        user=os.getenv('DB_USER', 'cl201107'),
        password=os.getenv('DB_PASSWORD', 'cl*02032005'),
        database=os.getenv('DB_NAME', 'cl201107')
    )
def abrir_arquivo(caminho):
    try:
        subprocess.Popen(["python", caminho], shell=True)
    except Exception as e:
        print(f"Erro ao abrir o arquivo {caminho}: {e}")

def buscar_dados_usuario():
    usuario = ler_usuario()
    if not usuario:
        print("Não foi possível ler o email do arquivo.")
        return None

    try:
        conn = conectar_bd()
        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados")
            cursor = conn.cursor()
            dados_professor = obter_dados_professor(usuario, cursor)
            if dados_professor:
                return dados_professor
            else:
                print("Nenhum dado de professor foi encontrado.")
            cursor.close()
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            print("Conexão ao MySQL foi fechada")
    return None

def criar_interface(dados_Professor):
    janela_main = ctk.CTk()
    janela_main.title("Tela Prof")
    janela_main.geometry("1000x650")
    janela_main.resizable(False, False)
    ctk.set_appearance_mode("Dark")

    menu = ctk.CTkFrame(janela_main, width=990, height=35, corner_radius=10)
    menu.place(x=5, y=1)

    icon_path = os.getenv('ICON_PATH', "Desktop\\codigos\\img\\minerva.ico")
    if os.path.exists(icon_path):
        icon_image = ctk.CTkImage(light_image=Image.open(icon_path), size=(25, 25))
        icon_label = ctk.CTkLabel(menu, text='', image=icon_image)
        icon_label.place(x=6, y=2)
    fonte = ctk.CTkFont(family="Cloister Black", size=14)
    text_label = ctk.CTkLabel(menu, text='Minerva', text_color='white', font=fonte)
    text_label.place(x=65, y=2)

    letra = dados_Professor['nome'][0] if dados_Professor else ""
    round_button = ctk.CTkButton(menu, text=letra, width=28, height=28, corner_radius=20, fg_color='#585858', font=fonte)
    round_button.place(x=950, y=2)

    frame1 = ctk.CTkFrame(janela_main, width=225, height=595, bg_color='#40444B', corner_radius=10)
    frame1.place(x=10, y=40)

    botoes = [
        ("Lista de alunos", r"Desktop\codigos\ADM\listaAluno.py"),
    ]

    for i, (texto, caminho) in enumerate(botoes):
        ctk.CTkButton(frame1, text=texto, text_color="white", width=200, height=40,
                      fg_color='#F04747', bg_color="#7289DA", corner_radius=5,
                      command=lambda c=caminho: abrir_arquivo(c)).place(x=8, y=10 + i * 50)

    scroll_frame = ctk.CTkScrollableFrame(janela_main, width=745, height=550, corner_radius=10, bg_color="#40444B")
    scroll_frame.place(x=240, y=40)

    try:
        conn = conectar_bd()
        if conn.is_connected():
            cursor = conn.cursor()

            # Obtém o usuário do professor
            usuario_professor = ler_usuario()

            # Verifica se o professor existe e obtém suas turmas
            cursor.execute("""
                SELECT pt.id_Turma, t.nomeTurma
                FROM Minerva_ProfessorTurma pt
                JOIN Minerva_Turma t ON pt.id_Turma = t.id_Turma
                JOIN Minerva_Professor p ON pt.matricula = p.matricula
                WHERE p.usuario = %s
            """, (global_usuario,))
            turmas = cursor.fetchall()

            # Processa cada turma encontrada
            for i, (id_turma, nome_turma) in enumerate(turmas):
                # Obtém as notas da turma
                cursor.execute("SELECT nota FROM Minerva_Atividades WHERE turma_id = %s", (id_turma,))
                notas = [float(nota[0]) for nota in cursor.fetchall()]

                # Classifica as notas
                abaixo = sum(1 for n in notas if 1 <= n <= 4)
                na_media = sum(1 for n in notas if 5 <= n <= 7)
                acima = sum(1 for n in notas if 8 <= n <= 10)
                dados = [abaixo, na_media, acima]

                # Cria o cartão da turma
                frame_turma = ctk.CTkFrame(scroll_frame, width=280, height=300, fg_color="#2C2F33", corner_radius=10)
                frame_turma.grid(row=i // 3, column=i % 3, padx=10, pady=15)
                criar_cartao_sala(frame_turma, dados, [], nome_turma, "#2C2F33", id_turma, dados_Professor)

            cursor.close()
    except Error as e:
        print(f"Erro ao buscar turmas ou notas: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
    

    janela_main.mainloop()

if __name__ == "__main__":
    dados_usuario = buscar_dados_usuario()
    criar_interface(dados_usuario)
