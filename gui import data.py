import tkinter as tk

def submit():
    name = entry_name.get()
    time = entry_time.get()
    school = entry_school.get()
    
    print(name, time, school)  # replace with DB insert

root = tk.Tk()
root.title("Enter Athlete Data")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Time").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="School").pack()
entry_school = tk.Entry(root)
entry_school.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()