from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

# Lista os arquivos da pasta imagens
arquivos = os.listdir('imagens')

# Variável para armazenar as imagens
imagens = []

# Percorre a lista de arquivos
for arquivo in arquivos:
    # Abre a imagem
    img = Image.open('imagens/' + arquivo)
    # Adiciona a imagem na lista
    imagens.append(ImageTk.PhotoImage(img))

# Exibe os arquivos em um Label
# arquivos_label = Label(root, text=arquivos)
# arquivos_label.pack()

img_label = Label(root, image=imagens[0])

img_label.pack()

root.mainloop()