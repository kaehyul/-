import tkinter as tk
from tkinter import messagebox, simpledialog

# get user's name using a text input field in a message box
name = simpledialog.askstring("your name", "What is your name?",  initialvalue="")
if name:
    messagebox.showinfo("Message", "Hello, " + str(name.capitalize()) + "!")
    ct = messagebox.askyesno("Question", "Do you know that you are cute, " + str(name.capitalize()) + "?")
    if ct == True:
        messagebox.showinfo("<3", "You are, infact you are really cute!")
        messagebox.showinfo("<3", str(name.capitalize()) + ", If you have million number of fans I am one of them.")
        messagebox.showinfo("<3", "If you have ten fans, I am one of them.")
        messagebox.showinfo("<3", "If you have only one fan and that is me.")
        messagebox.showinfo("<3", "If you have no fans, that means I am no longer on earth.")
        messagebox.showinfo("<3", "If the world against the you, I am against the world.")
    else:
        messagebox.showinfo("What!", "all of the world knows that")
        ag = messagebox.askyesno("wby", "do you agree with me?")
        if ag == True :
            messagebox.showinfo("<3", "Yay~!")
        else:
            messagebox.showinfo("</3", "stubborn you are")

else:
    messagebox.showinfo("this the end", "Why?")
messagebox.showinfo("bye", "sun doesn't shine forever, until we met again :'(")