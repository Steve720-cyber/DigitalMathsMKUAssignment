from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
import tkcalendar as tkc
from tkcalendar import DateEntry
import pandas as pd


#--------
try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    data = {
        "Budget":[],
        "Date": [],
        "Lunch":[],
        "Dinner": [],
        "Other": [],
        "Total":[]
    }

    df = pd.DataFrame(data)
#--------

# Create the master window
master = Tk()
master.geometry("920x540+10+10")  # Set window size
master.title("Main Window")


#Create date variable
date = dt.datetime.now()


# Functions to open new windows
#----------------------------------The Meal Budget Window-------------------------------------------------------------
def open_meal_window():



    meal_window = Toplevel(master)  # Create a new window
    meal_window.title("Meal Budget")
    meal_window.geometry("920x540")

    x = master.winfo_x()
    y = master.winfo_y()
    meal_window.geometry("+%d+%d" % (x + 400, y + 50))
    meal_window.wm_transient(master)

    #------------------------------Set the variables-------------------------------------------------------------------

    budget_var = StringVar()
    date_var = StringVar()
    lunch_var = StringVar()
    dinner_var = StringVar()
    other_var = StringVar()
    total_var = StringVar()
    date = date_var.get()



    #-------------------------------Create Widgets (Labels, Entries and Buttons)------------------------------------

    #-------------------------------Labels--------------------------------------------------------------------------


    budget_label = Label(meal_window, text = "Preset Daily Budget: ")
    date_label = Label(meal_window, text="Date (DD/MM/YY):")
    lunch_label = Label(meal_window, text="Input Lunch Expenses: ")
    dinner_label = Label(meal_window, text="Input Dinner Expenses: ")
    other_label = Label(meal_window, text="Input Other Expenses: ")
    total_label = Label(meal_window, text="Total Daily Expenses: ")
    #under_label = Label(meal_window, text="Under or equal to budget", bg='green')
    #over_label = Label(meal_window, text="Over budget, but within 10%", bg='#FFBF00')
    #excess_label = Label(meal_window, text="Exceeds budget parameters", bg='red')
    experiment_label = Label(meal_window, text="")

    #-------------------------------Entries------------------------------------------------------------------------

    budget_entry = Entry(meal_window, textvariable=budget_var, font=('calibre', 10, 'normal'))
    budget_entry.insert(0, "40")

    date_entry = tkc.DateEntry(meal_window, date_pattern='dd/mm/yyyy', font=('calibre', 10, 'normal'))

    lunch_entry = Entry(meal_window, textvariable=lunch_var, font=('calibre', 10, 'normal'))
    #lunch = lunch_entry.get()
    #lunch_entry_float = float(lunch)

    dinner_entry = Entry(meal_window, textvariable=dinner_var, font=('calibre', 10, 'normal'))
    #dinner = dinner_entry.get()
    #dinner_entry_float = float(dinner_entry)

    other_entry = Entry(meal_window, textvariable=other_var, font=('calibre', 10, 'normal'))
    #other = other_entry.get()
    #other_entry_float = float(other_entry)

    total_entry = Entry(meal_window, textvariable=total_var, font=('calibre', 10, 'normal'))
    #entries = lunch + dinner + other
    #total_entry = Entry(meal_window, entries)
    #date_entered = Label(meal_window, text = date)
    #date = Entry(meal_window, options)

    #--------------------------------------Focus the Lunch Entry Field on startup--------------------------------------

    lunch_entry.focus()

    #--------------------------------------Functions-------------------------------------------------------------------
    #def check_budget():



    def confirm_entries():
        lunch = lunch_entry.get()
        # budget = budget_entry.get()
        # budget2 = (float(budget) * 1.1)

        dinner = dinner_entry.get()
        other = other_entry.get()

        entries = float(lunch) + float(dinner) + float(other)
        total_var.set(entries)

        date = date_entry.get()
        lunch = lunch_entry.get()
        budget = budget_entry.get()
        budget2 = (float(budget) * 1.1)

        dinner = dinner_entry.get()
        other = other_entry.get()
        total = total_entry.get()


        if date and lunch and dinner and other:
            new_entry = pd.DataFrame({
                "Budget": [budget],
                "Date": [date],
                "Lunch": [lunch],
                "Dinner": [dinner],
                "Other": [other],
                "Total": [total]
            })



            #date_entry.delete(0, END)
            lunch_entry.delete(0, END)
            dinner_entry.delete(0, END)
            other_entry.delete(0, END)
            total_entry.delete(0, END)
            #entry_type.delete(0, END)


        else:
            messagebox.showerror("Error", "All fields are required.")

        if (lunch.isdigit() and dinner.isdigit() and other.isdigit()):
            entries = float(lunch) + float(dinner) + float(other)
            #total_var.set(entries)
            if entries <= float(budget):
                #fg1='green'
                #under_label.grid(row = 11, column=6, columnspan=2)
                experiment_label['text'] = "Under or equal to budget"
                experiment_label['bg'] = 'Green'
            elif entries <= float(budget2):
                #fg1='#FFBF00'
                #over_label.grid(row=11, column=6, columnspan=2)
                experiment_label['text'] = "Over budget, but within 10%"
                experiment_label['bg'] = 'Yellow'
            else:
                #fg1='red'
                #excess_label.grid(row=11, column=6, columnspan=2)
                experiment_label['text'] = "Exceeds budget parameters"
                experiment_label['bg'] = 'Red'

            total_var.set(entries)

            global df
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv('./records.csv', index=False)
            messagebox.showinfo("Success", "Entry saved successfully!")

            return True



        else:
            messagebox.showwarning("Invalid", "Invalid Data, Expenses Must Be Numeric Please")
