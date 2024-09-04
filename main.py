from customtkinter import *

count = 0
def Btn_click():
    global count
    count += 1
    label.configure(text=f"You've clicked this button {count} times :P")
app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
label = CTkLabel(master=app, text="You've clicked this button 0 times")
button = CTkButton(master=app, text="Hi :3", command=Btn_click)
label.place(relx=0.5,rely=0.4, anchor="center")
button.place(relx=0.5,rely=0.5, anchor="center")
app.mainloop()