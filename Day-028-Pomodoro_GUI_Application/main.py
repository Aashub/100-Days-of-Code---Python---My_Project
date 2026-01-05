from tkinter import *
import  math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- Global Variable which are changing ------------------------------- #
reps = 0
x_cor = 110
y_cor = 330
timer = None
tick_mark_list = []

# ---------------------------- TIMER RESET ------------------------------- #

def reset_pomodoro():
    """this function will reset the pomodoro all attributes so when start get clicked again new pomodoro gets started."""

    global reps, tick_mark_list, x_cor

    start_button.grid(row=2, column=0, padx=14)
    invisible_Label.grid_remove()
    x_cor = 110
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text= "Timer", fg = GREEN)

    for remove_tick in tick_mark_list:
        remove_tick.config(text= "")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """this function will check and update the timer by calling timer_countdown function as per the reps condition"""

    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60

    start_button.grid_remove()
    invisible_Label.grid(row=2, column=0, padx=31)
    global reps
    reps += 1

    # this is the 25 minute working reps
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_countdown(work_second)
        timer_label.config(fg = GREEN, text= "Work")

    # this is the 5 minute short break reps
    elif reps == 2 or reps == 4 or reps == 6:
        timer_countdown(short_break_second)
        timer_label.config(fg=PINK, text="Break")

    # this is the 20 minute long break rep
    elif reps == 8:
        timer_countdown(long_break_second)
        timer_label.config(fg=RED, text="Break")

    else:
        reps = 0
        start_button.config(command=start_timer)
        reset_pomodoro()
        invisible_Label.grid_remove()
        start_button.grid(row=2, column=0, padx=14)


def tick_mark_function():
    """this function will help in marking the the tick mark everytime the 2 reps are being completed."""

    global tick_mark_list
    tick_mark_label = Label(text="✔", font=("Courier", 15, "bold"))
    tick_mark_label.place(x = x_cor, y = y_cor)
    tick_mark_label.config(fg = GREEN, bg = YELLOW)
    tick_mark_list.append(tick_mark_label)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_countdown(seconds):
    """this function will update the timer in pomodoro as per the parameter value in minute & seconds"""

    count_minute = math.floor(seconds / 60)
    count_second = seconds % 60

    # this if statement will help in bypassing the issue of when seconds are left less than 10 so it will show then as an 09__08 and so on
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute} : {count_second}")

    # if seconds will be greater than 0 than .after() method will call the time_countdown function again & also subtract the second each second.
    if seconds > 0:
        global timer
        timer = window.after(5, timer_countdown, seconds - 1)

    # every time seconds count down become zero this else statement will get triggered and call the start_timer function again for the next reps
    else:
        global reps
        global x_cor

        start_timer()
        # here we are tackling the functionality of after completing two reps tick_mark_function() gets called.
        if reps % 2 != 0:

                tick_mark_function()
                x_cor += 30

# ---------------------------- UI SETUP ------------------------------- #

# here we are setting the window
window = Tk()
window.title("Pomodoro")
window.config(padx= 120, pady = 60, bg=YELLOW)

# timer label
timer_label = Label(text="Timer", font= ("Courier", 35, "bold"))
timer_label.config(pady=5, fg = GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)


# canvas object for adding image in the screen.
canvas = Canvas(width=200, height= 224)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", font= (FONT_NAME, 25, "bold"), fill= "white")
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column= 1)

# start_button
start_button = Button(text= "Start", font= ("Arial" , 10, "bold"), highlightthickness=0, command = start_timer)
start_button.grid(row=2, column=0, padx=14)

# reset_button
reset_button = Button(text= "Reset", font= ("Arial" , 10, "bold"), highlightthickness=0, command = reset_pomodoro)
reset_button.grid(row=2, column=2)

invisible_Label = Label(bg=YELLOW)


window.mainloop()
