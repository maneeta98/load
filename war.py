import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


from tkinter.font import Font
root=tk.Tk()
messageframe=tk.Frame(root,height=60,width=300,bg="darkorange2")
messageframe.pack()

roboto_font = Font(family="Roboto", size=16)
label = tk.Label(messageframe, text="Warning alert!", font=roboto_font,bg="darkorange2")
label.place(x=65,y=20)


root.mainloop()
