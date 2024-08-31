from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
DARK_GREY = '#3F4E4F'
FONT_NAME = 'Courier'
CHECK_MARK_CHAR = '✔'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() -> None:
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer() -> None:
    global reps
    reps += 1
    if reps % 2 != 0:
        time = WORK_MIN * 60
        title_label.config(text='Work', foreground=GREEN)
    elif reps % 8 == 0:
        time = LONG_BREAK_MIN * 60
        title_label.config(text='Break', foreground=RED)
    else:
        time = SHORT_BREAK_MIN * 60
        title_label.config(text='Break', foreground=PINK)
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time) -> None:
    count_min = math.floor(time / 60)
    count_second = time % 60
    if count_second < 10:
        count_second = f'0{count_second}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_second}')
    if time > 0:
        global timer
        timer = canvas.after(1000, count_down, time - 1)
    else:
        for _ in range(math.floor(reps / 2)):
            task_counter_label.config(text=task_counter_label.cget('text') + CHECK_MARK_CHAR)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro timer')
window.config(padx=100, pady=50, background=YELLOW, bd=0)

title_label = Label(text='Timer', font=(FONT_NAME, 35), background=YELLOW, foreground=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 112, text='00:00', font=(FONT_NAME, 35), fill='white')
canvas.grid(row=1, column=1)

start_button = Button(text='Start', font=FONT_NAME, background=GREEN, foreground=RED, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=FONT_NAME, background=GREEN, foreground=RED, command=reset_timer)
reset_button.grid(row=2, column=2)

task_counter_label = Label(font=(FONT_NAME, 16), background=YELLOW, foreground=DARK_GREY)
task_counter_label.grid(row=3, column=1)

window.mainloop()
