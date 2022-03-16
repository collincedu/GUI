import tkinter
import tkinter.messagebox


import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #Int attrubute
        self.radio_var = tkinter.IntVar()

        #create radio buttons
        self.rb1 = tkinter.Radiobutton(self.top_frame, text='Option 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Option 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Option 3', variable=self.radio_var, value=3)

        #set the default button 
        self.rb1.select()
        
        #pack radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        #create more buttons
        self.okbutton = tkinter.Button(self.bottom_frame,text='Ok!',command=self.show_choice)
        self.resetbutton = tkinter.Button(self.bottom_frame,text='Reset',command=self.rb1.select)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        #pack
        self.okbutton.pack(side='left')
        self.resetbutton.pack(side='left')
        self.quit_button.pack(sid ='right')

        #pack
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("selection", "You have selection option" + str(self.radio_var.get()))
      


my_GUI = MyGUI()