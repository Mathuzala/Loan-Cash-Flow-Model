import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import numpy_financial as npf
from PIL import ImageTk, Image
from sqlalchemy import true

win = Tk()

# Creating Frames
wrapper0 = LabelFrame(win, width = 900, height = 950)
wrapper1 = LabelFrame(win, width = 900, height = 950)
wrapper2 = LabelFrame(win, width = 900, height = 950)
wrapper3 = LabelFrame(win, width = 900, height = 950)
wrapper4 = LabelFrame(win, width = 900, height = 950)
wrapper5 = LabelFrame(win, width = 900, height = 950)

mycanvas = Canvas(wrapper0)
mycanvas.pack(side = LEFT, fill = "both", expand ="yes")

# Adding Image
my_image = ImageTk.PhotoImage(Image.open("mvww_v4.png"))
mycanvas.create_image(0,0,image=my_image, anchor="center")

image_label = Label(image = my_image)
image_label.pack(pady = 5)

wrapper0.pack(fill = "both", expand = "yes", padx = 10, pady = 10)


def start():

    hide_frames()
    
    global myframe
    mycanvas = Canvas(wrapper1)
    mycanvas.pack(side = LEFT, fill = "both", expand ="yes")
    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window = myframe, anchor = "nw")

    wrapper1.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

    myframe.pack(fill = "both", expand = 1)
    #start_label = Label(myframe, text = "Choose Length of Loan Model", font = ("Helvetica", 19)).pack(pady = 100)

    # Creating buttons
    home_button1 = Button(myframe, text = "View Menu", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 24, BOLD), command = home).pack(pady = 10)

def home():

    hide_frames()

    mycanvas = Canvas(wrapper2)
    mycanvas.pack(side = LEFT, fill = "both", expand ="yes")
    
    global myframe
    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window = myframe, anchor = "nw")

    wrapper2.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

    myframe.pack(fill = "both", expand = 1)
    start_label = Label(myframe, text = "Choose Length of Loan Model", font = ("Helvetica", 19)).pack(pady = 100)

    # Creating buttons
    home_button1 = Button(myframe, text = "12 Month Model", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 16, BOLD), command = second_home).pack(pady = 10)
    home_button2 = Button(myframe, text = "24 Month Model", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 16, BOLD), command = third_home).pack(pady = 10)
    home_button3 = Button(myframe, text = "60 Month Model", bg='#ffffff', activeforeground='#4444ff', font = ("Helvetica", 16, BOLD), command = fourth_home).pack(pady = 10)

def second_home():

    hide_frames1()

    mycanvas = Canvas(wrapper3)
    
    mycanvas.pack(side = LEFT, fill = "both", expand ="yes")

    yscrollbar = ttk.Scrollbar(wrapper3, orient = VERTICAL, command = mycanvas.yview)
    
    yscrollbar.pack(side = RIGHT, fill = "y")
    
    mycanvas.configure(yscrollcommand = yscrollbar.set)
    
    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    wrapper3.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window = myframe, anchor = "nw")

    second_label = Label(myframe, text = "Please Input Loan Parameters", font = ("Helvetica", 18), pady = 10, padx = 300).pack()

    # Creating a Back Button
    back_button = Button(myframe, text = "Previous Page", command = home)
    back_button.pack(pady = 10)

# Creating Input Box for Original Balance Month 1
    global og_bal_input
    og_bal_input = Entry(myframe)
    og_bal_input.pack(padx = 300)

    # Creating Label for Original Balance Month 1
    global og_bal_label
    og_bal_label = Label(myframe, text = "Enter Original Balance for Month 1")
    og_bal_label.pack(padx = 300)

    # Creating Input Box for Original Balance Month 2
    global og_bal_input2
    og_bal_input2 = Entry(myframe)
    og_bal_input2.pack(padx = 300)

    # Creating Label for Original Balance Month 2
    global og_bal_label2
    og_bal_label2 = Label(myframe, text = "Enter Original Balance for Month 2")
    og_bal_label2.pack(padx = 300)

    # Creating Input Box for Original Balance Month 3
    global og_bal_input3
    og_bal_input3 = Entry(myframe)
    og_bal_input3.pack(padx = 300)

    # Creating Label for Original Balance Month 3
    global og_bal_label3
    og_bal_label3 = Label(myframe, text = "Enter Original Balance for Month 3")
    og_bal_label3.pack(padx = 300)

    # Creating Input Box for Original Balance Month 4
    global og_bal_input4
    og_bal_input4 = Entry(myframe)
    og_bal_input4.pack(padx = 300)

    # Creating Label for Original Balance Month 4
    global og_bal_label4
    og_bal_label4 = Label(myframe, text = "Enter Original Balance for Month 4")
    og_bal_label4.pack(padx = 300)

    # Creating Input Box for Original Balance Month 5
    global og_bal_input5
    og_bal_input5 = Entry(myframe)
    og_bal_input5.pack(padx = 300)

    # Creating Label for Original Balance Month 5
    global og_bal_label5
    og_bal_label5 = Label(myframe, text = "Enter Original Balance for Month 5")
    og_bal_label5.pack(padx = 300)

    # Creating Input Box for Original Balance Month 6
    global og_bal_input6
    og_bal_input6 = Entry(myframe)
    og_bal_input6.pack(padx = 300)

    # Creating Label for Original Balance Month 6
    global og_bal_label6
    og_bal_label6 = Label(myframe, text = "Enter Original Balance for Month 6")
    og_bal_label6.pack(padx = 300)

    # Creating Input Box for Original Balance Month 7
    global og_bal_input7
    og_bal_input7 = Entry(myframe)
    og_bal_input7.pack(padx = 300)

    # Creating Label for Original Balance Month 7
    global og_bal_label7
    og_bal_label7 = Label(myframe, text = "Enter Original Balance for Month 7")
    og_bal_label7.pack(padx = 300)

    # Creating Input Box for Original Balance Month 8
    global og_bal_input8
    og_bal_input8 = Entry(myframe)
    og_bal_input8.pack(padx = 300)

    # Creating Label for Original Balance Month 8
    global og_bal_label8
    og_bal_label8 = Label(myframe, text = "Enter Original Balance for Month 8")
    og_bal_label8.pack(padx = 300)

    # Creating Input Box for Original Balance Month 9
    global og_bal_input9
    og_bal_input9 = Entry(myframe)
    og_bal_input9.pack(padx = 300)

    # Creating Label for Original Balance Month 9
    global og_bal_label9
    og_bal_label9 = Label(myframe, text = "Enter Original Balance for Month 9")
    og_bal_label9.pack(padx = 300)

    # Creating Input Box for Original Balance Month 10
    global og_bal_input10
    og_bal_input10 = Entry(myframe)
    og_bal_input10.pack(padx = 300)

    # Creating Label for Original Balance Month 10
    global og_bal_label10
    og_bal_label10 = Label(myframe, text = "Enter Original Balance for Month 10")
    og_bal_label10.pack(padx = 300)

    # Creating Input Box for Original Balance Month 11
    global og_bal_input11
    og_bal_input11 = Entry(myframe)
    og_bal_input11.pack(padx = 300)

    # Creating Label for Original Balance Month 11
    global og_bal_label11
    og_bal_label11 = Label(myframe, text = "Enter Original Balance for Month 11")
    og_bal_label11.pack(padx = 300)

    # Creating Input Box for Original Balance Month 12
    global og_bal_input12
    og_bal_input12 = Entry(myframe)
    og_bal_input12.pack(padx = 300)

    # Creating Label for Original Balance Month 12
    global og_bal_label12
    og_bal_label12 = Label(myframe, text = "Enter Original Balance for Month 12")
    og_bal_label12.pack(padx = 300)

    # Creating Second Input Box for Coupon Rate
    global coupon_input
    coupon_input = Entry(myframe)
    coupon_input.pack(padx = 300)

    # Creating Second Label for Coupon Rate
    global coupon_label
    coupon_label = Label(myframe, text = "Enter Coupon Rate for Loans")
    coupon_label.pack(padx = 300)

    # Creating Third Input Box for Loan Term
    global term_input
    term_input = Entry(myframe)
    term_input.pack(padx = 300)

    # Creating Third Label for Loan Term
    global term_label
    coupon_label = Label(myframe, text = "Enter Term Length for Loans")
    coupon_label.pack(padx = 300)

    # Creating Second Input Box for SMM Rate
    global smm_rate_input
    smm_rate_input = Entry(myframe)
    smm_rate_input.pack(padx = 300)

    # Creating Second Label for SMM Rate
    global smm_rate_label
    smm_rate_label = Label(myframe, text = "Enter SMM Rate for Prepaid Principal")
    smm_rate_label.pack(padx = 300)

    # Creating Second Input Box for Default Rate
    global def_rate_input
    def_rate_input = Entry(myframe)
    def_rate_input.pack(padx = 300)

    # Creating Second Label for Default Rate
    global def_rate_label
    def_rate_label = Label(myframe, text = "Enter Default Rate for Charge-Off Principal")
    def_rate_label.pack(padx = 300)

    # Creating a Calculate Button
    back_button = Button(myframe, text = "Calculate", command = Twelve_Month_Model)
    back_button.pack(pady = 10)
    
