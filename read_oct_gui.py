import tkinter as tk
from tkinter import filedialog, messagebox
from read_scan_type import read_scan


def run():
    file_path = entry.get()
    if file_path:
        read_scan(file_path, no_images=21, window_h=768, scan_len=1020)     # raster
    else:
        messagebox.showwarning("Warning", "Please provide a file path.")


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("OCT files", "*.OCT"), ("All files", "*.*")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


# Create the main window
root = tk.Tk()
root.title("OCT Reader")

label = tk.Label(root, text="OCT File Path:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5, padx=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=5)

run_button = tk.Button(root, text="Run", command=run)
run_button.pack(pady=10)

label = tk.Label(root, text="Licencjat: Dominika Wendland")
label.pack(pady=10)

# Run the application
root.mainloop()
