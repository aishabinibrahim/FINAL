import tkinter as tk
from tkinter import messagebox, ttk
import pickle
import os

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return {}

class EventManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")

        # Load data or initialize if not present
        self.data = {}
        self.data['employees'] = load_data('employees.pkl')
        self.data['events'] = load_data('events.pkl')
        self.data['clients'] = load_data('clients.pkl')
        self.data['guests'] = load_data('guests.pkl')
        self.data['suppliers'] = load_data('suppliers.pkl')
        self.data['venues'] = load_data('venues.pkl')

        # Create tabs
        self.notebook = ttk.Notebook(master)
        self.setup_tabs()
        self.notebook.pack(expand=1, fill='both')

    def setup_tabs(self):
        self.tabs = {}
        entities = ['Employee', 'Event', 'Client', 'Guest', 'Supplier', 'Venue']
        for entity in entities:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=f"{entity}s")
            self.tabs[entity] = tab
            self.setup_tab(tab, entity)

    def setup_tab(self, tab, entity_type):
        ttk.Label(tab, text="ID:").grid(row=0, column=0)
        id_entry = ttk.Entry(tab)
        id_entry.grid(row=0, column=1)

        ttk.Button(tab, text="Add", command=lambda: self.add_entry(entity_type, id_entry.get())).grid(row=1, column=0)
        ttk.Button(tab, text="Delete", command=lambda: self.delete_entry(entity_type, id_entry.get())).grid(row=1, column=1)
        ttk.Button(tab, text="Modify", command=lambda: self.modify_entry(entity_type, id_entry.get())).grid(row=1, column=2)
        ttk.Button(tab, text="Display", command=lambda: self.display_entry(entity_type, id_entry.get())).grid(row=1, column=3)

    def add_entry(self, entity_type, id_value):
        if id_value in self.data[entity_type.lower() + 's']:
            messagebox.showerror("Error", "ID already exists.")
        else:
            self.data[entity_type.lower() + 's'][id_value] = {"name": "New Entry"}  # Simplified data structure
            save_data(self.data[entity_type.lower() + 's'], f'{entity_type.lower()}s.pkl')
            messagebox.showinfo("Success", f"New {entity_type} added.")

    def delete_entry(self, entity_type, id_value):
        if id_value in self.data[entity_type.lower() + 's']:
            del self.data[entity_type.lower() + 's'][id_value]
            save_data(self.data[entity_type.lower() + 's'], f'{entity_type.lower()}s.pkl')
            messagebox.showinfo("Success", f"{entity_type} deleted.")
        else:
            messagebox.showerror("Error", "ID not found.")

    def modify_entry(self, entity_type, id_value):
        if id_value in self.data[entity_type.lower() + 's']:
            self.data[entity_type.lower() + 's'][id_value] = {"name": "Updated Entry"}  # Example modification
            save_data(self.data[entity_type.lower() + 's'], f'{entity_type.lower()}s.pkl')
            messagebox.showinfo("Success", f"{entity_type} modified.")
        else:
            messagebox.showerror("Error", "ID not found.")

    def display_entry(self, entity_type, id_value):
        if id_value in self.data[entity_type.lower() + 's']:
            entry_details = self.data[entity_type.lower() + 's'][id_value]
            messagebox.showinfo(f"{entity_type} Details", f"Details: {entry_details}")
        else:
            messagebox.showerror("Error", "ID not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()
