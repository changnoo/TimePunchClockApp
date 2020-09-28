import tkinter as tk
from PIL import ImageTk,Image
import datetime
import time


# global declaration of time variables so that all functions can access them
todaysDate = datetime.date.today()
hour = time.strftime("%I")
minute = time.strftime("%M")
second = time.strftime("%S")
AM_or_PM = time.strftime("%p")
which_day = time.strftime("%A")


# simply returns today's date and time in the form of yyyy-mm-dd-hh-mm-ss
# function is executed whenever the button is pressed using the command parameter
def returnTime():
    print(datetime.datetime.today())

    with open('Manual Time Log.txt', 'a+') as logger:

        if AM_or_PM=='AM':
            logger.write(f"{todaysDate} {which_day}: started work at {hour}:{minute} AM\n")
        else:
            logger.write(f"{todaysDate} {which_day}: left work at {hour}:{minute} PM\n\n")
# this function gets the current time from the time library
# if we wanted to push a label onto the window, we would have to make a label object and give it
# parameters like text and colors. however, because we want to preiodically change our labels configuration
# after the label object has been initialized, we do it this way
# We update the time by recursively calling the function every one second
def clock():
    
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    time_Label.config(text=hour + ":" + minute + ":" +second)
    time_Label.after(1000,clock)

# initialize the window we want to work in, called "window"
window = tk.Tk()
# we can customize the geometry of the window using the geometry method
window.geometry('400x300')
# we can customize the title of our window by using the title method
window.title("PRE-ADP CO-OP time punch program")

#using the PIL library, we imported a photo onto our window and assigned it to my_img
my_img = ImageTk.PhotoImage(Image.open("Corvus Energy Logo.png"))

# label widget is a standard Tkinter widget used to display a text or image on the screen
# in this case, I assigned an image to the label and packed it onto the window
my_Label = tk.Label(image=my_img)
my_Label.pack()


# here we initialize a label object called time_label, and give it parameters
# pady pushes its placement downward by the specified amount
time_Label = tk.Label(window, text='', font=('Verdana',50), fg='white', bg='black')
time_Label.pack(pady=10)

# because we wanted the clock to be put onto the window before the button, we initialize the button widget after
# the time_label has been initialized
# using the command parameter, we call the function "returnTime" whenever the button has been pressed
button1 = tk.Button(window, text="Click to get a time stamp", command = returnTime, height=5, width =20)

# just to make it look more tidy, I gave it 20 paddies
button1.pack(pady=20)

# here we simply call the function clock to display the clock on the window
# because all the labels have been initialized and packed, it should show up nicely
clock()

# this ensures that there is a window
window.mainloop()