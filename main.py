from customtkinter import *
import requests
count = 0
def Btn_click():
    global count
    count += 1
    label.configure(text=f"You've clicked this button {count} times :P")
app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
frame = CTkFrame(app)
title = CTkLabel(master=frame, text="Welcome to the Prota 17222 Point Tracker beta ",height=100,width=50, font=("Arial", 30) )
label = CTkLabel(master=frame, text="You've clicked this button 0 times")
button = CTkButton(master=frame, text="Hi :3", command=Btn_click)
title.grid(column=5,row=1)
label.grid(column=5,row=10)
button.grid(column=5,row=5)
frame.pack()
app.mainloop()