from tkinter import *
from PIL import *

root = Tk()

root.title("Ausgefwähltes Bild")
root.geometry("500x250")

#Bild anlegen und positionieren
image1 = PhotoImage(file="Gruppe1.png")
panel1 = Label(root, image=image1)
panel1.grid(
  row=0,
  column=0,
)

root.mainloop()

from PIL import Image

# Bild ist im gleichen Verzeichnis, wie das Python Programm
im = Image.open('Gruppe1.png')

# Bildgröße in Pixeln ermitteln, damit nachher die Ecken abgefragt werden können
width, height = im.size
width = int(width) - 1
height = int(height) - 1
rgb_im = im.convert('RGB')


# Funktion zur Abfrage der Pixelfarben
def pixelfarbe(rgb_im, x, y):
  rgb_im = rgb_im
  x = x
  y = y
  r, g, b = rgb_im.getpixel((x, y))
  print("Position:", (x, y), "RGB:", (r, g, b))
  # Y
  Y = (299 / 1000 * r + 587 / 1000 * g + 114 / 1000 * b)
  # Cb
  Cb = (-169 / 1000 * r - 331 / 1000 * g - 500 / 1000 * b)
  # Cr
  Cr = (500 / 1000 * r - 419 / 1000 * g - 81 / 1000 * b)
  print("Y=", Y)
  print("Cb=", Cb)
  print("Cr=", Cr)
  print(" ")

  if x == 0 and y == 0 or x == 0 and y == 1 or x == 1 and y == 0 or x == 1 and y == 1:
    print(Cb)
    print(Cr)
    print(" ")

  if x == 0 and y == 2 or x == 0 and y == 3 or x == 1 and y == 2 or x == 1 and y == 3:
    print("Cb neu")
    print("Cr neu")
    print(" ")

  if x == 2 and y == 0 or x == 2 and y == 1 or x == 3 and y == 0 or x == 3 and y == 1:
    print("Cb neu")
    print("Cr neu")
    print(" ")

  if x == 2 and y == 2 or x == 2 and y == 3 or x == 3 and y == 2 or x == 3 and y == 3:
    print("Cb neu")
    print("Cr neu")
    print(" ")


pixelfarbe(rgb_im, 0, 0)
pixelfarbe(rgb_im, 0, 1)
pixelfarbe(rgb_im, 1, 0)
pixelfarbe(rgb_im, 1, 1)

pixelfarbe(rgb_im, 0, 2)
pixelfarbe(rgb_im, 0, 3)
pixelfarbe(rgb_im, 1, 2)
pixelfarbe(rgb_im, 1, 3)

pixelfarbe(rgb_im, 2, 0)
pixelfarbe(rgb_im, 2, 1)
pixelfarbe(rgb_im, 3, 0)
pixelfarbe(rgb_im, 3, 1)

pixelfarbe(rgb_im, 2, 2)
pixelfarbe(rgb_im, 2, 3)
pixelfarbe(rgb_im, 3, 2)
pixelfarbe(rgb_im, 3, 3)