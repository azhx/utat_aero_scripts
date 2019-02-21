import json;
import tkinter as tk;
#Written by Alex Zhuang zhual@utschools.ca
with open('inputmap.json', 'r') as f:
    inputmap = json.load(f)
with open('inputsurveyphotos.json', 'r') as f:
    inputsurveyphotos = json.load(f)

print (inputmap)
print (inputsurveyphotos)
top = tk.Tk()
top.mainloop()
