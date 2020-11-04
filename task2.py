"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk 
from tkinter import *
import math

window = tk.Tk()
window.title("Factoring Simple Trinomials")

before = StringVar()
before.set("Answer")

def factor():
    b = e1.get()
    b = float(b)

    c = e2.get()
    c = float(c)

    d1 = math.sqrt((b**2)-(4*c))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    t2 = (-1*b)+t1
    x1 = t2/2

    e1 = math.sqrt((b**2)-(4*c))
    y2 = (-1*b)-y1
    x2 = y2/2

    equation = []
    equation.append(x1)
    equation.append(x2)
    answer = equation
    after.delete(0,END)
    after.insert(0,answer)

l1 = Label(window,text="fill in the coefficents for b and c")
l2 = Label(window,text='click the "=" button and your factored equation will appear')
l3 = Label(window,text="*note: a is equal to 1*")
l4 = Label(window,text="")
l5 = Label(window,text="x^2")
l6 = Label(window,text="+")
e1 = Entry(window,width=5)
l7 = Label(window,text="x")
l8 = Label(window,text="+")
e2 = Entry(window,width=5)
b1 = Button(window,text="=",command=factor)
after = Entry(window,width=20,textvariable=before)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l3.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=5,column=2)
e1.grid(row=5,column=3)
l7.grid(row=5,column=4)
e2.grid(row=5,column=6)
l8.grid(row=5,column=5)
b1.grid(row=5,column=7)
after.grid(row=5,column=8)

window.mainloop()
