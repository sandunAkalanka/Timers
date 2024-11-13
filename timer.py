import tkinter as tk
import time

root = tk.Tk()
root.title("Timer App")
root.geometry('400x300')
root.resizable(False , False)

root.config(bg = 'RoyalBlue4')

sec = tk.StringVar()
min = tk.StringVar()
hr = tk.StringVar()

tk.Entry(root , textvariable = sec , width = 2 , font = 'Helvetica 14').place(x = 220 , y =120)
sec.set('00')
tk.Entry(root , textvariable = min , width = 2 , font = 'Helvetica 14').place(x = 180 , y = 120)
min.set('00')
tk.Entry(root , textvariable = hr , width = 2 , font = 'Helvetica 14').place(x = 142 , y =120)
hr.set('00')

def countdownTimer():
    times = int(hr.get())*3600 + int(min.get())*60 + int(sec.get())
    while times > -1:
        minute , second = (times // 60 , times % 60)
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
        sec.set(second)
        min.set(minute)
        hr.set(hour)

        #Update the time    
        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            min.set('00')
            hr.set('00')
        times -= 1

tk.Label(root , font = ('Helvetica Bold' , 22) , text = "Enter Timer Values" , background = 'RoyalBlue4').place(x = 105 , y = 70)
tk.Button(root , font = ('Helvetica Bold' , 10) , text = "START" , bd = 2 , bg = 'midnight blue' , command = countdownTimer).place(x = 167 , y = 165)


root.mainloop()