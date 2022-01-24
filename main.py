from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 1500
SHORT_BREAK_SEC = 300
LONG_BREAK_SEC = 1200
cycle = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global cycle
    cycle = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global checkmark_text
    checkmark_text = ""
    global cycle
    cycle += 1
    if cycle % 8 == 0:
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 27, "bold"))
        checkmark_text = checkmark_text + "✔"
        checkmark_label.config(text=checkmark_text, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
    elif cycle % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 27, "bold"))
        checkmark_text = checkmark_text + "✔"
        checkmark_label.config(text=checkmark_text, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
    else:
        count_down(WORK_SEC)
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 27, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP --------------- ---------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)
window.maxsize(width=500, height=500)

# Timer
timer_label = Label()
timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 27, "bold"))
timer_label.grid(column=1, row=0)

# image
canvas = Canvas(height=235, width=200, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=tomato_image)
canvas_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

# button start
button_start = Button()
button_start.config(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

# buttot reset
button_reset = Button()
button_reset.config(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=3, row=2)

# checkmark label
checkmark_label = Label()
checkmark_text = ""
checkmark_label.config(text=checkmark_text, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
