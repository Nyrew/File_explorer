import tkinter as tk
from tkinter import filedialog, messagebox
from Scripts.file_utils import list_files, move_file, delete_file

class FileExplorerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Explorer")
        self.create_widgets()

    def create_widgets(self):
        # Top section for file path
        self.path_entry = tk.Entry(self.root, width=50)
        self.path_entry.pack()

        browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        browse_button.pack()

        # Table for file list
        self.file_listbox = tk.Listbox(self.root, width=100, height=20)
        self.file_listbox.pack()

        # Buttons for actions
        self.move_button = tk.Button(self.root, text="Move", command=self.move_selected)
        self.move_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_selected)
        self.delete_button.pack(side=tk.RIGHT)

    def browse_folder(self):
        directory = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, directory)
        self.update_file_list(directory)

    def update_file_list(self, directory):
        files = list_files(directory)
        self.file_listbox.delete(0, tk.END)
        for file_info in files:
            self.file_listbox.insert(tk.END, f"{file_info['name']} ({file_info['type']}) - {file_info['size']} bytes")

    def move_selected(self):
        # Logic for moving selected files
        pass

    def delete_selected(self):
        # Logic for deleting selected files
        pass

    def run(self):
        self.root.mainloop()
