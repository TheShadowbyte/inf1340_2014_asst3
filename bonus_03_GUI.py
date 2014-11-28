    __author__ = 'Shawn'

import tkinter
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from mining import *

class StockMinerGUI(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.stock_miner = None
        self.stock_name = StringVar()
        self.result_contents = StringVar()

        self.pack()
        self.create_widgets(master)


    def create_widgets(self, main_window):

        main_window.wm_title("Stock Miner Graphical User Interface")

        main_window.wm_minsize(400,100)
        main_window.wm_maxsize(400,1000)

        button_best_six = Button(main_window, text="Show Best Six Month", command=lambda: self.print_result_on_label(
            "BEST_MONTH"))
        button_worst_six = Button(main_window, text="Show Worst Six Month", command=lambda: self.print_result_on_label(
            "WORST_MONTH"))
        button_browse_file = Button(main_window, text="Choose Source File", command=self.open_file)
        button_quit = Button(main_window, text="Quit", command=self.quit)
        title_label = Label(main_window, text="MENU OPTIONS")
        stock_name_label = Label(main_window, textvariable=self.stock_name)
        stock_mining_result_label = Label(main_window, textvariable=self.result_contents )

        title_label.pack()
        button_browse_file.pack()
        button_best_six.pack()
        button_worst_six.pack()
        button_quit.pack()
        stock_name_label.pack()
        stock_mining_result_label.pack()

    def open_file(self):
        try:
            dialog_box = tkinter.filedialog.askopenfile(mode='r', title="Please choose JSON file with Stock Data",
                                                        filetypes=[("JSON Stock Data file", "*.json")])
            stock_file_path = dialog_box.name
        except AttributeError:
            print('You did not choose any file')
        else:
            #initialize
            entered_stock_name = ""
            while entered_stock_name == "":
                self.master.withdraw()
                input_dialog = TextInputBox(self.master)
                self.master.wait_window(input_dialog.top)
                entered_stock_name = input_dialog.get_entered_value()
                if entered_stock_name == "":
                    self.warning_box("Enter Stock Name", "Please enter the stock name to proceed.")

            self.master.deiconify()

            try:
                self.stock_miner = StockMiner(entered_stock_name, stock_file_path)
                temp_stock_name = "\n-Chosen Stock-\n" + self.stock_miner.stock_name
                self.stock_name.set(temp_stock_name)
                self.result_contents.set("")
            except ValueError:
                self.error_box("File Corrupted", "Chosen JSON stock file is corrupted...\nPlease choose correctly "
                                                 "formatted json stock file.")


    def print_result_on_label(self, request_type):
        if self.stock_miner is None:
            self.warning_box("Stock file not initialized", "Stock has not been initialized.\n "
                                                           "Please choose the stock file first.")
        else:
            try:
                if request_type == "BEST_MONTH":
                    temp_list = self.stock_miner.six_best_months()
                    temp_result_text = "-Showing Six Best Months-\n"
                else:
                    temp_list = self.stock_miner.six_worst_months()
                    temp_result_text = "-Showing Six Worst Months-\n"

                for (month, price) in temp_list:
                    temp_result_text += month + ": $" + str(price) + '\n'
                self.result_contents.set(temp_result_text)

            except KeyError:
                self.error_box("File Corrupted", "Chosen JSON stock file is corrupted...")


    @staticmethod
    def warning_box(title, content):
        tkinter.messagebox.showwarning(title, content)

    @staticmethod
    def message_box(title, content):
        tkinter.messagebox.showinfo(title, content)

    @staticmethod
    def error_box(title, content):
        tkinter.messagebox.showerror(title, content)


class TextInputBox:
    def __init__(self, parent):

        top_window = self.top = Toplevel(parent)

        Label(top_window, text="Enter Stock Name").pack()
        self.entry_dialog = Entry(top_window)
        self.entry_dialog.pack(padx=5)
        self.entered_value = ""

        b = Button(top_window, text="OK", command=self.process_entry)
        b.pack(pady=5)

    def process_entry(self):
        self.entered_value = self.entry_dialog.get()
        self.top.destroy()

    def get_entered_value(self):
        return self.entered_value

if __name__ == "__main__":

    root = Tk()
    app = StockMinerGUI(root)
    app.mainloop()



