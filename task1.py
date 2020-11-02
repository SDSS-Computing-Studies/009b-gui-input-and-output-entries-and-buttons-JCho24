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


before1 = StringVar()
before1.set("Hello my name is astronaut (name). \n I am on my way to planet (silly word). \n I will be gone for (number) days. \n I am very (adjective) about the trip but I will miss my (noun). \n I have heard that the atmosphere there is (adjective). \n Luckily my (relative) packed me a jacket to keep me (adjective). \n When I land on the planet I will (verb) for joy. \n I am (adjective) to walk on another planet. \n I could not be more (adjective) for this trip!")

def fill():
    f1 = e1.get()
    
    date.delete(0,END)
    date.insert(0,f1)

e1 = Entry(window, width = 20)
e2 = Entry(window, width = 20)
e3 = Entry(window, width = 20)
e4 = Entry(window, width = 20)
e5 = Entry(window, width = 20)
e6 = Entry(window, width = 20)

t1 = Label(window, text = "Date: ________")
t2 = Label(window, text = "(name) is sick")
t3 = Label(window, text = "with the (part of the body) flu.")
t4 = Label(window, text = "Drink more (type of fluid) and")
t5 = Label(window, text = "take (a substance) as needed.")
t6 = Label(window, text = "Signed: ________")



b1 = Button(window, text="Click to input answers", command=fill)
p1 = Label(window, width=50, textvariable=before1)

l1.grid(row = , column = )
e1.grid(row = , column = )
l2.grid(row = , column = )
b1.grid(row = , column = )

p1.grid(row = 1, column = 1)


window.mainloop()