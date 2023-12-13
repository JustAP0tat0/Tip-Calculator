#calculating tip
import tkinter

bill = 0

Tip1 = 0
Tip2 = 0
Tip3 = 0

Tip_1 = 0
Tip_2 = 0
Tip_3 = 0

root = tkinter.Tk() 

root.title("Calculating Tip")

root.geometry("400x400")

instructions = tkinter.Label(root, text = "Enter the total amount for your bill:", font = ("Helvetica", 12))
instructions.pack()

def set_bill(i):
    global bill
    bill = text.get()

def cal_tip(i):
    global bill
    bill = text.get()
    suggested_tip = tkinter.Label(root, text = "Suggested tip amount for " + str(bill) + " dollars:", font = ("Helvetica", 12))
    suggested_tip.pack()

    bill = text.get()

    global Tip1
    global Tip2
    global Tip3

    Tip1 = 18 * int(bill) / 100
    Tip2 = 20 * int(bill) / 100
    Tip3 = 22 * int(bill) / 100

    global total1
    global total2
    global total3

    total1 = int(Tip1) + int(bill)
    total2 = int(Tip2) + int(bill)
    total3 = int(Tip3) + int(bill)

    Tip_1 = tkinter.Label(root, text = "18%: " + str(Tip1) + "$", font = ("Helvetica", 12))
    Tip_1.pack()
    Tip_11 = tkinter.Label(root, text = "If you give a 18% tip you will have to pay " + str(total1) + "$", font = ("Helvetica", 12))
    Tip_11.pack()

    Tip_2 = tkinter.Label(root, text = "20%: " + str(Tip2) + "$", font = ("Helvetica", 12))
    Tip_2.pack()
    Tip_22 = tkinter.Label(root, text = "If you give a 18% tip you will have to pay " + str(total2) + "$", font = ("Helvetica", 12))
    Tip_22.pack()

    Tip_3 = tkinter.Label(root, text = "22%: " + str(Tip3) + "$", font = ("Helvetica", 12))
    Tip_3.pack()
    Tip_33 = tkinter.Label(root, text = "If you give a 18% tip you will have to pay " + str(total3) + "$", font = ("Helvetica", 12))
    Tip_33.pack()


root.bind("<Return>", set_bill,)

root.bind("<Return>", cal_tip)

text = tkinter.Entry(root)
text.pack()

text.focus_set()

root.mainloop()
