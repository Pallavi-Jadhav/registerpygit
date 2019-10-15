from tkinter import *
import mysql.connector
import re
import tkinter.messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
Fullname = StringVar()
Email = StringVar()
Gender = IntVar()
c = StringVar()
var1 = IntVar()
var2 = IntVar()


def database():
    name1 = entry_1.get()
    email = entry_2.get()
    country = c.get()
    prog1 = var1.get()
    prog2 = var2.get()
    if prog1 == 1:
        prog = 'Java'
    elif prog2 == 1:
        prog = 'Python'

    entry3 = Gender.get()
    if entry3 == 1:
        gender = 'Male'
    else:
        gender = 'Female'

    print(name1)
    print(email)
    print(gender)
    print(country)
    print(prog)

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="mysql1",
        passwd="1234",
        auth_plugin='mysql_native_password',
        port=3308
    )

    cursor = mydb.cursor()
    cursor.execute("use Pallavi9;")
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Employee (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
    cursor.execute('INSERT INTO Employee (FullName,Email,Gender,country,Programming) VALUES(%s,%s,%s,%s,%s)',
                   (name1, email, gender, country, prog))
    cursor.close()
    mydb.commit()

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)




label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)
entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240, y=180)
label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=Gender, value=1).place(x=235, y=230)

Radiobutton(root, text="Female", padx=20, variable=Gender, value=2).place(x=290, y=230)
entry_5 = Entry(root, textvar=Gender)
label_4 = Label(root, text="country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)
list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)

c.set('select your country')
droplist.place(x=240, y=280)
label_4 = Label(root, text="Programming", width=20, font=("bold", 10))

label_4.place(x=85, y=330)
Checkbutton(root, text="java", variable=var1).place(x=235, y=330)
Checkbutton(root, text="python", variable=var2).place(x=290, y=330)
Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)
root.mainloop()