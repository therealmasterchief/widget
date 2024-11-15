from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("message box")
window.geometry("400x400")

def msg():
    messagebox.askyesno("Virus detected","do you want to wipe this virus?")

button=Button(text="scan",command=msg,bg="green",fg="white")
button.pack()

window.mainloop()