"""
A program that stores book collection information and allows user to update and download new collection information in csv format.
"""

from tkinter import *
from backend import Database
import csv

database=Database("books_database.db")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def update_command():
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def delete_command():
    database.delete(selected_tuple[0])
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def download_command():
    database.download()



window=Tk()

window.configure(background='SlateGray4')
window.wm_title("A Personal Book Collection")

l1=Label(window,text="Title",bg='SlateGray4')
l1.grid(row=0,column=1)

l2=Label(window,text="Author",bg='SlateGray4')
l2.grid(row=0,column=3)

l3=Label(window,text="Year",bg='SlateGray4')
l3.grid(row=1,column=1)

l4=Label(window,text="ISBN",bg='SlateGray4')
l4.grid(row=1,column=3)


title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=2)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=2)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=4)

list1=Listbox(window,height=6,width=50)
list1.grid(row=2,column=2,rowspan=7,columnspan=5)

sb1=Scrollbar(window)
sb1.grid(row=2,column=1,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command,highlightbackground='SlateGray4')
b1.grid(row=1,column=0)

b2=Button(window,text="Search All",width=12,command=search_command,highlightbackground='SlateGray4')
b2.grid(row=2,column=0)

b3=Button(window,text="Add Entry",width=12,command=add_command,highlightbackground='SlateGray4')
b3.grid(row=3,column=0)

b4=Button(window,text="Update Entry",width=12,command=update_command,highlightbackground='SlateGray4')
b4.grid(row=4,column=0)

b5=Button(window,text="Delete Entry",width=12,command=delete_command,highlightbackground='SlateGray4')
b5.grid(row=5,column=0)

b6=Button(window,text="Close",width=12,command=window.destroy,highlightbackground='SlateGray4')
b6.grid(row=6,column=0)

b8=Button(window,text="Download File",width=12,highlightbackground='SlateGray4',command=download_command)
b8.grid(row=0,column=5)

window.mainloop()
