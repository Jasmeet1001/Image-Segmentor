from os import path
from PIL import Image
from itertools import product
# import hashlib
import secrets

def grid(filename, img_in, img_out, grid_size = 3):
    img_val = []
    
    name, ext = path.splitext(filename)
    img = Image.open(path.join(img_in, filename))
    width, height = img.size
    
    rect_w = width // grid_size
    rect_h = height // grid_size

    grid_tiles = product(range(0, height-1, rect_h), range(0, width-1, rect_w))

    for row, col in grid_tiles:
        box = (col, row, col+rect_w, row+rect_h)
        output = path.join(img_out, f'{name}_{row}_{col}{ext}')
        img_val.append((secrets.randbelow(9999999999999), img.crop(box)))
        img.crop(box).save(output)

    return img_val, output

def get_random_tile(tiles, dest_dir):
    choice = secrets.choice(tiles)
    choice[1].save(dest_dir)

result = grid('cat.jpg', r'C:\Users\Master\Documents\GPA_project\original images', r'C:\Users\Master\Documents\GPA_project\cropped images', 4)
get_random_tile(result[0], result[1])