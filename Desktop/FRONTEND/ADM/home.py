import customtkinter as ctk

# Criação da janela principal
janela_main = ctk.CTk()
janela_main.title("Tela ADM")
janela_main.geometry("1000x650")
janela_main.maxsize(width=1100, height=700)
janela_main.minsize(width=800, height=600)
janela_main.resizable(width=False, height=False)
ctk.set_appearance_mode("Dark")  # Modo escuro para uma aparência moderna

# Menu superior
menu = ctk.CTkFrame(master=janela_main, width=990, height=30, corner_radius=10)
menu.place(x=5, y=1)

# Exemplos de submenus
submenus = [
    ctk.CTkFrame(master=menu, width=55, height=30, fg_color='#2C2F33', corner_radius=5),  # Cor cinza escuro
    ctk.CTkFrame(master=menu, width=140, height=30, fg_color='#2C2F33', corner_radius=5),  # Cor cinza escuro
    ctk.CTkFrame(master=menu, width=40, height=30, fg_color='#2C2F33', corner_radius=5)    # Cor cinza escuro
]
x_positions = [6, 65, 960]
for index, submenu in enumerate(submenus):
    submenu.place(x=x_positions[index], y=2)

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