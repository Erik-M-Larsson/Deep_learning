import numpy as np
import os
import random as rnd
import matplotlib.pyplot as plt


def paths_data_folders(current_dir):
    data_mappar = ["experiment_small_data", "experiment_tiny_data"]
    undermappar = ["train", "val", "test"]

    paths = [
        os.path.join(current_dir, os.path.join(m, u))
        for m in data_mappar
        for u in undermappar
    ]
    return paths


def read_images(paths):
    train_filnamn = np.array(os.listdir(paths[0]))
    rnd.shuffle(train_filnamn)

    val_filnamn = np.array(os.listdir(paths[1]))
    rnd.shuffle(val_filnamn)

    test_filnamn = np.array(os.listdir(paths[2]))
    rnd.shuffle(test_filnamn)

    x_train = [plt.imread(os.path.join(paths[0], filnamn)) for filnamn in train_filnamn]
    x_val = [plt.imread(os.path.join(paths[1], filnamn)) for filnamn in val_filnamn]
    x_test = [plt.imread(os.path.join(paths[2], filnamn)) for filnamn in test_filnamn]

    # Utred vilka som är katter och vilka som är loppiga byrackor
    y_train = np.array(etiketter(train_filnamn) == "cat", dtype=np.int8)
    y_val = np.array(etiketter(val_filnamn) == "cat", dtype=np.int8)
    y_test = np.array(etiketter(test_filnamn) == "cat", dtype=np.int8)
    return x_train, x_val, x_test, y_train, y_val, y_test


def etiketter(fil_namn):
    return np.array([bild[:3] for bild in fil_namn])
