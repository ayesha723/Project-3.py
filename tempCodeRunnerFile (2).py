import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox
from datetime import datetime, timedelta

# In-memory dictionary to store birthdays and custom messages
birthdays = {
    "Mom": {"date": "1970-09-05", "email": "mom@example.com", "message": "I love you Mom! Happy Birthday!"},
    "Dad": {"date": "1968-10-10", "email": "dad@example.com", "message": "Happy Birthday Dad! Thanks for all your support!"},
    "Sister": {"date": "1995-06-15", "email": "sister@example.com", "message": "Happy Birthday Sis! You're amazing!"},
    "Friend1": {"date": "1993-11-20", "email": "friend1@example.com", "message": "Happy Birthday! Hope you have a fantastic day!"},
    "Friend2": {"date": "1994-12-25", "email": "friend2@example.com", "message": "Happy Birthday! Wishing you all the best!"}
}

# Simulate sending email
def send_email(recipient_email, message):
    messagebox.showinfo("Email Sent", f"Email sent to {recipient_email}:\n{message}")

# Simulate sending a birthday gift online
def send_gift(name):
    messagebox.showinfo("Gift Sent", f"Online gift sent to {name}.")

# Simulate sending a birthday treat reminder
def send_treat_reminder(name):
    messagebox.showinfo("Treat Reminder", f"Reminder to organize a birthday treat for {name}.")

# Simulate sending a cake reminder
def send_cake_reminder(name):
    messagebox.showinfo("Cake Reminder", f"Reminder to get a cake for {name}'s birthday.")

# Check today's birthdays
def check_birthdays():
    today = datetime.today().strftime('%m-%d')
    for name, info in birthdays.items():
        birthday = datetime.strptime(info["date"], '%Y-%m-%d').strftime('%m-%d')
        if today == birthday:
            message = f"Subject: Happy Birthday!\n\n{info['message']}"
            send_email(info["email"], message)
            send_gift(name)
            send_treat_reminder(name)
            send_cake_reminder(name)

# Add a new contact with a custom message
def add_contact():
    name = simpledialog.askstring("Input", "Enter the name:")
    if not name:
        return
    date = simpledialog.askstring("Input", "Enter the birthdate (YYYY-MM-DD):")
    if not date:
        return
    email = simpledialog.askstring("Input", f"Enter the email for {name}:")
    if not email:
        return
    message = simpledialog.askstring("Input", f"Enter a custom birthday message for {name}:")
    if not message:
        return
    birthdays[name] = {"date": date, "email": email, "message": message}
    messagebox.showinfo("Contact Added", f"Added {name}'s birthday with custom message.")

# Remove a contact
def remove_contact():
    name = simpledialog.askstring("Input", "Enter the name of the person to remove:")
    if name in birthdays:
        del birthdays[name]
        messagebox.showinfo("Contact Removed", f"Removed {name}'s birthday.")
    else:
        messagebox.showwarning("Not Found", f"No entry found for {name}.")

# Update a contact's info
def update_contact():
    name = simpledialog.askstring("Input", "Enter the name of the person to update:")
    if name in birthdays:
        date = simpledialog.askstring("Input", f"Enter the new birthdate for {name} (YYYY-MM-DD):")
        email = simpledialog.askstring("Input", f"Enter the new email for {name}:")
        message = simpledialog.askstring("Input", f"Enter the new custom message for {name}:")
        birthdays[name] = {"date": date, "email": email, "message": message}
        messagebox.showinfo("Contact Updated", f"Updated {name}'s birthday and custom message.")
    else:
        messagebox.showwarning("Not Found", f"No entry found for {name}.")

# List upcoming birthdays
def list_upcoming_birthdays():
    today = datetime.today()
    upcoming_days = simpledialog.askinteger("Input", "Enter the number of days to look ahead:")
    if upcoming_days is None:
        return
    upcoming_birthdays = []
    for name, info in birthdays.items():
        birthday = datetime.strptime(info["date"], '%Y-%m-%d')
        birthday_this_year = birthday.replace(year=today.year)
        if today <= birthday_this_year <= today + timedelta(days=upcoming_days):
            upcoming_birthdays.append(f"{name}: {birthday.strftime('%B %d')} - Custom Message: {info['message']}")
    if upcoming_birthdays:
        messagebox.showinfo("Upcoming Birthdays", "\n".join(upcoming_birthdays))
    else:
        messagebox.showinfo("Upcoming Birthdays", "No upcoming birthdays.")

# List all contacts
def list_all_contacts():
    if birthdays:
        all_contacts = "\n".join([f"Name: {name}, Date: {info['date']}, Email: {info['email']}, Message: {info['message']}" for name, info in birthdays.items()])
        messagebox.showinfo("All Contacts", all_contacts)
    else:
        messagebox.showinfo("All Contacts", "No contacts found.")

# Search for a contact
def search_contact():
    name = simpledialog.askstring("Input", "Enter the name of the person to search:")
    if name in birthdays:
        info = birthdays[name]
        messagebox.showinfo("Contact Found", f"Name: {name}, Date: {info['date']}, Email: {info['email']}, Message: {info['message']}")
    else:
        messagebox.showwarning("Not Found", f"No entry found for {name}.")

# Calculate age and send age reminder
def send_age_reminder():
    today = datetime.today()
    age_reminders = []
    for name, info in birthdays.items():
        birth_date = datetime.strptime(info["date"], '%Y-%m-%d')
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        age_reminders.append(f"Reminder: {name} will turn {age} years old today!")
    messagebox.showinfo("Age Reminders", "\n".join(age_reminders))

# Main application window
def main():
    root = tk.Tk()
    root.title("Birthday Reminder System")
    
    tk.Button(root, text="Check Today's Birthdays", command=check_birthdays).pack(pady=5)
    tk.Button(root, text="Add New Contact", command=add_contact).pack(pady=5)
    tk.Button(root, text="Remove Contact", command=remove_contact).pack(pady=5)
    tk.Button(root, text="Update Contact Info", command=update_contact).pack(pady=5)
    tk.Button(root, text="List Upcoming Birthdays", command=list_upcoming_birthdays).pack(pady=5)
    tk.Button(root, text="List All Contacts", command=list_all_contacts).pack(pady=5)
    tk.Button(root, text="Search for a Contact", command=search_contact).pack(pady=5)
    tk.Button(root, text="Send Age Reminder", command=send_age_reminder).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
