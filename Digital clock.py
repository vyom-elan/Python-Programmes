from tkinter import Label, Tk 
import time
clock_win = Tk()
clock_win.resizable(0,0)           #to resize the window generated change the condition to true(1,1)
clock_win.title("Clock") 
clock_win.geometry("1080x720")      #Dimension of the window generated of the clock 
text_font= ("Times New Roman", 80, 'italic')
background = "#8666b3"      #Violet colour
foreground= "#000000"       #Black colour
border_width = 250          #dimensions of the clock inside the window
label = Label(clock_win, font=text_font, bg=background, fg=foreground, bd=border_width) #for the application
label.grid(row=0, column=1)
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)
digital_clock()
clock_win.mainloop()
