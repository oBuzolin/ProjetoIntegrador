from tkinter import Menu
from turtle import color
import customtkinter as ctk

# criação da janela windons
janela = ctk.CTk()

# colocando as configuraçoes da tela principal
janela.title("tela ADM")
janela.geometry("1000x650")  
janela.maxsize(width=1100, height=700)
janela.minsize(width=800, height=600)
janela.resizable(width=False, height=False)
ctk.set_appearance_mode("Dark")

# criando frame
#menu 
menu = ctk.CTkFrame(master=janela,width=990,height=30).place(x=5,y=1)
segundo =  ctk.CTkFrame(master=menu,width=55,height=30,fg_color='grey').place(x=6, y=2)
terceiro =  ctk.CTkFrame(master=menu,width=140,height=30,fg_color='grey').place(x=65, y=2)
quarto =  ctk.CTkFrame(master=menu,width=40,height=30,fg_color='grey').place(x=960, y=2)



#menu ativo
frame1 = ctk.CTkFrame(master=janela, width=225, height=595).place(x=10, y=40)
button = ctk.CTkButton(master=frame1, text="Agenda", text_color="black", width=210, height=40,fg_color='red',bg_color="transparent").place(x=16, y=46)

#visão geral
turma1 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=250, y=45)
turma2 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=485, y=45)
turma3 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=720, y=45)

turma4 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=250, y=230)
turma5 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=485, y=230)
turma6 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=720, y=230)

turma7 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=250, y=415)
turma8 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=485, y=415)
turma9 = ctk.CTkFrame(master=janela,width=225,height=175,fg_color='grey').place(x=720, y=415)



# iniciando o loping
janela.mainloop()