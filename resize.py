import PIL
import os
from PIL import Image

f = '/home/arvinda/Projects/Sign Language Detection/data/train/what is your name?'   #d for test as well
print(os.listdir(f))

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((64, 64))
    img.save(f_img)