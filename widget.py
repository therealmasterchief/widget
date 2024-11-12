from tkinter import*

window=Tk()
window.title("adding widget")
window.geometry("800x800")

L1=Label(text="welcome", bg="Blue", fg="white",width=200)
L1.pack()

name_lab=Label(text="enter name")
name_entry=Entry()
name_lab.pack()
name_entry.pack()

def show():
    name=name_entry.get()
    greet="hello "+ name +" how are you?"
    txt.insert(END,greet)
txt=Text(height=2)
btn=Button(text="click",bg="blue",fg="white",command=show)
txt.pack()
btn.pack()

window.mainloop()
