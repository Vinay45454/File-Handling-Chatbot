import tkinter as tk
from tkinter import messagebox
from chatbot import process_user_input

def handle_user_input():
    user_input = entry.get()
    entry.delete(0, tk.END)
    response = process_user_input(user_input)
    chatbox.insert(tk.END, f"User: {user_input}\n")
    chatbox.insert(tk.END, f"ChatBot: {response}\n\n")
    chatbox.see(tk.END)

def exit_application():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

# Create the GUI window
window = tk.Tk()
window.title("File Management ChatBot")

# Create the chatbox
chatbox = tk.Text(window, width=50, height=20)
chatbox.pack(padx=10, pady=10)

# Create the input entry
entry = tk.Entry(window, width=40)
entry.pack(padx=10, pady=10)

# Create the send button
send_button = tk.Button(window, text="Send", command=handle_user_input)
send_button.pack(padx=10, pady=10)

# Bind the Enter key to the send button
window.bind('<Return>', lambda event: send_button.invoke())

# Create the exit button
exit_button = tk.Button(window, text="Exit", command=exit_application)
exit_button.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
