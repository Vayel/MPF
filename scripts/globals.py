# -*-coding: utf-8 -*-

import glob
import os.path
from path import path
import sys
import numpy as np
import matplotlib.pyplot as plt

def draw(filename, title="", xlabel="Days", ylabel="Production (L)"):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    
    ensure_dir(filename)
    plt.savefig(filename + ".png")
    plt.clf()

def ensure_dir(path):
    d = os.path.dirname(path)
    if not(os.path.exists(d)):
        os.makedirs(d)

def get_filename(path, name):
    return os.path.join(os.path.dirname(os.path.splitext(path)[0]), name)

def get_filenames():
    return [filename for filename in path("../data/").walkfiles()]
    
def get_values(f):
    x = []
    y = []
    
    for line in f.readlines():
        x_value, y_value = line.strip().split(" ")
        y_value = round(float(y_value.replace(",", ".")), 2)
            
        x.append(int(x_value))
        y.append(y_value)
            
    return x, y

if __name__ == "__main__":
    print get_filenames(sys.argv[1])
