import json;
import tkinter;
#written by Alex Zhuang zhual@utschools.ca
with open('inputmap.json', 'r') as f:
    inputmap = json.load(f)
with open('inputsurveyphotos.json', 'r') as f:
    inputsurveyphotos = json.load(f)

print (inputmap)
print (inputsurveyphotos)
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
def callback(event):
    print ("clicked at", event.x, event.y)

top.bind("<Button-1>", callback)

top.mainloop()
