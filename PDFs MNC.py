from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from PyPDF2 import PdfMerger
from pypdf import PdfReader, PdfWriter
import os

global file_list
file_list = []

win = Tk()
win.geometry("500x400")
win.config(bg="lightblue")
win.title("PDFs Merger and Compresser")
win.resizable(False, False)


def pdf_files():
    root = Tk()
    root.withdraw()
    file_type = dict(defaultextension=".pdf", filetypes=[("pdf file", "*.pdf")])
    file_path = filedialog.askopenfilename(**file_type)

    file = file_path.split("/")

    file_list.append(file[-1])
    _textbox.insert(INSERT, file[-1]+"\n")


def Merge():
    merge = PdfMerger()
    
    for pdf in file_list:
        merge.append(pdf)

    merge.write("Merged_files.pdf")
    merge.close()


def Compress():
    for file in file_list:
        reader = PdfReader(file)
        writer = PdfWriter()
        file_name = file
        
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        with open(file_name+"_compressed.pdf", "wb") as f:
            writer.write(f)


def Clear():
    _textbox.delete(3.0, "end-1c")
    file_list.clear()


def Exit():
    win.destroy()


_label_first = Label(win, text="< PDFs Merger and Compresser >", font=("Arial", 20), fg="black", bg="lightblue")
_label_first.place(x=37, y=10)

_textbox = scrolledtext.ScrolledText(win, undo=True, height=10, width=20, font=("Arial",15))
_textbox.place(x=230, y=100)

_textbox.insert(INSERT, "   <~ Selected PDFs ~>"+"\n")
_textbox.insert(INSERT, "____________________"+"\n")

_button_key = Button(win, text="Select PDFs", font=("Arial", 15), bg="lime", width=15, command=pdf_files)
_button_key.place(x=30, y=100)

_button_sum = Button(win, text="Merge PDFs", font=("Arial", 15), bg="lime", width=15, command=Merge)
_button_sum.place(x=30, y=150)

_button_sum = Button(win, text="Compress PDF", font=("Arial", 15), bg="lime", width=15, command=Compress)
_button_sum.place(x=30, y=200)

_button_clear = Button(win, text="Clear", font=("Arial", 15), bg="lime", width=15, command=Clear)
_button_clear.place(x=30, y=250)

_button_exit = Button(win, text="Exit", font=("Arial", 15), width="15", bg="lime", command=Exit)
_button_exit.place(x=30, y=300)

win.mainloop()
