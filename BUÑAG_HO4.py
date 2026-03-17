import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.configure(bg="lightblue")
window.geometry("600x300")
window.resizable(False,False)

title = tk.Label(window, text = "Profile Builder")
title.grid(row=0,column=1)

frame = tk.Label(window, bg="pink")
frame.grid()
first_name = tk.Label(frame, text = "First Name")
first_name.grid(row=4,column=2)

first_entry = tk.Entry(frame)
first_entry.grid(row=3,column=2)

middle_name = tk.Label(frame, text = "Middle Name")
middle_name.grid(row=4,column=5)
middle_entry = tk.Entry(frame)
middle_entry.grid(row=3,column=5)

last_name = tk.Label(frame, text = "Last Name")
last_name.grid(row=4,column=7)
last_entry = tk.Entry(frame)
last_entry.grid(row=3,column=7)

year_born = tk.Label(frame,text="Year Born")
year_born.grid(row=6,column=2)
year_entry= tk.Entry(frame)
year_entry.grid(row=5,column=2)

male_label = tk.Label(frame,text="Male")


window.mainloop()

