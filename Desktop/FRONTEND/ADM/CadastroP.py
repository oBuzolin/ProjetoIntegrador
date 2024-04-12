import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()

def tela():
  janela.geometry("700x400")
  janela.title("Sistema de Login")
  janela.resizable(False, False)

def telaLogin():
  img = ImageTk.PhotoImage(Image.open("foto2.png").resize((150, 300)))

  label_img = tk.Label(janela, image=img)
  label_img.place(x=20, y=100)

  titulo_label = tk.Label(janela, text="Entre na sua conta e tenha \n acesso a plataforma",
                          font=("Roboto", 20), foreground="#00B0F0")
  titulo_label.place(x=50, y=10)

  # frame
  login_frame = tk.Frame(janela, width=350, height=396)
  login_frame.pack(side="RIGHT")

  # frame widgets
  label = tk.Label(login_frame, text="Sistema de Login", font=('Arial',20,'bold'), foreground='white')
  label.place(x=25, y=5)

  # username entry
  username_entry = tk.Entry(login_frame, placeholder_text="Nome", width=300,
                             font=('Robot', 14))
  username_entry.place(x=25, y=105)

  # password entry
  senha_entry = tk.Entry(login_frame, placeholder_text="Senha", width=300,
                         font=('Robot', 14), show="*")
  senha_entry.place(x=25, y=175)

  # checkbox
  checkbox = tk.Checkbutton(login_frame, text="Lembre-se de mim sempre")
  checkbox.place(x=25, y=305)

  # login button
  login_buttom = tk.Button(login_frame, text="LOGIN", width=300)
  login_buttom.place(x=25, y=355)

tela()
telaLogin()
janela.mainloop()
