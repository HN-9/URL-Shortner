import requests
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def shorten_url():
    long_url = url_entry.get()

    if not long_url.strip():
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    api_url = "http://tinyurl.com/api-create.php"
    params = {"url": long_url}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        short_url = response.text

        result_entry.configure(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, short_url)
        result_entry.configure(state="readonly")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to shorten URL:\n{e}")


def copy_to_clipboard():
    short_url = result_entry.get()
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        messagebox.showinfo("Copied", "Short URL copied to clipboard!")


# ---------------- GUI DESIGN ---------------- #
root = ttk.Window(themename="flatly")
root.title("Modern URL Shortener")
root.geometry("550x300")
root.resizable(False, False)

title_label = ttk.Label(root, text="🔗 URL Shortener", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

# URL Entry Frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=5)

url_label = ttk.Label(input_frame, text="Enter URL:", font=("Helvetica", 12))
url_label.grid(row=0, column=0, padx=10)

url_entry = ttk.Entry(input_frame, width=45, bootstyle="info")
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Shorten Button
shorten_button = ttk.Button(
    root, text="Shorten URL", width=20, bootstyle="success", command=shorten_url
)
shorten_button.pack(pady=15)

# Result Frame
result_frame = ttk.Frame(root)
result_frame.pack(pady=5)

result_label = ttk.Label(result_frame, text="Shortened URL:", font=("Helvetica", 12))
result_label.grid(row=0, column=0, padx=10)

result_entry = ttk.Entry(result_frame, width=45, state="readonly", bootstyle="secondary")
result_entry.grid(row=0, column=1, padx=10, pady=5)

# Copy Button
copy_button = ttk.Button(
    root, text="Copy to Clipboard", width=20, bootstyle="primary", command=copy_to_clipboard
)
copy_button.pack(pady=15)

root.mainloop()
