from PIL import Image
from os import listdir
from tqdm import tqdm

def save_training_data(directory):
    images = []
    size = (3500, 4500)
    image = Image.open("./raw.jpg").convert("RGB").resize(size)
    count = 0
    for i in tqdm(range(7)):
        for j in range(9):
            temp = image.crop((i*500, j*500, i*500 + 500, j*500 + 500))
            temp.save(directory + "/" + str(count) + ".jpg")
            count += 1

save_training_data("./train_data")