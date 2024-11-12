from tkinter import *
window=Tk()
window.title("number pad")
window.geometry("200x300")

num=[
    [9,8,7],
    [6,5,4],
    [3,2,1],
    ["#",0,"*"]
]
for i in range(4):
    window.columnconfigure(i,minsize=70)
    window.rowconfigure(i,minsize=50)
    for j in range(0,3):
        fra=Frame(master=window,relief=RAISED,borderwidth=3)
        fra.grid(row=i,column=j)
        label=Label(master=fra,text=num[i][j], bg='pink')
        label.pack()

window.mainloop()