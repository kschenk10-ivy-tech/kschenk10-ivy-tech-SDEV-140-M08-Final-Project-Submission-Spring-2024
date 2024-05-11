Khristin Schenk<br>
May 11th, 2024
SDEV-140

# M08-Final-Project-Submission


```plaintext
 _   _    _       _                       _       _     _ 
| |_| | _(_)_ __ | |_ ___ _ __ __ _  ___ | |_ ___| |__ (_)
| __| |/ / | '_ \| __/ _ \ '__/ _` |/ _ \| __/ __| '_ \| |
| |_|   <| | | | | ||  __/ | | (_| | (_) | || (__| | | | |
 \__|_|\_\_|_| |_|\__\___|_|  \__, |\___/ \__\___|_| |_|_|
                              |___/                       
```

![](https://github.com/kschenk10-ivy-tech/kschenk10-ivy-tech-SDEV-140-M08-Final-Project-Submission-Spring-2024/blob/main/Screenshot%202024-05-11%20095705.png?raw=true)


- [GitHub Repository: M08](https://github.com/kschenk10-ivy-tech/SDEV-140-M08-Final-Project-Submission-Spring-2024)

- [Download the source code zip file](https://github.com/kschenk10-ivy-tech/SDEV-140-M08-Final-Project-Submission-Spring-2024/archive/refs/heads/main.zip)

![](https://github.com/kschenk10-ivy-tech/kschenk10-ivy-tech-SDEV-140-M08-Final-Project-Submission-Spring-2024/blob/main/Screenshot%202024-05-11%20142303.png?raw=true)

```python
# Version 1.0
# Program: `tkintergotchi.py`

"""
# Last updated on May 10th, 2024 by K.S.
This Python script is a simple implementation of a tkintergotchi-like game using the `tkinter` library for GUI development.
"""
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

class Pet:
    def __init__(self, name, hunger, happiness, cleanliness, health):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.cleanliness = cleanliness
        self.health = health

    def feed(self):
        self.hunger = max(0, self.hunger - 10)

    def play(self):
        self.happiness = min(100, self.happiness + 10)

    def clean(self):
        self.cleanliness = min(100, self.cleanliness + 10)

    def doctor(self):
        self.health = min(100, self.health + 10)

    def time_pass(self):
        self.hunger += 5
        self.happiness -= 5
        self.cleanliness -= 5
        self.health -= 5 if self.hunger > 50 or self.cleanliness < 50 else 0

    def is_alive(self):
        return self.health > 0

class Monster(Pet):
    def __init__(self, name):
        super().__init__(name, 50, 50, 50, 50)

class BlackCat(Pet):
    def __init__(self, name):
        super().__init__(name, 30, 70, 70, 60)

class IceBat(Pet):
    def __init__(self, name):
        super().__init__(name, 40, 60, 40, 80)

class tkintergotchiGame:
    def __init__(self, master):
        self.master = master
        self.master.title("tkintergotchi Virtual Pet Game")
        self.pet = None
        self.init_pet_selection()

    def init_pet_selection(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Enter your pet's name:").pack()
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.pack()

        tk.Label(self.frame, text="Choose your pet type:").pack()
        self.pet_type = tk.StringVar()
        self.pet_type.set("Monster")  # default value
        pet_options = ["Monster", "BlackCat", "IceBat"]
        for option in pet_options:
            ttk.Radiobutton(self.frame, text=option, value=option, variable=self.pet_type).pack()

        ttk.Button(self.frame, text="Start Game", command=self.start_game).pack()

    def start_game(self):
        pet_name = self.name_entry.get()
        pet_type = self.pet_type.get()
        if pet_type == "Monster":
            self.pet = Monster(pet_name)
        elif pet_type == "BlackCat":
            self.pet = BlackCat(pet_name)
        elif pet_type == "IceBat":
            self.pet = IceBat(pet_name)
        else:
            messagebox.showerror("Error", "Invalid pet type selected!")
            return

        self.frame.destroy()  # Remove the selection frame
        self.setup_game_interface()

    def setup_game_interface(self):
        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()

        ttk.Button(self.master, text="Feed", command=lambda: self.interact_with_pet('feed')).pack()
        ttk.Button(self.master, text="Play", command=lambda: self.interact_with_pet('play')).pack()
        ttk.Button(self.master, text="Clean", command=lambda: self.interact_with_pet('clean')).pack()
        ttk.Button(self.master, text="Doctor", command=lambda: self.interact_with_pet('doctor')).pack()
        self.update_status()

    def interact_with_pet(self, action):
        if action == 'feed':
            self.pet.feed()
        elif action == 'play':
            self.pet.play()
        elif action == 'clean':
            self.pet.clean()
        elif action == 'doctor':
            self.pet.doctor()
        self.update_status()

    def update_status(self):
        if not self.pet.is_alive():
            messagebox.showinfo("Game Over", f"{self.pet.name} has passed away!")
            self.master.quit()
        else:
            status = f"{self.pet.name} - Health: {self.pet.health}, Hunger: {self.pet.hunger}, Happiness: {self.pet.happiness}, Cleanliness: {self.pet.cleanliness}"
            self.status_label.config(text=status)

def main():
    root = tk.Tk()
    game = tkintergotchiGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

## How it works:  Code: Version 1.0
## User Manual and Documentation

This Python script is designed to run a virtual pet game called "tkintergotchi," built using the `tkinter` library in Python.

> [tkintergotchi.py](https://github.com/kschenk10-ivy-tech/kschenk10-ivy-tech-SDEV-140-M08-Final-Project-Submission-Spring-2024/blob/main/tkintergotchi.py)

 Here's a breakdown of the script's components and functionality:

### Imports and Dependencies
- **`tkinter as tk`**: This is Python's standard GUI (Graphical User Interface) toolkit, used here to create and manage various GUI components.
- **`from tkinter import simpledialog, messagebox, ttk`**: Imports additional specific modules from `tkinter`:
  - `simpledialog` provides simple dialogues to interact with the user (not directly used in this script).
  - `messagebox` is used to display message boxes for alerts and errors.
  - `ttk` (Themed Tkinter) is used for access to Tk themed widget set, which allows for styling of the GUI components.

### Classes and Methods
- **`Pet` class**: This class models a generic virtual pet. It initializes a pet with attributes like name, hunger, happiness, cleanliness, and health, and includes methods to feed, play with, clean, and provide medical attention to the pet. The `time_pass` method simulates the passage of time affecting the pet's stats, and `is_alive` checks the pet's health to determine if it is still alive.

- **`Monster`, `BlackCat`, `IceBat` classes**: These classes inherit from `Pet` and represent specific types of pets, each initialized with different default values for their attributes, making each pet type unique in its needs and care.

- **`tkintergotchiGame` class**: This is the main class for the game, handling the GUI and game interactions. It initializes the main window and setups the pet selection interface. Based on user input, it creates an instance of the chosen pet type. The game interface includes buttons to interact with the pet and a status label to display the pet's current state. Methods within this class allow for the updating of the pet's status and handling user interactions like feeding and playing.

### Game Flow
1. **Initialization**: Upon starting the game, the user is prompted to enter a name for their pet and select the type of pet from options (Monster, BlackCat, IceBat).

2. **Game Interface**: After selecting the pet, the main game interface is set up with buttons for different interactions (Feed, Play, Clean, Doctor) and a display for the pet's status (health, hunger, happiness, cleanliness).

3. **Interactions**: Each button triggers a specific method in the `Pet` class that affects the pet's attributes. The status label updates to reflect these changes.

4. **Game Over Condition**: The game checks if the pet is alive (based on the health attribute). If the pet dies, a game over message is shown, and the application closes.

5. **Running the Game**: The game is encapsulated in a `main()` function that creates a root window and runs the game loop until the application is closed.

This script showcases object-oriented programming principles and GUI development in Python, providing a simple yet interactive application.



[![](https://mermaid.ink/img/pako:eNptlN9P2zAQx_-VU_awl-NlCKQVaRNJ2lLoT9ICxa2QSRxiNY2jxIFVDf_7YjuBZKMv9d3ne3f2-eKj5YuAWT3rJaNpBEv3YpNA9bskcscTybIXIf2ID-mebeHk5FfJEy5LsIn6f0qZfMpZzHzJRbI1kbaSgUP6KhrmTH7PYarC29glTiREzhSH5SHt0j7xJM0kqKpgF1J-JO_rPYgE_Jj7uxIGRydi_u4jzbuRDbRsIpK82kMJQ-JkjEoGtWfbVtkx9XcOrQ511cgaV0c38pmtVKNGZRxdTfJKYx6UcE28SLxBP8tEU22oj3ZDXJbLTBzAa_oGg-yzPVdGZYxR27jWhm2MG22MicdkkZo-jVS_Q-o3mcZaMlGtlEUOY_rM4g6akgFjQbe_hszIPKaHr8icODGjyVdoQVzhS5F12VSzW1Pqsj0nM008U6pD5pos61IdtNBo1ZTqsFvN7sgqDdT1mHPXzDPMGMu2sWobd_oWzUjxEC5j_spKuD-OcrP-Xc_XvdatWV7CQ7ceuDxPqxNt28KpKGFNamJua_b6MYZrvYNHsii4GfnKb4gf0zx3WQgBC2kRSwh5HPe-hT9DVDO0Y71vp6en9frkjQcy6v1I_1z8E60-1Tr0-fkzNDw__y-0cQQ0j2iW0UMPzhDO2hnBRgdd7OMAh3iFI7zGGxzjBKc4wzku8BY9XOIK7_AeH3CNj3oDFxZae5btKQ-q1-aoEm4sGbE921i9akkLKTbWJnmvdGrtHRLf6smsYGgVusMup9UjtW-cLODVCEzM66UfMbRSmjwKUUve_wKEfH9I?type=png)](https://mermaid.live/edit#pako:eNptlN9P2zAQx_-VU_awl-NlCKQVaRNJ2lLoT9ICxa2QSRxiNY2jxIFVDf_7YjuBZKMv9d3ne3f2-eKj5YuAWT3rJaNpBEv3YpNA9bskcscTybIXIf2ID-mebeHk5FfJEy5LsIn6f0qZfMpZzHzJRbI1kbaSgUP6KhrmTH7PYarC29glTiREzhSH5SHt0j7xJM0kqKpgF1J-JO_rPYgE_Jj7uxIGRydi_u4jzbuRDbRsIpK82kMJQ-JkjEoGtWfbVtkx9XcOrQ511cgaV0c38pmtVKNGZRxdTfJKYx6UcE28SLxBP8tEU22oj3ZDXJbLTBzAa_oGg-yzPVdGZYxR27jWhm2MG22MicdkkZo-jVS_Q-o3mcZaMlGtlEUOY_rM4g6akgFjQbe_hszIPKaHr8icODGjyVdoQVzhS5F12VSzW1Pqsj0nM008U6pD5pos61IdtNBo1ZTqsFvN7sgqDdT1mHPXzDPMGMu2sWobd_oWzUjxEC5j_spKuD-OcrP-Xc_XvdatWV7CQ7ceuDxPqxNt28KpKGFNamJua_b6MYZrvYNHsii4GfnKb4gf0zx3WQgBC2kRSwh5HPe-hT9DVDO0Y71vp6en9frkjQcy6v1I_1z8E60-1Tr0-fkzNDw__y-0cQQ0j2iW0UMPzhDO2hnBRgdd7OMAh3iFI7zGGxzjBKc4wzku8BY9XOIK7_AeH3CNj3oDFxZae5btKQ-q1-aoEm4sGbE921i9akkLKTbWJnmvdGrtHRLf6smsYGgVusMup9UjtW-cLODVCEzM66UfMbRSmjwKUUve_wKEfH9I)


### Imports and Dependencies
```python
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
```
This section imports the necessary components from `tkinter`, a standard GUI toolkit in Python. It specifically imports the `messagebox` and `ttk` modules which are used for creating dialog boxes and styled widgets, respectively.

### Pet Class
```python
class Pet:
    ...
```
The `Pet` class is a base class representing a generic pet with attributes for `name`, `hunger`, `happiness`, `cleanliness`, and `health`. It also includes methods to modify these attributes (`feed`, `play`, `clean`, `doctor`) and to simulate time passing (`time_pass`), which affects the pet's attributes. There's also a method `is_alive` to check the pet's health.

### Subclasses of Pet
```python
class Monster(Pet):
    ...
class BlackCat(Pet):
    ...
class IceBat(Pet):
    ...
```
These subclasses (`Monster`, `BlackCat`, `IceBat`) extend `Pet` with specific starting values for the pet’s attributes. Each type of pet starts with different levels of hunger, happiness, cleanliness, and health.

### tkintergotchiGame Class
```python
class tkintergotchiGame:
    ...
```
This class handles the main game mechanics. It initializes the GUI, lets the user select a pet type, and manages game interactions such as feeding and playing with the pet. Here are the key methods:
- `init_pet_selection()`: Sets up the initial GUI for choosing a pet type and entering a pet name.
- `start_game()`: Retrieves the selected pet type and name, instantiates the appropriate pet subclass, and transitions to the game interface.
- `setup_game_interface()`: Creates the GUI for interacting with the pet (buttons for feeding, playing, etc.).
- `interact_with_pet(action)`: Calls the appropriate pet method based on the button pressed (feed, play, clean, doctor).
- `update_status()`: Updates the GUI with the pet's current status and checks if the pet is still alive.

### Main Function
```python
def main():
    ...
```
The `main()` function sets up the main window (`root`) and starts the game by creating an instance of `tkintergotchiGame`.

### Program Entry Point
```python
if __name__ == "__main__":
    main()
```


---
## Validation Testing and Documentation
Tests for button functionality, Tamagotchi growth stages, and error handling.



## 1. Functional Testing
This involves testing the functions of the Tamagotchi application to ensure they behave as expected.

The data structure and content:
- **Test Case ID**
- **Description**
- **Steps**
- **Expected Result**
- **Actual Result**
- **Status (Pass/Fail)**

> This document [Download the Excel file](#) outlines the style for validation testing and provides a test case template to efficiently track testing activities.

### Test Cases:

**TC1: Tamagotchi Growth**
- **Objective:** Ensure the Tamagotchi progresses through its life stages correctly.
- **Steps:** Initialize the application, simulate the passage of time or actions to increase age, and observe the stage transitions from Egg to Child to Adult.
- **Expected Result:** The Tamagotchi’s stage should update at the defined ages (5 for Child, 10 for Adult).

**TC2: Feeding Mechanism**
- **Objective:** Validate that feeding decreases hunger.
- **Steps:** Note the initial hunger level, click the feed button, and check the hunger level again.
- **Expected Result:** Hunger level should decrease by 1 with each feed action, not dropping below 0.

**TC3: Health and Sickness**
- **Objective:** Test that the health management and sickness features work.
- **Steps:** Induce sickness by using the `random_events` method or a button if implemented. Administer medicine and check health improvement.
- **Expected Result:** If sick, the health should improve by 1 and the sickness status should clear after administering medicine.

**TC4: Happiness and Play**
- **Objective:** Ensure that playing with the Tamagotchi increases happiness.
- **Steps:** Check the initial happiness, use the play function or a corresponding button, and recheck the happiness level.
- **Expected Result:** Happiness should increase by 1 with each play action, not exceeding 10.

**TC5: Discipline**
- **Objective:** Check if the discipline functionality works as expected.
- **Steps:** Observe the initial discipline level, apply discipline, and check the level again.
- **Expected Result:** Discipline level should increase by 1 with each action, not exceeding 10.

**TC6: Toilet Needs**
- **Objective:** Ensure that the toilet needs and flushing system functions.
- **Steps:** Manually set `needs_toilet` to True, use the flush function, and check the status.
- **Expected Result:** `needs_toilet` should become False after the flush.

## 2. Interface Testing
Test the GUI elements for functionality and to ensure they are displaying the correct information.

### Test Cases:

**TC7: GUI Updates**
- **Objective:** Validate that all GUI labels update correctly when actions are taken.
- **Steps:** Perform actions like feeding or playing and observe the changes in the GUI labels for hunger, happiness, and health.
- **Expected Result:** All labels should reflect the current status of the Tamagotchi correctly after any action.

**TC8: Button Functionality**
- **Objective:** Ensure all buttons trigger their respective functions.
- **Steps:** Click each button in the application and observe the expected action.
- **Expected Result:** Each button should perform its defined function without errors.

### 3. Error Handling
Test how the application handles unexpected user input or actions.

#### Test Cases:

**TC9: Overfeeding**
- **Objective:** Confirm the application handles overfeeding without crashing or errors.
- **Steps:** Attempt to feed the Tamagotchi when hunger is at 0.
- **Expected Result:** Application should not allow hunger to go below 0 and should handle the action gracefully, possibly with a message or no change in the hunger level.

**TC10: Excessive Playing**
- **Objective:** Check the handling of continuous play actions when happiness is maxed out.
- **Steps:** Max out the happiness level and attempt to increase it further.
- **Expected Result:** Happiness should not exceed 10, and the system should handle it appropriately.

### Documentation and Reporting
- [Download the Microsoft Excel File](#)


---

<!--
![](https://assets.codepen.io/6566924/favicon-96x96.png)

## Let's Connect
[CodePen](https://codepen.io/Khristin-Schenk) | [GitHub](https://github.com/kschenk10-ivy-tech)

Send electronic mail to:  [*khristinschenk@gmail.com*](mailto:khristinschenk@gmail.com)

Send ***Snail Mail*** to: **Khristin Schenk**
📍U.S.A. North America, Planet Earth, Solar System, Oort Cloud, Local Interstellar Cloud, Local Cavity, Orion Arm, Milky Way, Local Group, Virgo Supercluster, Laniakea Supercluster, the Universe.


---

> Written with [StackEdit](https://stackedit.io/).
