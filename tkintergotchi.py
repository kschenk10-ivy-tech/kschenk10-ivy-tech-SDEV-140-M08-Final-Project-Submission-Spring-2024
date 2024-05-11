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
