import tkinter as tk
from tkinter import messagebox
import webbrowser  

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def show_commands(self):
        return "\n".join(self.commands)

class PetRegistryGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pet Registry")

        self.pet_registry = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.species_label = tk.Label(master, text="Species:")
        self.species_label.grid(row=1, column=0)
        self.species_entry = tk.Entry(master)
        self.species_entry.grid(row=1, column=1)

        self.command_label = tk.Label(master, text="Command:")
        self.command_label.grid(row=2, column=0)
        self.command_entry = tk.Entry(master)
        self.command_entry.grid(row=2, column=1)

        self.add_pet_button = tk.Button(master, text="Add Pet", command=self.add_pet)
        self.add_pet_button.grid(row=3, column=0, columnspan=2)

        self.add_command_button = tk.Button(master, text="Add Command", command=self.add_command)
        self.add_command_button.grid(row=4, column=0, columnspan=2)

        self.show_commands_button = tk.Button(master, text="Show Commands", command=self.show_commands)
        self.show_commands_button.grid(row=5, column=0, columnspan=2)

        self.list_pets_button = tk.Button(master, text="List Pets", command=self.list_pets)
        self.list_pets_button.grid(row=6, column=0, columnspan=2)

        self.pet_selection_label = tk.Label(master, text="Select Pet:")
        self.pet_selection_label.grid(row=7, column=0)
        self.pet_selection = tk.StringVar(value="")
        self.pet_selection_dropdown = tk.OptionMenu(master, self.pet_selection, "")
        self.pet_selection_dropdown.grid(row=7, column=1)

    def add_pet(self):
        name = self.name_entry.get()
        species = self.species_entry.get()
        if name and species:
            pet = Pet(name, species)
            self.pet_registry.append(pet)
            self.update_pet_selection()
            if species == "Monkey" and name == "SpaceMonkey":
                webbrowser.open("https://www.youtube.com/watch?v=vKOv8ohYJTA&t=52")
            messagebox.showinfo("Success", f"{pet.species} named {pet.name} added to the registry.")
        else:
            messagebox.showerror("Error", "Please enter both name and species.")

    def add_command(self):
        selected_pet_name = self.pet_selection.get()
        command = self.command_entry.get()
        if selected_pet_name:
            selected_pet = next((pet for pet in self.pet_registry if pet.name == selected_pet_name), None)
            if selected_pet:
                selected_pet.add_command(command)
                messagebox.showinfo("Success", f"Command '{command}' added to {selected_pet_name}.")
            else:
                messagebox.showerror("Error", f"Pet '{selected_pet_name}' not found.")
        else:
            messagebox.showerror("Error", "Please select a pet.")

    def show_commands(self):
        selected_pet_name = self.pet_selection.get()
        if selected_pet_name:
            selected_pet = next((pet for pet in self.pet_registry if pet.name == selected_pet_name), None)
            if selected_pet:
                messagebox.showinfo("Commands", f"Commands for {selected_pet_name}:\n" + selected_pet.show_commands())
            else:
                messagebox.showerror("Error", f"Pet '{selected_pet_name}' not found.")
        else:
            messagebox.showerror("Error", "Please select a pet.")

    def list_pets(self):
        if self.pet_registry:
            pet_list = "\n".join([f"{pet.species} named {pet.name}" for pet in self.pet_registry])
            messagebox.showinfo("Pet Registry", "Pets in the registry:\n" + pet_list)
        else:
            messagebox.showinfo("Pet Registry", "No pets in the registry.")

    def update_pet_selection(self):
        pet_names = [pet.name for pet in self.pet_registry]
        self.pet_selection.set("")  # Clear previous selection
        self.pet_selection_dropdown["menu"].delete(0, "end")
        for name in pet_names:
            self.pet_selection_dropdown["menu"].add_command(label=name, command=tk._setit(self.pet_selection, name))

def main():
    root = tk.Tk()
    app = PetRegistryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
