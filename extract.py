from tkinter import filedialog
from tkinter import *
from zipfile import ZipFile

root=Tk()
root.geometry("500x100")
root.title("Zip File Extractor")
root.iconbitmap("extract.ico")

def extract():
    folder=filedialog.askopenfilename()
    with ZipFile(folder, 'r') as zip:
        print("Extracting File...")
        zip.extractall()
        print("Done!")

title=Label(text="Zip File Extractor",fg="red",font=["Arial",40])
title.pack(anchor="center")

extract_button=Button(text="Extract File",width=20,bg="lightgreen",command=extract)
extract_button.pack(side="bottom")

root.mainloop()
