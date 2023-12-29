import tkinter as tk
from tkinter import simpledialog

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def view_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [contact for contact in self.contacts if query.lower() in contact["name"].lower()]

    def update_contact(self, old_name, new_name, new_phone):
        for contact in self.contacts:
            if contact["name"] == old_name:
                contact["name"] = new_name
                contact["phone"] = new_phone

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"] != name]

class CustomMessageBox(tk.Toplevel):
    def __init__(self, title, message):
        super().__init__()
        self.title(title)
        self.geometry("300x100")
        self.configure(bg="lightblue")

        label = tk.Label(self, text=message, bg="lightblue", padx=10, pady=10)
        label.pack()

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack()

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contact_book = ContactBook()

        self.label = tk.Label(master, text="Contact Book", font=("Helvetica", 16))
        self.label.pack()

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.pack()

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        if not name:
            return
        phone = simpledialog.askstring("Add Contact", "Enter phone:")
        if not phone:
            return
        self.contact_book.add_contact(name, phone)
        self.show_message("Contact Added", f"Contact {name} added successfully.")

    def view_contacts(self):
        contacts = self.contact_book.view_contacts()
        if contacts:
            contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in contacts])
            self.show_message("Contacts", contact_list)
        else:
            self.show_message("Contacts", "No contacts found.")

    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter name to search:")
        if not query:
            return
        result = self.contact_book.search_contact(query)
        if result:
            contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in result])
            self.show_message("Search Results", contact_list)
        else:
            self.show_message("Search Results", f"No contacts found for '{query}'.")

    def update_contact(self):
        old_name = simpledialog.askstring("Update Contact", "Enter name to update:")
        if not old_name:
            return
        new_name = simpledialog.askstring("Update Contact", "Enter new name:")
        if not new_name:
            return
        new_phone = simpledialog.askstring("Update Contact", "Enter new phone:")
        if not new_phone:
            return
        self.contact_book.update_contact(old_name, new_name, new_phone)
        self.show_message("Contact Updated", f"Contact {old_name} updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
        if not name:
            return
        self.contact_book.delete_contact(name)
        self.show_message("Contact Deleted", f"Contact {name} deleted successfully.")

    def show_message(self, title, message):
        message_box = CustomMessageBox(title, message)
        message_box.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
