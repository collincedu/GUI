import tkinter
import tkinter.messagebox


import tkinter

class MyGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        #pack
        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3.pack(side="top")
        self.frame4.pack(side="top")
        self.frame5.pack(side="top")
        
        #create
        self.test1 = tkinter.Label(self.frame1, text="Enter the score for test 1:")
        self.test1_entry = tkinter.Entry(self.frame1, width=10)

        self.test2 = tkinter.Label(self.frame2, text="Enter the score for test 2:")
        self.test2_entry = tkinter.Entry(self.frame2, width=10)

        self.test3 = tkinter.Label(self.frame3, text="Enter the score for test 3:")
        self.test3_entry = tkinter.Entry(self.frame3, width=10)

        #pack
        self.test1.pack(side="left")
        self.test1_entry.pack(side="left")
        self.test2.pack(side="left")
        self.test2_entry.pack(side="left")
        self.test3.pack(side="left")
        self.test3_entry.pack(side="left")

        #Create average label
        self.desc_label = tkinter.Label(self.frame4, text="Average:")
        self.average_var = tkinter.StringVar()
        self.average_label = tkinter.Label(self.frame4, textvariable=self.average_var)

        #pack
        self.desc_label.pack(side='left')
        self.average_label.pack(side='left')
        #Buttons
        self.mybutton = tkinter.Button(self.main_window,text='Average',command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        self.mybutton.pack(side='left')
        self.quit_button.pack(sid ='left')


        tkinter.mainloop()

    def do_something(self):
    
        score1 = float(self.test1_entry.get())
        score2 = float(self.test2_entry.get())
        score3 = float(self.test3_entry.get())

        average = round(((score1 + score2 + score3) / 3),2) 
        
        self.average_var.set(average)
        



        tkinter.messagebox.showinfo('Response',self.message)

        tkinter.mainloop()

my_gui = MyGUI()