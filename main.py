import pprint as pp
import os
import  matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from PIL import Image  
import PIL
from tqdm import tqdm
from pma_python import core

#=========STUFF TO CHANGE==========

scale = 4
pma_start_slide_dir = "Root/Users/cyb3rblaz3/Desktop/Python Projects/ScnConverter/data"
slideIndex = 1

#==================================


try:
    os.remove("./slide.jpg")
except:
    pass

print("pma_python library loaded; version", core.__version__)

version = core.get_api_version()
pp.pprint(version)

core.get_api_verion_string()

sessionID = core.connect()

if (sessionID == None):
	print("Unable to connect to PMA.start");
else:
	print("Successfully connected to PMA.start; sessionID = ", sessionID)

scale = 10
def get_concat(im1, im2, x, y):
    dst = Image.new('RGB', (512*scale, 512*scale))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (x, y))
    return dst

slides = core.get_slides(pma_start_slide_dir)
print(slides)
slide = slides[slideIndex]
for zl in range(0, core.get_max_zoomlevel(slide)):
    (x, y, tot) = core.get_number_of_tiles(slide, zl)
    if tot > scale*scale and x >= scale and y >= scale:
        break

prevImage = None
currY = 0

for i in tqdm(range(1,scale*scale+1)):
    xr = 1 + (i-1) % scale
    yr = int((i-1) / scale) + 1
    tile = core.get_tile(slide, xr, yr, zl)
    if prevImage == None:
        prevImage = tile
    else:
        if (i-1)%scale == 0:
            currY +=1
        prevImage = get_concat(prevImage, tile, ((i-1)%scale)*512, currY*512)

prevImage.save("./slide.jpg")