#import tinker library
import tkinter as tk

#declaring the function
def button_click():
    print("Button Clicked")

#Create the root window
root=tk.Tk()
root.title("Button Example")    


#create the button object, including the 3 argument 
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack()

#
root.mainloop()