def third_home():

    hide_frames()

    mycanvas = Canvas(wrapper4)
    
    mycanvas.pack(side = LEFT, fill = "both", expand ="yes")

    yscrollbar = ttk.Scrollbar(wrapper4, orient = VERTICAL, command = mycanvas.yview)
    
    yscrollbar.pack(side = RIGHT, fill = "y")
    
    mycanvas.configure(yscrollcommand = yscrollbar.set)
    
    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    wrapper4.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window = myframe, anchor = "nw")

    second_label = Label(myframe, text = "Please Input Loan Parameters", font = ("Helvetica", 18), pady = 10, padx = 325).pack()

    # Creating a Back Button
    back_button = Button(myframe, text = "Previous Page", command = home)
    back_button.pack(pady = 10)

# Creating Input Box for Original Balance Month 1
    og_bal_input = Entry(myframe)
    og_bal_input.pack(padx = 325)

    # Creating Label for Original Balance Month 1
    og_bal_label = Label(myframe, text = "Enter Original Balance for Month 1")
    og_bal_label.pack(padx = 325)

    # Creating Input Box for Original Balance Month 2
    og_bal_input2 = Entry(myframe)
    og_bal_input2.pack(padx = 325)

    # Creating Label for Original Balance Month 2
    og_bal_label2 = Label(myframe, text = "Enter Original Balance for Month 2")
    og_bal_label2.pack(padx = 325)

    # Creating Input Box for Original Balance Month 3
    og_bal_input3 = Entry(myframe)
    og_bal_input3.pack(padx = 325)

    # Creating Label for Original Balance Month 3
    og_bal_label3 = Label(myframe, text = "Enter Original Balance for Month 3")
    og_bal_label3.pack(padx = 325)

    # Creating Input Box for Original Balance Month 4
    og_bal_input4 = Entry(myframe)
    og_bal_input4.pack(padx = 325)

    # Creating Label for Original Balance Month 4
    og_bal_label4 = Label(myframe, text = "Enter Original Balance for Month 4")
    og_bal_label4.pack(padx = 325)

    # Creating Input Box for Original Balance Month 5
    og_bal_input5 = Entry(myframe)
    og_bal_input5.pack(padx = 325)

    # Creating Label for Original Balance Month 5
    og_bal_label5 = Label(myframe, text = "Enter Original Balance for Month 5")
    og_bal_label5.pack(padx = 325)

    # Creating Input Box for Original Balance Month 6
    og_bal_input6 = Entry(myframe)
    og_bal_input6.pack(padx = 325)

    # Creating Label for Original Balance Month 6
    og_bal_label6 = Label(myframe, text = "Enter Original Balance for Month 6")
    og_bal_label6.pack(padx = 325)

    # Creating Input Box for Original Balance Month 7
    global og_bal_input7
    og_bal_input7 = Entry(myframe)
    og_bal_input7.pack(padx = 325)

    # Creating Label for Original Balance Month 7
    og_bal_label7 = Label(myframe, text = "Enter Original Balance for Month 7")
    og_bal_label7.pack(padx = 325)

    # Creating Input Box for Original Balance Month 8
    og_bal_input8 = Entry(myframe)
    og_bal_input8.pack(padx = 325)

    # Creating Label for Original Balance Month 8
    og_bal_label8 = Label(myframe, text = "Enter Original Balance for Month 8")
    og_bal_label8.pack(padx = 325)

    # Creating Input Box for Original Balance Month 9
    og_bal_input9 = Entry(myframe)
    og_bal_input9.pack(padx = 325)

    # Creating Label for Original Balance Month 9
    og_bal_label9 = Label(myframe, text = "Enter Original Balance for Month 9")
    og_bal_label9.pack(padx = 325)

    # Creating Input Box for Original Balance Month 10
    og_bal_input10 = Entry(myframe)
    og_bal_input10.pack(padx = 325)

    # Creating Label for Original Balance Month 10
    og_bal_label10 = Label(myframe, text = "Enter Original Balance for Month 10")
    og_bal_label10.pack(padx = 325)

    # Creating Input Box for Original Balance Month 11
    og_bal_input11 = Entry(myframe)
    og_bal_input11.pack(padx = 325)

    # Creating Label for Original Balance Month 11
    og_bal_label11 = Label(myframe, text = "Enter Original Balance for Month 11")
    og_bal_label11.pack(padx = 325)

    # Creating Input Box for Original Balance Month 12
    og_bal_input12 = Entry(myframe)
    og_bal_input12.pack(padx = 325)

    # Creating Label for Original Balance Month 12
    og_bal_label12 = Label(myframe, text = "Enter Original Balance for Month 12")
    og_bal_label12.pack(padx = 325)

     # Creating Input Box for Original Balance Month 13
    og_bal_input13 = Entry(myframe)
    og_bal_input13.pack(padx = 325)

    # Creating Label for Original Balance Month 13
    og_bal_label13 = Label(myframe, text = "Enter Original Balance for Month 13")
    og_bal_label13.pack(padx = 325)

    # Creating Input Box for Original Balance Month 14
    og_bal_input14 = Entry(myframe)
    og_bal_input14.pack(padx = 325)

    # Creating Label for Original Balance Month 14
    og_bal_label14 = Label(myframe, text = "Enter Original Balance for Month 14")
    og_bal_label14.pack(padx = 325)

    # Creating Input Box for Original Balance Month 15
    og_bal_input15 = Entry(myframe)
    og_bal_input15.pack(padx = 325)

    # Creating Label for Original Balance Month 15
    og_bal_label15 = Label(myframe, text = "Enter Original Balance for Month 15")
    og_bal_label15.pack(padx = 325)

    # Creating Input Box for Original Balance Month 16
    og_bal_input16 = Entry(myframe)
    og_bal_input16.pack(padx = 325)

    # Creating Label for Original Balance Month 16
    og_bal_label16 = Label(myframe, text = "Enter Original Balance for Month 16")
    og_bal_label16.pack(padx = 325)

    # Creating Input Box for Original Balance Month 17
    og_bal_input17 = Entry(myframe)
    og_bal_input17.pack(padx = 325)

    # Creating Label for Original Balance Month 17
    og_bal_label17 = Label(myframe, text = "Enter Original Balance for Month 17")
    og_bal_label17.pack(padx = 325)

    # Creating Input Box for Original Balance Month 18
    og_bal_input18 = Entry(myframe)
    og_bal_input18.pack(padx = 325)

    # Creating Label for Original Balance Month 18
    og_bal_label18 = Label(myframe, text = "Enter Original Balance for Month 18")
    og_bal_label18.pack(padx = 325)

    # Creating Input Box for Original Balance Month 19
    og_bal_input19 = Entry(myframe)
    og_bal_input19.pack(padx = 325)

    # Creating Label for Original Balance Month 19
    og_bal_label19 = Label(myframe, text = "Enter Original Balance for Month 19")
    og_bal_label19.pack(padx = 325)

    # Creating Input Box for Original Balance Month 20
    og_bal_input20 = Entry(myframe)
    og_bal_input20.pack(padx = 325)

    # Creating Label for Original Balance Month 20
    og_bal_label20 = Label(myframe, text = "Enter Original Balance for Month 20")
    og_bal_label20.pack(padx = 325)

    # Creating Input Box for Original Balance Month 21
    og_bal_input21 = Entry(myframe)
    og_bal_input21.pack(padx = 325)

    # Creating Label for Original Balance Month 21
    og_bal_label21 = Label(myframe, text = "Enter Original Balance for Month 21")
    og_bal_label21.pack(padx = 325)

    # Creating Input Box for Original Balance Month 22
    og_bal_input22 = Entry(myframe)
    og_bal_input22.pack(padx = 325)

    # Creating Label for Original Balance Month 22
    og_bal_label22 = Label(myframe, text = "Enter Original Balance for Month 22")
    og_bal_label22.pack(padx = 325)

    # Creating Input Box for Original Balance Month 23
    og_bal_input23 = Entry(myframe)
    og_bal_input23.pack(padx = 325)

    # Creating Label for Original Balance Month 23
    og_bal_label23 = Label(myframe, text = "Enter Original Balance for Month 23")
    og_bal_label23.pack(padx = 325)

    # Creating Input Box for Original Balance Month 24
    og_bal_input24 = Entry(myframe)
    og_bal_input24.pack(padx = 325)

    # Creating Label for Original Balance Month 24
    og_bal_label24 = Label(myframe, text = "Enter Original Balance for Month 24")
    og_bal_label24.pack(padx = 325)

