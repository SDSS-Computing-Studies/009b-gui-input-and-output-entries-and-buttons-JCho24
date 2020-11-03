"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

# Space exploration Madlib

import tkinter as tk 
from tkinter import *

window = tk.Tk()

out1 = StringVar()
out1.set("(name)")
out2 = StringVar()
out2.set("(silly word)")
out3 = StringVar()
out3.set("(number)")
out4 = StringVar()
out4.set("(adjective)")
out5 = StringVar()
out5.set("(noun)")
out6 = StringVar()
out6.set("(adjective)")
out7 = StringVar()
out7.set("(relative)")
out8 = StringVar()
out8.set("(adjective)")
out9 = StringVar()
out9.set("(verb)")
out10 = StringVar()
out10.set("(adjective)")
out11 = StringVar()
out11.set("(adjective)")


def fill():
    d1 = e1.get()
    
    f1.delete(0,END)
    f1.insert(0,d1)

    d2 = e2.get()
    
    f2.delete(0,END)
    f2.insert(0,d2)

    d3 = e3.get()
    
    f3.delete(0,END)
    f3.insert(0,d3)

    d4 = e4.get()
    
    f4.delete(0,END)
    f4.insert(0,d4)

    d5 = e5.get()
    
    f5.delete(0,END)
    f5.insert(0,d5)

    d6 = e6.get()
    
    f6.delete(0,END)
    f6.insert(0,d6)

    d7 = e7.get()
    
    f7.delete(0,END)
    f7.insert(0,d7)

    d8 = e8.get()
    
    f8.delete(0,END)
    f8.insert(0,d8)

    d9 = e9.get()
    
    f9.delete(0,END)
    f9.insert(0,d9)

    d10 = e10.get()
    
    f10.delete(0,END)
    f10.insert(0,d10)

    d11 = e11.get()
    
    f11.delete(0,END)
    f11.insert(0,d11)


e1 = Entry(window, width = 15)
e2 = Entry(window, width = 15)
e3 = Entry(window, width = 15)
e4 = Entry(window, width = 15)
e5 = Entry(window, width = 15)
e6 = Entry(window, width = 15)
e7 = Entry(window, width = 15)
e8 = Entry(window, width = 15)
e9 = Entry(window, width = 15)
e10 = Entry(window, width = 15)
e11 = Entry(window, width = 15)

f1 = Entry(window, width = 15, textvariable=out1)
f2 = Entry(window, width = 15, textvariable=out2)
f3 = Entry(window, width = 15, textvariable=out3)
f4 = Entry(window, width = 15, textvariable=out4)
f5 = Entry(window, width = 15, textvariable=out5)
f6 = Entry(window, width = 15, textvariable=out6)
f7 = Entry(window, width = 15, textvariable=out7)
f8 = Entry(window, width = 15, textvariable=out8)
f9 = Entry(window, width = 15, textvariable=out9)
f10 = Entry(window, width = 15, textvariable=out10)
f11 = Entry(window, width = 15, textvariable=out11)

t1 = Label(window, text = "(name)")
t2 = Label(window, text = "(silly word)")
t3 = Label(window, text = "(number)")
t4 = Label(window, text = "(adjective)")
t5 = Label(window, text = "(noun)")
t6 = Label(window, text = "(adjective)")
t7 = Label(window, text = "(relative)")
t8 = Label(window, text = "(adjective)")
t9 = Label(window, text = "(verb)")
t10 = Label(window, text = "(adjective)")
t11 = Label(window, text = "(adjective)")

p1 = Label(window, text ="Hello my name is astronaut")
p2 = Label(window, text ="I am on my way to planet")
p3 = Label(window, text ="I will be gone for")
p4 = Label(window, text ="days")
p5 = Label(window, text ="I am very")
p6 = Label(window, text ="about the trip but I will miss my")
p7 = Label(window, text ="I have heard that the atmosphere there is")
p8 = Label(window, text ="Luckily my")
p9 = Label(window, text ="packed me a jacket to keep me")
p10 = Label(window, text ="When I land on the planet I will")
p11 = Label(window, text ="for joy")
p12 = Label(window, text ="I am")
p13 = Label(window, text ="to walk on another planet.")
p14 = Label(window, text ="I could not be more")
p15 = Label(window, text ="for this trip!")


b1 = Button(window, text="Click to see complete story!", command=fill)



t1.grid(row = 1, column = 1)
e1.grid(row = 1, column = 2)
t2.grid(row = 2, column = 1)
e2.grid(row = 2, column = 2)
t3.grid(row = 3, column = 1)
e3.grid(row = 3, column = 2)
t4.grid(row = 4, column = 1)
e4.grid(row = 4, column = 2)
t5.grid(row = 5, column = 1)
e5.grid(row = 5, column = 2)
t6.grid(row = 6, column = 1)
e6.grid(row = 6, column = 2)
t7.grid(row = 7, column = 1)
e7.grid(row = 7, column = 2)
t8.grid(row = 8, column = 1)
e8.grid(row = 8, column = 2)
t9.grid(row = 9, column = 1)
e9.grid(row = 9, column = 2)
t10.grid(row = 10, column = 1)
e10.grid(row = 10, column = 2)
t11.grid(row = 11, column = 1)
e11.grid(row = 11, column = 2)

b1.grid(row = 6, column = 3)


p1.grid(row = 1, column = 4, sticky = E)
f1.grid(row = 1, column = 5, sticky = W)

p2.grid(row = 2, column = 4, sticky = E)
f2.grid(row = 2, column = 5, sticky = W)

p3.grid(row = 3, column = 4, sticky = E)
f3.grid(row = 3, column = 5, sticky = W)
p4.grid(row = 3, column = 6, sticky = W)

p5.grid(row = 4, column = 4, sticky = E)
f4.grid(row = 4, column = 5, sticky = W)
p6.grid(row = 4, column = 6, sticky = W)
f5.grid(row = 4, column = 7, sticky = W)

p7.grid(row = 5, column = 4, sticky = E)
f6.grid(row = 5, column = 5, sticky = W)

p8.grid(row = 6, column = 4, sticky = E)
f7.grid(row = 6, column = 5, sticky = W)
p9.grid(row = 6, column = 6, sticky = W)
f8.grid(row = 6, column = 7, sticky = W)

p10.grid(row = 7, column = 4, sticky = E)
f9.grid(row = 7, column = 5, sticky = W)
p11.grid(row = 7, column = 6, sticky = W)

p12.grid(row = 8, column = 4, sticky = E)
f10.grid(row = 8, column = 5, sticky = W)
p13.grid(row = 8, column = 6, sticky = W)

p14.grid(row = 9, column = 4, sticky = E)
f11.grid(row = 9, column = 5, sticky = W)
p15.grid(row = 9, column = 6, sticky = W)



window.mainloop()