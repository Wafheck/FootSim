from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import random
from PIL import Image, ImageTk
import os
import sys

# INTIALIZE WINDOW
root = tk.Tk()
root.title("FootSim - Python based match engine")
root.geometry("1920x1080")
menubar = Menu(root) 
genfont = ("Courier New", 12)
smolfont = ("Arial", 7)
biggfont = ("Verdana", 16)
ratefont = ("Arial", 14)
redcanva = Canvas(root, bg="red")
redcanva.place(x=0, y=0, width=960, height=1080)
bluecanva = Canvas(root, bg="Blue")
bluecanva.place(x=961, y=0, width=960, height=1080)
pform = (-3,-2,-1,0,1,2,3)
randratings = list(range(45, 100))

#INI SETTINGS
simlgh = 3
fieldpath = f"/home/wafiq/Downloads/supply/field.jpg"
afieldpath = f"/home/wafiq/Downloads/supply/afield.png"
bfieldpath = f"/home/wafiq/Downloads/supply/bfield.png"
dfieldpath = f"/home/wafiq/Downloads/supply/dfield.png" 
t1name = ""
t2name = ""
f1val = 0
f2val = 0
t1a = 3
t1m = 3
t1d = 5
t2a = 3
t2m = 3
t2d = 5
name1 = 0
name2 = 0
t1strat = 0
t2strat = 0
FORMATIONS = [
    "4-3-3", 
    "4-2-3-1",
    "4-4-2",
    "3-4-3",
    "5-3-2"
]


def updatestar1():
    print("Updating Stars")
    x = float(aforwardavg_var.get())
    y = float(amidavg_var.get())
    z = float(adefenseavg_var.get())
    avg = (x + y + z) / 3
    strval = 0
    if avg > 93:
        global t1star5
        clearstar1()
        strval = 5
        t1star5.place(x=206, y=720)
    elif avg > 85 and avg < 94:
        global t1star45
        clearstar1()
        strval = 4.5
        t1star45.place(x=206, y=720)
    elif avg > 80  and avg < 86:
        global t1star4
        clearstar1()
        strval = 4
        t1star4.place(x=206, y=720)
    elif avg > 75 and avg < 81:
        clearstar1()
        strval = 3.5
        t1star35.place(x=206, y=720)
    elif avg > 70 and avg < 76:
        clearstar1()
        strval = 3
        t1star3.place(x=206, y=720)
    elif avg > 65 and avg < 71:
        clearstar1()
        strval = 2.5
        t1star25.place(x=206, y=720)
    elif avg > 60 and avg < 66:
        clearstar1()
        strval = 2
        t1star2.place(x=206, y=720)
    elif avg > 55 and avg < 61:
        clearstar1()
        strval = 1.5
        t1star15.place(x=206, y=720)
    elif avg > 50 and avg < 56:
        clearstar1()
        strval = 1
        t1star1.place(x=206, y=720)
    elif avg > 0 and avg < 51:
        clearstar1()
        strval = 0.5
        t1star05.place(x=206, y=720)

def updatestar2():
    print("Updating Stars2")
    x = float(bforwardavg_var.get())
    y = float(bmidavg_var.get())
    z = float(bdefenseavg_var.get())
    avg = (x + y + z) / 3
    strval = 0
    if avg > 93:
        global t2star5
        clearstar2()
        strval = 5
        t2star5.place(x=1186, y=720)
    elif avg > 85 and avg < 94:
        global t2star45
        clearstar2()
        strval = 4.5
        t2star45.place(x=1186, y=720)
    elif avg > 80  and avg < 86:
        global t2star4
        clearstar2()
        strval = 4
        t2star4.place(x=1186, y=720)
    elif avg > 75 and avg < 81:
        clearstar2()
        strval = 3.5
        t2star35.place(x=1186, y=720)
    elif avg > 70 and avg < 76:
        clearstar2()
        strval = 3
        t2star3.place(x=1186, y=720)
    elif avg > 65 and avg < 71:
        clearstar2()
        strval = 2.5
        t2star25.place(x=1186, y=720)
    elif avg > 60 and avg < 66:
        clearstar2()
        strval = 2
        t2star2.place(x=1186, y=720)
    elif avg > 55 and avg < 61:
        clearstar2()
        strval = 1.5
        t2star15.place(x=1186, y=720)
    elif avg > 50 and avg < 56:
        clearstar2()
        strval = 1
        t2star1.place(x=1186, y=720)
    elif avg > 0 and avg < 51:
        clearstar2()
        strval = 0.5
        t2star05.place(x=1186, y=720)

def limit_value(value):
    try:
        num = int(value)
        if num > 99:
            return "99"
        if num == 0 or num < 0:
            return "1"
        return value
    except ValueError:
        return ""

def update_sum_fw(*args):
    af0_var.set(limit_value(af0_var.get()))
    af1_var.set(limit_value(af1_var.get()))
    af2_var.set(limit_value(af2_var.get()))
 
    if t1a == 3:
            t1a0 = float(af0_var.get())
            t1a1 = float(af1_var.get())
            t1a2 = float(af2_var.get())
            aforwardsum_var.set(t1a0 + t1a1 + t1a2)
            aforwardavg_ntrun3 = float(aforwardsum_var.get()) / 3
            aforwardavg_var.set(round(aforwardavg_ntrun3, 2))
            updatestar1()
    if t1a == 2:
            t1a0 = float(af0_var.get())
            t1a2 = float(af2_var.get())
            aforwardsum_var.set(t1a0 + t1a2)
            aforwardavg_ntrun2 = float(aforwardsum_var.get()) / 2
            aforwardavg_var.set(round(aforwardavg_ntrun2, 2))
            updatestar1()
    if t1a == 1:
            t1a1 = float(af1_var.get())
            aforwardsum_var.set(t1a1)
            aforwardavg_var.set(t1a1)
            updatestar1()

def bupdate_sum_fw(*args):
    bf0_var.set(limit_value(bf0_var.get()))
    bf1_var.set(limit_value(bf1_var.get()))
    bf2_var.set(limit_value(bf2_var.get()))
    
    if t2a == 3:
            t2a0 = float(bf0_var.get())
            t2a1 = float(bf1_var.get())
            t2a2 = float(bf2_var.get())
            bforwardsum_var.set(t2a0 + t2a1 + t2a2)
            bforwardavg_ntrun3 = float(bforwardsum_var.get()) / 3
            bforwardavg_var.set(round(bforwardavg_ntrun3, 2))
            updatestar2()
    if t2a == 2:
            t2a0 = float(bf0_var.get())
            t2a2 = float(bf2_var.get())
            bforwardsum_var.set(t2a0 + t2a2)
            bforwardavg_ntrun2 = float(bforwardsum_var.get()) / 2
            bforwardavg_var.set(round(bforwardavg_ntrun2, 2))
            updatestar2()
    if t2a == 1:
            t2a1 = float(bf1_var.get())
            bforwardsum_var.set(t2a1)
            bforwardavg_var.set(t2a1)
            updatestar2()

def update_sum_md(*args):
    am0_var.set(limit_value(am0_var.get()))
    am1_var.set(limit_value(am1_var.get()))
    am2_var.set(limit_value(am2_var.get()))
    am3_var.set(limit_value(am3_var.get()))
    am4_var.set(limit_value(am4_var.get()))
  
    if t1m == 3:
        t1m0 = float(am0_var.get())
        t1m1 = float(am1_var.get())
        t1m2 = float(am2_var.get())
        amidsum_var.set(t1m0 + t1m1 + t1m2)
        amidavg_ntrun3 = float(amidsum_var.get()) / 3
        amidavg_var.set(round(amidavg_ntrun3, 2))
        updatestar1()
    elif t1m == 4:
        t1m0 = float(am0_var.get())
        t1m1 = float(am1_var.get())
        t1m2 = float(am2_var.get())
        t1m3 = float(am3_var.get())
        amidsum_var.set(t1m0 + t1m1 + t1m2 + t1m3)
        amidavg_ntrun4 = float(amidsum_var.get()) / 4
        amidavg_var.set(round(amidavg_ntrun4, 2))
        updatestar1()
    elif t1m == 5:
        t1m0 = float(am0_var.get())
        t1m1 = float(am1_var.get())
        t1m2 = float(am2_var.get())
        t1m3 = float(am3_var.get())
        t1m4 = float(am4_var.get())
        amidsum_var.set(t1m0 + t1m1 + t1m2 + t1m3 + t1m4)
        amidavg_ntrun5 = float(amidsum_var.get()) / 5
        amidavg_var.set(round(amidavg_ntrun5, 2))
        updatestar1()

def bupdate_sum_md(*args):
    bm0_var.set(limit_value(bm0_var.get()))
    bm1_var.set(limit_value(bm1_var.get()))
    bm2_var.set(limit_value(bm2_var.get()))
    bm3_var.set(limit_value(bm3_var.get()))
    bm4_var.set(limit_value(bm4_var.get()))
    
    if t2m == 3:
        t2m0 = float(bm0_var.get())
        t2m1 = float(bm1_var.get())
        t2m2 = float(bm2_var.get())
        bmidsum_var.set(t2m0 + t2m1 + t2m2)
        bmidavg_ntrun3 = float(bmidsum_var.get()) / 3
        bmidavg_var.set(round(bmidavg_ntrun3, 2))
        updatestar2()
    elif t2m == 4:
        t2m0 = float(bm0_var.get())
        t2m1 = float(bm1_var.get())
        t2m2 = float(bm2_var.get())
        t2m3 = float(bm3_var.get())
        bmidsum_var.set(t2m0 + t2m1 + t2m2 + t2m3)
        bmidavg_ntrun4 = float(bmidsum_var.get()) / 4
        bmidavg_var.set(round(bmidavg_ntrun4, 2))
        updatestar2()
    elif t2m == 5:
        t2m0 = float(bm0_var.get())
        t2m1 = float(bm1_var.get())
        t2m2 = float(bm2_var.get())
        t2m3 = float(bm3_var.get())
        t2m4 = float(bm4_var.get())
        bmidsum_var.set(t2m0 + t2m1 + t2m2 + t2m3 + t2m4)
        bmidavg_ntrun5 = float(bmidsum_var.get()) / 5
        bmidavg_var.set(round(bmidavg_ntrun5, 2))
        updatestar2()

def update_sum_df(*args):
    ad0_var.set(limit_value(ad0_var.get()))
    ad1_var.set(limit_value(ad1_var.get()))
    ad2_var.set(limit_value(ad2_var.get()))
    ad3_var.set(limit_value(ad3_var.get()))
    ad4_var.set(limit_value(ad4_var.get()))
    ag0_var.set(limit_value(ag0_var.get()))
    
    if t1d == 4:
        t1d0 = float(ad0_var.get())
        t1d1 = float(ad1_var.get())
        t1d2 = float(ad2_var.get())
        t1g0 = float(ag0_var.get())
        adefensesum_var.set(t1d0 + t1d1 + t1d2 + t1g0)
        adefenseavg_ntrun4 = float(adefensesum_var.get()) / 4
        adefenseavg_var.set(round(adefenseavg_ntrun4, 2))
        updatestar1()
    elif t1d == 5:
        t1d0 = float(ad0_var.get())
        t1d1 = float(ad1_var.get())
        t1d2 = float(ad2_var.get())
        t1d3 = float(ad3_var.get())
        t1g0 = float(ag0_var.get())
        adefensesum_var.set(t1d0 + t1d1 + t1d2 + t1d3 + t1g0)
        adefenseavg_ntrun5 = float(adefensesum_var.get()) / 5
        adefenseavg_var.set(round(adefenseavg_ntrun5, 2))
        updatestar1()
    elif t1d == 6:
        t1d0 = float(ad0_var.get())
        t1d1 = float(ad1_var.get())
        t1d2 = float(ad2_var.get())
        t1d3 = float(ad3_var.get())
        t1d4 = float(ad4_var.get())
        t1g0 = float(ag0_var.get())
        adefensesum_var.set(t1d0 + t1d1 + t1d2 + t1d3 + t1d4 + t1g0)
        adefenseavg_ntrun6 = float(adefensesum_var.get()) / 6
        adefenseavg_var.set(round(adefenseavg_ntrun6, 2))
        updatestar1()

