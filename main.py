from tkinter import *
import math
from venv import create

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_n = None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    window.after_cancel(timer_n)
    timer.config(text= "Timer", fg= GREEN)
    check_mark.config(text= "")
    canvas.itemconfig(time_counter, text= "00 : 00" )
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counting():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8== 0:
        count_down(long_break)
        timer.config(text= "Break", fg= RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text= "Break", fg= PINK)
    else:
        count_down(work_sec)
        timer.config(text= "Work", fg= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_n
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_counter, text= f"{count_min} : {count_sec}")
    if count > 0:
        timer_n = window.after(1000, count_down, count-1)
    else:
        start_counting()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check_mark.config(text= mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 200, pady= 100, bg=YELLOW)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= pomodoro_img)
time_counter = canvas.create_text(100, 112, text= "00:00", font= (FONT_NAME, 35, "bold"), fill= "white")
canvas.grid(column=2, row= 2)

timer = Label(text="Timer", fg= GREEN, font=(FONT_NAME, 50, "bold"), bg= YELLOW, highlightthickness=0)
timer.grid(column=2, row=1)

check_mark = Label(text= " ", bg= YELLOW, fg= GREEN, highlightthickness=0)
check_mark.grid(column= 2, row= 4)
check_mark.config(padx= 50, pady= 15)

start = Button(text="Start", command=start_counting, highlightthickness=0)
start.grid(column= 1, row= 3)

reset = Button(text= "Reset", highlightthickness=0, command= timer_reset)
reset.grid(column= 3, row=3)



window.mainloop()
