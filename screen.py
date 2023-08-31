import tkinter as tk
from PIL import Image, ImageTk
import math
# ---------------------------- CONSTANTS ------------------------------- #
# These are the constants angela yu used.
PINK = "#e2979c"
FONT = ("Courier", 35, "bold")
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


class Screen:

    def __init__(self,
                 bgcolor=PINK):
        self.bgcolor = bgcolor
        self.window = None
        self.canvas = None
        self.tomato_image = None
        self.timer_text = None
        self.timer_label = None
        self.checks_label = None
        self.setup_screen()
        self.run()

    def setup_screen(self):
        self.initiate_window()
        self.initiate_canvas()
        self.labels()
        self.buttons()

    def initiate_window(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=100, bg=self.bgcolor)

    def initiate_canvas(self):
        self.tomato_image = Image.open("tomato.png")
        self.tomato_image = self.tomato_image.resize((200, 200), Image.ANTIALIAS)
        self.tomato_image = ImageTk.PhotoImage(self.tomato_image)
        self.canvas = tk.Canvas(width=300, height=300, bg=PINK, highlightthickness=0)
        self.canvas.create_image(50, 0, image=self.tomato_image, anchor="nw")
        self.timer_text = self.canvas.create_text(150, 250, text="00:00", fill="white", font=FONT)
        self.canvas.grid(column=1, row=1)

    def labels(self):
        self.timer_label = tk.Label()
        self.timer_label.config(text="Timer", fg=GREEN, bg=PINK, highlightthickness=0, font=(FONT_NAME, 40, "bold"))
        self.timer_label.grid(column=1, row=0)
        self.checks_label = tk.Label()
        self.checks_label.config(text="", fg=GREEN, bg=PINK, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
        self.checks_label.grid(column=1, row=3)

    def buttons(self):
        start_button = tk.Button()
        start_button.config(text="Start", command=self.start_timer)  # want countdown after canvas has been instantiated
        start_button.grid(column=0, row=2, pady=50)

        reset_button = tk.Button()
        reset_button.config(text="Reset", command=self.reset_timer)
        reset_button.grid(column=2, row=2, pady=50, )

    def reset_timer(self):
        self.window.after_cancel(TIMER)
        self.canvas.itemconfig(self.timer_text, text="00:00")  # note canvas yung timer_text
        self.timer_label.config(text="TIMER")
        self.checks_label.config(text="")
        global REPS
        REPS = 0

    def start_timer(self):
        global REPS
        REPS += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if REPS % 2 == 1:
            self.timer_label.config(text="WERK WERK", fg=YELLOW)
            self.checks_label.config(text="✓" * math.floor(REPS / 2))
            self.count_down(count=work_sec)
        elif REPS % 2 == 0 and REPS != 8:
            self.timer_label.config(text="BREAK, 5MIN", fg=GREEN)
            self.count_down(short_break_sec)
        else:
            REPS = 0
            self.timer_label.config(text="BREAK, 20MIN", fg=RED)
            self.count_down(long_break_sec)

    def count_down(self, count):
        count_min = math.trunc(count / 60)
        count_sec = count % 60
        # Python Dynamic Typing - bawal for java/c
        if count_sec <= 9:
            count_sec = f"0{count_sec}"
        if count_min <= 9:
            count_min = f"0{count_min}"
        # End of Dynamic Typing
        display = f"{count_min}:{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=display)
        if count > 0:
            global TIMER
            TIMER = self.window.after(2, self.count_down, count - 1)
            # recursion, func=count_down, every 1000ms, count_down(count-1)
        else:  # pag tapos na
            self.start_timer()

    def run(self):
        self.window.mainloop()
