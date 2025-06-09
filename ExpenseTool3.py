from tkinter import *
#import tkinter as tk
from tkinter.ttk import *
#from tkinter import ttk
import datetime as dt


# Create the master window
master = Tk()
master.geometry("920x540")  # Set window size
master.title("Main Window")
#window
#window=tk.Tk()
#window.title('Grid')
#window.geometry('920x540')

#Create date variable
date = dt.datetime.now()


# Functions to open new windows
def open_meal_window():
    meal_window = Toplevel(master)  # Create a new window
    meal_window.title("Meal Budget")
    meal_window.geometry("920x540")

    date_var = StringVar()
    date_entered = date_var.get()
    budget_var = StringVar()
    budget_entered = budget_var.get()

    #Label(meal_window, text="Meal Budget").pack(pady=20)
    budget_label = Label(meal_window, text = "Preset Daily Budget: ")
    budget_entry = Entry(meal_window, textvariable=budget_var, font=('calibre', 10, 'normal'))
    disp_budget.insert(0,f'budget_entered') 
    disp_budget = Entry(meal_window)
    ##def frame_sentence():
    ##name = name_tf.get()
    ##age = int(age_tf.get())
    ##desc = descipline_tf.get()

    ##disp_tf.insert(0,f'{age} years old {name} became {desc}.')
    #budget = Label(meal_window, text = budget_entered)
    
    expense_date = Label(meal_window, text = "Enter Date of Expense")
    date_entry = Entry(meal_window, textvariable=date_var, font=('calibre', 10, 'normal'))
    date_to_use = Label(meal_window, text = date_entered)
    #date = Entry(meal_window, options)
    meal_window.columnconfigure((0, 1, 2), weight=1, uniform='a')
    meal_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')

    #button1 = (Button(meal_window, text="Meal Budget", command=open_meal_window))

    budget_label.grid(row=0, column=0)
    budget_entry.grid(row = 0, column = 2 )
    disp_budget.grid (row = 1, column = 3)
    expense_date.grid(row=1, column=0)
    date_entry.grid(row=3, column=0)
    date_entered.grid(row=4, column=0)
    
    #label_date.grid(row=1, column=3, columnspan=3, rowspan=2, sticky="nsew")
    #button1.grid(row=4, column=1, rowspan=2, sticky="nsew")
    #button2.grid(row=7, column=1, rowspan=2, sticky="nsew")
    #button3.grid(row=10, column=1, rowspan=2, sticky="nsew")

def open_fuel_window():
    new_window = Toplevel(master)  # Create a new window
    new_window.title("Fuel")
    new_window.geometry("250x150")

    Label(new_window, text="Fuel Claim").pack(pady=20)

def open_flexi_window():
    new_window = Toplevel(master)  # Create a new window
    new_window.title("FlexiTime")
    new_window.geometry("250x150")

    Label(new_window, text="Flexi Monitor").pack(pady=20)

#Widgets
label_today = Label(master, text="Today's Date Is:  ", font="Calibri, 16", foreground = "red")
label_date = Label(master, text=f"{date:%A, %B %d, %Y}", font="Calibri, 16")
label1 = Label(master, text="Meal Budget", background = 'blue')
label2 = Label(master, text="Fuel Claim", background = 'green')
label3 = Label(master, text="Flexi time", background = 'red')

# Create a label and a button to open the new window
#Label(master, text="This is the main window").pack(pady=10)
#Button(master, text="Open New Window", command=open_new_window).pack(pady=10)

button1 = (Button(master, text = "Meal Budget", command=open_meal_window))
           #.pack(pady=10))
button2 = (Button(master, text = "Fuel Claim", command=open_fuel_window))
#.pack(pady=10)
button3 = (Button(master, text = "Flexi Time", command=open_flexi_window))
#.pack(pady=10)

#Define a Grid
master.columnconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')
#window.columnconfigure(1, weight = 1)
#window.columnconfigure(2, weight = 1)
#window.columnconfigure(3, weight = 1)
#window.columnconfigure(4, weight = 1)
#window.columnconfigure(5, weight = 1)
#window.columnconfigure(6, weight = 1)

master.rowconfigure((0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16), weight = 1, uniform = 'a')
# window.rowconfigure(1, weight = 1)
# window.rowconfigure(2, weight = 1)
# window.rowconfigure(3, weight = 1)
# window.rowconfigure(4, weight = 1)
# window.rowconfigure(5, weight = 1)
# window.rowconfigure(6, weight = 1)
# window.rowconfigure(7, weight = 1)
# window.rowconfigure(8, weight = 1)
# window.rowconfigure(9, weight = 1)
#window.rowconfigure(10, weight = 1)

# place a widget
label_today.grid(row=1, column=1, columnspan=2, rowspan=2)
label_date.grid(row=1, column=3, columnspan=3, rowspan=2, sticky="nsew")
button1.grid(row=4, column=1, rowspan=2, sticky="nsew")
button2.grid(row=7, column=1, rowspan=2, sticky="nsew")
button3.grid(row=10, column=1, rowspan=2, sticky="nsew")

master.mainloop()

#if __name__ == '__main__':
 #   MainWindow()
