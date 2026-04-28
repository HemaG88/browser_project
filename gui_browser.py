import tkinter as tk
import webbrowser

# Functions
def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_github():
    webbrowser.open("https://github.com")

def open_instagram(): 
    webbrowser.open("https://www.instagram.com")

# Create window
root = tk.Tk()
root.title("Browser Opener")
root.geometry("300x200")

# Buttons
btn1 = tk.Button(root, text="Open Google", command=open_google)
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Open YouTube", command=open_youtube)
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Open GitHub", command=open_github)
btn3.pack(pady=10)

btn4= tk.Button(root, text="open Instagram",command=open_instagram)
btn4.pack(pady=10)

# Run app
root.mainloop()