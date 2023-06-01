import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.withdraw()

messagebox.showerror ("Error","This is error message")
messagebox.showwarning("Warning","This is warning message")
messagebox.showinfo("Info","This is info message")
messagebox.askquestion("Question","Do you want to install this software")
messagebox.askokcancel("askokcancel","Do you want to run this program")
messagebox.askyesno("askyesno","Do you want to run the code")
messagebox.askretrycancel("retry","Do you want to retry or cancel")

root.mainloop()