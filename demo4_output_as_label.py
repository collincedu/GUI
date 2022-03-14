import tkinter
import tkinter.messagebox


import tkinter

class KiloConverterGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)

        #pack
        self.top_frame.pack(side="top")
        self.mid_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        
        #create
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in Kilomerters:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        #pack
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")

        #create
        self.descr_label = tkinter.Label(self.mid_frame, text="Convert to miles:")

        self.miles_var = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_var)

        #pack
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')
        
        #create
        self.calcbutton = tkinter.Button(self.main_window,text='Convert!',command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        #pack
        self.calcbutton.pack(side='left')
        self.quit_button.pack(sid ='right')

       

        tkinter.mainloop()

    def do_something(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214),2)
        
        self.miles_var.set(miles)


kilo_conv = KiloConverterGUI()