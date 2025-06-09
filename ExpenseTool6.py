from tkinter import *
#import tkinter as tk
from tkinter.ttk import *
#from tkinter import ttk
import datetime as dt
import pandas as pd
import ttkbootstrap as tb


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

#def populate_budget():
 #   budget_entry = Entry(meal_window, textvariable=budget_var, font=('calibre', 10, 'normal'))
  #  budget = budget_entry.get()
   # disp_budget.insert(0,f'{budget}')


def open_meal_window():
    def populate_budget():
        
        budget = budget_entry.get()
        disp_budget.insert(0,f'{budget}')

    def show_date_1():

        date_entered_1 = date_entry_1.entry.get()
        disp_date_1.insert(0,f'{date_entered_1}')

    def show_date_2():

        date_entered_2 = date_entry_2.entry.get()
        disp_date_2.insert(0,f'{date_entered_2}')

    def show_date_3():

        date_entered_3 = date_entry_3.entry.get()
        disp_date_3.insert(0,f'{date_entered_3}')

    def show_date_4():

        date_entered_4 = date_entry_4.entry.get()
        disp_date_4.insert(0,f'{date_entered_4}')

    def show_date_5():

        date_entered_5 = date_entry_5.entry.get()
        disp_date_5.insert(0,f'{date_entered_5}')

    def show_date_6():

        date_entered_6 = date_entry_6.entry.get()
        disp_date_6.insert(0,f'{date_entered_6}')

    def show_date_7():

        date_entered_7 = date_entry_7.entry.get()
        disp_date_7.insert(0,f'{date_entered_7}')

    meal_window = Toplevel(master)  # Create a new window
    meal_window.title("Meal Budget")
    meal_window.geometry("920x540")

    # date_var = StringVar()
    # date_entered = date_var.get()
    budget_var = StringVar()
    # budget_entered = budget_var.get()

    # date_entered = tb.DateEntry(meal_window, bootstyle="danger")
    # date_entered.grid(row=4, column=0)



    budget_label = Label(meal_window, text = "Preset Daily Budget: ")
    budget_entry = Entry(meal_window, textvariable=budget_var, font=('calibre', 10, 'normal'))
    budget_btn = Button(meal_window, text='Enter', command=populate_budget)
    disp_budget = Entry(meal_window)
    
        
    expense_date = Label(meal_window, text = "Enter Date of Expense")
    expense_date_entered = Label(meal_window, text = "Expense Date")
    expense_type = Label(meal_window, text="Enter Type of Expense")
    expense_amount = Label(meal_window, text="Enter Amount of Expense")
    #date_entry = Entry(meal_window, textvariable=date_var, font=('calibre', 10, 'normal'))
    date_entry_1 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_1 = Button(meal_window, text='Confirm', command=show_date_1)
    date_entry_2 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_2 = Button(meal_window, text='Confirm', command=show_date_2)
    date_entry_3 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_3 = Button(meal_window, text='Confirm', command=show_date_3)
    date_entry_4 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_4 = Button(meal_window, text='Confirm', command=show_date_4)
    date_entry_5 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_5 = Button(meal_window, text='Confirm', command=show_date_5)
    date_entry_6 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_6 = Button(meal_window, text='Confirm', command=show_date_6)
    date_entry_7 = tb.DateEntry(meal_window, bootstyle="danger")
    date_btn_7 = Button(meal_window, text='Confirm', command=show_date_7)

    #date_to_use = Label(meal_window, text = date_entered)
    #date = Entry(meal_window, options)
    meal_window.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
    meal_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')

    #button1 = (Button(meal_window, text="Meal Budget", command=open_meal_window))

    budget_label.grid(row=0, column=0)
    budget_entry.grid(row = 0, column = 1 )

    budget_btn.grid(row=0, column = 2)
    disp_budget.grid (row = 0, column = 3)


    expense_date.grid(row=1, column=0)

    expense_date_entered.grid(row=1, column=2)

    expense_type.grid(row=1, column=3)
    expense_amount.grid(row=1, column=4)

    date_entry_1.grid(row=2, column=0)
    date_btn_1.grid(row=2, column=1)
    disp_date_1 = Entry(meal_window)
    disp_date_1.grid(row=2, column=2)
    date_entry_2.grid(row=3, column=0)
    date_btn_2.grid(row=3, column=1)
    disp_date_2 = Entry(meal_window)
    disp_date_2.grid(row=3, column=2)
    date_entry_3.grid(row=4, column=0)
    date_btn_3.grid(row=4, column=1)
    disp_date_3 = Entry(meal_window)
    disp_date_3.grid(row=4, column=2)
    date_entry_4.grid(row=5, column=0)
    date_btn_4.grid(row=5, column=1)
    disp_date_4 = Entry(meal_window)
    disp_date_4.grid(row=5, column=2)
    date_entry_5.grid(row=6, column=0)
    date_btn_5.grid(row=6, column=1)
    disp_date_5 = Entry(meal_window)
    disp_date_5.grid(row=6, column=2)
    date_entry_6.grid(row=7, column=0)
    date_btn_6.grid(row=7, column=1)
    disp_date_6 = Entry(meal_window)
    disp_date_6.grid(row=7, column=2)
    date_entry_7.grid(row=8, column=0)
    date_btn_7.grid(row=8, column=1)
    disp_date_7 = Entry(meal_window)
    disp_date_7.grid(row=8, column=2)
    #date_entered.grid(row=9, column=0)
    
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