def fourth_home():

    hide_frames()

    mycanvas = Canvas(wrapper5)
    
    mycanvas.pack(side = LEFT, fill = "both", expand ="yes")

    yscrollbar = ttk.Scrollbar(wrapper5, orient = VERTICAL, command = mycanvas.yview)
    
    yscrollbar.pack(side = RIGHT, fill = "y")
    
    mycanvas.configure(yscrollcommand = yscrollbar.set)
    
    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    wrapper5.pack(fill = "both", expand = "yes", padx = 10, pady = 10)

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0), window = myframe, anchor = "nw")

    second_label = Label(myframe, text = "Please Input Loan Parameters", font = ("Helvetica", 18), pady = 10, padx = 325).pack()

    # Creating a Back Button
    back_button = Button(myframe, text = "Previous Page", command = home)
    back_button.pack(pady = 10)

# Creating Input Box for Original Balance Month 1
    global og_bal_input
    og_bal_input = Entry(myframe)
    og_bal_input.pack(padx = 325)

    # Creating Label for Original Balance Month 1
    global og_bal_label
    og_bal_label = Label(myframe, text = "Enter Original Balance for Month 1")
    og_bal_label.pack(padx = 325)

    # Creating Input Box for Original Balance Month 2
    global og_bal_input2
    og_bal_input2 = Entry(myframe)
    og_bal_input2.pack(padx = 325)

    # Creating Label for Original Balance Month 2
    global og_bal_label2
    og_bal_label2 = Label(myframe, text = "Enter Original Balance for Month 2")
    og_bal_label2.pack(padx = 325)

    # Creating Input Box for Original Balance Month 3
    global og_bal_input3
    og_bal_input3 = Entry(myframe)
    og_bal_input3.pack(padx = 325)

    # Creating Label for Original Balance Month 3
    global og_bal_label3
    og_bal_label3 = Label(myframe, text = "Enter Original Balance for Month 3")
    og_bal_label3.pack(padx = 325)

    # Creating Input Box for Original Balance Month 4
    global og_bal_input4
    og_bal_input4 = Entry(myframe)
    og_bal_input4.pack(padx = 325)

    # Creating Label for Original Balance Month 4
    global og_bal_label4
    og_bal_label4 = Label(myframe, text = "Enter Original Balance for Month 4")
    og_bal_label4.pack(padx = 325)

    # Creating Input Box for Original Balance Month 5
    global og_bal_input5
    og_bal_input5 = Entry(myframe)
    og_bal_input5.pack(padx = 325)

    # Creating Label for Original Balance Month 5
    global og_bal_label5
    og_bal_label5 = Label(myframe, text = "Enter Original Balance for Month 5")
    og_bal_label5.pack(padx = 325)

    # Creating Input Box for Original Balance Month 6
    global og_bal_input6
    og_bal_input6 = Entry(myframe)
    og_bal_input6.pack(padx = 325)

    # Creating Label for Original Balance Month 6
    global og_bal_label6
    og_bal_label6 = Label(myframe, text = "Enter Original Balance for Month 6")
    og_bal_label6.pack(padx = 325)

    # Creating Input Box for Original Balance Month 7
    global og_bal_input7
    og_bal_input7 = Entry(myframe)
    og_bal_input7.pack(padx = 325)

    # Creating Label for Original Balance Month 7
    global og_bal_label7
    og_bal_label7 = Label(myframe, text = "Enter Original Balance for Month 7")
    og_bal_label7.pack(padx = 325)

    # Creating Input Box for Original Balance Month 8
    global og_bal_input8
    og_bal_input8 = Entry(myframe)
    og_bal_input8.pack(padx = 325)

    # Creating Label for Original Balance Month 8
    global og_bal_label8
    og_bal_label8 = Label(myframe, text = "Enter Original Balance for Month 8")
    og_bal_label8.pack(padx = 325)

    # Creating Input Box for Original Balance Month 9
    global og_bal_input9
    og_bal_input9 = Entry(myframe)
    og_bal_input9.pack(padx = 325)

    # Creating Label for Original Balance Month 9
    global og_bal_label9
    og_bal_label9 = Label(myframe, text = "Enter Original Balance for Month 9")
    og_bal_label9.pack(padx = 325)

    # Creating Input Box for Original Balance Month 10
    global og_bal_input10
    og_bal_input10 = Entry(myframe)
    og_bal_input10.pack(padx = 325)

    # Creating Label for Original Balance Month 10
    global og_bal_label10
    og_bal_label10 = Label(myframe, text = "Enter Original Balance for Month 10")
    og_bal_label10.pack(padx = 325)

    # Creating Input Box for Original Balance Month 11
    global og_bal_input11
    og_bal_input11 = Entry(myframe)
    og_bal_input11.pack(padx = 325)

    # Creating Label for Original Balance Month 11
    global og_bal_label11
    og_bal_label11 = Label(myframe, text = "Enter Original Balance for Month 11")
    og_bal_label11.pack(padx = 325)

    # Creating Input Box for Original Balance Month 12
    global og_bal_input12
    og_bal_input12 = Entry(myframe)
    og_bal_input12.pack(padx = 325)

    # Creating Label for Original Balance Month 12
    global og_bal_label12
    og_bal_label12 = Label(myframe, text = "Enter Original Balance for Month 12")
    og_bal_label12.pack(padx = 325)

     # Creating Input Box for Original Balance Month 13
    global og_bal_input13
    og_bal_input13 = Entry(myframe)
    og_bal_input13.pack(padx = 325)

    # Creating Label for Original Balance Month 13
    global og_bal_label13
    og_bal_label13 = Label(myframe, text = "Enter Original Balance for Month 13")
    og_bal_label13.pack(padx = 325)

    # Creating Input Box for Original Balance Month 14
    global og_bal_input14
    og_bal_input14 = Entry(myframe)
    og_bal_input14.pack(padx = 325)

    # Creating Label for Original Balance Month 14
    global og_bal_label14
    og_bal_label14 = Label(myframe, text = "Enter Original Balance for Month 14")
    og_bal_label14.pack(padx = 325)

    # Creating Input Box for Original Balance Month 15
    global og_bal_input15
    og_bal_input15 = Entry(myframe)
    og_bal_input15.pack(padx = 325)

    # Creating Label for Original Balance Month 15
    global og_bal_label15
    og_bal_label15 = Label(myframe, text = "Enter Original Balance for Month 15")
    og_bal_label15.pack(padx = 325)

    # Creating Input Box for Original Balance Month 16
    global og_bal_input16
    og_bal_input16 = Entry(myframe)
    og_bal_input16.pack(padx = 325)

    # Creating Label for Original Balance Month 16
    global og_bal_label16
    og_bal_label16 = Label(myframe, text = "Enter Original Balance for Month 16")
    og_bal_label16.pack(padx = 325)

    # Creating Input Box for Original Balance Month 17
    global og_bal_input17
    og_bal_input17 = Entry(myframe)
    og_bal_input17.pack(padx = 325)

    # Creating Label for Original Balance Month 17
    global og_bal_label17
    og_bal_label17 = Label(myframe, text = "Enter Original Balance for Month 17")
    og_bal_label17.pack(padx = 325)

    # Creating Input Box for Original Balance Month 18
    global og_bal_input18
    og_bal_input18 = Entry(myframe)
    og_bal_input18.pack(padx = 325)

    # Creating Label for Original Balance Month 18
    global og_bal_label18
    og_bal_label18 = Label(myframe, text = "Enter Original Balance for Month 18")
    og_bal_label18.pack(padx = 325)

    # Creating Input Box for Original Balance Month 19
    global og_bal_input19
    og_bal_input19 = Entry(myframe)
    og_bal_input19.pack(padx = 325)

    # Creating Label for Original Balance Month 19
    global og_bal_label19
    og_bal_label19 = Label(myframe, text = "Enter Original Balance for Month 19")
    og_bal_label19.pack(padx = 325)

    # Creating Input Box for Original Balance Month 20
    global og_bal_input20
    og_bal_input20 = Entry(myframe)
    og_bal_input20.pack(padx = 325)

    # Creating Label for Original Balance Month 20
    global og_bal_label20
    og_bal_label20 = Label(myframe, text = "Enter Original Balance for Month 20")
    og_bal_label20.pack(padx = 325)

    # Creating Input Box for Original Balance Month 21
    global og_bal_input21
    og_bal_input21 = Entry(myframe)
    og_bal_input21.pack(padx = 325)

    # Creating Label for Original Balance Month 21
    global og_bal_label21
    og_bal_label21 = Label(myframe, text = "Enter Original Balance for Month 21")
    og_bal_label21.pack(padx = 325)

    # Creating Input Box for Original Balance Month 22
    global og_bal_input22
    og_bal_input22 = Entry(myframe)
    og_bal_input22.pack(padx = 325)

    # Creating Label for Original Balance Month 22
    global og_bal_label22
    og_bal_label22 = Label(myframe, text = "Enter Original Balance for Month 22")
    og_bal_label22.pack(padx = 325)

    # Creating Input Box for Original Balance Month 23
    global og_bal_input23
    og_bal_input23 = Entry(myframe)
    og_bal_input23.pack(padx = 325)

    # Creating Label for Original Balance Month 23
    global og_bal_label23
    og_bal_label23 = Label(myframe, text = "Enter Original Balance for Month 23")
    og_bal_label23.pack(padx = 325)

    # Creating Input Box for Original Balance Month 24
    global og_bal_input24
    og_bal_input24 = Entry(myframe)
    og_bal_input24.pack(padx = 325)

    # Creating Label for Original Balance Month 24
    global og_bal_label24
    og_bal_label24 = Label(myframe, text = "Enter Original Balance for Month 24")
    og_bal_label24.pack(padx = 325)

    # Creating Input Box for Original Balance Month 25
    global og_bal_input25
    og_bal_input25 = Entry(myframe)
    og_bal_input25.pack(padx = 325)

    # Creating Label for Original Balance Month 25
    global og_bal_label25
    og_bal_label25 = Label(myframe, text = "Enter Original Balance for Month 25")
    og_bal_label25.pack(padx = 325)

    # Creating Input Box for Original Balance Month 26
    global og_bal_input26
    og_bal_input26 = Entry(myframe)
    og_bal_input26.pack(padx = 325)

    # Creating Label for Original Balance Month 26
    global og_bal_label26
    og_bal_label26 = Label(myframe, text = "Enter Original Balance for Month 26")
    og_bal_label26.pack(padx = 325)

    # Creating Input Box for Original Balance Month 27
    global og_bal_input27
    og_bal_input27 = Entry(myframe)
    og_bal_input27.pack(padx = 325)

    # Creating Label for Original Balance Month 27
    global og_bal_label27
    og_bal_label27 = Label(myframe, text = "Enter Original Balance for Month 27")
    og_bal_label27.pack(padx = 325)

    # Creating Input Box for Original Balance Month 28
    global og_bal_input28
    og_bal_input28 = Entry(myframe)
    og_bal_input28.pack(padx = 325)

    # Creating Label for Original Balance Month 28
    global og_bal_label28
    og_bal_label28 = Label(myframe, text = "Enter Original Balance for Month 28")
    og_bal_label28.pack(padx = 325)

    # Creating Input Box for Original Balance Month 29
    global og_bal_input29
    og_bal_input29 = Entry(myframe)
    og_bal_input29.pack(padx = 325)

    # Creating Label for Original Balance Month 29
    global og_bal_label29
    og_bal_label29 = Label(myframe, text = "Enter Original Balance for Month 29")
    og_bal_label29.pack(padx = 325)

    # Creating Input Box for Original Balance Month 30
    global og_bal_input30
    og_bal_input30 = Entry(myframe)
    og_bal_input30.pack(padx = 325)

    # Creating Label for Original Balance Month 30
    global og_bal_label30
    og_bal_label30 = Label(myframe, text = "Enter Original Balance for Month 30")
    og_bal_label30.pack(padx = 325)

    # Creating Input Box for Original Balance Month 31
    global og_bal_input31
    og_bal_input31 = Entry(myframe)
    og_bal_input31.pack(padx = 325)

    # Creating Label for Original Balance Month 31
    global og_bal_label31
    og_bal_label31 = Label(myframe, text = "Enter Original Balance for Month 31")
    og_bal_label31.pack(padx = 325)

    # Creating Input Box for Original Balance Month 32
    global og_bal_input32
    og_bal_input32 = Entry(myframe)
    og_bal_input32.pack(padx = 325)

    # Creating Label for Original Balance Month 32
    global og_bal_label32
    og_bal_label32 = Label(myframe, text = "Enter Original Balance for Month 32")
    og_bal_label32.pack(padx = 325)

    # Creating Input Box for Original Balance Month 33
    global og_bal_input33
    og_bal_input33 = Entry(myframe)
    og_bal_input33.pack(padx = 325)

    # Creating Label for Original Balance Month 33
    global og_bal_label33
    og_bal_label33 = Label(myframe, text = "Enter Original Balance for Month 33")
    og_bal_label33.pack(padx = 325)

    # Creating Input Box for Original Balance Month 34
    global og_bal_input34
    og_bal_input34 = Entry(myframe)
    og_bal_input34.pack(padx = 325)

    # Creating Label for Original Balance Month 34
    global og_bal_label34
    og_bal_label34 = Label(myframe, text = "Enter Original Balance for Month 34")
    og_bal_label34.pack(padx = 325)

    # Creating Input Box for Original Balance Month 35
    global og_bal_input35
    og_bal_input35 = Entry(myframe)
    og_bal_input35.pack(padx = 325)

    # Creating Label for Original Balance Month 35
    global og_bal_label35
    og_bal_label35 = Label(myframe, text = "Enter Original Balance for Month 35")
    og_bal_label35.pack(padx = 325)

    # Creating Input Box for Original Balance Month 36
    global og_bal_input36
    og_bal_input36 = Entry(myframe)
    og_bal_input36.pack(padx = 325)

    # Creating Label for Original Balance Month 36
    global og_bal_label36
    og_bal_label36 = Label(myframe, text = "Enter Original Balance for Month 36")
    og_bal_label36.pack(padx = 325)

