from tkinter import *
from tkinter import messagebox
import csv


def mainadd ():
    root = Tk()
    root.title("New Room Available")
    root.geometry("300x170")

    #buat label
    noLabel = Label(root, text="No. Kamar",font=('Arial Bold',10) )
    typekamarLabel = Label(root, text="Tipe Kamar",font=('Arial Bold',10))
    priceLabel = Label(root, text="Harga",font=('Arial Bold',10))

    #buat grid
    noLabel.grid(row=1, column=0,padx=10, pady=10)
    typekamarLabel.grid(row=2, column=0,padx=10, pady=10)
    priceLabel.grid(row=3, column=0,padx=10, pady=10)

    #buat entry
    entryno = Entry(root, width=25, bd=5)
    entrytypekamar = Entry(root, width=25, bd=3)
    entryprice = Entry(root, width=25, bd=3)

    #buat grid
    entryno.grid(row=1, column=1, columnspan=3,padx=5, pady=5)
    entrytypekamar.grid(row=2, column=1, columnspan=3,padx=5, pady=5)
    entryprice.grid(row=3, column=1, columnspan=3,padx=5, pady=5)

    buttonEnter= Button(root, text="Enter", padx=5,width=5,bd=2,font=('Arial',10), bg="#8899ff")
    buttonUpdate= Button(root, text="Update", padx=5,width=5,bd=2,font=('Arial',10), bg="#8899ff")
    buttonDelete= Button(root, text="Delete", padx=5,width=5,bd=2,font=('Arial',10), bg="#8899ff")

    buttonEnter.grid(row=5,column=1,columnspan=1)
    buttonUpdate.grid(row=5,column=2,columnspan=1)
    buttonDelete.grid(row=5,column=3,columnspan=1)

    root.resizable(False,False)
    root.mainloop()