import tkinter
import tkinter.messagebox


import tkinter

class KiloConverterGUI:
    def __init__(self):
        
        self.main_window = tkinter.Tk()
        
        #top_frame is what we, the user, calls it: an attribute of the self object
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
        

        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a distance in Kilomerters:")

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)



        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side="left")
        

        self.calcbutton = tkinter.Button(self.main_window,text='Convert!',command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        
        self.calcbutton.pack(side='left')
        self.quit_button.pack(sid ='right')

       

        tkinter.mainloop()

    def do_something(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo * 0.6214),2)
        tkinter.messagebox.showinfo('Results', str(kilo) + 'kilometers is equal to ' + str(miles) + 'miles.')

        tkinter.mainloop()

kilo_conv = KiloConverterGUI()



