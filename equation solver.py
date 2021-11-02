import tkinter as tk
import math
from tkinter.constants import END

#WINDOW SETTINGS
window = tk.Tk()
window.geometry('400x400')
window.title('SOLVER')
#SETTING LEFT MARGIN
lbl_margin=tk.Label(text = '               ')
lbl_margin.grid(row=0 , column=0)
#HEADING LABELS
lbl_heading = tk.Label(text='equation solver', height=2)
lbl_des = tk.Label(text='"ax² + bx + c = 0"', height=4 , width= 20)
lbl_heading.grid(row= 0, columnspan=2 , column=1)
lbl_des.grid(row=1 , columnspan= 2 , column=1)

#INITIALIZING VARIABLES
var_a = tk.StringVar()
var_b = tk.StringVar()
var_c = tk.StringVar()

#ENTRY FORMS
ent_a = tk.Entry(textvariable= var_a, width=10)
ent_a.grid(row= 2, column=2)
lbl_a = tk.Label(text= "a = ")
lbl_a.grid(row = 2, column=1)

ent_b = tk.Entry(textvariable= var_b, width=10)
ent_b.grid(row= 3, column=2)
lbl_b = tk.Label(text= "b = ")
lbl_b.grid(row = 3, column=1)

ent_c = tk.Entry(textvariable= var_c, width=10)
ent_c.grid(row= 4, column=2)
lbl_c = tk.Label(text= "c = ")
lbl_c.grid(row = 4, column=1)

#OUTPUTS
lbl_delta=tk.Label(text= "")
lbl_x=tk.Label(text= "")
lbl_x1=tk.Label(text= "")
lbl_x2=tk.Label(text= "")
lbl_non=tk.Label(text= "")

#BUTTON FUNCTIONS
def clear():
    global lbl_delta
    global lbl_x
    global lbl_x1
    global lbl_x2
    global lbl_non
    ent_a.delete(0, END)
    ent_b.delete(0, END)
    ent_c.delete(0, END)
    lbl_delta.destroy()
    lbl_x.destroy()
    lbl_x1.destroy()
    lbl_x2.destroy()
    lbl_non.destroy()

def count():
    #SETTING VARIABLES
    global lbl_delta
    global lbl_x
    global lbl_x1
    global lbl_x2
    global lbl_non
    
    a = var_a.get()
    b = var_b.get()
    c = var_c.get()
    #SOLVING THE EQUATION
    D = float(b) **2 - 4 * float(a) * float(c)
    lbl_delta=tk.Label(text= "Δ =" + str(D))
    if D > 0 :
        x1 = ( - float(b) - math.sqrt(D)) / (2 * float(a))
        x2 = ( - float(b) + math.sqrt(D)) / (2 * float(a))
        lbl_delta = tk.Label(text="Δ = "+ str(D))
        lbl_delta.grid(row=6, columnspan=2, column=1)
        lbl_x1 = tk.Label(text="x1 = "+ str(x1))
        lbl_x1.grid(row=7, columnspan=2, column=1)
        lbl_x2 = tk.Label(text="x2 = " + str(x2))
        lbl_x2.grid(row=8, columnspan=2, column=1)
                
    elif D == 0 :
        x = (-1 * float(b)) / (2 * float(a))
        lbl_delta = tk.Label(text="Δ = " + str(D))
        lbl_delta.grid(row=6, columnspan=2, column=1)
        lbl_x = tk.Label(text="x = " + str(x))
        lbl_x.grid(row=7, columnspan=2, column=1)

    elif D < 0 :
        lbl_delta = tk.Label(text="Δ = " + str(D))
        lbl_delta.grid(row=6, columnspan=2, column=1)
        lbl_non = tk.Label(text=" NO SOLUTION IN |R ")
        lbl_non.grid(row=7, columnspan=2, column=1)

#BUTTONS
btn1 = tk.Button(text="COUNT", command=count)
btn1.grid(row=5, column=2 )
btn2 = tk.Button(text="CLEAR", command=clear)
btn2.grid(row=5, column=1 )

window.mainloop()