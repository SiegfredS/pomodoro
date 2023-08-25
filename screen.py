import tkinter as tk
from PIL import Image, ImageTk
PINK = "#e2979c"
FONT = ("Courier", 35, "bold")


class Screen:

    def __init__(self,
                 bgcolor=PINK):
        self.bgcolor = bgcolor
        self.window = None
        self.canvas = None
        self.tomato_image = None
        self.setup_screen()
        self.run()

    def setup_screen(self):
        self.initiate_window()
        self.initiate_canvas()

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
        timer_text = self.canvas.create_text(150, 250, text="00:00", fill="white", font=FONT)
        self.canvas.grid(column=1, row=1)

    def run(self):
        self.window.mainloop()
