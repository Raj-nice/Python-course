from tkinter import *

root = Tk()

root.title("Number Pad")
root.geometry("250x300")

nums = [[7, 8, 9], [4, 5, 6], [1, 2, 3], ["*", 0, "#"]]

for i in range(4):
    root.columnconfigure(i, weight = 2, minsize = 100)
    root.rowconfigure(i, weight = 2, minsize = 75)
    for j in range(0,3):
        frame = Frame(master=root, relief= SUNKEN, borderwidth = 1)

        frame.grid(row=i, column=j)
        label = Label(master=frame, text = nums[i][j],bg = "yellow")
        label.pack(padx=3, pady= 3)
root.mainloop()