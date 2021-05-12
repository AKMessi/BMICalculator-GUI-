from tkinter import *

root = Tk()

root.geometry("450x300")

root.title("BMI Calculator")

root.resizable(0, 0)

welcome_text = Label(root, text="Welcome to BMI Calculator", font="TimesNewRoman 15 bold").place(x=95, y=20)

weight = IntVar()
enter_weight_text = Label(root, text="Enter Your Weight : ", font="TimesNewRoman, 12").place(x=15, y=80)
weight_entry = Entry(root, width=10, textvariable=weight).place(x=180, y=83)

height = IntVar()
enter_height_text = Label(root, text="Enter Your Height(cm) : ", font="TimesNewRoman 12").place(x=15, y=140)
height_entry = Entry(root, width=10, textvariable=height).place(x=180, y=143)

def bmi_calculator():
    bmi = weight.get()/((height.get()*0.01)*(height.get()*0.01))
    Label(root, text=f"Your BMI is {bmi}"[:17], font="TimesNewRoman 14").place(x=118, y=230)

    if bmi <= 18.5:
        Label(root, text="You are Underweight", font="TimesNewRoman 14").place(x=93, y=260)

    elif bmi <= 24.9:
        Label(root, text="You have a normal weight", font="TimesNewRoman 14").place(x=93, y=260)

    elif bmi >= 25.0:
        Label(root, text="You are overweight", font="TimesNewRoman 14").place(x=93, y=260)

    elif bmi > 24.9:
        Label(root, text="You have a normal weight", font="TimesNewRoman 14").place(x=93, y=260)

def clear():
    height.set(0)
    weight.set(0)

calculate_bmi = Button(root, text="Calculate BMI", font="TimesNewRoman 15", command=bmi_calculator).place(x=100, y=180)

clear_button = Button(root, text="Clear", font="TimesNewRoman 15", command=clear).place(x=250, y=180)

root.mainloop()
