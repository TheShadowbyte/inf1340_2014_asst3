__author__ = 'Shawn'

import tkinter
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from mining import *

class StockMinerGUI(Frame):

    def __init__(self, master=None):
        """
        initialization function for the StockMiner GUI
        :param master: Master Tkinter frame
        :return:
        """
        Frame.__init__(self, master)

        self.stock_miner = None
        self.stock_name = StringVar()
        self.result_contents = StringVar()


        self.pack()
        self.create_widgets(master)

    def create_widgets(self, main_window):
        """
        Function to initialize all the widgets and its properties
        :param main_window: Tkinter Frame variable where the UI will be displayed.
        """

        # Window Initialization
        main_window.wm_title("Stock Miner Graphical User Interface")
        main_window.wm_minsize(400,100)
        main_window.wm_maxsize(400,1000)

        # Buttons and labels initialization
        button_best_six = Button(main_window, text="Show Best Six Month", command=lambda: self.print_result_on_label(
            "BEST_MONTH"))
        button_worst_six = Button(main_window, text="Show Worst Six Month", command=lambda: self.print_result_on_label(
            "WORST_MONTH"))
        button_browse_file = Button(main_window, text="Choose Source File", command=self.open_file)
        button_quit = Button(main_window, text="Quit", command=self.quit)
        title_label = Label(main_window, text="MENU OPTIONS")
        stock_name_label = Label(main_window, textvariable=self.stock_name)
        stock_mining_result_label = Label(main_window, textvariable=self.result_contents )

        # packing all widget elements.
        title_label.pack()
        button_browse_file.pack()
        button_best_six.pack()
        button_worst_six.pack()
        button_quit.pack()
        stock_name_label.pack()
        stock_mining_result_label.pack()

    def open_file(self):
        """
        Function that opens the stock json file and gives custom stock name to opened file
        """
        try:
            dialog_box = tkinter.filedialog.askopenfile(mode='r', title="Please choose JSON file with Stock Data",
                                                        filetypes=[("JSON Stock Data file", "*.json")])
            stock_file_path = dialog_box.name
        except AttributeError:
            print('You did not choose any file')
        else:
            # initialize chosen stock name
            entered_stock_name = ""

            while entered_stock_name == "":
                self.master.withdraw()
                input_dialog = TextInputBox(self.master)
                self.master.wait_window(input_dialog.top)
                entered_stock_name = input_dialog.get_entered_value()

                if entered_stock_name == "":
                    self.warning_box("Enter Stock Name", "Please enter the stock name to proceed.")

            self.master.deiconify()

            # Initialize StockMiner variable with chosen file. Raise error if the chose file is incomplete/damaged.
            try:
                self.stock_miner = StockMiner(entered_stock_name, stock_file_path)
                temp_stock_name = "\n-Chosen Stock-\n" + self.stock_miner.stock_name
                self.stock_name.set(temp_stock_name)
                self.result_contents.set("")
            except ValueError:
                self.error_box("File Corrupted", "Chosen JSON stock file is corrupted...\nPlease choose correctly "
                                                 "formatted json stock file.")

    def print_result_on_label(self, request_type):
        """
        Function that displays either best six or worst six of chosen stock file depends on the passed parameter
        :param request_type: String variable that decides the type of output to be displayed
        """
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
        """
        display the warning dialog with passed title and contents
        :param title:Title of the warning dialog box
        :param content: Content of the warning dialog box
        """
        tkinter.messagebox.showwarning(title, content)

    @staticmethod
    def message_box(title, content):
        """
        display the normal message dialog with passed title and contents
        :param title:Title of the normal message dialog box
        :param content: Content of the normal message dialog box
        """
        tkinter.messagebox.showinfo(title, content)

    @staticmethod
    def error_box(title, content):
        """
        display the error dialog with passed title and contents
        :param title:Title of the error dialog box
        :param content: Content of the error dialog box
        """
        tkinter.messagebox.showerror(title, content)


# class for Text input box which is being used for naming the stock when JSON file is chosen.
class TextInputBox:

    def __init__(self, parent):
        """
        initialization function for the TextInputBox class
        :param parent: variable for the parents window.
        :return:
        """
        top_window = self.top = Toplevel(parent)

        Label(top_window, text="Enter Stock Name").pack()
        self.entry_dialog = Entry(top_window)
        self.entry_dialog.pack(padx=5)
        self.entered_value = ""

        b = Button(top_window, text="OK", command=self.process_entry)
        b.pack(pady=5)

    def process_entry(self):
        """
        Store the stock name entered from the input dialog to the internal class variable
        then destroy the TextInputDialog Box
        """
        self.entered_value = self.entry_dialog.get()
        self.top.destroy()

    def get_entered_value(self):
        """
        getter function to return the entered_value variable.
        :return:
        """
        return self.entered_value

if __name__ == "__main__":

    root = Tk()
    app = StockMinerGUI(root)
    app.mainloop()



