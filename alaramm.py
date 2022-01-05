from tkinter import *
import datetime
import time
from alarm import actual_time
def actual_alarm():
    set_time= f"{hour.get()}:{min.get()}:{sec.get()}"  
    alarm(set_time)
clock= Tk()
clock.title()
clock.resizable(0,0)
clock.geometry('400x200')
Label(clock,text="enter the time for alarm",bg="red",font="arial").place(x=60,y=120)
hour= StringVar()
min=StringVar()
sec=StringVar()
Entry(clock,textvariable = hour,font='arial').place(x=110,y=30)
Entry(clock,textvariable = min ,font='arial').place(x=150,y=30)
Entry(clock,textvariable = sec ,font='arial').place(x=200,y=30)
submit = Button(clock,textvariabe='',font='',width=10,command=actual_time).place(x=110,y=70)
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time= datetime.datetime.now()
        now=current_time.strftime("%H:%M:%S")
        date= current_time.strftime("%d/%M/%Y")
        print("tHe date is",date)
        print(now)
        if now==set_alarm_timer:
            print("motHer fucker just wake up")
clock.mainloop()

