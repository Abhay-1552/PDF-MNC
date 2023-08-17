from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import os


class Pdf:
    def __init__(self):
        self.file_list = []

        self.win = Tk()
        self.win.geometry("500x400")
        self.win.config(bg="lightblue")
        self.win.title("PDFs Merger and Compressor")
        self.win.resizable(False, False)

        self._label_first = Label(self.win, text="< PDFs Merger and Compressor >", font=("Arial", 20), fg="black",
                                  bg="lightblue")
        self._label_first.place(x=37, y=10)

        self._textbox = scrolledtext.ScrolledText(self.win, undo=True, height=10, width=20, font=("Arial", 15))
        self._textbox.place(x=230, y=100)

        self._textbox.insert(INSERT, "   <~ Selected PDFs ~>\n")
        self._textbox.insert(INSERT, "____________________\n")

        self._button_key = Button(self.win, text="Select PDFs", font=("Arial", 15), bg="lime", width=15,
                                  command=self.pdf_files)
        self._button_key.place(x=30, y=100)

        self._button_sum = Button(self.win, text="Merge PDFs", font=("Arial", 15), bg="lime", width=15,
                                  command=self.merge)
        self._button_sum.place(x=30, y=150)

        self._button_sum = Button(self.win, text="Compress PDF", font=("Arial", 15), bg="lime", width=15,
                                  command=self.compress)
        self._button_sum.place(x=30, y=200)

        self._button_clear = Button(self.win, text="Clear", font=("Arial", 15), bg="lime", width=15,
                                    command=self.clear)
        self._button_clear.place(x=30, y=250)

        self._button_exit = Button(self.win, text="Exit", font=("Arial", 15), width="15", bg="lime",
                                   command=self.close)
        self._button_exit.place(x=30, y=300)

        self.win.mainloop()

    def pdf_files(self):
        root = Tk()
        root.withdraw()
        file_type = dict(defaultextension=".pdf", filetypes=[("pdf file", "*.pdf")])
        file_path = filedialog.askopenfilename(**file_type)

        file = file_path.split("/")

        self.file_list.append(file_path)
        self._textbox.insert(INSERT, file[-1] + "\n")

    def merge(self):
        merge = PdfMerger()

        for pdf in self.file_list:
            merge.append(pdf)

        output_path = os.path.expanduser("~/Downloads/Merged_files.pdf")
        merge.write(output_path)
        merge.close()

    def compress(self):
        for file in self.file_list:
            reader = PdfReader(file)
            writer = PdfWriter()
            file_name = file

            for page in reader.pages:
                page.compress_content_streams()
                writer.add_page(page)

            output_path = os.path.expanduser(f"~/Downloads/{file_name}_compressed.pdf")
            with open(output_path, "wb") as f:
                writer.write(f)

    def clear(self):
        self._textbox.delete(3.0, "end-1c")
        self.file_list.clear()

    def close(self):
        self.win.destroy()


if __name__ == "__main__":
    pdf_app = Pdf()
