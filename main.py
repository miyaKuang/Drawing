from tkinter import *
from quickdraw import QuickDrawData
qd = QuickDrawData()
def animate():
    drawing = qd.get_drawing(entry.get(),61)
    print(entry.get())
    for stroke in drawing.strokes: #strokes is a list of lists
        for pointIndex in range(len(stroke)):
            print(stroke[pointIndex])
            canvas.create_line()


    canvas.create_line((1,1,250,250),fill="purple",width = 5)
root = Tk()
label = Label(root, text = "type what you want to draw")
label.pack()
entry = Entry(root)
entry.pack()
submitButton = Button(root, text ="submit",command = animate )
submitButton.pack()
canvas = Canvas(root,width=300,height = 300)
canvas.pack(anchor='nw',fill='both',expand =1)



root.mainloop()
