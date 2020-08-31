import mouse
import keyboard
from PIL import Image
import pyscreenshot
from time import sleep
import os

def ver():
  while True:
    img = pyscreenshot.grab()
    width, height = img.size
    pixel_values = list(img.getdata())
    print (pixel_values[width*mouse.get_position()[1]+mouse.get_position()[0]])


ver()
