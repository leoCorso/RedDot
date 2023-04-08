import tkinter as tk
import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import CTk
# Create a transparent window

class RedDot(CTk):
    red_dot_enabled = False
    red_dot_window = None
    switch_var = None

    def __init__(self):
        super().__init__()
        self.title("Red Dot - Zer0_music")
        self.geometry(f"{200}x{100}")

        customtkinter.set_appearance_mode("Dark")  # Other: "Light", "System" (only macOS)

        self.switch_var = customtkinter.StringVar(value="off")
        switch_1 = customtkinter.CTkSwitch(master=self, text="Red Dot", command=self.switch_event,
                                           variable=self.switch_var, onvalue="on", offvalue="off")
        switch_1.pack(padx=20, pady=10)
        switch_1.place(relx=0.50, rely=0.50, anchor=tkinter.CENTER)
        self.mainloop()

    def switch_event(self):
        if self.switch_var.get() == 'on':
            self.enable_reddot()
        else:
            self.disable_reddot()

    def enable_reddot(self):
        if self.red_dot_enabled:
            return
        self.red_dot_enabled = True
        self.red_dot_window = tk.Tk()
        self.red_dot_window.attributes('-alpha', 100.0)
        self.red_dot_window.config(cursor="none")

        self.red_dot_window.attributes('-fullscreen', True)

        # Create a canvas and draw a red dot in the center
        canvas = tk.Canvas(self.red_dot_window, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.create_oval(1275, 715, 1285, 725, fill='red')
        canvas.config(cursor="none")
        self.red_dot_window.wm_attributes('-transparentcolor','black')
        self.red_dot_window.attributes('-topmost', True)

        # Run the main event loop
        self.red_dot_window.mainloop()

    def disable_reddot(self):
        if self.red_dot_window is not None:
            self.red_dot_window.destroy()
            self.red_dot_enabled = False


app = RedDot()

