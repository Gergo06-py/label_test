from tkinter import *

root = Tk()
root.title("Image")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")

frame = LabelFrame(root, text="this is a label", padx=50, pady=50)
frame.pack(padx=10, pady=10)


button1 = Button(frame, text="DO NOT CLICK HERE")
button2 = Button(frame, text="OR HERE")
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

root.mainloop()
