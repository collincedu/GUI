import tkinter
import tkinter.messagebox


import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #create three IntVar objects to sue with
        #the Checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #set the Intvar objects to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)


        self.cb1 = tkinter.Checkbutton(self.top_frame, text="Option1", variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text="Option2", variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text="Option3", variable=self.cb_var3)

        #pack
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.mybutton = tkinter.Button(self.main_window,text='Ok!',command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        self.mybutton.pack(side='bottom')
        self.quit_button.pack(sid ='bottom')

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        tkinter.mainloop()

    def do_something(self):
        self.message = 'You have selected:\n'

        if self.cb_var1.get() == 1:
            self.message += '1\n'
        if self.cb_var2.get() == 1:
            self.message += '2\n'
        if self.cb_var3.get() == 1:
            self.message += '3\n'

        tkinter.messagebox.showinfo('Response',self.message)

my_gui = MyGUI()