def bupdate_sum_df(*args):
    bd0_var.set(limit_value(bd0_var.get()))
    bd1_var.set(limit_value(bd1_var.get()))
    bd2_var.set(limit_value(bd2_var.get()))
    bd3_var.set(limit_value(bd3_var.get()))
    bd4_var.set(limit_value(bd4_var.get()))
    bg0_var.set(limit_value(bg0_var.get()))
    
    if t2d == 4:
        t2d0 = float(bd0_var.get())
        t2d1 = float(bd1_var.get())
        t2d2 = float(bd2_var.get())
        t2g0 = float(bg0_var.get())
        bdefensesum_var.set(t2d0 + t2d1 + t2d2 + t2g0)
        bdefenseavg_ntrun4 = float(bdefensesum_var.get()) / 4
        bdefenseavg_var.set(round(bdefenseavg_ntrun4, 2))
        updatestar2()
    elif t2d == 5:
        t2d0 = float(bd0_var.get())
        t2d1 = float(bd1_var.get())
        t2d2 = float(bd2_var.get())
        t2d3 = float(bd3_var.get())
        t2g0 = float(bg0_var.get())
        bdefensesum_var.set(t2d0 + t2d1 + t2d2 + t2d3 + t2g0)
        bdefenseavg_ntrun5 = float(bdefensesum_var.get()) / 5
        bdefenseavg_var.set(round(bdefenseavg_ntrun5, 2))
        updatestar2()
    elif t2d == 6:
        t2d0 = float(bd0_var.get())
        t2d1 = float(bd1_var.get())
        t2d2 = float(bd2_var.get())
        t2d3 = float(bd3_var.get())
        t2d4 = float(bd4_var.get())
        t2g0 = float(bg0_var.get())
        bdefensesum_var.set(t2d0 + t2d1 + t2d2 + t2d3 + t2d4 + t2g0)
        bdefenseavg_ntrun6 = float(bdefensesum_var.get()) / 6
        bdefenseavg_var.set(round(bdefenseavg_ntrun6, 2))

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def clear():
    welcome.place_forget()
    condapply.place_forget()
    startbutton.place_forget()
    disp_simlgh.place_forget()
    simlgh1.place_forget()
    simlgh2.place_forget()
    simlgh3.place_forget()
    sim_length.place_forget()
    iniprog.place_forget()
    field1.place_forget()
    field2.place_forget()
    enteam1.place_forget()
    getteam1.place_forget()
    team1.place_forget()
    team2.place_forget()
    getteam2.place_forget()
    enteam2.place_forget()
    aforwardavg.place_forget()
    amidavg.place_forget()
    adefenseavg.place_forget()
    bforwardavg.place_forget()
    bmidavg.place_forget()
    bdefenseavg.place_forget()
    att1.place_forget()
    mid1.place_forget()
    def1.place_forget()
    att2.place_forget()
    mid2.place_forget()
    def2.place_forget()
    Freeze1.place_forget()
    Freeze2.place_forget()
    simulate.place_forget()
    selformations1.place_forget()
    selformations2.place_forget()
    attack_button.place_forget()
    balanced_button.place_forget()
    defend_button.place_forget()
    dynamic_button.place_forget()
    bdynamic_button.place_forget()
    bdefend_button.place_forget()
    bbalanced_button.place_forget()
    battack_button.place_forget()
    reset1.place_forget()
    reset2.place_forget()
    randomfill1.place_forget()
    randomfill2.place_forget()
    clearsim()
    clearfield1()
    clearfield2()
    hiderat1()
    hiderat2()
    clearstar1()
    clearstar2()

def start():
    welcome.place(x=960, y=340, anchor=CENTER)
    condapply.place(x=960, y=750, anchor=CENTER)
    startbutton.place(x=960, y=540, anchor=CENTER)

def Continue1():
    clear()
    menubar.add_cascade(label="Main Menu", menu=main)
    menubar.add_cascade(label="Options", menu=options)
    root.config(menu=menubar)
    iniprog.place(x=960, y=650, anchor=CENTER) 

def Continue2():
    clear()
    iniprog.place(x=960, y=650, anchor=CENTER)

def settings():
    clear()
    disp_simlgh.place(x=550, y=750)
    simlgh1.place(x=100, y=100)
    simlgh2.place(x=100, y=135)
    simlgh3.place(x=100, y=170)
    sim_length.place(x=100, y=50)

def simlength1():
    simlgh = 3
    disp_simlgh_var.set(simlgh)

def simlength2():
    simlgh = 5
    disp_simlgh_var.set(simlgh)
    
def simlength3():
    simlgh = 10
    disp_simlgh_var.set(simlgh)

def initialize():
    clear()
    if t1strat == 0:
        field1.place(x=100, y=150)
    elif t1strat == 1:
        dfield1.place(x=100, y=150)
    elif t1strat == 2:
        bfield1.place(x=100, y=150)
    elif t1strat == 3:
        afield1.place(x=100, y=150)
    if t2strat == 0:
        field2.place(x=1400, y=150)
    elif t2strat == 1:
        dfield2.place(x=1400, y=150)
    elif t2strat == 2:
        bfield2.place(x=1400, y=150)
    elif t2strat == 3:
        afield2.place(x=1400, y=150)
    if name1 == 0:
        enteam1.place(x=100, y=130)
        getteam1.place(x=225, y=130)
    if name1 == 1:
        team1.place(x=100, y=125)
    if name2 == 0:
        enteam2.place(x=1080, y=130)
        getteam2.place(x=1205, y=130)
    if name2 == 1:
        team2.place(x=1080, y=125)
    aforwardavg.place(x=0, y=210)
    amidavg.place(x=0, y=310)
    adefenseavg.place(x=0, y=410)
    bforwardavg.place(x=1795, y=250)
    bmidavg.place(x=1795, y=350)
    bdefenseavg.place(x=1795, y=450)
    att1.place(x=0, y=180)
    mid1.place(x=0, y=280)
    def1.place(x=0, y=380)
    att2.place(x=1460, y=220)
    mid2.place(x=1440, y=320)
    def2.place(x=1450, y=420)
    t1star0.place(x=206, y=720)
    t2star0.place(x=1186, y=720)
    Freeze1.place(x=100, y=635)
    Freeze2.place(x=1080, y=635)
    simulate.place(x=700, y=650)
    selformations1.place(x=100, y=106)
    selformations2.place(x=1080, y=106)
    dynamic_button.place(x=164, y=635)
    defend_button.place(x=234, y=635)
    balanced_button.place(x=304, y=635)
    attack_button.place(x=374, y=635)
    bdynamic_button.place(x=1144, y=635)
    bdefend_button.place(x=1214, y=635)
    bbalanced_button.place(x=1284, y=635)
    battack_button.place(x=1354, y=635)
    reset1.place(x=100, y=660)
    reset2.place(x=1080, y=660)
    randomfill1.place(x=100, y=680)
    randomfill2.place(x=1080, y=680)
    showrat1()
    showrat2()

def clearstar1():

    t1star0.place_forget()
    t1star05.place_forget()
    t1star15.place_forget()
    t1star1.place_forget()
    t1star25.place_forget()
    t1star3.place_forget()
    t1star35.place_forget()
    t1star4.place_forget()
    t1star45.place_forget()
    t1star5.place_forget()
def clearstar2():
    t2star0.place_forget()
    t1star05.place_forget()
    t2star15.place_forget()
    t2star1.place_forget()
    t2star2.place_forget()
    t2star25.place_forget()
    t2star3.place_forget()
    t2star35.place_forget()
    t2star4.place_forget()
    t2star45.place_forget()
    t2star5.place_forget()

def setteam1():
    global name1
    t1name_var.set(str(enteam1.get()))
    team1.place(x=100, y=125)
    name1 = 1
    getteam1.place_forget()
    enteam1.place_forget()

def setteam2():
    global name2
    name2 = 1
    t2name_var.set(str(enteam2.get()))
    team2.place(x=1080, y=125)
    getteam2.place_forget()
    enteam2.place_forget()

