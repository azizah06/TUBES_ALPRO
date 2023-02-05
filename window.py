import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
# from PIL import ImageTk, Image
from addroom import mainadd

global kamar_list
global item

def read_kamar():
    kamar = []
    with open('kamar.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            kamar.append(row)
    return kamar

def search_kamar(kamar, item):
    # kamar = []
    with open('kamar.csv', 'r',encoding='utf-8' ) as dataFile:
        openCSV = csv.reader(dataFile, delimiter=",")
        # item = entry1.get()
        for row in openCSV:
            if item == row[0] or item == row[1] or item == row[2]:
                print(row)
                for item in kamar:
                    kamar_list.insert(0, f"  {row[0]}   -   {row[1]}   -   Rp. {row[2]}")
        
            
def sort_kamar(kamar):  #insertion sort
    with open('kamar.csv', 'r',encoding='utf-8' ) as dataFile:
        openCSV = csv.reader(dataFile, delimiter=",")
        next(openCSV)
        for row in openCSV:   
            for row in range(len(kamar)):
                for j in range(1, len(kamar)):
                    a = kamar[row]
                    j = row-1
                    while j>=0 and a< kamar[j]:
                        kamar[j+1] =kamar[j]
                        j -= 1
                    kamar[j+1] = a
            return kamar

def display_kamar(kamar):
    for i in range(len(kamar)):
        print(f"{i+1}. {kamar[i][0]}   -   Rp. {kamar[i][1]}")
        
def main():
    
    kamar = read_kamar()
    root = tk.Tk()
    root.title("Management Hotel Greimory")
#---------------------------------------------------------------------------------------------/
    # Create a LabelFrame
    # frame = ttk.LabelFrame(root)
    # frame.grid(column=0, row=0, padx=10, pady=25)

    # Create a Listbox
    # kamarlabel = Label(root, image=logo, bd=0, compound="top")
    kamar_list = tk.Listbox(root, width=40, height=10)
    kamar_list.grid(column=11, row=11, padx=5, pady=5)
    root.geometry("430x270")
    kamar_list.place(x = 40, y = 40)
    
    # kamarlabel.pack()
    

    # Insert menu items into the Listbox
    
    # Create a Search button
    search_btn = ttk.Button(root, text="Search", command=lambda: search_kamar(item, entry1.get()))
    search_btn.grid(column=3, row=1, padx=10, pady=10)
    search_btn.place(x=340, y=10)
    
    # Create a Add button
    tambah_btn = ttk.Button(root, text="Add room", command=mainadd)
    tambah_btn.grid(column=3, row=1, padx=10, pady=10)
    tambah_btn.place(x=340, y=240)

    # Create an Entry widget
    global entry1
    entry1 = Entry(root)
    entry1.grid(column=3, row=0, padx=10, pady=10)
    entry1.place(x=200, y=10)

    # Create a Sort button
    teks = ttk.Label(root)
    teks = Label(root, text="Sort by: ")
    teks.grid()
    teks.place(x=20, y=215)
    sort_btn = ttk.Button(root, text="Harga", command=lambda: sort_kamar(kamar))
    sort_btn.grid(column=2, row=1, padx=10, pady=10)
    sort_btn.place(x=20, y=240)
    
    sort_btn = ttk.Button(root, text="No. Kamar", command=lambda: sort_kamar(kamar))
    sort_btn.grid(column=2, row=1, padx=10, pady=10)
    sort_btn.place(x=100, y=240)
    
    # logo = ttk.Label(root)
    # resize = logo.resize
    # logo = PhotoImage(file="hotel.png")
    # labelkamar = Label(root, image=logo, width=50, height=50, compound="left")
    # labelkamar.pack()
    root.resizable(False,False)
    root.mainloop()
    
if __name__ == "__main__":
    main()

