import customtkinter as ctk
from tkinter import *

from scipy import stats
import seaborn as sns

app=ctk.CTk()
app.title("calculator")
app.geometry("250x350")
app.config(bg = "#000000")

font1 = ('Arial', 20, 'bold')

i=0
equation=""

def show(value):
    global i
    global equation
    equation+=value
    result_entry.insert(i,value)
    i = i + 1

def clear():
    global equation
    result_entry.delete(0,END)
    equation=""

def calculate():
    global equation
    result = ""
    result = eval(equation)
    clear()
    result_entry.insert(0,result)


result_entry=ctk.CTkEntry(app, font=font1, width=250, fg_color="#000000", border_color="#000000")
result_entry.place(x=0, y=15)

bclear = ctk.CTkButton(app, command=clear, text="C", font=font1, width=50, height=2)
bclear.place(x=10,y=60)

bperc = ctk.CTkButton(app, command=lambda:show("%"), text="%", font=font1, width=50, height=2,  hover_color="#b5520b")
bperc.place(x=70, y=60)

bdiv = ctk.CTkButton(app, command=lambda:show("/"), text="/", font=font1, width=50, height=2, hover_color="#b5520b")
bdiv.place(x=130, y=60)

btimes = ctk.CTkButton(app, command=lambda:show("*"), text="x", font=font1, width=50, height=2, hover_color="#b5520b")
btimes.place(x=190, y=60)

b7 = ctk.CTkButton(app, command=lambda:show("7"), text="7", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b7.place(x=10, y=120)

b8 = ctk.CTkButton(app, command=lambda:show("8"), text="8", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b8.place(x=70, y=120)

b9 = ctk.CTkButton(app, command=lambda:show("9"), text="9", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b9.place(x=130, y=120)

bplus = ctk.CTkButton(app, command=lambda:show("+"), text="+", font=font1, width=50, height=2,  hover_color="#b5520b")
bplus.place(x=190, y=120)

b4 = ctk.CTkButton(app, command=lambda:show("4"), text="4", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b4.place(x=10, y=180)

b5 = ctk.CTkButton(app, command=lambda:show("5"), text="5", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b5.place(x=70, y=180)

b6 = ctk.CTkButton(app, command=lambda:show("6"), text="6", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b6.place(x=130, y=180)

bminus = ctk.CTkButton(app, command=lambda:show("-"), text="-", font=font1, width=50, height=2, hover_color="#b5520b")
bminus.place(x=190, y=180)

b1 = ctk.CTkButton(app, command=lambda:show("1"), text="1", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b1.place(x=10, y=240)

b2 = ctk.CTkButton(app, command=lambda:show("2"), text="2", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b2.place(x=70, y=240)

b3 = ctk.CTkButton(app, command=lambda:show("3"), text="3", font=font1, width=50, height=2, fg_color="#b5520b", hover_color="#b5520b")
b3.place(x=130, y=240)

beq = ctk.CTkButton(app, command=calculate, text="=", font=font1, width=50, height=90, hover_color="#b5520b")
beq.place(x=190, y=240)

b0 = ctk.CTkButton(app, command=lambda:show("0"), text="0", font=font1, width=110, height=2, fg_color="#b5520b", hover_color="#b5520b")
b0.place(x=10, y=300)

bdot = ctk.CTkButton(app, command=lambda:show("."), text=".", font=font1, width=50, height=2, hover_color="#b5520b")
bdot.place(x=130, y=300)






app.mainloop()