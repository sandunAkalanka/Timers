import tkinter as tk
import time

root = tk.Tk()
root.title("Timer Animation")
root.geometry('300x300')

frame = tk.Frame(root)

def rgbToHex(rgb):
    return '#%02x%02x%02x' % rgb

timer = 8
red = 100
green , blue = 0 , 0

lbl1 = tk.Label(frame , width = 2 , height = 1)
lbl2 = tk.Label(frame , width = 2 , height = 1)
lbl3 = tk.Label(frame , width = 2 , height = 1)
lbl4 = tk.Label(frame , width = 2 , height = 1)
lbl5 = tk.Label(frame , width = 2 , height = 1)
lbl6 = tk.Label(frame , width = 2 , height = 1)

lbl1.grid(row = 0 , column = 0)
lbl2.grid(row = 0 , column = 1)
lbl3.grid(row = 0 , column = 2)
lbl4.grid(row = 0 , column = 3)
lbl5.grid(row = 0 , column = 4)
lbl6.grid(row = 0 , column = 5)

frame.pack(expand = 1)

while timer > 0:
    bg1 = rgbToHex((red, green , blue))
    bg2 = rgbToHex(((red - 20) , green , blue))
    bg3 = rgbToHex(((red - 40) , green , blue))
    bg4 = rgbToHex(((red - 60) , green , blue))
    bg5 = rgbToHex(((red - 80) , green , blue))
    bg6 = rgbToHex(((red - 100) , green , blue))

    lbl1.config(bg = bg1)
    lbl2.config(bg = bg2)
    lbl3.config(bg = bg3)
    lbl4.config(bg = bg4)
    lbl5.config(bg = bg5)
    lbl6.config(bg = bg6)

    red +=20

    root.update()
    time.sleep(1)
    timer -=1

root.mainloop()