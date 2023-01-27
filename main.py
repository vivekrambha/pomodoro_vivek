from tkinter import *
import math
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
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    che.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    shot_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps %8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", font=("papyrus",24), fg=RED, bg=YELLOW)
    elif reps % 2 ==0:
        count_down(shot_break_sec)
        timer.config(text="Break", font=("papyrus", 24), fg=RED, bg=YELLOW)
    else:
        count_down(work_sec)
        timer.config(text="Work", font=("papyrus", 25), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count>0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            che.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
#lable
timer = Label(text="Timer", font=("papyrus",24), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tamato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tamato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=("papyrus",34))
canvas.grid(column=1,row=1)


#button
start = Button(text="START",font=("papyrus",12),highlightthickness=0,bg=GREEN,fg="#7B2869", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="RESET",font=("papyrus",12),highlightthickness=0,bg=GREEN,fg="#7B2869", command=reset_timer)
reset.grid(row=2, column=2)

#check
#text="✔"
che = Label(fg=GREEN, bg=YELLOW,font=("papyrus",24,"bold"))
che.grid(row=3,column=1)


window.mainloop()