def showrat1():
    ###4-3-3###
    if t1a == 3 and t1m == 3 and t1d == 5:
        af0.place(x=200, y=250)
        af1.place(x=260, y=250)
        af2.place(x=320, y=250)
        am0.place(x=200, y=375)
        am1.place(x=260, y=375)
        am2.place(x=320, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
    ###4-2-3-1###
    if t1a == 1 and t1m == 5 and t1d == 5:
        af1.place(x=260, y=250)
        am0.place(x=150, y=318)
        am1.place(x=260, y=318)
        am2.place(x=370, y=318)
        am3.place(x=230, y=375)
        am4.place(x=290, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
    ###4-4-2###
    if t1a == 2 and t1m == 4 and t1d == 5:
        af0.place(x=200, y=250)
        af2.place(x=320, y=250)
        am0.place(x=150, y=375)
        am1.place(x=230, y=375)
        am2.place(x=290, y=375)
        am3.place(x=370, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
    if t1a == 3 and t1m == 4 and t1d == 4:
        af0.place(x=200, y=250)
        af1.place(x=260, y=250)
        af2.place(x=320, y=250)
        am0.place(x=150, y=375)
        am1.place(x=230, y=375)
        am2.place(x=290, y=375)
        am3.place(x=370, y=375)
        ad0.place(x=200, y=500)
        ad1.place(x=260, y=500)
        ad2.place(x=320, y=500)
    if t1a == 3 and t1m == 4 and t1d == 6:
        af0.place(x=200, y=250)
        af1.place(x=260, y=250)
        af2.place(x=320, y=250)
        am0.place(x=200, y=375)
        am1.place(x=260, y=375)
        am2.place(x=320, y=375)
        ad0.place(x=150, y=463)
        ad1.place(x=200, y=500)
        ad2.place(x=260, y=500)
        ad3.place(x=320, y=500)
        ad4.place(x=370, y=463)
    if t1a == 2 and t1m == 3 and t1d == 6:
        af0.place(x=200, y=250)
        af2.place(x=320, y=250)
        am0.place(x=200, y=375)
        am1.place(x=260, y=375)
        am2.place(x=320, y=375)
        ad0.place(x=150, y=463)
        ad1.place(x=200, y=500)
        ad2.place(x=260, y=500)
        ad3.place(x=320, y=500)
        ad4.place(x=370, y=463)
    ag0.place(x=260, y=590)

def showrat2():
    ###4-3-3###
    if t2a == 3 and t2m == 3 and t2d == 5:
        bf0.place(x=1500, y=250)
        bf1.place(x=1560, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1500, y=375)
        bm1.place(x=1560, y=375)
        bm2.place(x=1620, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1510, y=500)
        bd2.place(x=1570, y=500)
        bd3.place(x=1630, y=500)
    ###4-2-3-1###
    if t2a == 1 and t2m == 5 and t2d == 5:
        bf1.place(x=1560, y=250)
        bm0.place(x=1450, y=318)
        bm1.place(x=1560, y=318)
        bm2.place(x=1670, y=318)
        bm3.place(x=1520, y=375)
        bm4.place(x=1580, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1530, y=500)
        bd2.place(x=1590, y=500)
        bd3.place(x=1670, y=500)
    ###4-4-2###
    if t2a == 2 and t2m == 4 and t2d == 5:
        bf0.place(x=1500, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1450, y=375)
        bm1.place(x=1530, y=375)
        bm2.place(x=1590, y=375)
        bm3.place(x=1670, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1530, y=500)
        bd2.place(x=1590, y=500)
        bd3.place(x=1670, y=500)
    if t2a == 3 and t2m == 4 and t2d == 4:
        bf0.place(x=1500, y=250)
        bf1.place(x=1560, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1450, y=375)
        bm1.place(x=1530, y=375)
        bm2.place(x=1590, y=375)
        bm3.place(x=1670, y=375)
        bd0.place(x=1500, y=500)
        bd1.place(x=1560, y=500)
        bd2.place(x=1620, y=500)
    if t2a == 3 and t2m == 4 and t2d == 6:
        bf0.place(x=1500, y=250)
        bf1.place(x=1560, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1500, y=375)
        bm1.place(x=1560, y=375)
        bm2.place(x=1620, y=375)
        bd0.place(x=1450, y=463)
        bd1.place(x=1500, y=500)
        bd2.place(x=1560, y=500)
        bd3.place(x=1620, y=500)
        bd4.place(x=1670, y=463)
    if t2a == 2 and t2m == 3 and t2d == 6:
        bf0.place(x=1500, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1500, y=375)
        bm1.place(x=1560, y=375)
        bm2.place(x=1620, y=375)
        bd0.place(x=1450, y=463)
        bd1.place(x=1500, y=500)
        bd2.place(x=1560, y=500)
        bd3.place(x=1620, y=500)
        bd4.place(x=1670, y=463)
    bg0.place(x=1560, y=590)
    
def hiderat2():
    bf0.place_forget()
    bf1.place_forget()
    bf2.place_forget()
    bm0.place_forget()
    bm1.place_forget()
    bm2.place_forget()
    bm3.place_forget()
    bm4.place_forget()
    bd0.place_forget()
    bd1.place_forget()
    bd2.place_forget()
    bd3.place_forget()
    bd4.place_forget()
    bg0.place_forget()
    
def hiderat1():
    af0.place_forget()
    af1.place_forget()
    af2.place_forget()
    am0.place_forget()
    am1.place_forget()
    am2.place_forget()
    am3.place_forget()
    am4.place_forget()
    ad0.place_forget()
    ad1.place_forget()
    ad2.place_forget()
    ad3.place_forget()
    ad4.place_forget()
    ag0.place_forget()
    
def freeze1():
    global f1val
    if f1val == 0:
        af0.config(state="disable")
        af1.config(state="disable")
        af2.config(state="disable")
        am0.config(state="disable")
        am1.config(state="disable")
        am2.config(state="disable")
        ad0.config(state="disable")
        ad1.config(state="disable")
        ad2.config(state="disable")
        ad3.config(state="disable")
        ag0.config(state="disable")
        selformations1.config(state="disable")
        attack_button.config(state="disable")
        balanced_button.config(state="disable")
        defend_button.config(state="disable")
        dynamic_button.config(state="disable")
        randomfill1.config(state="disable")
        f1val = 1
        freeze1_var.set("UNFREEZE")
    elif f1val == 1:
        af0.config(state="normal")
        af1.config(state="normal")
        af2.config(state="normal")
        am0.config(state="normal")
        am1.config(state="normal")
        am2.config(state="normal")
        ad0.config(state="normal")
        ad1.config(state="normal")
        ad2.config(state="normal")
        ad3.config(state="normal")
        ag0.config(state="normal")
        selformations1.config(state= "readonly")
        attack_button.config(state="normal")
        balanced_button.config(state="normal")
        defend_button.config(state="normal")
        dynamic_button.config(state="normal")
        randomfill1.config(state="normal")
        f1val = 0
        freeze1_var.set("FREEZE")
        
def freeze2():
    global f2val
    if f2val == 0:
        bf0.config(state="disable")
        bf1.config(state="disable")
        bf2.config(state="disable")
        bm0.config(state="disable")
        bm1.config(state="disable")
        bm2.config(state="disable")
        bd0.config(state="disable")
        bd1.config(state="disable")
        bd2.config(state="disable")
        bd3.config(state="disable")
        bg0.config(state="disable")
        selformations2.config(state="disable")
        battack_button.config(state="disable")
        bbalanced_button.config(state="disable")
        bdefend_button.config(state="disable")
        bdynamic_button.config(state="disable")
        randomfill2.config(state="disable")
        f2val = 1
        freeze2_var.set("UNFREEZE")
    elif f2val == 1:
        bf0.config(state="normal")
        bf1.config(state="normal")
        bf2.config(state="normal")
        bm0.config(state="normal")
        bm1.config(state="normal")
        bm2.config(state="normal")
        bd0.config(state="normal")
        bd1.config(state="normal")
        bd2.config(state="normal")
        bd3.config(state="normal")
        bg0.config(state="normal")
        selformations2.config(state= "readonly")
        battack_button.config(state="normal")
        bbalanced_button.config(state="normal")
        bdefend_button.config(state="normal")
        bdynamic_button.config(state="normal") 
        randomfill2.config(state="normal") 
        f2val = 0
        freeze2_var.set("FREEZE")    

def resetrate1():
    af0_var.set("")
    af1_var.set("")
    af2_var.set("")
    am0_var.set("")
    am1_var.set("")
    am2_var.set("")
    am3_var.set("")
    am4_var.set("")
    ad0_var.set("")
    ad1_var.set("")
    ad2_var.set("")
    ad3_var.set("")
    ad4_var.set("")
    ag0_var.set("")
    aforwardavg_var.set("")
    amidavg_var.set("")
    adefenseavg_var.set("")
    clearstar1()
    t1star0.place(x=206, y=720)

def resetrate2():
    bf0_var.set("")
    bf1_var.set("")
    bf2_var.set("")
    bm0_var.set("")
    bm1_var.set("")
    bm2_var.set("")
    bm3_var.set("")
    bm4_var.set("")
    bd0_var.set("")
    bd1_var.set("")
    bd2_var.set("")
    bd3_var.set("")
    bd4_var.set("")
    bg0_var.set("")
    bforwardavg_var.set("")
    bmidavg_var.set("")
    bdefenseavg_var.set("")
    clearstar2()
    t2star0.place(x=1186, y=720)

def aupdate_avg_433():
    aupdfwdsum = int(t1f1_var.get()) + int(t1f2_var.get()) + int(t1f3_var.get())
    aupdmdsum = int(t1m1_var.get()) + int(t1m2_var.get()) + int(t1m3_var.get())
    aupddfsum = int(t1d1_var.get()) + int(t1d2_var.get()) + int(t1d3_var.get()) + int(t1d4_var.get()) + int(t1gk_var.get())
    aupdfwdavg_ntrun = float(aupdfwdsum / 3)
    aupdmidavg_ntrun = float(aupdmdsum / 3)
    aupddfavg_ntrun = float(aupddfsum / 5)
    aupdfwdavg_var.set(round(aupdfwdavg_ntrun, 2))
    aupdmidavg_var.set(round(aupdmidavg_ntrun, 2))
    aupddfavg_var.set(round(aupddfavg_ntrun, 2))
    if aupdfwdavg_var.get() >= aforwardavg_var.get():
         aupdfwdavg.config(bg="green", fg="white")
         aupdfwdavg.place(x=0, y=240)
         aupdfwdavg.tkraise()
    elif aupdfwdavg_var.get() < aforwardavg_var.get():
         aupdfwdavg.config(bg="yellow", fg="black")
         aupdfwdavg.place(x=0, y=240)
         aupdfwdavg.tkraise()
    if aupdmidavg_var.get() >= amidavg_var.get():
         aupdmidavg.config(bg="green", fg="white")
         aupdmidavg.place(x=0, y=340)
         aupdmidavg.tkraise()
    elif aupdmidavg_var.get() < amidavg_var.get():
         aupdmidavg.config(bg="yellow", fg="black")
         aupdmidavg.place(x=0, y=340)
         aupdmidavg.tkraise()
    if aupddfavg_var.get() >= adefenseavg_var.get():
         aupddfavg.config(bg="green", fg="white")
         aupddfavg.place(x=0, y=440)
         aupddfavg.tkraise()
    elif aupddfavg_var.get() < adefenseavg_var.get():
         aupddfavg.config(bg="yellow", fg="black")
         aupddfavg.place(x=0, y=440)
         aupddfavg.tkraise()
         aupdfwdavg.place(x=0, y=240)
         aupdmidavg.place(x=0, y=340)
         aupddfavg.place(x=0, y=440)

def bupdate_avg_433():
    bupdfwdsum = int(t2f1_var.get()) + int(t2f2_var.get()) + int(t2f3_var.get())
    bupdmdsum = int(t2m1_var.get()) + int(t2m2_var.get()) + int(t2m3_var.get())
    bupddfsum = int(t2d1_var.get()) + int(t2d2_var.get()) + int(t2d3_var.get()) + int(t2d4_var.get()) + int(t2gk_var.get())
    bupdfwdavg_ntrun = float(bupdfwdsum / 3)
    bupdmdavg_ntrun = float(bupdmdsum / 3)
    bupddfavg_ntrun = float(bupddfsum / 5)
    bupdfwdavg_var.set(round(bupdfwdavg_ntrun, 2))
    bupdmdavg_var.set(round(bupdmdavg_ntrun, 2))
    bupddfavg_var.set(round(bupddfavg_ntrun, 2))
    if bupdfwdavg_var.get() >= bforwardavg_var.get():
         bupdfwdavg.config(bg="green", fg="white")
         bupdfwdavg.place(x=1482, y=280)
         bupdfwdavg.tkraise()
    elif bupdfwdavg_var.get() < bforwardavg_var.get():
         bupdfwdavg.config(bg="yellow", fg="black")
         bupdfwdavg.place(x=1482, y=280)
         bupdfwdavg.tkraise()
    if bupdmdavg_var.get() >= bmidavg_var.get():
         bupdmdavg.config(bg="green", fg="white")
         bupdmdavg.place(x=1482, y=380)
         bupdmdavg.tkraise()
    elif bupdmdavg_var.get() < bmidavg_var.get():
         bupdmdavg.config(bg="yellow", fg="black")
         bupdmdavg.place(x=1482, y=380)
         bupdmdavg.tkraise()
    if bupddfavg_var.get() >= bdefenseavg_var.get():
         bupddfavg.config(bg="green", fg="white")
         bupddfavg.place(x=1482, y=480)
         bupddfavg.tkraise()
    elif bupddfavg_var.get() < bdefenseavg_var.get():
         bupddfavg.config(bg="yellow", fg="black")
         bupddfavg.place(x=1482, y=480)
         bupddfavg.tkraise()
         bupdfwdavg.place(x=1482, y=280)
         bupdmdavg.place(x=1482, y=380) 
         bupddfavg.place(x=1482, y=480)
def Simulate():
    print("sim clicked")
    clearsim()
    if f1val == 0 or f2val == 0 or aforwardavg_var.get() == "" or amidavg_var.get() == "" or adefenseavg_var.get() == "" or bforwardavg_var.get() == "" or bmidavg_var.get() == "" or bdefenseavg_var.get() == "":
        messagebox.showerror("Error", "Please freeze all player ratings. Make sure all player values are filled.") 
    elif f1val == 1 and f2val == 1:
        if t1a == 3 and t1m == 3 and t1d == 5:
            t1f1_var.set(int(af0_var.get()) + random.choice(pform))
            if t1f1_var.get() >= af0_var.get():
                t1f1.config(bg="green", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            else:
                t1f1.config(bg="red", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            t1f2_var.set(int(af1_var.get()) + random.choice(pform))
            if t1f2_var.get() >= af1_var.get():
                t1f2.config(bg="green", fg="white")
                t1f2.place(x=260, y=270)
                t1f2.tkraise()
            else:
                t1f2.config(bg="red", fg="white")
                t1f2.place(x=260, y=270)
                t1f2.tkraise()
            t1f3_var.set(int(af2_var.get()) + random.choice(pform))
            if t1f3_var.get() >= af2_var.get():
                t1f3.config(bg="green", fg="white")
                t1f3.place(x=320, y=270)
                t1f3.tkraise()
            else:
                t1f3.config(bg="red", fg="white")
                t1f3.place(x=320, y=270)
                t1f3.tkraise()
            t1m1_var.set(int(am0_var.get()) + random.choice(pform)) 
            if t1m1_var.get() >= am0_var.get():
                t1m1.config(bg="green", fg="white")
                t1m1.place(x=200, y=395)
                t1m1.tkraise()
            else:
                t1m1.config(bg="red", fg="white")
                t1m1.place(x=200, y=395)
                t1m1.tkraise()
            t1m2_var.set(int(am1_var.get()) + random.choice(pform))
            if t1m2_var.get() >= am1_var.get():
                t1m2.config(bg="green", fg="white")
                t1m2.place(x=260, y=395)
                t1m2.tkraise()
            else:
                t1m2.config(bg="red", fg="white")
                t1m2.place(x=260, y=395)
                t1m2.tkraise()
            t1m3_var.set(int(am2_var.get()) + random.choice(pform))
            if t1m3_var.get() >= am2_var.get():
                t1m3.config(bg="green", fg="white")
                t1m3.place(x=320, y=395)
                t1m3.tkraise()
            else:
                t1m3.config(bg="red", fg="white")
                t1m3.place(x=320, y=395)
                t1m3.tkraise()
            t1d1_var.set(int(ad0_var.get()) + random.choice(pform))
            if t1d1_var.get() >= ad0_var.get():
                t1d1.config(bg="green", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            else:
                t1d1.config(bg="red", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            t1d2_var.set(int(ad1_var.get()) + random.choice(pform))
            if t1d2_var.get() >= ad1_var.get():
                t1d2.config(bg="green", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            else:
                t1d2.config(bg="red", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            t1d3_var.set(int(ad2_var.get()) + random.choice(pform))
            if t1d3_var.get() >= ad2_var.get():
                t1d3.config(bg="green", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            else:
                t1d3.config(bg="red", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            t1d4_var.set(int(ad3_var.get()) + random.choice(pform))
            if t1d4_var.get() >= ad3_var.get():
                t1d4.config(bg="green", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            else:
                t1d4.config(bg="red", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            t1gk_var.set(int(ag0_var.get()) + random.choice(pform))
            if t1gk_var.get() >= ag0_var.get():
                t1gk.config(bg="green", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            else:
                t1gk.config(bg="red", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            aupdate_avg_433()
            
        if t1a == 1 and t1m == 5 and t1d == 5:
            t1f1_var.set(int(af1_var.get()) + random.choice(pform))
            if t1f1_var.get() >= af1_var.get():
                t1f1.config(bg="green", fg="white")
                t1f1.place(x=260, y=270)
                t1f1.tkraise()
            else:
                t1f1.config(bg="red", fg="white")
                t1f1.place(x=260, y=270)
                t1f1.tkraise()
            t1m1_var.set(int(am0_var.get()) + random.choice(pform))
            if t1m1_var.get() >= am0_var.get():
                t1m1.config(bg="green", fg="white")
                t1m1.place(x=150, y=338)
                t1m1.tkraise()
            else:
                t1m1.config(bg="red", fg="white")
                t1m1.place(x=150, y=338)
                t1m1.tkraise()
            t1m2_var.set(int(am1_var.get()) + random.choice(pform))
            if t1m2_var.get() >= am1_var.get():
                t1m2.config(bg="green", fg="white")
                t1m2.place(x=260, y=338)
                t1m2.tkraise()
            else:
                t1m2.config(bg="red", fg="white")
                t1m2.place(x=260, y=338)
                t1m2.tkraise()
            t1m3_var.set(int(am2_var.get()) + random.choice(pform))
            if t1m3_var.get() >= am2_var.get():
                t1m3.config(bg="green", fg="white")
                t1m3.place(x=370, y=338)
                t1m3.tkraise()
            else:
                t1m3.config(bg="red", fg="white")
                t1m3.place(x=370, y=338)
                t1m3.tkraise()
            t1m4_var.set(int(am3_var.get()) + random.choice(pform))
            if t1m4_var.get() >= am3_var.get():
                t1m4.config(bg="green", fg="white")
                t1m4.place(x=230, y=395)
                t1m4.tkraise()
            else:
                t1m4.config(bg="red", fg="white")
                t1m4.place(x=230, y=395)
                t1m4.tkraise()
            t1m5_var.set(int(am4_var.get()) + random.choice(pform))
            if t1m5_var.get() >= am4_var.get():
                t1m5.config(bg="green", fg="white")
                t1m5.place(x=290, y=395)
                t1m5.tkraise()
            else:
                t1m5.config(bg="red", fg="white")
                t1m5.place(x=290, y=395)
                t1m5.tkraise()
            t1d1_var.set(int(ad0_var.get()) + random.choice(pform))
            if t1d1_var.get() >= ad0_var.get():
                t1d1.config(bg="green", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            else:
                t1d1.config(bg="red", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            t1d2_var.set(int(ad1_var.get()) + random.choice(pform))
            if t1d2_var.get() >= ad1_var.get():
                t1d2.config(bg="green", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            else:
                t1d2.config(bg="red", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            t1d3_var.set(int(ad2_var.get()) + random.choice(pform))
            if t1d3_var.get() >= ad2_var.get():
                t1d3.config(bg="green", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            else:
                t1d3.config(bg="red", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            t1d4_var.set(int(ad3_var.get()) + random.choice(pform))
            if t1d4_var.get() >= ad3_var.get():
                t1d4.config(bg="green", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            else:
                t1d4.config(bg="red", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            t1gk_var.set(int(ag0_var.get()) + random.choice(pform))
            if t1gk_var.get() >= ag0_var.get():
                t1gk.config(bg="green", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            else:
                t1gk.config(bg="red", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
        if t1a == 2 and t1m == 4 and t1d == 5:
            t1f1_var.set(int(af0_var.get()) + random.choice(pform))
            if t1f1_var.get() >= af0_var.get():
                t1f1.config(bg="green", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            else:
                t1f1.config(bg="red", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            t1f2_var.set(int(af2_var.get()) + random.choice(pform))
            if t1f2_var.get() >= af2_var.get():
                t1f2.config(bg="green", fg="white")
                t1f2.place(x=320, y=270)
                t1f2.tkraise()
            else:
                t1f2.config(bg="red", fg="white")
                t1f2.place(x=320, y=270)
                t1f2.tkraise()
            t1m1_var.set(int(am0_var.get()) + random.choice(pform))
            if t1m1_var.get() >= am0_var.get():
                t1m1.config(bg="green", fg="white")
                t1m1.place(x=150, y=395)
                t1m1.tkraise()
            else:
                t1m1.config(bg="red", fg="white")
                t1m1.place(x=150, y=395)
                t1m1.tkraise()
            t1m2_var.set(int(am1_var.get()) + random.choice(pform))
            if t1m2_var.get() >= am1_var.get():
                t1m2.config(bg="green", fg="white")
                t1m2.place(x=230, y=395)
                t1m2.tkraise()
            else:
                t1m2.config(bg="red", fg="white")
                t1m2.place(x=230, y=395)
                t1m2.tkraise()
            t1m3_var.set(int(am2_var.get()) + random.choice(pform))
            if t1m3_var.get() >= am2_var.get():
                t1m3.config(bg="green", fg="white")
                t1m3.place(x=290, y=395)
                t1m3.tkraise()
            else:    
                t1m3.config(bg="red", fg="white")
                t1m3.place(x=290, y=395)
                t1m3.tkraise()  
            t1m4_var.set(int(am3_var.get()) + random.choice(pform))
            if t1m4_var.get() >= am3_var.get():
                t1m4.config(bg="green", fg="white")
                t1m4.place(x=370, y=395)
                t1m4.tkraise()
            else:
                t1m4.config(bg="red", fg="white")
                t1m4.place(x=370, y=395)
                t1m4.tkraise()
            t1d1_var.set(int(ad0_var.get()) + random.choice(pform))
            if t1d1_var.get() >= ad0_var.get():
                t1d1.config(bg="green", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            else:
                t1d1.config(bg="red", fg="white")
                t1d1.place(x=150, y=520)
                t1d1.tkraise()
            t1d2_var.set(int(ad1_var.get()) + random.choice(pform))
            if t1d2_var.get() >= ad1_var.get():
                t1d2.config(bg="green", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            else:
                t1d2.config(bg="red", fg="white")
                t1d2.place(x=230, y=520)
                t1d2.tkraise()
            t1d3_var.set(int(ad2_var.get()) + random.choice(pform))
            if t1d3_var.get() >= ad2_var.get():
                t1d3.config(bg="green", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            else:
                t1d3.config(bg="red", fg="white")
                t1d3.place(x=290, y=520)
                t1d3.tkraise()
            t1d4_var.set(int(ad3_var.get()) + random.choice(pform))
            if t1d4_var.get() >= ad3_var.get():
                t1d4.config(bg="green", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            else:
                t1d4.config(bg="red", fg="white")
                t1d4.place(x=370, y=520)
                t1d4.tkraise()
            t1gk_var.set(int(ag0_var.get()) + random.choice(pform))
            if t1gk_var.get() >= ag0_var.get():
                t1gk.config(bg="green", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            else:
                t1gk.config(bg="red", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
        if t1a == 3 and t1m == 4 and t1d == 4:
            t1f1_var.set(int(af0_var.get()) + random.choice(pform))
            if t1f1_var.get() >= af0_var.get():
                t1f1.config(bg="green", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            else:
                t1f1.config(bg="red", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            t1f2_var.set(int(af1_var.get()) + random.choice(pform))
            if t1f2_var.get() >= af1_var.get():
                t1f2.config(bg="green", fg="white")
                t1f2.place(x=260, y=270)
                t1f2.tkraise()
            else:
                t1f2.config(bg="red", fg="white")
                t1f2.place(x=260, y=270)
                t1f2.tkraise()
            t1f3_var.set(int(af2_var.get()) + random.choice(pform))
            if t1f3_var.get() >= af2_var.get():
                t1f3.config(bg="green", fg="white")
                t1f3.place(x=320, y=270)
                t1f3.tkraise()
            else:
                t1f3.config(bg="red", fg="white")
                t1f3.place(x=320, y=270)
                t1f3.tkraise()
            t1m1_var.set(int(am0_var.get()) + random.choice(pform))
            if t1m1_var.get() >= am0_var.get():
                t1m1.config(bg="green", fg="white")
                t1m1.place(x=150, y=395)
                t1m1.tkraise()
            else:
                t1m1.config(bg="red", fg="white")
                t1m1.place(x=150, y=395)
                t1m1.tkraise()
            t1m2_var.set(int(am1_var.get()) + random.choice(pform))
            if t1m2_var.get() >= am1_var.get():
                t1m2.config(bg="green", fg="white")
                t1m2.place(x=230, y=395)
                t1m2.tkraise()
            else:
                t1m2.config(bg="red", fg="white")
                t1m2.place(x=230, y=395)
                t1m2.tkraise()
            t1m3_var.set(int(am2_var.get()) + random.choice(pform))
            if t1m3_var.get() >= am2_var.get():
                t1m3.config(bg="green", fg="white")
                t1m3.place(x=290, y=395)
                t1m3.tkraise()
            else:
                t1m3.config(bg="red", fg="white")
                t1m3.place(x=290, y=395)
                t1m3.tkraise()
            t1m4_var.set(int(am3_var.get()) + random.choice(pform))
            if t1m4_var.get() >= am3_var.get():
                t1m4.config(bg="green", fg="white")
                t1m4.place(x=370, y=395)
                t1m4.tkraise()
            else:
                t1m4.config(bg="red", fg="white")
                t1m4.place(x=370, y=395)
                t1m4.tkraise()
            t1d1_var.set(int(ad0_var.get()) + random.choice(pform))
            if t1d1_var.get() >= ad0_var.get():
                t1d1.config(bg="green", fg="white")
                t1d1.place(x=200, y=520)
                t1d1.tkraise()
            else:
                t1d1.config(bg="red", fg="white")
                t1d1.place(x=200, y=520)
                t1d1.tkraise()
            t1d2_var.set(int(ad1_var.get()) + random.choice(pform))
            if t1d2_var.get() >= ad1_var.get():
                t1d2.config(bg="green", fg="white")
                t1d2.place(x=260, y=520)
                t1d2.tkraise()
            else:
                t1d2.config(bg="red", fg="white")
                t1d2.place(x=260, y=520)
                t1d2.tkraise()
            t1d3_var.set(int(ad2_var.get()) + random.choice(pform))
            if t1d3_var.get() >= ad2_var.get():
                t1d3.config(bg="green", fg="white")
                t1d3.place(x=320, y=520)
                t1d3.tkraise()
            else:
                t1d3.config(bg="red", fg="white")
                t1d3.place(x=320, y=520)
                t1d3.tkraise()
            t1gk_var.set(int(ag0_var.get()) + random.choice(pform))
            if t1gk_var.get() >= ag0_var.get():
                t1gk.config(bg="green", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            else:
                t1gk.config(bg="red", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
        if t1a == 2 and t1m == 3 and t1d == 6:
            t1f1_var.set(int(af0_var.get()) + random.choice(pform))
            if t1f1_var.get() >= af0_var.get():
                t1f1.config(bg="green", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            else:
                t1f1.config(bg="red", fg="white")
                t1f1.place(x=200, y=270)
                t1f1.tkraise()
            t1f2_var.set(int(af2_var.get()) + random.choice(pform))
            if t1f2_var.get() >= af2_var.get():
                t1f2.config(bg="green", fg="white")
                t1f2.place(x=320, y=270)
                t1f2.tkraise()
            else:
                t1f2.config(bg="red", fg="white")
                t1f2.place(x=320, y=270)
                t1f2.tkraise()
            t1m1_var.set(int(am0_var.get()) + random.choice(pform))
            if t1m1_var.get() >= am0_var.get():
                t1m1.config(bg="green", fg="white")
                t1m1.place(x=200, y=395)
                t1m1.tkraise()
            else:
                t1m1.config(bg="red", fg="white")
                t1m1.place(x=200, y=395)
                t1m1.tkraise()
            t1m2_var.set(int(am1_var.get()) + random.choice(pform))
            if t1m2_var.get() >= am1_var.get():
                t1m2.config(bg="green", fg="white")
                t1m2.place(x=260, y=395)
                t1m2.tkraise()
            else:
                t1m2.config(bg="red", fg="white")
                t1m2.place(x=260, y=395)
                t1m2.tkraise()
            t1m3_var.set(int(am2_var.get()) + random.choice(pform))
            if t1m3_var.get() >= am2_var.get():
                t1m3.config(bg="green", fg="white")
                t1m3.place(x=320, y=395)
                t1m3.tkraise()
            else:
                t1m3.config(bg="red", fg="white")
                t1m3.place(x=320, y=395)
                t1m3.tkraise()
            t1d1_var.set(int(ad0_var.get()) + random.choice(pform))
            if t1d1_var.get() >= ad0_var.get():
                t1d1.config(bg="green", fg="white")
                t1d1.place(x=150, y=458)
                t1d1.tkraise()
            else:
                t1d1.config(bg="red", fg="white")
                t1d1.place(x=150, y=458)
                t1d1.tkraise()
            t1d2_var.set(int(ad1_var.get()) + random.choice(pform))
            if t1d2_var.get() >= ad1_var.get():
                t1d2.config(bg="green", fg="white")
                t1d2.place(x=200, y=520)
                t1d2.tkraise()
            else:
                t1d2.config(bg="red", fg="white")
                t1d2.place(x=200, y=520)
                t1d2.tkraise()
            t1d3_var.set(int(ad2_var.get()) + random.choice(pform))
            if t1d3_var.get() >= ad2_var.get():
                t1d3.config(bg="green", fg="white")
                t1d3.place(x=260, y=520)
                t1d3.tkraise()
            else:
                t1d3.config(bg="red", fg="white")
                t1d3.place(x=260, y=520)
                t1d3.tkraise()
            t1d4_var.set(int(ad3_var.get()) + random.choice(pform))
            if t1d4_var.get() >= ad3_var.get():
                t1d4.config(bg="green", fg="white")
                t1d4.place(x=320, y=520)
                t1d4.tkraise()
            else:
                t1d4.config(bg="red", fg="white")
                t1d4.place(x=320, y=520)
                t1d4.tkraise()
            t1d5_var.set(int(ad4_var.get()) + random.choice(pform))
            if t1d5_var.get() >= ad4_var.get():
                t1d5.config(bg="green", fg="white")
                t1d5.place(x=370, y=458)
                t1d5.tkraise()
            else:
                t1d5.config(bg="red", fg="white")
                t1d5.place(x=370, y=458)
                t1d5.tkraise()
            t1gk_var.set(int(ag0_var.get()) + random.choice(pform))
            if t1gk_var.get() >= ag0_var.get():
                t1gk.config(bg="green", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
            else:
                t1gk.config(bg="red", fg="white")
                t1gk.place(x=260, y=610)
                t1gk.tkraise()
        if t2a == 3 and t2m == 3 and t2d == 5:
            t2f1_var.set(int(bf0_var.get()) + random.choice(pform))
            if t2f1_var.get() >= bf0_var.get():
                t2f1.config(bg="green", fg="white")
                t2f1.place(x=1500, y=270)
                t2f1.tkraise()
            else:
                t2f1.config(bg="red", fg="white")
                t2f1.place(x=1500, y=270)
                t2f1.tkraise()
            t2f2_var.set(int(bf1_var.get()) + random.choice(pform))
            if t2f2_var.get() >= bf1_var.get():
                t2f2.config(bg="green", fg="white")
                t2f2.place(x=1560, y=270)
                t2f2.tkraise()
            else:
                t2f2.config(bg="red", fg="white")
                t2f2.place(x=1560, y=270)
                t2f2.tkraise()
            t2f3_var.set(int(bf2_var.get()) + random.choice(pform))
            if t2f3_var.get() >= bf2_var.get():
                t2f3.config(bg="green", fg="white")
                t2f3.place(x=1620, y=270)
                t2f3.tkraise()
            else:
                t2f3.config(bg="red", fg="white")
                t2f3.place(x=1620, y=270)
                t2f3.tkraise()
            t2m1_var.set(int(bm0_var.get()) + random.choice(pform))
            if t2m1_var.get() >= bm0_var.get():
                t2m1.config(bg="green", fg="white")
                t2m1.place(x=1500, y=395)
                t2m1.tkraise()
            else:
                t2m1.config(bg="red", fg="white")
                t2m1.place(x=1500, y=395)
                t2m1.tkraise()
            t2m2_var.set(int(bm1_var.get()) + random.choice(pform))
            if t2m2_var.get() >= bm1_var.get():
                t2m2.config(bg="green", fg="white")
                t2m2.place(x=1560, y=395)
                t2m2.tkraise()
            else:
                t2m2.config(bg="red", fg="white")
                t2m2.place(x=1560, y=395)
                t2m2.tkraise()
            t2m3_var.set(int(bm2_var.get()) + random.choice(pform))
            if t2m3_var.get() >= bm2_var.get():
                t2m3.config(bg="green", fg="white")
                t2m3.place(x=1620, y=395)
                t2m3.tkraise()
            else:
                t2m3.config(bg="red", fg="white")
                t2m3.place(x=1620, y=395)
                t2m3.tkraise()
            t2d1_var.set(int(bd0_var.get()) + random.choice(pform))
            if t2d1_var.get() >= bd0_var.get():
                t2d1.config(bg="green", fg="white")
                t2d1.place(x=1450, y=520)
                t2d1.tkraise()
            else:
                t2d1.config(bg="red", fg="white")
                t2d1.place(x=1450, y=520)
                t2d1.tkraise()
            t2d2_var.set(int(bd1_var.get()) + random.choice(pform))
            if t2d2_var.get() >= bd1_var.get():
                t2d2.config(bg="green", fg="white")
                t2d2.place(x=1530, y=520)
                t2d2.tkraise()
            else:
                t2d2.config(bg="red", fg="white")
                t2d2.place(x=1530, y=520)
                t2d2.tkraise()
            t2d3_var.set(int(bd2_var.get()) + random.choice(pform))
            if t2d3_var.get() >= bd2_var.get():
                t2d3.config(bg="green", fg="white")
                t2d3.place(x=1590, y=520)
                t2d3.tkraise()
            else:
                t2d3.config(bg="red", fg="white")
                t2d3.place(x=1590, y=520)
                t2d3.tkraise()
            t2d4_var.set(int(bd3_var.get()) + random.choice(pform))
            if t2d4_var.get() >= bd3_var.get():
                t2d4.config(bg="green", fg="white")
                t2d4.place(x=1670, y=520)
                t2d4.tkraise()
            else:
                t2d4.config(bg="red", fg="white")
                t2d4.place(x=1670, y=520)
                t2d4.tkraise()
            t2gk_var.set(int(bg0_var.get()) + random.choice(pform))
            if t2gk_var.get() >= bg0_var.get():
                t2gk.config(bg="green", fg="white")
                t2gk.place(x=1560, y=610)
                t2gk.tkraise()
            else:
                t2gk.config(bg="red", fg="white")
                t2gk.place(x=1560, y=610)
                t2gk.tkraise()
            bupdate_avg_433()
        if t2a == 1 and t2m == 5 and t2d == 5:
            t2f1_var.set(int(bf1_var.get()) + random.choice(pform))
            if t2f1_var.get() >= bf1_var.get():
                t2f1.config(bg="green", fg="white")
                t2f1.place(x=1560, y=270)
                t2f1.tkraise()
            else:
                t2f1.config(bg="red", fg="white")
                t2f1.place(x=1560, y=270)
                t2f1.tkraise()
            t2m1_var.set(int(bm0_var.get()) + random.choice(pform))
            if t2m1_var.get() >= bm0_var.get():
                t2m1.config(bg="green", fg="white")
                t2m1.place(x=1450, y=338)
                t2m1.tkraise()
            else:
                t2m1.config(bg="red", fg="white")
                t2m1.place(x=1450, y=338)
                t2m1.tkraise()
            t2m2_var.set(int(bm1_var.get()) + random.choice(pform))
            if t2m2_var.get() >= bm1_var.get():
                t2m2.config(bg="green", fg="white")
                t2m2.place(x=1530, y=338)
                t2m2.tkraise()
            else:
                t2m2.config(bg="red", fg="white")
                t2m2.place(x=1530, y=338)
                t2m2.tkraise()
            t2m3_var.set(int(bm2_var.get()) + random.choice(pform))
            if t2m3_var.get() >= bm2_var.get():
                t2m3.config(bg="green", fg="white")
                t2m3.place(x=1590, y=338)
                t2m3.tkraise()
            else:
                t2m3.config(bg="red", fg="white")
                t2m3.place(x=1590, y=338)
                t2m3.tkraise()
            t2m4_var.set(int(bm3_var.get()) + random.choice(pform))
            if t2m4_var.get() >= bm3_var.get():
                t2m4.config(bg="green", fg="white")
                t2m4.place(x=1670, y=338)
                t2m4.tkraise()
            else:
                t2m4.config(bg="red", fg="white")
                t2m4.place(x=1670, y=338)
                t2m4.tkraise()
            t2d1_var.set(int(bd0_var.get()) + random.choice(pform))
            if t2d1_var.get() >= bd0_var.get():
                t2d1.config(bg="green", fg="white")
                t2d1.place(x=1450, y=520)
                t2d1.tkraise()
            else:
                t2d1.config(bg="red", fg="white")
                t2d1.place(x=1450, y=520)
                t2d1.tkraise()
            t2d2_var.set(int(bd1_var.get()) + random.choice(pform))
            if t2d2_var.get() >= bd1_var.get():
                t2d2.config(bg="green", fg="white")
                t2d2.place(x=1530, y=520)
                t2d2.tkraise()
            else:
                t2d2.config(bg="red", fg="white")
                t2d2.place(x=1530, y=520)
                t2d2.tkraise()
            t2d3_var.set(int(bd2_var.get()) + random.choice(pform))
            if t2d3_var.get() >= bd2_var.get():
                t2d3.config(bg="green", fg="white")
                t2d3.place(x=1590, y=520)
                t2d3.tkraise()
            else:
                t2d3.config(bg="red", fg="white")
                t2d3.place(x=1590, y=520)
                t2d3.tkraise()
            t2d4_var.set(int(bd3_var.get()) + random.choice(pform))
            if t2d4_var.get() >= bd3_var.get():
                t2d4.config(bg="green", fg="white")
                t2d4.place(x=1670, y=5120)
                t2d4.tkraise()
            else:
                t2d4.config(bg="red", fg="white")
                t2d4.place(x=1670, y=520)
                t2d4.tkraise()
            t2gk_var.set(int(bg0_var.get()) + random.choice(pform))
            if t2gk_var.get() >= bg0_var.get():
                t2gk.config(bg="green", fg="white")
                t2gk.place(x=1560, y=610)
                t2gk.tkraise()
            else:
                t2gk.config(bg="red", fg="white")
                t2gk.place(x=1560, y=610)
                t2gk.tkraise()
            
    else:
        messagebox.showerror("Error", "Please freeze all player ratings. Make sure all player values are filled.")

def clearsim():
    t1f1.place_forget()
    t1f2.place_forget()
    t1f3.place_forget()
    t1m1.place_forget()
    t1m2.place_forget()
    t1m3.place_forget()
    t1m4.place_forget()
    t1m5.place_forget()
    t1d1.place_forget()
    t1d2.place_forget()
    t1d3.place_forget()
    t1d4.place_forget()
    t1d5.place_forget()
    t1gk.place_forget()
    t2f1.place_forget()
    t2f2.place_forget()
    t2f3.place_forget()
    t2m1.place_forget()
    t2m2.place_forget()
    t2m3.place_forget()
    t2m4.place_forget()
    t2m5.place_forget()
    t2d1.place_forget()
    t2d2.place_forget()
    t2d3.place_forget()
    t2d4.place_forget()
    t2d5.place_forget()
    t2gk.place_forget()
                
def changeform1(*args):
    global t1a
    global t1m
    global t1d
    resetrate1()
    if str(formations1.get()) == "4-3-3":
        t1a = 3
        t1m = 3
        t1d = 5
        hiderat1()
        af0.place(x=200, y=250)
        af1.place(x=260, y=250)
        af2.place(x=320, y=250)
        am0.place(x=200, y=375)
        am1.place(x=260, y=375)
        am2.place(x=320, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
        ag0.place(x=260, y=590)
        
    if str(formations1.get()) == "4-2-3-1":
        t1a = 1
        t1m = 5
        t1d = 5
        hiderat1()
        af1.place(x=260, y=250)
        am0.place(x=150, y=318)
        am1.place(x=260, y=318)
        am2.place(x=370, y=318)
        am3.place(x=230, y=375)
        am4.place(x=290, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
        ag0.place(x=260, y=590)
    
    if str(formations1.get()) == "4-4-2":
        t1a = 2
        t1m = 4
        t1d = 5
        hiderat1()
        af0.place(x=200, y=250)
        af2.place(x=320, y=250)
        am0.place(x=150, y=375)
        am1.place(x=230, y=375)
        am2.place(x=290, y=375)
        am3.place(x=370, y=375)
        ad0.place(x=150, y=500)
        ad1.place(x=230, y=500)
        ad2.place(x=290, y=500)
        ad3.place(x=370, y=500)
        ag0.place(x=260, y=590)
    
    if str(formations1.get()) == "3-4-3":
        t1a = 3
        t1m = 4
        t1d = 4
        hiderat1()
        af0.place(x=200, y=250)
        af1.place(x=260, y=250)
        af2.place(x=320, y=250)
        am0.place(x=150, y=375)
        am1.place(x=230, y=375)
        am2.place(x=290, y=375)
        am3.place(x=370, y=375)
        ad0.place(x=200, y=500)
        ad1.place(x=260, y=500)
        ad2.place(x=320, y=500)
        ag0.place(x=260, y=590)
    
    if str(formations1.get()) == "5-3-2":
        t1a = 2
        t1m = 3
        t1d = 6
        hiderat1()
        af0.place(x=200, y=250)
        af2.place(x=320, y=250)
        am0.place(x=200, y=375)
        am1.place(x=260, y=375)
        am2.place(x=320, y=375)
        ad0.place(x=150, y=438)
        ad1.place(x=200, y=500)
        ad2.place(x=260, y=500)
        ad3.place(x=320, y=500)
        ad4.place(x=370, y=438)
        ag0.place(x=260, y=590)

def changeform2(*args):
    global t2a
    global t2m
    global t2d
    resetrate2()
    if str(formations2.get()) == "4-3-3":
        t2a = 3
        t2m = 3
        t2d = 5
        hiderat2()
        bf0.place(x=1500, y=250)
        bf1.place(x=1560, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1500, y=375)
        bm1.place(x=1560, y=375)
        bm2.place(x=1620, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1530, y=500)
        bd2.place(x=1590, y=500)
        bd3.place(x=1670, y=500)
        bg0.place(x=1560, y=590)
        
    if str(formations2.get()) == "4-2-3-1":
        t2a = 1
        t2m = 5
        t2d = 5
        hiderat2()
        bf1.place(x=1560, y=250)
        bm0.place(x=1440, y=318)
        bm1.place(x=1560, y=318)
        bm2.place(x=1670, y=318)
        bm3.place(x=1530, y=375)
        bm4.place(x=1590, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1530, y=500)
        bd2.place(x=1590, y=500)
        bd3.place(x=1670, y=500)
        bg0.place(x=1560, y=590)
    
    if str(formations2.get()) == "4-4-2":
        t2a = 2
        t2m = 4
        t2d = 5
        hiderat2()
        bf0.place(x=1500, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1450, y=375)
        bm1.place(x=1530, y=375)
        bm2.place(x=1590, y=375)
        bm3.place(x=1670, y=375)
        bd0.place(x=1450, y=500)
        bd1.place(x=1530, y=500)
        bd2.place(x=1590, y=500)
        bd3.place(x=1670, y=500)
        bg0.place(x=1560, y=590)
    
    if str(formations2.get()) == "3-4-3":
        t2a = 3
        t2m = 4
        t2d = 4
        hiderat2()
        bf0.place(x=1500, y=250)
        bf1.place(x=1560, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1450, y=375)
        bm1.place(x=1530, y=375)
        bm2.place(x=1590, y=375)
        bm3.place(x=1670, y=375)
        bd0.place(x=1500, y=500)
        bd1.place(x=1560, y=500)
        bd2.place(x=1620, y=500)
        bg0.place(x=1560, y=590)
    
    if str(formations2.get()) == "5-3-2":
        t2a = 2
        t2m = 3
        t2d = 6
        hiderat2()
        bf0.place(x=1500, y=250)
        bf2.place(x=1620, y=250)
        bm0.place(x=1500, y=375)
        bm1.place(x=1560, y=375)
        bm2.place(x=1620, y=375)
        bd0.place(x=1450, y=438)
        bd1.place(x=1500, y=500)
        bd2.place(x=1560, y=500)
        bd3.place(x=1620, y=500)
        bd4.place(x=1670, y=438)
        bg0.place(x=1560, y=590)

def clearfield1():
    field1.place_forget()
    afield1.place_forget()
    bfield1.place_forget()
    dfield1.place_forget()

def t1attack():
    global t1strat
    t1strat = 3
    clearfield1()
    afield1.place(x=100, y=150)
def t1balance():
    global t1strat
    t1strat = 2
    clearfield1()
    bfield1.place(x=100, y=150)
def t1defend():
    global t1strat
    t1strat = 1
    clearfield1()
    dfield1.place(x=100, y=150)
def t1dyn():
    global t1strat
    t1strat = 0
    clearfield1()
    field1.place(x=100, y=150)
    
def clearfield2():
    field2.place_forget()
    afield2.place_forget()
    bfield2.place_forget()
    dfield2.place_forget()

def t2attack():
    global t2strat
    t2strat = 3
    clearfield2()
    afield2.place(x=1080, y=150)
def t2balance():
    global t2strat
    t2strat = 2
    clearfield2()
    bfield2.place(x=1080, y=150)
def t2defend():
    global t2strat
    t2strat = 1
    clearfield2()
    dfield2.place(x=1080, y=150)
def t2dyn():
    global t2strat
    t2strat = 0
    clearfield2()
    field2.place(x=1080, y=150)
def Randomfill1():
    if t1a == 3 and t1m == 3 and t1d == 5:
        af0_var.set(random.choice(randratings))
        af1_var.set(random.choice(randratings))
        af2_var.set(random.choice(randratings))
        am0_var.set(random.choice(randratings))
        am1_var.set(random.choice(randratings))
        am2_var.set(random.choice(randratings))
        ad0_var.set(random.choice(randratings))
        ad1_var.set(random.choice(randratings))
        ad2_var.set(random.choice(randratings))
        ad3_var.set(random.choice(randratings))
        ag0_var.set(random.choice(randratings))
    if t1a == 1 and t1m == 5 and t1d == 5:
        af1_var.set(random.choice(randratings))
        am0_var.set(random.choice(randratings))
        am1_var.set(random.choice(randratings))
        am2_var.set(random.choice(randratings))
        am3_var.set(random.choice(randratings))
        am4_var.set(random.choice(randratings))
        ad0_var.set(random.choice(randratings))
        ad1_var.set(random.choice(randratings))
        ad2_var.set(random.choice(randratings))
        ad3_var.set(random.choice(randratings))
        ag0_var.set(random.choice(randratings))
    if t1a == 2 and t1m == 4 and t1d == 5:
        af0_var.set(random.choice(randratings))
        af2_var.set(random.choice(randratings))
        am0_var.set(random.choice(randratings))
        am1_var.set(random.choice(randratings))
        am2_var.set(random.choice(randratings))
        am3_var.set(random.choice(randratings))
        ad0_var.set(random.choice(randratings))
        ad1_var.set(random.choice(randratings))
        ad2_var.set(random.choice(randratings))
        ad3_var.set(random.choice(randratings))
        ag0_var.set(random.choice(randratings))
    if t1a == 3 and t1m == 4 and t1d == 4:
        af0_var.set(random.choice(randratings))
        af1_var.set(random.choice(randratings))
        af2_var.set(random.choice(randratings))
        am0_var.set(random.choice(randratings))
        am1_var.set(random.choice(randratings))
        am2_var.set(random.choice(randratings))
        am3_var.set(random.choice(randratings))
        ad0_var.set(random.choice(randratings))
        ad1_var.set(random.choice(randratings))
        ad2_var.set(random.choice(randratings))
        ag0_var.set(random.choice(randratings))
    if t1a == 2 and t1m == 3 and t1d == 6:
        af0_var.set(random.choice(randratings))
        af2_var.set(random.choice(randratings))
        am0_var.set(random.choice(randratings))
        am1_var.set(random.choice(randratings))
        am2_var.set(random.choice(randratings))
        ad0_var.set(random.choice(randratings))
        ad1_var.set(random.choice(randratings))
        ad2_var.set(random.choice(randratings))
        ad3_var.set(random.choice(randratings))
        ad4_var.set(random.choice(randratings))
        ag0_var.set(random.choice(randratings))
    updatestar1()
def Randomfill2():
    if t2a == 3 and t2m == 3 and t2d == 5:
        bf0_var.set(random.choice(randratings))
        bf1_var.set(random.choice(randratings))
        bf2_var.set(random.choice(randratings))
        bm0_var.set(random.choice(randratings))
        bm1_var.set(random.choice(randratings))
        bm2_var.set(random.choice(randratings))
        bd0_var.set(random.choice(randratings))
        bd1_var.set(random.choice(randratings))
        bd2_var.set(random.choice(randratings))
        bd3_var.set(random.choice(randratings))
        bg0_var.set(random.choice(randratings))
    if t2a == 1 and t2m == 5 and t2d == 5:
        bf1_var.set(random.choice(randratings))
        bm0_var.set(random.choice(randratings))
        bm1_var.set(random.choice(randratings))
        bm2_var.set(random.choice(randratings))
        bm3_var.set(random.choice(randratings))
        bm4_var.set(random.choice(randratings))
        bd0_var.set(random.choice(randratings))
        bd1_var.set(random.choice(randratings))
        bd2_var.set(random.choice(randratings))
        bd3_var.set(random.choice(randratings))
        bg0_var.set(random.choice(randratings))
    if t2a == 2 and t2m == 4 and t2d == 5:
        bf0_var.set(random.choice(randratings))
        bf2_var.set(random.choice(randratings))
        bm0_var.set(random.choice(randratings))
        bm1_var.set(random.choice(randratings))
        bm2_var.set(random.choice(randratings))
        bm3_var.set(random.choice(randratings))
        bd0_var.set(random.choice(randratings))
        bd1_var.set(random.choice(randratings))
        bd2_var.set(random.choice(randratings))
        bd3_var.set(random.choice(randratings))
        bg0_var.set(random.choice(randratings))
    if t2a == 3 and t2m == 4 and t2d == 4:
        bf0_var.set(random.choice(randratings))
        bf1_var.set(random.choice(randratings))
        bf2_var.set(random.choice(randratings))
        bm0_var.set(random.choice(randratings))
        bm1_var.set(random.choice(randratings))
        bm2_var.set(random.choice(randratings))
        bm3_var.set(random.choice(randratings))
        bd0_var.set(random.choice(randratings))
        bd1_var.set(random.choice(randratings))
        bd2_var.set(random.choice(randratings))
        bg0_var.set(random.choice(randratings))
    if t2a == 2 and t2m == 3 and t2d == 6:
        bf0_var.set(random.choice(randratings))
        bf2_var.set(random.choice(randratings))
        bm0_var.set(random.choice(randratings))
        bm1_var.set(random.choice(randratings))
        bm2_var.set(random.choice(randratings))
        bd0_var.set(random.choice(randratings))
        bd1_var.set(random.choice(randratings))
        bd2_var.set(random.choice(randratings))
        bd3_var.set(random.choice(randratings))
        bd4_var.set(random.choice(randratings))
        bg0_var.set(random.choice(randratings))
    updatestar2()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

    

# START
welcome = Label(root, text="FOOTSIM -- A tool created to predict football matches.*", font=genfont)
condapply = Label(root, text="*Conditions apply: This is in no way an accurate way to predict such affairs, this is made purely for fun.", font=smolfont)
startbutton = Button(root, text="Continue", font=genfont, command=Continue1)
start()

# CONTINUE/INITIALIZE MENUS
main = Menu(menubar, tearoff=0)
main.add_command(label="Simulate", command=Continue2)
options = Menu(menubar, tearoff=0)
options.add_command(label="Settings", command=settings)
options.add_command(label="Quit", command=quit)
options.add_command(label="Restart", command=restart_program)
iniprog = Button(root, text="Initialize", font=genfont, command=initialize)

# SETTINGS
disp_simlgh_var = StringVar()
disp_simlgh_var.set(simlgh)
disp_simlgh = Label(root, textvariable=disp_simlgh_var, font=smolfont)
simlgh1 = Radiobutton(root, text="3-off Simulation", command=simlength1, value=0)
simlgh2 = Radiobutton(root, text="5-off Simulation", command=simlength2, value=1)
simlgh3 = Radiobutton(root, text="10-off Simulation", command=simlength3, value=2)
sim_length = Label(root, text="Simulation Length", font=genfont)

# SIMSPACE
enteam1 = EntryWithPlaceholder(root, "ENTER TEAM 1 NAME")
enteam2 = EntryWithPlaceholder(root, "ENTER TEAM 2 NAME")
getteam1 = Button(root, text="SET", command=setteam1)
getteam2 = Button(root, text="SET", command=setteam2)
t1name_var = StringVar()
t2name_var = StringVar()
t1name_var.set(t1name)
t2name_var.set(t2name)
team1 = Label(root, textvariable=t1name_var, font=biggfont)
team2 = Label(root, textvariable=t2name_var, font=biggfont)
att1 = Label(root, text="ATTACK:", font=genfont)
mid1 = Label(root, text="MIDFIELD:", font=genfont)
def1 = Label(root, text="DEFENSE:", font=genfont)
att2 = Label(root, text="ATTACK:", font=genfont)
mid2 = Label(root, text="MIDFIELD:", font=genfont)
def2 = Label(root, text="DEFENSE:", font=genfont)
freeze1_var = StringVar()
freeze1_var.set("FREEZE")
Freeze1 = Button(root, textvariable=freeze1_var, command=freeze1, width=8)
freeze2_var = StringVar()
freeze2_var.set("FREEZE")
Freeze2 = Button(root, textvariable=freeze2_var, command=freeze2, width=8)
simulate = Button(root, text="SIMULATE", command=Simulate, font=ratefont)
formations1 = StringVar()
formations1.set("4-3-3")
selformations1 = ttk.Combobox(root, textvariable=formations1, values=FORMATIONS, state= "readonly")
selformations1.bind("<<ComboboxSelected>>", changeform1)
formations2 = StringVar()
formations2.set("4-3-3")
selformations2 = ttk.Combobox(root, textvariable=formations2, values=FORMATIONS, state= "readonly")
selformations2.bind("<<ComboboxSelected>>", changeform2)
switch_variable = tk.StringVar(value="off")
bswitch_variable = tk.StringVar(value="off")

dynamic_button = tk.Radiobutton(root, text="Dynamic", variable=switch_variable, indicatoron=True, value="off", width=6, command=t1dyn, bg="gray")
defend_button = tk.Radiobutton(root, text="Defensive", variable=switch_variable, indicatoron=True, value="low", width=6, command=t1defend, bg="Green")
balanced_button = tk.Radiobutton(root, text="Balanced", variable=switch_variable, indicatoron=True, value="medium", width=6, command=t1balance, bg="Yellow")
attack_button = tk.Radiobutton(root, text="Attacking", variable=switch_variable, indicatoron=True, value="high", width=6, command=t1attack, bg="Orange")

bdynamic_button = tk.Radiobutton(root, text="Dynamic", variable=bswitch_variable, indicatoron=True, value="off", width=6, bg="gray", command=t2dyn)
bdefend_button = tk.Radiobutton(root, text="Defensive", variable=bswitch_variable, indicatoron=True, value="low", width=6, bg="Green", command=t2defend)
bbalanced_button = tk.Radiobutton(root, text="Balanced", variable=bswitch_variable, indicatoron=True, value="medium", width=6, bg="Yellow", command=t2balance)
battack_button = tk.Radiobutton(root, text="Attacking", variable=bswitch_variable, indicatoron=True, value="high", width=6, bg="Orange", command=t2attack)

reset1 = Button(root, text="RESET", command=resetrate1, font=smolfont, width=56)
reset2 = Button(root, text="RESET", command=resetrate2, font=smolfont, width=56)
randomfill1 = Button(root, text="RANDOMIZE", command=Randomfill1, font=smolfont, width=56)
randomfill2 = Button(root, text="RANDOMIZE", command=Randomfill2, font=smolfont, width=56)
pp_var = StringVar()
pp_var.set("bigg pp vs smol pp")
pp = Entry(root, textvariable=pp_var, state="disable")

###PLAY

t1f1_var = StringVar() 
t1f1_var.set("")
t1f1 = Entry(root, textvariable=t1f1_var, width=3)
t1f2_var = StringVar()
t1f2_var.set("")
t1f2 = Entry(root, textvariable=t1f2_var, width=3)
t1f3_var = StringVar()
t1f3_var.set("")
t1f3 = Entry(root, textvariable=t1f3_var, width=3)
aupdfwdavg_var = StringVar()
aupdfwdavg_var.set("")
aupdfwdavg = Label(root, textvariable=aupdfwdavg_var, font=genfont, width=5)

t1m1_var = StringVar()
t1m1_var.set("")
t1m1 = Entry(root, textvariable=t1m1_var, width=3)
t1m2_var = StringVar()
t1m2_var.set("")
t1m2 = Entry(root, textvariable=t1m2_var, width=3)
t1m3_var = StringVar()
t1m3_var.set("")
t1m3 = Entry(root, textvariable=t1m3_var, width=3)
t1m4_var = StringVar()
t1m4_var.set("")
t1m4 = Entry(root, textvariable=t1m4_var, width=3)
t1m5_var = StringVar()
t1m5_var.set("")
t1m5 = Entry(root, textvariable=t1m5_var, width=3)
aupdmidavg_var = StringVar()
aupdmidavg_var.set("")
aupdmidavg = Label(root, textvariable=aupdmidavg_var, font=genfont, width=5)

t1d1_var = StringVar()
t1d1_var.set("")
t1d1 = Entry(root, textvariable=t1d1_var, width=3)
t1d2_var = StringVar()
t1d2_var.set("")
t1d2 = Entry(root, textvariable=t1d2_var, width=3)
t1d3_var = StringVar()
t1d3_var.set("")
t1d3 = Entry(root, textvariable=t1d3_var, width=3)
t1d4_var = StringVar()
t1d4_var.set("")
t1d4 = Entry(root, textvariable=t1d4_var, width=3)
t1d5_var = StringVar()
t1d5_var.set("")
t1d5 = Entry(root, textvariable=t1d5_var, width=3)

t1gk_var = StringVar()
t1gk_var.set("")
t1gk = Entry(root, textvariable=t1gk_var, width=3)
aupddfavg_var = StringVar()
aupddfavg_var.set("")
aupddfavg = Label(root, textvariable=aupddfavg_var, font=genfont, width=5)


t2f1_var = StringVar()
t2f1_var.set("")
t2f1 = Entry(root, textvariable=t2f1_var, width=3)
t2f2_var = StringVar()
t2f2_var.set("")
t2f2 = Entry(root, textvariable=t2f2_var, width=3)
t2f3_var = StringVar()
t2f3_var.set("")
t2f3 = Entry(root, textvariable=t2f3_var, width=3)
bupdfwdavg_var = StringVar()
bupdfwdavg_var.set("")
bupdfwdavg = Label(root, textvariable=bupdfwdavg_var, font=genfont, width=5)

t2m1_var = StringVar()
t2m1_var.set("")
t2m1 = Entry(root, textvariable=t2m1_var, width=3)
t2m2_var = StringVar()
t2m2_var.set("")
t2m2 = Entry(root, textvariable=t2m2_var, width=3)
t2m3_var = StringVar()
t2m3_var.set("")
t2m3 = Entry(root, textvariable=t2m3_var, width=3)
t2m4_var = StringVar()
t2m4_var.set("")
t2m4 = Entry(root, textvariable=t2m4_var, width=3)
t2m5_var = StringVar()
t2m5_var.set("")
t2m5 = Entry(root, textvariable=t2m5_var, width=3)
bupdmdavg_var = StringVar()
bupdmdavg_var.set("")
bupdmdavg = Label(root, textvariable=bupdmdavg_var, font=genfont, width=5)

t2d1_var = StringVar()
t2d1_var.set("")
t2d1 = Entry(root, textvariable=t2d1_var, width=3)
t2d2_var = StringVar()
t2d2_var.set("")
t2d2 = Entry(root, textvariable=t2d2_var, width=3)
t2d3_var = StringVar()
t2d3_var.set("")
t2d3 = Entry(root, textvariable=t2d3_var, width=3)
t2d4_var = StringVar()
t2d4_var.set("")
t2d4 = Entry(root, textvariable=t2d4_var, width=3)
t2d5_var = StringVar()
t2d5_var.set("")
t2d5 = Entry(root, textvariable=t2d5_var, width=3)
bupddfavg_var = StringVar()
bupddfavg_var.set("")
bupddfavg = Label(root, textvariable=bupddfavg_var, font=genfont, width=5)

t2gk_var = StringVar()
t2gk_var.set("")
t2gk = Entry(root, textvariable=t2gk_var, width=3)



####IMAGES1
fieldimg1 = Image.open(fieldpath)
fieldimg1 = fieldimg1.resize((340, 481))
fieldimage1 = ImageTk.PhotoImage(fieldimg1)
field1 = Label(root, image=fieldimage1)
fieldimg2 = Image.open(fieldpath)
fieldimg2 = fieldimg2.resize((340, 481))
fieldimage2 = ImageTk.PhotoImage(fieldimg2)
field2 = Label(root, image=fieldimage2)
dfieldimg1 = Image.open(dfieldpath)
dfieldimg1 = dfieldimg1.resize((340, 481))
dfieldimage1 = ImageTk.PhotoImage(dfieldimg1)
dfield1 = Label(root, image=dfieldimage1)
dfieldimg2 = Image.open(dfieldpath)
dfieldimg2 = dfieldimg2.resize((340, 481))
dfieldimage2 = ImageTk.PhotoImage(dfieldimg2)
dfield2 = Label(root, image=dfieldimage2)
afieldimg1 = Image.open(afieldpath)
afieldimg1 = afieldimg1.resize((340, 481))
afieldimage1 = ImageTk.PhotoImage(afieldimg1)
afield1 = Label(root, image=afieldimage1)
afieldimg2 = Image.open(afieldpath)
afieldimg2 = afieldimg2.resize((340, 481))
afieldimage2 = ImageTk.PhotoImage(afieldimg2)
afield2 = Label(root, image=afieldimage2)
bfieldimg1 = Image.open(bfieldpath)
bfieldimg1 = bfieldimg1.resize((340, 481))
bfieldimage1 = ImageTk.PhotoImage(bfieldimg1)
bfield1 = Label(root, image=bfieldimage1)
bfieldimg2 = Image.open(bfieldpath)
bfieldimg2 = bfieldimg2.resize((340, 481))
bfieldimage2 = ImageTk.PhotoImage(bfieldimg2)
bfield2 = Label(root, image=bfieldimage2)


str1path = f'/home/wafiq/Downloads/star/0.1.png'
str1image = Image.open(str1path)
strlimage = str1image.resize((500, 500))
str1 = ImageTk.PhotoImage(str1image)
t1star0 = Label(root, image=str1)
t1str5path = f'/home/wafiq/Downloads/star/5.png'
t1str5image = Image.open(t1str5path)
t1str5 = ImageTk.PhotoImage(t1str5image)
t1star5 = Label(root, image=t1str5)
t1star45path = f'/home/wafiq/Downloads/star/4.5.png'
t1star45image = Image.open(t1star45path)
t1str45 = ImageTk.PhotoImage(t1star45image)
t1star45 = Label(root, image=t1str45)
t1star4path = f'/home/wafiq/Downloads/star/4.png'
t1star4image = Image.open(t1star4path)
t1str4 = ImageTk.PhotoImage(t1star4image)
t1star4 = Label(root, image=t1str4)
t1star35path = f'/home/wafiq/Downloads/star/3.5.png'
t1star35image = Image.open(t1star35path)
t1str35 = ImageTk.PhotoImage(t1star35image)
t1star35 = Label(root, image=t1str35)
t1star3path = f'/home/wafiq/Downloads/star/3.png'
t1star3image = Image.open(t1star3path)
t1str3 = ImageTk.PhotoImage(t1star3image)
t1star3 = Label(root, image=t1str3)
t1star25path = f'/home/wafiq/Downloads/star/2.5.png'
t1star25image = Image.open(t1star25path)
t1str25 = ImageTk.PhotoImage(t1star25image)
t1star25 = Label(root, image=t1str25)
t1star2path = f'/home/wafiq/Downloads/star/2.png'
t1star2image = Image.open(t1star2path)
t1str2 = ImageTk.PhotoImage(t1star2image)
t1star2 = Label(root, image=t1str2)
t1star15path = f'/home/wafiq/Downloads/star/1.5.png'
t1star15image = Image.open(t1star15path)
t1str15 = ImageTk.PhotoImage(t1star15image)
t1star15 = Label(root, image=t1str15)
t1star1path = f'/home/wafiq/Downloads/star/1.png'
t1star1image = Image.open(t1star1path)
t1str1 = ImageTk.PhotoImage(t1star1image)
t1star1 = Label(root, image=t1str1)
t1star05path = f'/home/wafiq/Downloads/star/0.5.png'
t1star05image = Image.open(t1star05path)
t1str05 = ImageTk.PhotoImage(t1star05image)
t1star05 = Label(root, image=t1str05)
####
#####IMAGES2
t2star0 = Label(root, image=str1)
t2str5path = f'/home/wafiq/Downloads/star/5.png'
t2str5image = Image.open(t2str5path)
t2str5 = ImageTk.PhotoImage(t2str5image)
t2star5 = Label(root, image=t2str5)
t2star45path = f'/home/wafiq/Downloads/star/4.5.png'
t2star45image = Image.open(t2star45path)
t2str45 = ImageTk.PhotoImage(t2star45image)
t2star45 = Label(root, image=t2str45)
t2star4path = f'/home/wafiq/Downloads/star/4.png'
t2star4image = Image.open(t2star4path)
t2str4 = ImageTk.PhotoImage(t2star4image)
t2star4 = Label(root, image=t2str4)
t2star35path = f'/home/wafiq/Downloads/star/3.5.png'
t2star35image = Image.open(t2star35path)
t2str35 = ImageTk.PhotoImage(t2star35image)
t2star35 = Label(root, image=t2str35)
t2star3path = f'/home/wafiq/Downloads/star/3.png'
t2star3image = Image.open(t2star3path)
t2str3 = ImageTk.PhotoImage(t2star3image)
t2star3 = Label(root, image=t2str3)
t2star25path = f'/home/wafiq/Downloads/star/2.5.png'
t2star25image = Image.open(t2star25path)
t2str25 = ImageTk.PhotoImage(t2star25image)
t2star25 = Label(root, image=t2str25)
t2star2path = f'/home/wafiq/Downloads/star/2.png'
t2star2image = Image.open(t2star2path)
t2str2 = ImageTk.PhotoImage(t2star2image)
t2star2 = Label(root, image=t2str2)
t2star15path = f'/home/wafiq/Downloads/star/1.5.png'
t2star15image = Image.open(t2star15path)
t2str15 = ImageTk.PhotoImage(t2star15image)
t2star15 = Label(root, image=t2str15)
t2star1path = f'/home/wafiq/Downloads/star/1.png'
t2star1image = Image.open(t2star1path)
t2str1 = ImageTk.PhotoImage(t2star1image)
t2star1 = Label(root, image=t2str1)
t2star05path = f'/home/wafiq/Downloads/star/0.5.png'
t2star05image = Image.open(t2star05path)
t2str05 = ImageTk.PhotoImage(t2star05image)
t2star05 = Label(root, image=t2str05)
####

# PLAYER INI
# TEAM1
af0_var = StringVar()
af1_var = StringVar()
af2_var = StringVar()
af0_var.set("")
af1_var.set("")
af2_var.set("")

af0 = Entry(root, width=3, textvariable=af0_var, validate="key", validatecommand=(root.register(limit_value), '%P'))
af1 = Entry(root, width=3, textvariable=af1_var, validate="key", validatecommand=(root.register(limit_value), '%P'))
af2 = Entry(root, width=3, textvariable=af2_var, validate="key", validatecommand=(root.register(limit_value), '%P'))

aforwardsum_var = StringVar()
aforwardavg_var = StringVar()
aforwardavg = Label(root, textvariable=aforwardavg_var, width=5, font=ratefont)

am0_var = StringVar()
am1_var = StringVar()
am2_var = StringVar()
am3_var = StringVar()
am4_var = StringVar()
am0_var.set("")
am1_var.set("")
am2_var.set("")
am3_var.set("")
am4_var.set("")

am0 = Entry(root, width=3, textvariable=am0_var)
am1 = Entry(root, width=3, textvariable=am1_var)
am2 = Entry(root, width=3, textvariable=am2_var)
am3 = Entry(root, width=3, textvariable=am3_var)
am4 = Entry(root, width=3, textvariable=am4_var)

amidsum_var = StringVar()
amidavg_var = StringVar()
amidavg = Label(root, textvariable=amidavg_var, width=5, font=ratefont)

ad0_var = StringVar()
ad1_var = StringVar()
ad2_var = StringVar()
ad3_var = StringVar()
ad4_var = StringVar()
ad0_var.set("")
ad1_var.set("")
ad2_var.set("")
ad3_var.set("")
ad4_var.set("")

ad0 = Entry(root, width=3, textvariable=ad0_var)
ad1 = Entry(root, width=3, textvariable=ad1_var)
ad2 = Entry(root, width=3, textvariable=ad2_var)
ad3 = Entry(root, width=3, textvariable=ad3_var)
ad4 = Entry(root, width=3, textvariable=ad4_var)

adefensesum_var = StringVar()
adefenseavg_var = StringVar()
adefenseavg = Label(root, textvariable=adefenseavg_var, width=5, font=ratefont)

ag0_var = StringVar()
ag0_var.set("")

ag0 = Entry(root, width=3, textvariable=ag0_var)

af0_var.trace("w", update_sum_fw)
af1_var.trace("w", update_sum_fw)
af2_var.trace("w", update_sum_fw)    
am0_var.trace("w", update_sum_md)
am1_var.trace("w", update_sum_md)
am2_var.trace("w", update_sum_md)
am3_var.trace("w", update_sum_md)
am4_var.trace("w", update_sum_md)
ad0_var.trace("w", update_sum_df)
ad1_var.trace("w", update_sum_df)
ad2_var.trace("w", update_sum_df)
ad3_var.trace("w", update_sum_df)
ad4_var.trace("w", update_sum_df)
ag0_var.trace("w", update_sum_df)

#TEAM2
bf0_var = StringVar()
bf1_var = StringVar()
bf2_var = StringVar()
bf0_var.set("")
bf1_var.set("")
bf2_var.set("")
bf0 = Entry(root, width=3, textvariable=bf0_var)
bf1 = Entry(root, width=3, textvariable=bf1_var)
bf2 = Entry(root, width=3, textvariable=bf2_var)

bforwardsum_var = StringVar()
bforwardavg_var = StringVar()
bforwardavg = Label(root, textvariable=bforwardavg_var, width=5, font=ratefont)

bm0_var = StringVar()
bm1_var = StringVar()
bm2_var = StringVar()
bm3_var = StringVar()
bm4_var = StringVar()
bm0_var.set("")
bm1_var.set("")
bm2_var.set("")
bm3_var.set("")
bm4_var.set("")
bm0 = Entry(root, width=3, textvariable=bm0_var)
bm1 = Entry(root, width=3, textvariable=bm1_var)
bm2 = Entry(root, width=3, textvariable=bm2_var)
bm3 = Entry(root, width=3, textvariable=bm3_var)
bm4 = Entry(root, width=3, textvariable=bm4_var)

bmidsum_var = StringVar()
bmidavg_var = StringVar()
bmidavg = Label(root, textvariable=bmidavg_var, width=5, font=ratefont)

bd0_var = StringVar()
bd1_var = StringVar()
bd2_var = StringVar()
bd3_var = StringVar()
bd4_var = StringVar()
bd0_var.set("")
bd1_var.set("")
bd2_var.set("")
bd3_var.set("")
bd4_var.set("")
bd0 = Entry(root, width=3, textvariable=bd0_var)
bd1 = Entry(root, width=3, textvariable=bd1_var)
bd2 = Entry(root, width=3, textvariable=bd2_var)
bd3 = Entry(root, width=3, textvariable=bd3_var)
bd4 = Entry(root, width=3, textvariable=bd4_var)

bdefensesum_var = StringVar()
bdefenseavg_var = StringVar()
bdefenseavg = Label(root, textvariable=bdefenseavg_var, width=5, font=ratefont)

bg0_var = StringVar()
bg0_var.set("")
bg0 = Entry(root, width=3, textvariable=bg0_var)

bf0_var.trace("w", bupdate_sum_fw)
bf1_var.trace("w", bupdate_sum_fw)
bf2_var.trace("w", bupdate_sum_fw)
bm0_var.trace("w", bupdate_sum_md)
bm1_var.trace("w", bupdate_sum_md)
bm2_var.trace("w", bupdate_sum_md)
bm3_var.trace("w", bupdate_sum_md)
bm4_var.trace("w", bupdate_sum_md)
bd0_var.trace("w", bupdate_sum_df)
bd1_var.trace("w", bupdate_sum_df)
bd2_var.trace("w", bupdate_sum_df)
bd3_var.trace("w", bupdate_sum_df)
bd4_var.trace("w", bupdate_sum_df)
bg0_var.trace("w", bupdate_sum_df)

root.mainloop()
