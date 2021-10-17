

import tkinter as tk
from tkinter import *
import webbrowser

def click():#created function
    html_text = "<html> <body> <h1>{}</h1> </body> </html>".format(el.get())#variable with value that = html format
    f = open("pythonhtml.html", "w")
    f.write(html_text)
    f.close()

    webbrowser.open_new_tab("pythonhtml.html")#gives command to open html browser

r = tk.Tk()#creating gui
r.title('Submission')#title of gui
button = tk.Button(r, text='Click', width=25, command=click)#created button widget 
button.pack()
el = Entry(r, width=30)#created entry widget that 
el.pack()
r.mainloop()