#===============================================================================================================

    def view_entries():
        global df
        top = Toplevel(meal_window)
        top.geometry("800x400")
        top.title("View Entries")

        text = Text(top)
        text.pack(fill=BOTH, expand=1)

        for index, row in df.iterrows():
            text.insert(END, "Budget: " + str(row['Budget']) + " | Date: " + str(row['Date']) + " | Lunch:" + str(row['Lunch']) + " | Dinner:" + str(row['Dinner']) + " | Other:" + str(row['Other']) + " | Total: " + str(row['Total']) +"\n" )

            edit_button = Button(top, text="Edit", bg = "green",command=lambda i=index: edit_entry(i))
            delete_button = Button(top, text="Delete", bg = "red",command=lambda i=index: delete_entry(i))
            text.window_create(END, window=edit_button)
            text.window_create(END, window=delete_button)
            text.insert(END, "\n\n")

    def edit_entry(index):
        global df
        edit_top = Toplevel()
        edit_top.title("Edit Entry")

        edit_budget = Entry(edit_top)
        edit_budget.insert(0, df.at[index, 'Budget'])
        edit_budget.pack()

        edit_date = Entry(edit_top)
        edit_date.insert(0, df.at[index, 'Date'])
        edit_date.pack()

        edit_lunch = Entry(edit_top)
        edit_lunch.insert(0, df.at[index, 'Lunch'])
        edit_lunch.pack()

        edit_dinner = Entry(edit_top)
        edit_dinner.insert(0, df.at[index, 'Dinner'])
        edit_dinner.pack()

        edit_other = Entry(edit_top)
        edit_other.insert(0, df.at[index, 'Other'])
        edit_other.pack()

        save_button = Button(edit_top, text="Save", command= lambda i=index: save_edit(i))
        save_button.pack()


        def save_edit(index):
            global df
            newLunch = edit_lunch.get()
            newDinner = edit_dinner.get()
            newOther = edit_other.get()
            df.at[index, 'Budget'] = edit_budget.get()
            df.at[index, 'Date'] = edit_date.get()
            df.at[index, 'Lunch'] = float(edit_lunch.get())
            df.at[index, 'Dinner'] = float(edit_dinner.get())
            df.at[index, 'Other'] = float(edit_other.get())
            df.at[index, 'Total'] = float(newLunch) + float(newDinner) + float(newOther)
            df.to_csv('./records.csv',index=False)
            messagebox.showinfo("Success", "Entry updated successfully!")
            edit_top.destroy()
            #top.destroy()
            view_entries()

    def delete_entry(index):
        global df
        conf = messagebox.askyesno("Confirm Delete", "Are you sure you wish to delete this entry?")
        if conf == 1:
            df.drop(index,inplace=True)
            df.reset_index(drop=True, inplace=True)
            df.to_csv('./records.csv',index=False)
            messagebox.showinfo("Success", "Entry deleted successfully!")
            view_entries()
        else:
            view_entries()
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

    #----------------------------------------Buttons-------------------------------------------------------------------

    confirm_button = (Button(meal_window, text="Confirm Entries", bg = "#5f9ea0",  command=confirm_entries).grid(row=10, column=0, columnspan=2))
    #check_button = (Button(meal_window, text="check budget", bg="#5f9ea0", command=check_budget).grid(row=10, column=4,
    #                                                                                            columnspan=2))

    #button_add = tk.Button(root, text="Add Entry", command=self.add_entry)
    #button_add.grid(row=4, column=0, columnspan=2)

    view_button = Button(meal_window, text="View Entries", bg = "#5f9ea0",command=view_entries)
    view_button.grid(row=10, column=1, columnspan=2)
    #
    # button_search = tk.Button(root, text="Search Entries", command=self.search_entries)
    # button_search.grid(row=6, column=0, columnspan=2)
    #
    # button_summary = tk.Button(root, text="Monthly Summary", command=self.monthly_summary)
    # button_summary.grid(row=7, column=0, columnspan=2)

    #---------------------------------------Configure Main Meal Window Grid-------------------------------------

    meal_window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')
    meal_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')

    #---------------------------------------Position Widgets----------------------------------------------------------

    budget_label.grid(row=0, column=0, columnspan=2, rowspan=1)
    budget_entry.grid(row=1, column=0, columnspan=2, rowspan=1)
    date_label.grid(row=0, column=2, columnspan=2, rowspan=1)
    date_entry.grid(row=1, column=2, columnspan=2, rowspan=1)
    lunch_label.grid(row=3, column=0, columnspan=5, rowspan=1)
    lunch_entry.grid(row=4, column=0, columnspan=5, rowspan=1)
    dinner_label.grid(row=5, column=0, columnspan=5, rowspan=1)
    dinner_entry.grid(row=6, column=0, columnspan=5, rowspan=1)
    other_label.grid(row=7, column=0, columnspan=5, rowspan=1)
    other_entry.grid(row=8, column=0, columnspan=5, rowspan=1)
    total_label.grid(row=4, column=4, columnspan=5, rowspan=3)
    total_entry.grid(row=6, column=4, columnspan=5, rowspan=3)
    experiment_label.grid(row=11, column=6, columnspan=2)
    
    #label_date.grid(row=1, column=3, columnspan=3, rowspan=2, sticky="nsew")
    #confirm_button.grid(row=10, column=1, rowspan=2, sticky="nsew")
    #button2.grid(row=7, column=1, rowspan=2, sticky="nsew")
    #button3.grid(row=10, column=1, rowspan=2, sticky="nsew")

