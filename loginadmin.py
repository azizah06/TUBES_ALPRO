from tkinter import *
from tkinter import messagebox
import csv
from window import main

def loginuser():
    with open('login.csv', 'r', encoding='utf-8') as csvfile:        
        reader = csv.reader(csvfile, delimiter=';')    
        next(reader)
        username = entry1.get()
        password = entry2.get()
        
        for row in reader:
            if username == row[0] and password == row[1]:
                messagebox.showinfo("", "Login Success")
                print("Selamat datang")
                root.destroy()
                main()
                break
                
            elif username == "" and password == "":
                messagebox.showinfo("","Blank not allowed")
                loginuser()
            else:
                messagebox.showinfo("","incorrect username and password")
                # loginulang()
                # break 
def loginsuccess():
    loginuser()        
    

root = Tk()
root.title("Login Admin!")
root.geometry("300x190")
root.configure(bg="#fffaef")

global entry1
global entry2

#buat label
Label(root, text="Username").place(x=20, y=20) #place untuk mengatur letak
Label(root, text="Password").place(x=20, y=70)

entry1= Entry(root, bd=3) #bd untuk menentukan ketebalan komponen entry
entry1.place(x=140, y= 20)

entry2= Entry(root, bd=3, show="*") #bd untuk menentukan ketebalan komponen entry
entry2.place(x=140, y= 70)

#buat button
Button(root, text="Login", command=loginsuccess, height=1, width=10,bd=2).place(x=100,y=120)

root.mainloop()