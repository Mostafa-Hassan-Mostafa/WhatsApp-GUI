from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
# Contact names
CONTACTS = ["Mostafa", "Ahmed", "Abd-Allah", "Mazen", "Hassan"]
# Welcome Screen
def open_welcome_screen():
    welcome = Toplevel()
    welcome.title("WhatsApp - Welcome")
    welcome.geometry("400x500")
    welcome.configure(bg="green")
# WhatsApp image
    if os.path.exists("Whatsapp Photo.png"):
        logo_img = Image.open("Whatsapp Photo.png")
        logo_img = logo_img.resize((150, 150))
        logo = ImageTk.PhotoImage(logo_img)
        logo_label = Label(welcome, image=logo, bg="green")
        logo_label.image = logo  # Keep a reference to avoid garbage collection
        logo_label.pack(pady=20)
    else:
        Label(welcome, text="WhatsApp Logo", font=("Arial", 18), bg="black", fg="white").pack(pady=20)

    Label(welcome, text="Welcome to WhatsApp", font=("Arial", 24, "bold"), bg="green").pack(pady=10)
# Contacts button
    Button(welcome, text="Open Contacts", font=("Arial", 12), command=open_contact_list).pack(pady=30)
# Contact List
def open_contact_list():
    contacts_win = Toplevel()
    contacts_win.title("WhatsApp - Contacts")
    contacts_win.geometry("1000x1000")
    contacts_win.configure(bg="#e5e5e5")

    Label(contacts_win, text="Your Contacts", font=("Arial", 24, "bold"), bg="#e5e5e5").pack(pady=10)

    for name in CONTACTS:
        Button(contacts_win, text=name, width=50, height=5, command=lambda n=name: open_chat_window(n)).pack(pady=5)
# Chat Window
def open_chat_window(contact_name):
    chat_win = Toplevel()
    chat_win.title(f"Chat with {contact_name}")
    chat_win.geometry("400x500")
    chat_win.configure(bg="green")

    Label(chat_win, text=f"Chat with {contact_name}", font=("Helvetica", 18, "bold"), bg="green", width=400).pack()
# Message display
    chat_area = Text(chat_win, height=20, state=DISABLED, bg="#f0f0f0")
    chat_area.pack(padx=10, pady=10)
# Writing Message
    msg_entry = Entry(chat_win, width=50)
    msg_entry.pack(side=LEFT, padx=(10, 5), pady=10)
# Send button
    def send_message():
        msg = msg_entry.get()
        if msg.strip():
            chat_area.config(state=NORMAL)
            chat_area.insert(END, f"You: {msg}\n")
            chat_area.config(state=DISABLED)
            msg_entry.delete(0, END)

    Button(chat_win, text="Send", command=send_message).pack(side=LEFT, padx=5, pady=10)
# Main app launcher
def main():
    root = Tk()
    root.title("WhatsApp GUI")
    root.geometry("300x200")
    root.configure(bg="green")

    Label(root, text="Start WhatsApp", font=("Helvetica", 18, "bold"), bg="green").pack(pady=40)
    Button(root, text="Open App", command=open_welcome_screen).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()