def Twelve_Month_Model():

    #1--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance1 = int(og_bal_input.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment1 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance1)
    principal_payment1 = npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance1)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table1
    cf_data1 = {'Interest': interest_payment1, 'Principal': principal_payment1}

    cf_table1 = pd.DataFrame(data = cf_data1, index=periods)

    cf_table1['Payment'] = cf_table1['Interest'] + cf_table1['Principal']
    
    cf_table1['Ending Balance'] = original_balance1 - \
                                cf_table1['Principal'].cumsum()

    cf_table1['Beginning Balance'] = [original_balance1] + \
                                    list(cf_table1['Ending Balance'])[:-1]

    cf_table1['SMM'] = float(smm_rate_input.get())

    cf_table1['Default'] = float(def_rate_input.get())

    cf_table1['Total_SMM_Loss'] = cf_table1['SMM'] + cf_table1['Default']

    cf_table1.loc[0, 'Net Outstanding Balance'] = int(og_bal_input.get())
    cf_table1.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table1)):
        
        cf_table1.loc[i, 'Survival Factor'] = cf_table1.loc[i-1, 'Survival Factor'] - (cf_table1.loc[i-1, 'Survival Factor'] * cf_table1.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table1.loc[i, 'Prepaid Principal'] = cf_table1.loc[i-1, 'Net Outstanding Balance'] * cf_table1.loc[i, 'SMM']/100
        cf_table1.loc[i, 'Charge-Off Principal'] = cf_table1.loc[i-1, 'Net Outstanding Balance'] * cf_table1.loc[i, 'Default']/100
        cf_table1.loc[i, 'Scheduled Principle Received'] = cf_table1.loc[i, 'Principal'] * cf_table1.loc[i, 'Survival Factor']/100

        cf_table1.loc[i, 'Net Outstanding Balance'] = cf_table1.loc[i-1, 'Net Outstanding Balance'] - cf_table1.loc[i, 'Prepaid Principal'] - cf_table1.loc[i, 'Charge-Off Principal'] - cf_table1.loc[i, 'Scheduled Principle Received']

        cf_table1.loc[i, 'Total Principal Collections'] = cf_table1.loc[i, 'Scheduled Principle Received'] + cf_table1.loc[i, 'Prepaid Principal'] 

    cf_table1.head(cf_table1.shape[0] -1)


    cf_table1 = cf_table1[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

    
    #2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance2 = int(og_bal_input2.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment2 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance2)
    principal_payment2 = npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance2)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table1
    cf_data2 = {'Interest': interest_payment2, 'Principal': principal_payment2}

    cf_table2 = pd.DataFrame(data = cf_data2, index=periods)

    cf_table2['Payment'] = cf_table2['Interest'] + cf_table2['Principal']
    
    cf_table2['Ending Balance'] = original_balance2 - \
                                cf_table2['Principal'].cumsum()

    cf_table2['Beginning Balance'] = [original_balance2] + \
                                    list(cf_table2['Ending Balance'])[:-1]

    cf_table2['SMM'] = float(smm_rate_input.get())

    cf_table2['Default'] = float(def_rate_input.get())

    cf_table2['Total_SMM_Loss'] = cf_table2['SMM'] + cf_table2['Default']

    cf_table2.loc[0, 'Net Outstanding Balance'] = int(og_bal_input2.get())
    cf_table2.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table2)):
        
        cf_table2.loc[i, 'Survival Factor'] = cf_table2.loc[i-1, 'Survival Factor'] - (cf_table2.loc[i-1, 'Survival Factor'] * cf_table2.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table2.loc[i, 'Prepaid Principal'] = cf_table2.loc[i-1, 'Net Outstanding Balance'] * cf_table2.loc[i, 'SMM']/100
        cf_table2.loc[i, 'Charge-Off Principal'] = cf_table2.loc[i-1, 'Net Outstanding Balance'] * cf_table2.loc[i, 'Default']/100
        cf_table2.loc[i, 'Scheduled Principle Received'] = cf_table2.loc[i, 'Principal'] * cf_table2.loc[i, 'Survival Factor']/100

        cf_table2.loc[i, 'Net Outstanding Balance'] = cf_table2.loc[i-1, 'Net Outstanding Balance'] - cf_table2.loc[i, 'Prepaid Principal'] - cf_table2.loc[i, 'Charge-Off Principal'] - cf_table2.loc[i, 'Scheduled Principle Received']

        cf_table2.loc[i, 'Total Principal Collections'] = cf_table2.loc[i, 'Scheduled Principle Received'] + cf_table2.loc[i, 'Prepaid Principal'] 

    cf_table2.head(cf_table2.shape[0] -1)

    cf_table2 = cf_table2[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

    
#3--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance3 = int(og_bal_input3.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment3 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance3)
    principal_payment3 = npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance3)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table3
    cf_data3 = {'Interest': interest_payment3, 'Principal': principal_payment3}

    cf_table3 = pd.DataFrame(data = cf_data3, index=periods)

    cf_table3['Payment'] = cf_table3['Interest'] + cf_table3['Principal']
    
    cf_table3['Ending Balance'] = original_balance3 - \
                                cf_table3['Principal'].cumsum()

    cf_table3['Beginning Balance'] = [original_balance3] + \
                                    list(cf_table3['Ending Balance'])[:-1]

    cf_table3['SMM'] = float(smm_rate_input.get())

    cf_table3['Default'] = float(def_rate_input.get())

    cf_table3['Total_SMM_Loss'] = cf_table3['SMM'] + cf_table3['Default']

    cf_table3.loc[0, 'Net Outstanding Balance'] = int(og_bal_input3.get())
    cf_table3.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table3)):
        
        cf_table3.loc[i, 'Survival Factor'] = cf_table3.loc[i-1, 'Survival Factor'] - (cf_table3.loc[i-1, 'Survival Factor'] * cf_table3.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table3.loc[i, 'Prepaid Principal'] = cf_table3.loc[i-1, 'Net Outstanding Balance'] * cf_table3.loc[i, 'SMM']/100
        cf_table3.loc[i, 'Charge-Off Principal'] = cf_table3.loc[i-1, 'Net Outstanding Balance'] * cf_table3.loc[i, 'Default']/100
        cf_table3.loc[i, 'Scheduled Principle Received'] = cf_table3.loc[i, 'Principal'] * cf_table3.loc[i, 'Survival Factor']/100

        cf_table3.loc[i, 'Net Outstanding Balance'] = cf_table3.loc[i-1, 'Net Outstanding Balance'] - cf_table3.loc[i, 'Prepaid Principal'] - cf_table3.loc[i, 'Charge-Off Principal'] - cf_table3.loc[i, 'Scheduled Principle Received']

        cf_table3.loc[i, 'Total Principal Collections'] = cf_table3.loc[i, 'Scheduled Principle Received'] + cf_table3.loc[i, 'Prepaid Principal'] 

    cf_table3.head(cf_table3.shape[0] -1)

    cf_table3 = cf_table3[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]


#4--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance4 = int(og_bal_input4.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment4 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance4)
    principal_payment4= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance4)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 4
    cf_data4 = {'Interest': interest_payment4, 'Principal': principal_payment4}

    cf_table4 = pd.DataFrame(data = cf_data4, index=periods)

    cf_table4['Payment'] = cf_table4['Interest'] + cf_table4['Principal']
    
    cf_table4['Ending Balance'] = original_balance4 - \
                                cf_table4['Principal'].cumsum()

    cf_table4['Beginning Balance'] = [original_balance4] + \
                                    list(cf_table4['Ending Balance'])[:-1]

    cf_table4['SMM'] = float(smm_rate_input.get())

    cf_table4['Default'] = float(def_rate_input.get())

    cf_table4['Total_SMM_Loss'] = cf_table4['SMM'] + cf_table4['Default']

    cf_table4.loc[0, 'Net Outstanding Balance'] = int(og_bal_input4.get())
    cf_table4.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table4)):
        
        cf_table4.loc[i, 'Survival Factor'] = cf_table4.loc[i-1, 'Survival Factor'] - (cf_table4.loc[i-1, 'Survival Factor'] * cf_table4.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table4.loc[i, 'Prepaid Principal'] = cf_table4.loc[i-1, 'Net Outstanding Balance'] * cf_table4.loc[i, 'SMM']/100
        cf_table4.loc[i, 'Charge-Off Principal'] = cf_table4.loc[i-1, 'Net Outstanding Balance'] * cf_table4.loc[i, 'Default']/100
        cf_table4.loc[i, 'Scheduled Principle Received'] = cf_table4.loc[i, 'Principal'] * cf_table4.loc[i, 'Survival Factor']/100

        cf_table4.loc[i, 'Net Outstanding Balance'] = cf_table4.loc[i-1, 'Net Outstanding Balance'] - cf_table4.loc[i, 'Prepaid Principal'] - cf_table4.loc[i, 'Charge-Off Principal'] - cf_table4.loc[i, 'Scheduled Principle Received']

        cf_table4.loc[i, 'Total Principal Collections'] = cf_table4.loc[i, 'Scheduled Principle Received'] + cf_table4.loc[i, 'Prepaid Principal'] 

    cf_table4.head(cf_table4. shape[0] -1)

    cf_table4 = cf_table4[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#5--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance5 = int(og_bal_input5.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment5 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance5)
    principal_payment5= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance5)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 5
    cf_data5 = {'Interest': interest_payment5, 'Principal': principal_payment5}

    cf_table5 = pd.DataFrame(data = cf_data5, index=periods)

    cf_table5['Payment'] = cf_table5['Interest'] + cf_table5['Principal']
    
    cf_table5['Ending Balance'] = original_balance5 - \
                                cf_table5['Principal'].cumsum()

    cf_table5['Beginning Balance'] = [original_balance5] + \
                                    list(cf_table5['Ending Balance'])[:-1]

    cf_table5['SMM'] = float(smm_rate_input.get())

    cf_table5['Default'] = float(def_rate_input.get())

    cf_table5['Total_SMM_Loss'] = cf_table5['SMM'] + cf_table5['Default']

    cf_table5.loc[0, 'Net Outstanding Balance'] = int(og_bal_input5.get())
    cf_table5.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table5)):
        
        cf_table5.loc[i, 'Survival Factor'] = cf_table5.loc[i-1, 'Survival Factor'] - (cf_table5.loc[i-1, 'Survival Factor'] * cf_table5.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table5.loc[i, 'Prepaid Principal'] = cf_table5.loc[i-1, 'Net Outstanding Balance'] * cf_table5.loc[i, 'SMM']/100
        cf_table5.loc[i, 'Charge-Off Principal'] = cf_table5.loc[i-1, 'Net Outstanding Balance'] * cf_table5.loc[i, 'Default']/100
        cf_table5.loc[i, 'Scheduled Principle Received'] = cf_table5.loc[i, 'Principal'] * cf_table5.loc[i, 'Survival Factor']/100

        cf_table5.loc[i, 'Net Outstanding Balance'] = cf_table5.loc[i-1, 'Net Outstanding Balance'] - cf_table5.loc[i, 'Prepaid Principal'] - cf_table5.loc[i, 'Charge-Off Principal'] - cf_table5.loc[i, 'Scheduled Principle Received']

        cf_table5.loc[i, 'Total Principal Collections'] = cf_table5.loc[i, 'Scheduled Principle Received'] + cf_table5.loc[i, 'Prepaid Principal'] 

    cf_table5.head(cf_table5. shape[0] -1)

    cf_table5 = cf_table5[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#6--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance6 = int(og_bal_input6.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment6 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance6)
    principal_payment6= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance6)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 6
    cf_data6 = {'Interest': interest_payment6, 'Principal': principal_payment6}

    cf_table6 = pd.DataFrame(data = cf_data6, index=periods)

    cf_table6['Payment'] = cf_table6['Interest'] + cf_table6['Principal']
    
    cf_table6['Ending Balance'] = original_balance6 - \
                                cf_table6['Principal'].cumsum()

    cf_table6['Beginning Balance'] = [original_balance6] + \
                                    list(cf_table6['Ending Balance'])[:-1]

    cf_table6['SMM'] = float(smm_rate_input.get())

    cf_table6['Default'] = float(def_rate_input.get())

    cf_table6['Total_SMM_Loss'] = cf_table6['SMM'] + cf_table6['Default']

    cf_table6.loc[0, 'Net Outstanding Balance'] = int(og_bal_input6.get())
    cf_table6.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table6)):
        
        cf_table6.loc[i, 'Survival Factor'] = cf_table6.loc[i-1, 'Survival Factor'] - (cf_table6.loc[i-1, 'Survival Factor'] * cf_table6.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table6.loc[i, 'Prepaid Principal'] = cf_table6.loc[i-1, 'Net Outstanding Balance'] * cf_table6.loc[i, 'SMM']/100
        cf_table6.loc[i, 'Charge-Off Principal'] = cf_table6.loc[i-1, 'Net Outstanding Balance'] * cf_table6.loc[i, 'Default']/100
        cf_table6.loc[i, 'Scheduled Principle Received'] = cf_table6.loc[i, 'Principal'] * cf_table6.loc[i, 'Survival Factor']/100

        cf_table6.loc[i, 'Net Outstanding Balance'] = cf_table6.loc[i-1, 'Net Outstanding Balance'] - cf_table6.loc[i, 'Prepaid Principal'] - cf_table6.loc[i, 'Charge-Off Principal'] - cf_table6.loc[i, 'Scheduled Principle Received']

        cf_table6.loc[i, 'Total Principal Collections'] = cf_table6.loc[i, 'Scheduled Principle Received'] + cf_table6.loc[i, 'Prepaid Principal'] 

    cf_table6.head(cf_table6. shape[0] -1)

    cf_table6 = cf_table6[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#7--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance7 = int(og_bal_input7.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment7 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance7)
    principal_payment7= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance7)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 7
    cf_data7 = {'Interest': interest_payment7, 'Principal': principal_payment7}

    cf_table7 = pd.DataFrame(data = cf_data7, index=periods)

    cf_table7['Payment'] = cf_table7['Interest'] + cf_table7['Principal']
    
    cf_table7['Ending Balance'] = original_balance7 - \
                                cf_table7['Principal'].cumsum()

    cf_table7['Beginning Balance'] = [original_balance7] + \
                                    list(cf_table7['Ending Balance'])[:-1]

    cf_table7['SMM'] = float(smm_rate_input.get())

    cf_table7['Default'] = float(def_rate_input.get())

    cf_table7['Total_SMM_Loss'] = cf_table7['SMM'] + cf_table7['Default']

    cf_table7.loc[0, 'Net Outstanding Balance'] = int(og_bal_input7.get())
    cf_table7.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table7)):
        
        cf_table7.loc[i, 'Survival Factor'] = cf_table7.loc[i-1, 'Survival Factor'] - (cf_table7.loc[i-1, 'Survival Factor'] * cf_table7.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table7.loc[i, 'Prepaid Principal'] = cf_table7.loc[i-1, 'Net Outstanding Balance'] * cf_table7.loc[i, 'SMM']/100
        cf_table7.loc[i, 'Charge-Off Principal'] = cf_table7.loc[i-1, 'Net Outstanding Balance'] * cf_table7.loc[i, 'Default']/100
        cf_table7.loc[i, 'Scheduled Principle Received'] = cf_table7.loc[i, 'Principal'] * cf_table7.loc[i, 'Survival Factor']/100

        cf_table7.loc[i, 'Net Outstanding Balance'] = cf_table7.loc[i-1, 'Net Outstanding Balance'] - cf_table7.loc[i, 'Prepaid Principal'] - cf_table7.loc[i, 'Charge-Off Principal'] - cf_table7.loc[i, 'Scheduled Principle Received']

        cf_table7.loc[i, 'Total Principal Collections'] = cf_table7.loc[i, 'Scheduled Principle Received'] + cf_table7.loc[i, 'Prepaid Principal'] 

    cf_table7.head(cf_table7. shape[0] -1)

    cf_table7 = cf_table7[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]


#8--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance8 = int(og_bal_input8.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment8 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance8)
    principal_payment8= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance8)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 8
    cf_data8 = {'Interest': interest_payment8, 'Principal': principal_payment8}

    cf_table8 = pd.DataFrame(data = cf_data8, index=periods)

    cf_table8['Payment'] = cf_table8['Interest'] + cf_table8['Principal']
    
    cf_table8['Ending Balance'] = original_balance8 - \
                                cf_table8['Principal'].cumsum()

    cf_table8['Beginning Balance'] = [original_balance8] + \
                                    list(cf_table8['Ending Balance'])[:-1]

    cf_table8['SMM'] = float(smm_rate_input.get())

    cf_table8['Default'] = float(def_rate_input.get())

    cf_table8['Total_SMM_Loss'] = cf_table8['SMM'] + cf_table8['Default']

    cf_table8.loc[0, 'Net Outstanding Balance'] = int(og_bal_input8.get())
    cf_table8.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table8)):
        
        cf_table8.loc[i, 'Survival Factor'] = cf_table8.loc[i-1, 'Survival Factor'] - (cf_table8.loc[i-1, 'Survival Factor'] * cf_table8.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table8.loc[i, 'Prepaid Principal'] = cf_table8.loc[i-1, 'Net Outstanding Balance'] * cf_table8.loc[i, 'SMM']/100
        cf_table8.loc[i, 'Charge-Off Principal'] = cf_table8.loc[i-1, 'Net Outstanding Balance'] * cf_table8.loc[i, 'Default']/100
        cf_table8.loc[i, 'Scheduled Principle Received'] = cf_table8.loc[i, 'Principal'] * cf_table8.loc[i, 'Survival Factor']/100

        cf_table8.loc[i, 'Net Outstanding Balance'] = cf_table8.loc[i-1, 'Net Outstanding Balance'] - cf_table8.loc[i, 'Prepaid Principal'] - cf_table8.loc[i, 'Charge-Off Principal'] - cf_table8.loc[i, 'Scheduled Principle Received']

        cf_table8.loc[i, 'Total Principal Collections'] = cf_table8.loc[i, 'Scheduled Principle Received'] + cf_table8.loc[i, 'Prepaid Principal'] 

    cf_table8.head(cf_table8. shape[0] -1)

    cf_table8 = cf_table8[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#9--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance9 = int(og_bal_input9.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment9 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance9)
    principal_payment9= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance9)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 9
    cf_data9 = {'Interest': interest_payment9, 'Principal': principal_payment9}

    cf_table9 = pd.DataFrame(data = cf_data9, index=periods)

    cf_table9['Payment'] = cf_table9['Interest'] + cf_table9['Principal']
    
    cf_table9['Ending Balance'] = original_balance9 - \
                                cf_table9['Principal'].cumsum()

    cf_table9['Beginning Balance'] = [original_balance9] + \
                                    list(cf_table9['Ending Balance'])[:-1]

    cf_table9['SMM'] = float(smm_rate_input.get())

    cf_table9['Default'] = float(def_rate_input.get())

    cf_table9['Total_SMM_Loss'] = cf_table9['SMM'] + cf_table9['Default']

    cf_table9.loc[0, 'Net Outstanding Balance'] = int(og_bal_input9.get())
    cf_table9.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table9)):
        
        cf_table9.loc[i, 'Survival Factor'] = cf_table9.loc[i-1, 'Survival Factor'] - (cf_table9.loc[i-1, 'Survival Factor'] * cf_table9.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table9.loc[i, 'Prepaid Principal'] = cf_table9.loc[i-1, 'Net Outstanding Balance'] * cf_table9.loc[i, 'SMM']/100
        cf_table9.loc[i, 'Charge-Off Principal'] = cf_table9.loc[i-1, 'Net Outstanding Balance'] * cf_table9.loc[i, 'Default']/100
        cf_table9.loc[i, 'Scheduled Principle Received'] = cf_table9.loc[i, 'Principal'] * cf_table9.loc[i, 'Survival Factor']/100

        cf_table9.loc[i, 'Net Outstanding Balance'] = cf_table9.loc[i-1, 'Net Outstanding Balance'] - cf_table9.loc[i, 'Prepaid Principal'] - cf_table9.loc[i, 'Charge-Off Principal'] - cf_table9.loc[i, 'Scheduled Principle Received']

        cf_table9.loc[i, 'Total Principal Collections'] = cf_table9.loc[i, 'Scheduled Principle Received'] + cf_table9.loc[i, 'Prepaid Principal'] 

    cf_table9.head(cf_table9. shape[0] -1)

    cf_table9 = cf_table9[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#10--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance10 = int(og_bal_input10.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment10 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance10)
    principal_payment10= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance10)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 10
    cf_data10 = {'Interest': interest_payment10, 'Principal': principal_payment10}

    cf_table10 = pd.DataFrame(data = cf_data10, index=periods)

    cf_table10['Payment'] = cf_table10['Interest'] + cf_table10['Principal']
    
    cf_table10['Ending Balance'] = original_balance10 - \
                                cf_table10['Principal'].cumsum()

    cf_table10['Beginning Balance'] = [original_balance10] + \
                                    list(cf_table10['Ending Balance'])[:-1]

    cf_table10['SMM'] = float(smm_rate_input.get())

    cf_table10['Default'] = float(def_rate_input.get())

    cf_table10['Total_SMM_Loss'] = cf_table10['SMM'] + cf_table10['Default']

    cf_table10.loc[0, 'Net Outstanding Balance'] = int(og_bal_input10.get())
    cf_table10.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table10)):
        
        cf_table10.loc[i, 'Survival Factor'] = cf_table10.loc[i-1, 'Survival Factor'] - (cf_table10.loc[i-1, 'Survival Factor'] * cf_table10.loc[i, 'Total_SMM_Loss']/100)
        
        cf_table10.loc[i, 'Prepaid Principal'] = cf_table10.loc[i-1, 'Net Outstanding Balance'] * cf_table10.loc[i, 'SMM']/100
        cf_table10.loc[i, 'Charge-Off Principal'] = cf_table10.loc[i-1, 'Net Outstanding Balance'] * cf_table10.loc[i, 'Default']/100
        cf_table10.loc[i, 'Scheduled Principle Received'] = cf_table10.loc[i, 'Principal'] * cf_table10.loc[i, 'Survival Factor']/100

        cf_table10.loc[i, 'Net Outstanding Balance'] = cf_table10.loc[i-1, 'Net Outstanding Balance'] - cf_table10.loc[i, 'Prepaid Principal'] - cf_table10.loc[i, 'Charge-Off Principal'] - cf_table10.loc[i, 'Scheduled Principle Received']

        cf_table10.loc[i, 'Total Principal Collections'] = cf_table10.loc[i, 'Scheduled Principle Received'] + cf_table10.loc[i, 'Prepaid Principal'] 

    cf_table10.head(cf_table10. shape[0] -1)

    cf_table10 = cf_table10[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

    
#11--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance11 = int(og_bal_input11.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment11 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance11)
    principal_payment11= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance11)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 11
    cf_data11 = {'Interest': interest_payment11, 'Principal': principal_payment11}

    cf_table11 = pd.DataFrame(data = cf_data11, index=periods)

    cf_table11['Payment'] =cf_table11['Interest'] +cf_table11['Principal']
    
    cf_table11['Ending Balance'] = original_balance11 - \
                               cf_table11['Principal'].cumsum()

    cf_table11['Beginning Balance'] = [original_balance11] + \
                                    list(cf_table11['Ending Balance'])[:-1]

    cf_table11['SMM'] = float(smm_rate_input.get())

    cf_table11['Default'] = float(def_rate_input.get())

    cf_table11['Total_SMM_Loss'] =cf_table11['SMM'] +cf_table11['Default']

    cf_table11.loc[0, 'Net Outstanding Balance'] = int(og_bal_input11.get())
    cf_table11.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table11)):
        
       cf_table11.loc[i, 'Survival Factor'] =cf_table11.loc[i-1, 'Survival Factor'] - (cf_table11.loc[i-1, 'Survival Factor'] *cf_table11.loc[i, 'Total_SMM_Loss']/100)
        
       cf_table11.loc[i, 'Prepaid Principal'] =cf_table11.loc[i-1, 'Net Outstanding Balance'] *cf_table11.loc[i, 'SMM']/100
       cf_table11.loc[i, 'Charge-Off Principal'] =cf_table11.loc[i-1, 'Net Outstanding Balance'] *cf_table11.loc[i, 'Default']/100
       cf_table11.loc[i, 'Scheduled Principle Received'] =cf_table11.loc[i, 'Principal'] *cf_table11.loc[i, 'Survival Factor']/100

       cf_table11.loc[i, 'Net Outstanding Balance'] =cf_table11.loc[i-1, 'Net Outstanding Balance'] -cf_table11.loc[i, 'Prepaid Principal'] -cf_table11.loc[i, 'Charge-Off Principal'] -cf_table11.loc[i, 'Scheduled Principle Received']

       cf_table11.loc[i, 'Total Principal Collections'] =cf_table11.loc[i, 'Scheduled Principle Received'] +cf_table11.loc[i, 'Prepaid Principal'] 

    cf_table11.head(cf_table11.shape[0] -1)

    cf_table11 =cf_table11[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#12--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    original_balance12 = int(og_bal_input12.get())
    coupon = float(coupon_input.get())
    term = int(term_input.get())

    # Payments
    periods = range(1, term + 1)
    interest_payment12 = npf.ipmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance12)
    principal_payment12= npf.ppmt(rate = coupon / 12, per = periods, nper = term, pv = -original_balance12)

    # Pandas Float Formatting_
    pd.options.display.float_format = '{:,.2f}'.format

    # Cash Flow Table 12
    cf_data12 = {'Interest': interest_payment12, 'Principal': principal_payment12}

    cf_table12 = pd.DataFrame(data = cf_data12, index=periods)

    cf_table12['Payment'] =cf_table12['Interest'] +cf_table12['Principal']
    
    cf_table12['Ending Balance'] = original_balance12 - \
                               cf_table12['Principal'].cumsum()

    cf_table12['Beginning Balance'] = [original_balance12] + \
                                    list(cf_table12['Ending Balance'])[:-1]

    cf_table12['SMM'] = float(smm_rate_input.get())

    cf_table12['Default'] = float(def_rate_input.get())

    cf_table12['Total_SMM_Loss'] =cf_table12['SMM'] +cf_table12['Default']

    cf_table12.loc[0, 'Net Outstanding Balance'] = int(og_bal_input12.get())
    cf_table12.loc[0, 'Survival Factor'] = 100

    for i in range(1, len(cf_table12)):
        
       cf_table12.loc[i, 'Survival Factor'] =cf_table12.loc[i-1, 'Survival Factor'] - (cf_table12.loc[i-1, 'Survival Factor'] *cf_table12.loc[i, 'Total_SMM_Loss']/100)
        
       cf_table12.loc[i, 'Prepaid Principal'] =cf_table12.loc[i-1, 'Net Outstanding Balance'] *cf_table12.loc[i, 'SMM']/100
       cf_table12.loc[i, 'Charge-Off Principal'] =cf_table12.loc[i-1, 'Net Outstanding Balance'] *cf_table12.loc[i, 'Default']/100
       cf_table12.loc[i, 'Scheduled Principle Received'] =cf_table12.loc[i, 'Principal'] *cf_table12.loc[i, 'Survival Factor']/100

       cf_table12.loc[i, 'Net Outstanding Balance'] =cf_table12.loc[i-1, 'Net Outstanding Balance'] -cf_table12.loc[i, 'Prepaid Principal'] -cf_table12.loc[i, 'Charge-Off Principal'] -cf_table12.loc[i, 'Scheduled Principle Received']

       cf_table12.loc[i, 'Total Principal Collections'] =cf_table12.loc[i, 'Scheduled Principle Received'] +cf_table12.loc[i, 'Prepaid Principal'] 

    cf_table12.head(cf_table12. shape[0] -1)

    cf_table12 =cf_table12[['Beginning Balance', 'Payment', 'Interest', 
                        'Principal', 'Scheduled Principle Received', 'Prepaid Principal', 'Charge-Off Principal', 'Total Principal Collections', 'Net Outstanding Balance', 'Ending Balance']]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    writer = pd.ExcelWriter('New_Amort_Sched.xlsx', engine = 'xlsxwriter')

    cf_table1.to_excel(writer, sheet_name='Month 1')
    cf_table2.to_excel(writer, sheet_name='Month 2')
    cf_table3.to_excel(writer, sheet_name='Month 3')
    cf_table4.to_excel(writer, sheet_name='Month 4')
    cf_table5.to_excel(writer, sheet_name='Month 5')
    cf_table6.to_excel(writer, sheet_name='Month 6')
    cf_table7.to_excel(writer, sheet_name='Month 7')
    cf_table8.to_excel(writer, sheet_name='Month 8')
    cf_table9.to_excel(writer, sheet_name='Month 9')
    cf_table10.to_excel(writer, sheet_name='Month 10')
    cf_table11.to_excel(writer, sheet_name='Month 11')
    cf_table12.to_excel(writer, sheet_name='Month 12')

    #cf_table1.to_excel(writer, sheet_name = 'Amort Sched')

    writer.save()

