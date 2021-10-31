'''from tkinter import *
from utils import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

def close_window():
    window.destroy()

window = Tk()
app = Window(window)

window.wm_title("Note app")
window.geometry("800x800")


create_button_no_command(window, "Hello World", 350,350)
#create_button_no_command(window, "HELLLO", 690, 10)

close1 = PhotoImage(file="C:/Users/Nave/Desktop/Python_VSC/imgs/close2.png")
btn = Button(image=close1, command=close_window)
btn.place(x=720, y=5)

input_label = Entry()
input_label.place(x=400, y=400)


window.mainloop()

quit()
'''

'''
def Fibonacci(num):
    sum = 1
    for x in range(1, (num + 1), 1):
        sum = sum * x
    print(f" {num} | {sum}")

for i in range(2000):
   Fibonacci(i)
'''
import hashlib
from types import TracebackType

def convert_text_to_md5(text:str):
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

inp = input("Enter the text: ")
import time as t
found = False
start_time = t.time()
hash_passowrd = convert_text_to_md5(inp)
with open("passwords.txt", "r") as passwords_file:
    all_lines = passwords_file.read().splitlines()
    for line in all_lines:
        if (convert_text_to_md5(str(line)) == hash_passowrd):
            print("PASSWORD FOUND")
            print(line)
            found = True
            break

print("PASSWORD MD5: ", hash_passowrd)
if not found:
    print("The password does not appear in the txt file.")
    with open("passwords.txt", "a") as f: #Append text and NOT REWRITE. w REWRITES.
        f.write(f"\n{inp}")
print("--- %s seconds ---" % (t.time() - start_time))  