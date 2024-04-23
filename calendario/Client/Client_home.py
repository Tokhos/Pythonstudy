import tkinter as tk
from tkinter import ttk
from Client.Client_screen import ClientScreen
from Client.Client_list import Clientlist


class Clienthome(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        tk.Button(self, text="Client Screen", width=20, height=5, command=self.openscreen5).pack(side=tk.LEFT, padx=10, pady=10)

        tk.Button(self, text="Client List", width=20, height=5, command=self.openscreen4).pack(
            side=tk.LEFT, padx=10, pady=10)

    def openscreen4(self):
        screen2 = Clientlist(self)
    
    def openscreen5(self):
        screen2 = ClientScreen(self)