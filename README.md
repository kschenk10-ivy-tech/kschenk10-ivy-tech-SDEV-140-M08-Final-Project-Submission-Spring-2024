Khristin Schenk
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
- [GitHub Repository: M08](https://github.com/kschenk10-ivy-tech/SDEV-140-M08-Final-Project-Submission-Spring-2024)

- [Download the source code zip file](https://github.com/kschenk10-ivy-tech/SDEV-140-M08-Final-Project-Submission-Spring-2024/archive/refs/heads/main.zip)

### Code: Version 1.0

```python
# Version 1.0
# Last updated on May 10th, 2024 by K.S. 
import tkinter as tk
import random

class Tamagotchi:
    def __init__(self):
        self.hunger = 5
        self.happiness = 5
        self.health = 5
        self.discipline_level = 5
        self.is_sick = False
        self.needs_toilet = False
        self.age = 0
        self.stage = "Egg"

    def grow(self):
        self.age += 1
        if self.age == 5:
            self.stage = "Child"
        elif self.age == 10:
            self.stage = "Adult"

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1

    def play(self):
        if self.happiness < 10:
            self.happiness += 1

    def give_medicine(self):
        if self.is_sick:
            self.is_sick = False
            self.health += 1

    def flush(self):
        if self.needs_toilet:
            self.needs_toilet = False

    def check_health(self):
        return f"Health: {self.health}, Hunger: {self.hunger}, Happiness: {self.happiness}, Discipline: {self.discipline_level}"

    def discipline(self):
        if self.discipline_level < 10:
            self.discipline_level += 1

    def random_events(self):
        if random.randint(1, 5) == 1:
            self.is_sick = True
        if random.randint(1, 5) == 1:
            self.needs_toilet = True

# Initialize the Tamagotchi instance
tamagotchi = Tamagotchi()

def update_gui():
    hunger_label.config(text=f"Hunger: {tamagotchi.hunger}")
    happiness_label.config(text=f"Happiness: {tamagotchi.happiness}")
    health_label.config(text=f"Health: {tamagotchi.health}")
    discipline_label.config(text=f"Discipline: {tamagotchi.discipline_level}")
    stage_label.config(text=f"Stage: {tamagotchi.stage}")

def feed_tamagotchi():
    tamagotchi.feed()
    update_gui()

root = tk.Tk()
root.title("Tamagotchi Simulator")

stage_label = tk.Label(root, text=f"Stage: {tamagotchi.stage}")
stage_label.pack()

hunger_label = tk.Label(root, text=f"Hunger: {tamagotchi.hunger}")
hunger_label.pack()

happiness_label = tk.Label(root, text=f"Happiness: {tamagotchi.happiness}")
happiness_label.pack()

health_label = tk.Label(root, text=f"Health: {tamagotchi.health}")
health_label.pack()

discipline_label = tk.Label(root, text=f"Discipline: {tamagotchi.discipline_level}")
discipline_label.pack()

feed_button = tk.Button(root, text="Feed", command=feed_tamagotchi)
feed_button.pack()

root.mainloop()
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
