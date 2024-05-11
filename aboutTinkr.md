# Making a GUI application in Python using `tkinter`

> Learn the latest modern Tk features at: ***[TkDocs](https://tkdocs.com/tutorial/onepage.html)*** and ***[Tkinter Class API Reference](https://tkdocs.com/pyref/onepage.html)***

## Basic Example 
*This setup can be expanded with more functionality in each window, such as additional buttons, text entry fields, or other widgets, depending on your application's needs.*

## Step 1: Set Up a Python Environment

Make sure that you have installed Python. 
    
*Tkinter is included with Python, so no additional installation is generally needed for tkinter.*

## Step 2: Write the Code
Here's a simple example to demonstrate a Tkinter application with two windows:

```python
import tkinter as tk
from tkinter import Toplevel

def open_new_window():
    new_window = Toplevel(root)
    new_window.title("Second Window")
    new_window.geometry("300x200")
    tk.Label(new_window, text="This is the second window").pack()

# Main window setup
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Button to open a new window
open_window_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_window_button.pack(pady=50)

root.mainloop()
```

### Step 3: Explanation of the Code

1. **Importing Libraries**: We import `tkinter` for GUI components and `Toplevel` from `tkinter` for creating additional windows.

2. **Function to Open New Window**:
    - `open_new_window`: This function creates a new window (`Toplevel`) when called. `Toplevel` is a separate window that functions as a child window to the main window (`root`). It sets the title and size and adds a simple label.

3. **Main Window Setup**:
    - The `root` object is the main Tk window.
    - `title` sets the title of the window.
    - `geometry` defines the size of the window.

4. **Creating a Button**:
    - We create a button that, when clicked, will call the `open_new_window` function to open the new window.

5. **Main Event Loop**:
    - `root.mainloop()` starts the Tkinter event loop, necessary for handling user interactions and displaying the GUI.

### Step 4: Run the Code
Save the script in a `.py` file and run it using Python. Your main window will appear, and you can click the button to open additional windows.




---

Adding Images to Version 1.5

References:
[Tcl8.6.14/Tk8.6.14 Documentation](https://tcl.tk/man/tcl8.6/contents.htm) Copyright © 1989-1994 The Regents of the University of California



**[CREATING PHOTOS](https://tcl.tk/man/tcl8.6/TkCmd/image.htm)**
















> Written with [StackEdit](https://stackedit.io/).
