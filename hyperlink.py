import tkinter as tk
import webbrowser

def open_link(url):
    webbrowser.open(url)

# Create the main window
window = tk.Tk()

# Create a label with the hyperlink text
link_label = tk.Label(window, text="Click here to visit Google", fg="blue", cursor="hand2")
link_label.pack(pady=10)

# Bind the label to the open_link function
link_label.bind("<Button-1>", lambda e: open_link("https://www.google.com"))

# Start the GUI application
window.mainloop()