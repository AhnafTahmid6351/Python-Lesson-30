'''
Create a Python Tkinter application titled "Interactive Logger" with a window size of 300x200. The interface should feature a single Button labeled "Log Action". When the button is left-clicked, it must print a message to the console using an event handler bound to <Button-1>. Additionally, bind the <Key> event to the main window so that pressing any key on your keyboard displays a warning message box alerting the user that a key press was detected.
'''
from tkinter import *
from tkinter import messagebox


main = Tk()
main.title("Interactive Logger")
main.geometry("300x200")

def msgBox(event):
    messagebox.showwarning("Alert! Key pressed", event.char)

main.bind("<Key>", msgBox)


def click(event):
    print("\nThe button was clicked")

button = Button(text="Log action")
button.pack()
button.bind("<Button-1>", click)

main.mainloop()