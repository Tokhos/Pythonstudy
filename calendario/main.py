import tkinter as tk
from tkinter import ttk, messagebox
from Client.Client_screen import ClientScreen
from Professional.Professional_screen import ProfessionalScreen
from Schedule.Schedule_screen import ScheduleScreen
import sqlite3
from datetime import datetime

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Schedule Management")
        self.iconbitmap("icon.ico")

        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        
        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()

        
        self.home_frame = tk.Frame(self.notebook)
        self.client_frame = ClientScreen(self.notebook, self.update_combobox_users)
        self.professional_frame = ProfessionalScreen(self.notebook, self.update_combobox_pro)
        self.schedule_frame = ScheduleScreen(self.notebook, self.update_combobox_users, self.update_combobox_pro)

        self.notebook.add(self.home_frame, text="Home Screen")
        self.notebook.add(self.client_frame, text="Client Screen")
        self.notebook.add(self.professional_frame, text="Professional Screen")
        self.notebook.add(self.schedule_frame, text="Schedule Screen")

        
        self.notebook.enable_traversal()
        
        style = ttk.Style()
        style.configure('Home.TButton', font=('Helvetica', 14), padding=(10, 5))

        
        tk.Label(self, text="Schedule Management Program", font=('Helvetica', 16)).pack(pady=20)

        
        tk.Button(self.home_frame, text="Client", command=lambda: self.notebook.select(1), height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.home_frame, text="Professional", command=lambda: self.notebook.select(2), height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.home_frame, text="Schedule", command=lambda: self.notebook.select(3), height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)


        
        self.notebook.bind("<<NotebookTabChanged>>", self.tab_changed)

        
        self.tab_changed(None)

    def update_combobox_users(self):
        
        messagebox.showinfo("Information", "Success")

    def update_combobox_pro(self):
        
        messagebox.showinfo("Information", "Success")

    def tab_changed(self, event):
        
        current_tab = self.notebook.index(self.notebook.select())

        if current_tab == 0:  # Home Screen
            pass

        elif current_tab == 1:  # Client Screen
            pass

        elif current_tab == 2:  # Professional Screen
            pass

        elif current_tab == 3:  # Schedule Screen
            pass

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
