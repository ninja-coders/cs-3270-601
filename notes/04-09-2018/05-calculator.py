import tkinter

from tkinter import Tk, Label, Button, Menu, messagebox, Entry, Frame, StringVar


class CalcGui:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.create_menu()
        self.create_calculator()

    def create_menu(self):
        menu = Menu(self.master)
        self.menu = menu
        self.master.config(menu=self.menu)

        file = Menu(self.menu)
        file.add_command(label='Exit', command=self.menu_exit)
        self.menu.add_cascade(label='File', menu=file)

    def create_calculator(self):
        calc_frame = Frame()
        calc_frame.pack(padx=10, pady=10)
        #calc_frame.pack()
        
        parent = calc_frame
        Label(parent, text='Left: ').grid(row=0, sticky=tkinter.E)
        #Label(parent, text='Left: ').grid(row=0)
       
        left_entry = Entry(parent, width=30)
        left_entry.grid(row=0, column=1)
        
        Label(parent, text='Right: ').grid(row=1, sticky=tkinter.E)
        
        right_entry = Entry(parent, width=30)
        right_entry.grid(row=1, column=1)
        
        action_frame = Frame()
        action_frame.pack()
        
        parent = action_frame
        result_text = StringVar()
        result_text.set('No result')

        def calculate_result_command():
            left = int(left_entry.get())
            right = int(right_entry.get())
            solution = left + right
            result_text.set(str(solution))
        
        add_button = Button(parent, command=calculate_result_command, text='Add')
        add_button.pack(side=tkinter.LEFT)        

        result = Label(parent, textvariable=result_text)
        result.pack(side=tkinter.LEFT, padx=10)
                
    def menu_exit(self):
        #messagebox.showinfo('Title', 'Exit was called')
        self.master.destroy()

root = Tk()
root.geometry('250x100')
my_gui = CalcGui(root)
root.mainloop()


