import json;
import tkinter;
import PIL.Image, PIL.ImageTk
from tkinter import messagebox
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#written by Alex Zhuang zhual@utschools.ca
with open('inputmap.json', 'r') as f:
    inputmap = json.load(f)
with open('inputsurveyphotos.json', 'r') as f:
    inputsurveyphotos = json.load(f)

global index, basewidth
index = 0
basewidth = 300


print (inputmap)
print (inputsurveyphotos)

top = tkinter.Tk()


img = PIL.Image.open(inputmap['filename']);
photo =PIL.ImageTk.PhotoImage(img)

top.geometry('{}x{}'.format(photo.width(), photo.height()) )

print (photo.height(), photo.width())
canvas = tkinter.Canvas(top, width = photo.width(), height = photo.height())
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

canvas.pack()



def clicked(event):
    if (event.x >= 0 and event.x <= photo.width() and event.y >= 0 and event.y <= photo.height()):
        second = tkinter.Toplevel(width = 300)

        print ("clicked at", event.x, event.y)
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)

        #Assumed that image is oriented North
        #(relative y of point in image * distance between latitude coordinates) + most southern latitude coordinate
        lat = (((photo.height()-event.y)/photo.height())*abs(inputmap['topleft']['lat']-inputmap['bottomright']['lat']))+inputmap['bottomright']['lat']
        #(relative x of point in image * distance between longitude coordinates) + most western longitude coordinate
        long = ((event.x/photo.width())*abs(inputmap['topleft']['long']-inputmap['bottomright']['long']))+inputmap['topleft']['long']
        point = canvas.create_oval(x1, y1, x2, y2, fill="#FF0000", outline="#FF0000", width=10)
        second.grab_set()
        second.title("New Label")

        def delete():
            canvas.delete(point)
            second.destroy()

        msg = tkinter.Message(second, justify = 'center', width = 300, text="Label at (lat,long) \n{}, {}".format(lat, long))
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

canvas.bind("<Button-1>", clicked)
global cycle
cycle = tkinter.Toplevel()
cycleimg = PIL.Image.open(inputsurveyphotos[index])
wpercent = (basewidth/float(cycleimg.size[0]))
hsize = int((float(cycleimg.size[1])*float(wpercent)))
cycleimg = cycleimg.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
cyclephoto =PIL.ImageTk.PhotoImage(cycleimg)
cycle.geometry('{}x{}'.format(cyclephoto.width(), cyclephoto.height()+80))
cyclecanvas = tkinter.Canvas(cycle, width = cyclephoto.width(), height = cyclephoto.height())
cyclecanvas.create_image(0, 0, image=cyclephoto, anchor=tkinter.NW)
cyclecanvas.pack()


def refresh():
    global cycle
    cycleimg = PIL.Image.open(inputsurveyphotos[index])
    wpercent = (basewidth/float(cycleimg.size[0]))
    hsize = int((float(cycleimg.size[1])*float(wpercent)))
    cycleimg = cycleimg.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    cyclephoto =PIL.ImageTk.PhotoImage(cycleimg)
    cycle.cyclephoto = cyclephoto
    cycle.geometry('{}x{}'.format(cyclephoto.width(), cyclephoto.height()+80))
    cyclecanvas.create_image(0, 0, image=cyclephoto, anchor=tkinter.NW)
    cyclecanvas.pack()

def prev():
    global index
    if (index >0):
        index -=1
        refresh()
        print (index)
def next():
    global index
    if (index < len(inputsurveyphotos)-1):
        index += 1
        refresh()
        print (index)

next = tkinter.Button(cycle, text="Next", command=next)
next.pack()
prev = tkinter.Button(cycle, text="Previous", command=prev)
prev.pack()


print (inputsurveyphotos[index])


print (index)


top.mainloop()
cycle.mainloop()
