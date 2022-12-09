from tkinter import *

root=Tk()
root.title("Sales Application")
root.geometry("400x400")
root.configure(background = 'purple')

max_label=Label(root, bg="light pink")
min_label=Label(root, bg="light pink")
label_month=Label(root, bg="light pink")
label_profit=Label(root, bg="light pink")

month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December") 
label_month["text"]= "Months : " + str(month)


profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)
label_profit["text"]= "Profits : " + str(profits)

def max_profit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)

    max_profit_month = month[max_profit_index]
    max_label["text"]="The maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)

btn_max=Button(root, text="Show Max Profitable Month", command=max_profit, bg='gold', fg='black')
btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)

def min_profit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)

    min_profit_month = month[min_profit_index]
    min_label["text"]="The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

btn_min=Button(root, text="Show Min Profitable Month", command=min_profit, bg='gold', fg='black')
btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)
label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5, rely=0.3, anchor=CENTER)
max_label.place(relx=0.5, rely=0.5, anchor=CENTER)
min_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