# def open_fuel_window():
#     fuel_window = Toplevel(master)  # Create a new window
#     fuel_window.title("Fuel")
#     fuel_window.geometry("920x540")
#
#     fuel_var = StringVar()
#     distance_var = StringVar()
#
#     fuel_window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')
#     fuel_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')
#
#     fuelclaim_label = Label(fuel_window, text="Preset Claim Policy: ")
#     fuelclaim_entry = Entry(fuel_window, textvariable=fuel_var, font=('calibre', 10, 'normal'))
#     distance_label = Label(fuel_window, text="Input Distance Travelled (In Miles): ")
#     distance_entry = Entry(fuel_window, textvariable=distance_var, font=('calibre', 10, 'normal'))
#
#     fuelclaim_label.grid(row=0, column=0, columnspan=2, rowspan=1)
#     fuelclaim_entry.grid(row=1, column=0, columnspan=2, rowspan=1)
#     distance_label.grid(row=3, column=0, columnspan=5, rowspan=1)
#     distance_entry.grid(row=4, column=0, columnspan=5, rowspan=1)
#
def open_flexi_window():
    flexi_window = Toplevel(master)  # Create a new window
    flexi_window.title("FlexiTime")
    flexi_window.geometry("920x540")

    flexi_var = StringVar()
    mon_var = StringVar()
    tue_var = StringVar()
    wed_var = StringVar()
    thu_var = StringVar()
    fri_var = StringVar()
    hours_var = StringVar()
    bonus_var = StringVar()

    def confirm_entries():
        flex = flexihours_entry.get
        mon = mon_entry.get()
        tue = tue_entry.get()
        wed = wed_entry.get()
        thu = thu_entry.get()
        fri = fri_entry.get()

        total = float(mon) + float(tue) + float(wed) + float(thu) + float(fri)
        bonus = total - float(flex())

        hours_var.set(total)
        bonus_var.set(bonus)

        # date = date_entry.get()
        # lunch = lunch_entry.get()
        # budget = budget_entry.get()
        # budget2 = (float(budget) * 1.1)
        #
        # dinner = dinner_entry.get()
        # other = other_entry.get()
        # total = total_entry.get()

    flexi_window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')
    flexi_window.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1, uniform='a')

    confirm_button = (
        Button(flexi_window, text="Confirm Entries", bg="#5f9ea0", command=confirm_entries).grid(row=10, column=4,
                                                                                                columnspan=2))

    flexihours_label = Label(flexi_window, text="Preset Weekly Hours: ")
    flexihours_entry = Entry(flexi_window, textvariable=flexi_var, font=('calibre', 10, 'normal'))
    mon_label = Label(flexi_window, text="Time clocked in on Monday: ")
    mon_entry = Entry(flexi_window, textvariable=mon_var, font=('calibre', 10, 'normal'))
    tue_label = Label(flexi_window, text="Time clocked in on Tuesday: ")
    tue_entry = Entry(flexi_window, textvariable=tue_var, font=('calibre', 10, 'normal'))
    wed_label = Label(flexi_window, text="Time clocked in on Wednesday: ")
    wed_entry = Entry(flexi_window, textvariable=wed_var, font=('calibre', 10, 'normal'))
    thu_label = Label(flexi_window, text="Time clocked in on Thursday: ")
    thu_entry = Entry(flexi_window, textvariable=thu_var, font=('calibre', 10, 'normal'))
    fri_label = Label(flexi_window, text="Time clocked in on Friday: ")
    fri_entry = Entry(flexi_window, textvariable=fri_var, font=('calibre', 10, 'normal'))
    hours_label = Label(flexi_window, text="Total time clocked in: ")
    hours_entry = Entry(flexi_window, textvariable=hours_var, font=('calibre', 10, 'normal'))
    bonus_label = Label(flexi_window, text="FlexiTime Gained/Lost: ")
    bonus_entry = Entry(flexi_window, textvariable=bonus_var, font=('calibre', 10, 'normal'))

    flexihours_label.grid(row=0, column=0, columnspan=2, rowspan=1)
    flexihours_entry.grid(row=1, column=0, columnspan=2, rowspan=1)
    mon_label.grid(row=3, column=0, columnspan=5, rowspan=1)
    mon_entry.grid(row=4, column=0, columnspan=5, rowspan=1)
    tue_label.grid(row=5, column=0, columnspan=5, rowspan=1)
    tue_entry.grid(row=6, column=0, columnspan=5, rowspan=1)
    wed_label.grid(row=7, column=0, columnspan=5, rowspan=1)
    wed_entry.grid(row=8, column=0, columnspan=5, rowspan=1)
    thu_label.grid(row=9, column=0, columnspan=5, rowspan=1)
    thu_entry.grid(row=10, column=0, columnspan=5, rowspan=1)
    fri_label.grid(row=11, column=0, columnspan=5, rowspan=1)
    fri_entry.grid(row=12, column=0, columnspan=5, rowspan=1)
    hours_label.grid(row=4, column=4, columnspan=5, rowspan=3)
    hours_entry.grid(row=6, column=4, columnspan=5, rowspan=3)
    bonus_label.grid(row=4, column=8, columnspan=5, rowspan=3)
    bonus_entry.grid(row=6, column=8, columnspan=5, rowspan=3)

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
#button2 = (Button(master, text = "Fuel Claim", command=open_fuel_window))
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
#button2.grid(row=7, column=1, rowspan=2, sticky="nsew")
button3.grid(row=10, column=1, rowspan=2, sticky="nsew")

master.mainloop()

#if __name__ == '__main__':
 #   MainWindow()
