import tkinter as tk
from tkinter import Canvas, Entry, PhotoImage

class MyApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x1024")
        self.configure(bg="#C5D5FF")

        self.canvas = Canvas(
            self,
            bg="#C5D5FF",
            height=1024,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.initialize_widgets()

    def initialize_widgets(self):
        image_1 = self.canvas.create_image(
            306.0,
            545.0,
        )

        # Similarly, initialize other widgets like Entry, Buttons etc.

    def run(self):
        # This method starts the Tkinter event loop
        self.mainloop()

if __name__ == "__main__":
    app = MyApplication()
    app.run()
