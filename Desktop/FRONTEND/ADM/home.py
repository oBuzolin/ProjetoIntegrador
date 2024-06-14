import customtkinter as ctk

# criação da janela
janela_main = ctk.CTk()
janela_main.title("Tela ADM")
janela_main.geometry("1000x650")
janela_main.maxsize(width=1100, height=700)
janela_main.minsize(width=800, height=600)
janela_main.resizable(width=False, height=False)
ctk.set_appearance_mode("Dark")

# Menu
menu = ctk.CTkFrame(master=janela_main, width=990, height=30)
menu.place(x=5, y=1)

segundo = ctk.CTkFrame(master=menu, width=55, height=30, fg_color='grey')
segundo.place(x=6, y=2)

terceiro = ctk.CTkFrame(master=menu, width=140, height=30, fg_color='grey')
terceiro.place(x=65, y=2)

quarto = ctk.CTkFrame(master=menu, width=40, height=30, fg_color='grey')
quarto.place(x=960, y=2)

# Menu ativo
frame1 = ctk.CTkFrame(master=janela_main, width=225, height=595)
frame1.place(x=10, y=40)

button = ctk.CTkButton(master=frame1, text="Agenda", text_color="black", width=210, height=40, fg_color='red', bg_color="transparent")
button.place(x=16, y=46)

# Visão geral das turmas
x_positions = [250, 485, 720]
y_positions = [45, 230, 415]

for x in x_positions:
    for y in y_positions:
        ctk.CTkFrame(master=janela_main, width=225, height=175, fg_color='grey').place(x=x, y=y)

# Loop principal da janela
janela_main.mainloop()
