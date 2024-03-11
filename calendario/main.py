import tkinter as tk
from tkinter import ttk, messagebox
from Client.Client_screen import ClientScreen
from Client.Client_list import Clientlist
from Client.Client_home import Clienthome
from Professional.Professional_screen import ProfessionalScreen
from Schedule.Schedule_screen import ScheduleScreen
import sqlite3
from datetime import datetime
from database.db import *

def init_db():
    # Connect to or create the database file
    conn = sqlite3.connect('database/usuarios.db')
    cursor = conn.cursor()

    # Commit changes and close the connection
    conn.commit()
    conn.close()

#Interface
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Schedule Management")
        self.iconbitmap("icon.ico")

        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        
        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()

        
        self.home_frame = tk.Frame(self.notebook)

        self.notebook.add(self.home_frame, text="Home Screen")


        
        self.notebook.enable_traversal()
        
        style = ttk.Style()
        style.configure('Home.TButton', font=('Helvetica', 14), padding=(10, 5))

        
        tk.Label(self, text="Schedule Management Program", font=('Helvetica', 16)).pack(pady=20)

        
        tk.Button(self.home_frame, text="Client", command=self.openscreen1, height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.home_frame, text="Professional", command=self.openscreen2, height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)
        tk.Button(self.home_frame, text="Schedule", command=self.openscreen3, height=10, width=30).pack(
            side=tk.LEFT, padx=10, pady=10)


        
        self.notebook.bind("<<NotebookTabChanged>>", self.tab_changed)

        
        self.tab_changed(None)
    
    
    def openscreen3(self):
        screen3 = ScheduleScreen(self)
        
    def openscreen2(self):
        screen2 = ProfessionalScreen(self)
    
    def openscreen1(self):
        screen2 = Clienthome(self)
    
    def update_combobox_users(self):
        
        messagebox.showinfo("Information", "Success")

    def update_combobox_pro(self):
        
        messagebox.showinfo("Information", "Success")

    def tab_changed(self, event):
        
        current_tab = self.notebook.index(self.notebook.select())


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
