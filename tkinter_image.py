from tkinter import *
from PIL import ImageTk, Image, ImageOps
import os

root = Tk()

# Lista os arquivos da pasta imagens
arquivos = os.listdir('imagens')

# Variável para armazenar as imagens
imagens = []

# Variável de controle do índice da imagem atual
imagem_atual = 0

# Percorre a lista de arquivos
for arquivo in arquivos:
    # Abre a imagem
    img = Image.open('imagens/' + arquivo)
    # Redimensiona a imagem
    img = ImageOps.contain(img, (200, 200))
    # Adiciona a imagem na lista
    imagens.append(ImageTk.PhotoImage(img))

# Exibe os arquivos em um Label
# arquivos_label = Label(root, text=arquivos)
# arquivos_label.pack()

img_label = Label(root, image=imagens[imagem_atual])

img_label.grid(column=0, row=0, columnspan=3)

def prev_image():
    global imagem_atual
    global img_label
    global imagens
    
    # Verifica se é a primeira imagem. Se sim, volta para a última imagem
    if imagem_atual == 0:
        imagem_atual = len(imagens) - 1
    else:
        imagem_atual -= 1

    # Apaga a imagem atual
    img_label.grid_forget()

    # Exibe a nova imagem
    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0, row=0, columnspan=3)

def next_image():
    global imagem_atual
    global img_label
    global imagens
    
    # Verifica se é a primeira imagem. Se sim, volta para a última imagem
    if imagem_atual == len(imagens) - 1:
        imagem_atual = 0
    else:
        imagem_atual += 1

    # Apaga a imagem atual
    img_label.grid_forget()

    # Exibe a nova imagem
    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=0, row=0, columnspan=3)

# Botão para mostrar a próxima imagem
next_btn = Button(root, text='Próxima', command=next_image)
next_btn.grid(column=2, row=1)
# Botão para mostrar a imagem anterior
prev_btn = Button(root, text='Anterior', command=prev_image)
prev_btn.grid(column=0, row=1)
# Botão para fecha a janela
quit_btn = Button(root, text='Sair', command=root.quit)
quit_btn.grid(column=1, row=1)

root.mainloop()



