from tkinter import Tk, Label, Button, Menu, messagebox

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.create_menu()

    def create_menu(self):
        menu = Menu(self.master)
        self.menu = menu
        self.master.config(menu=self.menu)

        file = Menu(self.menu)
        file.add_command(label='Exit', command=self.menu_exit)
        self.menu.add_cascade(label='File', menu=file)


    def menu_exit(self):
        messagebox.showinfo('Title', 'Exit was called')

    def greet(self):
        print("Greetings!")

root = Tk()
root.geometry('400x300')
my_gui = MyFirstGUI(root)
root.mainloop()


