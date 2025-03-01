##import tinker library
import tkinter as tk
from tkinter import ttk

#Declaring the function
def on_select(event):

    #Create an item object that obtains the value of the selected item.
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Create the root window object and Set the title of the window
root = tk.Tk()
root.title("Kibrom is silly")    

#Listing Items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
#Create the combo box object, put the object in the root window and populate values.
combo_box = ttk.Combobox(root, values=items)

#The bind function will tie the selected item to the on_selected function.
combo_box.bind("<<ComboboxSelected>>", on_select)
#Pack the
combo_box.pack()

#mainloop keep the root parent window visible. 
root.mainloop()
#