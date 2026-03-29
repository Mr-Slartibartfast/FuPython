from tkinter import Tk, filedialog
import pandas as pd

Tk().withdraw()

file_path = filedialog.askopenfilename()

df = pd.read_csv(file_path)
print(df.head())