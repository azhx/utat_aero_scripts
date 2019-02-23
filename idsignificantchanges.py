import json;
import tkinter;
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
global point
#written by Alex Zhuang zhual@utschools.ca
with open('inputmap.json', 'r') as f:
    inputmap = json.load(f)
with open('inputsurveyphotos.json', 'r') as f:
    inputsurveyphotos = json.load(f)

print (inputmap)
print (inputsurveyphotos)
top = tkinter.Tk()
img = PIL.Image.open("test.jpg");
photo =PIL.ImageTk.PhotoImage(img)

top.geometry('{}x{}'.format(photo.width(), photo.height()) )

print (photo.height(), photo.width())
canvas = tkinter.Canvas(top, width = photo.width(), height = photo.height())

canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

canvas.pack()



def clicked(event):
    second = tkinter.Toplevel(width = 300)
    red = "#FF0000"

    print ("clicked at", event.x, event.y)
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)

    point = canvas.create_oval(x1, y1, x2, y2, fill=red, outline=red, width=10)
    second.grab_set()
    second.title("New Label")

    def delete():
        canvas.delete(point)
        second.destroy()

    msg = tkinter.Message(second, justify = 'center', width = 100, text="Label at (x,y) \n{}, {}".format(event.x, event.y))
    msg.pack()

    t = tkinter.Text(second, height=5, width=40)
    t.pack()

    def save():
        desc = t.get("1.0", 'end-1c')
        print(desc)
        second.destroy()

    button = tkinter.Button(second, text="Save and Quit", command=save)
    button.pack()

    second.protocol("WM_DELETE_WINDOW", delete)

    second.mainloop()

top.bind("<Button-1>", clicked)


top.mainloop()
