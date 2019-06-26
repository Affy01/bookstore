from tkinter import *
from model import sql_db

sql_data = sql_db("book")

def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def get_selected_row(event=None):
    global book
    if list1.curselection():
        index = list1.curselection()[0]
        book = list1.get(index)
        clear_entries()
        e1.insert(END, book[1])
        e2.insert(END, book[2])
        e3.insert(END, book[3])
        e4.insert(END, book[4])


def view_command():
    list1.delete(0, END)
    rows = sql_data.get_all()
    for row in rows:
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    rows = sql_data.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    for row in rows:
        list1.insert(END, row)


def add_command():
    list1.delete(0, END)
    sql_data.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    list1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))


def delete_command():
    sql_data.delete(book[0])
    view_command()


def update_command():
    sql_data.update(book[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    print(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()


window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_value = StringVar()
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0, column=1)

author_value = StringVar()
e2 = Entry(window, textvariable=author_value)
e2.grid(row=0, column=3)

year_value = StringVar()
e3 = Entry(window, textvariable=year_value)
e3.grid(row=1, column=1)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
