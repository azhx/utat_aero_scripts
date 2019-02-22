import json;
import tkinter;
import PIL.Image, PIL.ImageTk
#written by Alex Zhuang zhual@utschools.ca
with open('inputmap.json', 'r') as f:
    inputmap = json.load(f)
with open('inputsurveyphotos.json', 'r') as f:
    inputsurveyphotos = json.load(f)

print (inputmap)
print (inputsurveyphotos)
top = tkinter.Tk()
img = PIL.Image.open("test.jpg");
height, width = img.size
canvas = tkinter.Canvas(top, width = width, height = height)
canvas.pack()

photo =PIL.ImageTk.PhotoImage(img)

canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

canvas.pack()
def callback(event):
    print ("clicked at", event.x, event.y)

top.bind("<Button-1>", callback)

top.mainloop()
