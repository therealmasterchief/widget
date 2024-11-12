from tkinter import*

window=Tk()
window.title("login screen")
window.geometry("400x400")

fra=Frame(master=window,height=200,width=300,bg="pink")
lb1=Label(fra,text="Enter a name",bg="blue",fg="white")
name_entry=Entry(fra)

def display():
    name=name_entry.get()
    greet="hello"+name
    textbox.insert(END,greet)
btn=Button(text="create Account",command=display)
textbox=Text(bg="blue")

fra.place(x=20,y=0)
lb1.place(x=10,y=20)
name_entry.place(x=150,y=20)
btn.place(x=130,y=210)
textbox.place(y=250)

window.mainloop()