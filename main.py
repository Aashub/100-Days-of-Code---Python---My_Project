from tkinter import  *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
# here we will reset our pomodoro so we can restart it again as per our wish
def reset_timer():
    """this function will cancel the count to zero by which we our program starts from zero time, canvas text to zero,
     timer name and check mark all will be updated to zero"""
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text = "00:00")
    tomato_name.config(text = "Timer")
    check_mark.config(text = "")
    global  reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """this function will used to start the timer in pomodoro """
    global  reps

    reps += 1

    # here we have assigned the total minute into sec so we can use them in countdown function
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 30
    long_break_sec = LONG_BREAK_MIN *15

    # here we will check the condition that at which rep work, break and long break countdown() function needs to run
    if reps%2 > 0:
        countdown(work_sec)
        tomato_name.config(text= "Work", fg="GREEN")

    elif reps%8 == 0:
        countdown(long_break_sec)
        tomato_name.config(text= "Long Break", fg="RED")

    elif reps % 2 == 0:
        countdown(short_break_sec)
        tomato_name.config(text= "Break", fg="PINK")



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """this function is responsible for updating the time and converting them into minute and sec so it can properly show in screen"""
    minute = math.floor(count/60)
    second = count%60

    # if second is equal to or less than 9 than this loop will run which makes our program much more good
    if second <= 9:
        second = f"0{second}"
    canvas.itemconfig(canvas_text, text = f"{minute}:{second}")

    # if timer value is greater than zero than we will call the countdown function again and again so it will reduce 1 second at a time
    # until count value doesn't become zero
    if count > 0:
        global timer
        timer = window.after(100, countdown, count-1)

    # when count value does became zero than we will call the start_timer function again to continue the program
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in  range(work_sessions):
            marks += "✔"
        check_mark.config(text = marks)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=1000, pady=100, bg=YELLOW)


tomato_name = Label(text= "Timer", bg= YELLOW, fg=GREEN, font= (FONT_NAME, 32, "bold"), padx=0, pady=0 )
tomato_name.grid(row= 0, column = 1)

# we use canvas to add a image by using tkinter
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,111, image = tomato_image)
canvas_text = canvas.create_text(100, 131, text="00:00", fill= "white", font= (FONT_NAME, 26, "bold"))

canvas.grid(column=1, row = 1)


check_mark = Label(bg= YELLOW, fg=GREEN, font= (FONT_NAME, 17, "bold"), pady = 5 )
check_mark.grid(row= 4, column = 1)

button = Button(text="Start", font=("Roboto",8,"bold"), padx=0, pady=0, highlightthickness= 0, command= start_timer)
button.grid(column=0, row=3)

button = Button(text="Reset", font=("Roboto",8,"bold"), padx=0, pady=0, highlightthickness= 0, command= reset_timer)
button.grid(column=2, row=3)


window.mainloop()

