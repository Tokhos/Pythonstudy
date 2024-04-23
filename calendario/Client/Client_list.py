import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from Client.client_edit import EditUserScreen


class Clientlist(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()   
        self.client_treeview = ttk.Treeview(self, columns=("Name", "Phone", "Mail", "Address"), show="headings")
        self.client_treeview.heading("Name", text="Name")
        self.client_treeview.heading("Phone", text="Phone")
        self.client_treeview.heading("Mail", text="Mail")
        self.client_treeview.heading("Address", text="Address")
        self.client_treeview.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")
        self.client_treeview.bind("<<TreeviewSelect>>", self.on_user_select)
        self.grid_rowconfigure(4, weight=1)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)

        tk.Button(self, text="Show Info", command=self.show_info).grid(row=3, column=2, pady=10)
        tk.Button(self, text="Edit User Info", command=self.edit_user).grid(row=3, column=4, pady=10)
        self.schedule_treeview = ttk.Treeview(self)
        self.schedule_treeview.grid(column=1, columnspan=3, pady=10, sticky="nsew")
        
        self.schedule_treeview["columns"] = ("User", "Professional", "Date", "Status")
        self.schedule_treeview.heading("#0", text="ID")
        self.schedule_treeview.heading("User", text="User")
        self.schedule_treeview.heading("Professional", text="Professional")
        self.schedule_treeview.heading("Date", text="Date")
        self.schedule_treeview.heading("Status", text="Status")
        
        self.search_entry = tk.Entry(self)
        self.search_entry.grid(pady=5) 
        self.search_btn = tk.Button(self, text="Search", command=self.search)
        self.search_btn.grid()
        
    def edit_user(self):
        selected_item = self.client_treeview.selection()[0]
        print("No user selected DEBUG 1846", selected_item)  
        user_data = list(self.client_treeview.item(selected_item, "values"))
        edit_screen = EditUserScreen(self, user_data)
        edit_screen.mainloop()
   
    def show_info(self):
        self.client_treeview.delete(*self.client_treeview.get_children())
        client_data = self.cursor.execute(
            """
            SELECT users.name, users.phone, users.mail, users.adress
            FROM users
        """
        ).fetchall()

        for user in client_data:
            name, phone, mail, adress = user
            self.client_treeview.insert("", "end", values=(name, phone, mail, adress))
    
    def search(self):
        search_query = self.search_entry.get().lower()
        self.client_treeview.delete(*self.client_treeview.get_children())
        self.schedule_treeview.delete(*self.schedule_treeview.get_children())
        client_data = self.cursor.execute(
            """
            SELECT name, phone, mail, adress
            FROM users
            WHERE name LIKE ? OR phone LIKE ? OR mail LIKE ? OR adress LIKE ?
            """,
            ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%')
        ).fetchall()
        for user in client_data:
            self.client_treeview.insert("", "end", values=user)

        schedule_data = self.cursor.execute('''
            SELECT users.name, professional.name_pro, schedule.available_data, users.status
            FROM schedule
            JOIN users ON schedule.id_user = users.id
            JOIN professional ON schedule.id_pro = professional.id_pro
            WHERE users.name LIKE ? OR professional.name_pro LIKE ? OR schedule.available_data LIKE ?
        ''', ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%')).fetchall()

        for schedule in schedule_data:
            user_name, professional_name, available_data, status = schedule
            status_label = "Active" if status == 1 else "Inactive"
            self.schedule_treeview.insert('', 'end', values=(user_name, professional_name, available_data, status_label))
                    
    def on_user_select(self, event):
        selected_items = self.client_treeview.selection()  
        if selected_items:  
            selected_item = selected_items[0]  
            user_name = self.client_treeview.item(selected_item, "values")[0]  
            self.show_user_schedule(user_name)  
        else:
            print("No user selected DEBUG 1564")  
    
    def show_user_schedule(self, user_name_schedule):
    
        self.schedule_treeview.delete(*self.schedule_treeview.get_children())
    
        schedule_data = self.cursor.execute('''
        SELECT users.name, professional.name_pro, schedule.available_data, users.status
        FROM schedule
        JOIN users ON schedule.id_user = users.id
        JOIN professional ON schedule.id_pro = professional.id_pro
        WHERE users.name = ?
         ''', (user_name_schedule,)).fetchall()
    
        for schedule in schedule_data:
            user_name, professional_name, available_data, status = schedule
            status_label = "Active" if status == 1 else "Inactive"
            self.schedule_treeview.insert('', 'end', values=(user_name, professional_name, available_data, status_label))