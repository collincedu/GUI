
import tkinter
import tkinter.messagebox


import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        

        self.label1 = tkinter.Label(self.top_frame, text="John")

        self.label2 = tkinter.Label(self.top_frame, text="Jill")

        self.label3 = tkinter.Label(self.top_frame, text="James")

        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

        self.label4 = tkinter.Label(self.top_frame, text="John")
        self.label5 = tkinter.Label(self.top_frame, text="Jill")
        self.label6 = tkinter.Label(self.top_frame, text="James")
        
        self.label4.pack(side="left")
        self.label5.pack(side="left")
        self.label6.pack(side="left")

        self.mybutton = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        self.mybutton.pack(side='left')
        self.quit_button.pack(sid ='right')

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

        tkinter.mainloop()

my_gui = MyGUI()

print("moving on...")