# Creating a Hide Frame Function
def hide_frames():
    # Destroying the widgets in each frame
    for widget in wrapper0.winfo_children():
        widget.destroy()
    for widget in wrapper1.winfo_children():
        widget.destroy()
    for widget in wrapper2.winfo_children():
        widget.destroy()
    for widget in wrapper3.winfo_children():
        widget.destroy()
    for widget in wrapper4.winfo_children():
        widget.destroy()
    
    # Hiding all frames
    wrapper0.pack_forget()
    wrapper1.pack_forget()
    wrapper2.pack_forget()
    wrapper3.pack_forget()
    wrapper4.pack_forget()
    #myframe.pack_forget()

# Creating a Hide Frame Function
def hide_frames1():
    # Destroying the widgets in each frame
    #for widget in wrapper0.winfo_children():
    #    widget.destroy()
    for widget in wrapper1.winfo_children():
        widget.destroy()
    for widget in wrapper2.winfo_children():
        widget.destroy()
    for widget in wrapper3.winfo_children():
        widget.destroy()
    for widget in wrapper4.winfo_children():
        widget.destroy()
    
    # Hiding all frames
    #wrapper0.pack_forget()
    wrapper1.pack_forget()
    wrapper2.pack_forget()
    wrapper3.pack_forget()
    wrapper4.pack_forget()

# Defining a Main Menu
my_menu = Menu(win)
win.config(menu = my_menu)

# Creating Menu Items
app_menu = Menu(my_menu)
my_menu.add_cascade(label = "Options", menu = app_menu)
app_menu.add_command(label = "Home", command = home)
app_menu.add_separator()
app_menu.add_command(label = "Exit", command = win.quit)

win.geometry("900x950")
#win.resizable(False, False)
win.title("Capital Markets - Loan Cash Flow Model Creator")

start()

win.mainloop()