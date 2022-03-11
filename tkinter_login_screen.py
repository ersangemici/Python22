import tkinter as tk
from tkinter import messagebox
brain={}
def register():
    user=username_entry.get()
    password=password_entry.get()
    brain.update({user:password})
    messagebox.showinfo("Information","Register succesful!")    

def login():
    user=username_entry.get()
    password=password_entry.get()
    psw=brain.get(user)
    if password==psw :
        messagebox.showinfo("Information","Login succesful!")           
    else :
        messagebox.showerror("Warming","Wrong password or username")
    

root = tk.Tk()
root.geometry("250x150")
root.title("Password Administrator")
root.resizable(False,False)

username_label=tk.Label(root,text="Username:")
username_label.grid(column=1,row=1)
username_entry=tk.Entry(root)
username_entry.grid(column=3,row=1)


password_label=tk.Label(root,text="Password:")
password_label.grid(column=1,row=3)
password_entry=tk.Entry(root,show="*")
password_entry.grid(column=3,row=3)

login_button=tk.Button(root,text="Login",command=login)
login_button.grid(column=1,row=5)

register_button=tk.Button(root,text="Register",command=register)
register_button.grid(column=3,row=5)

root.mainloop()
