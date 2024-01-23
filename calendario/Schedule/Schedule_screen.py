import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class ScheduleScreen(tk.Frame):
    def __init__(self, parent, update_combobox_users, update_combobox_pro):
        super().__init__(parent)

        self.update_combobox_users = update_combobox_users
        self.update_combobox_pro = update_combobox_pro

        
        self.conn = sqlite3.connect("usuarios.db")
        self.cursor = self.conn.cursor()

        
        self.combobox_user_name = ttk.Combobox(self, values=self.get_user_names())
        self.combobox_professional_name = ttk.Combobox(self, values=self.get_professional_names())

        
        tk.Label(self, text="User Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self, text="Professional Name:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self, text="Date (YYYY/MM/DD HH:MM):").grid(row=2, column=0, sticky=tk.W)

        
        self.combobox_user_name.grid(row=0, column=1)
        self.combobox_professional_name.grid(row=1, column=1)

        
        self.entry_date = tk.Entry(self)
        self.entry_date.grid(row=2, column=1)
        self.entry_date.insert(0, "YYYY/MM/DD HH:MM")  # Default format preview

        
        tk.Button(self, text="Create Schedule", command=self.create_schedule).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Show Info", command=self.show_info_on_treeview).grid(row=3, column=2, pady=10)
        tk.Button(self, text="Update Status", command=self.update_user_status).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Delete Schedule", command=self.delete_schedule).grid(row=5, column=2, pady=10)
        
        
        
        self.schelude_treeview = ttk.Treeview(self, columns=('User', 'Professional', 'Date', 'Status'), show='headings')
        self.schelude_treeview.heading('User', text='User')
        self.schelude_treeview.heading('Professional', text='Professional')
        self.schelude_treeview.heading('Date', text='Date')
        self.schelude_treeview.heading('Status', text='Status')
        self.schelude_treeview.grid(row=4, column=0, columnspan=3, pady=10, sticky='nsew')

        
        self.grid_rowconfigure(4, weight=1)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
            

    def get_user_names(self):
        return [user[0] for user in self.cursor.execute('SELECT name FROM users').fetchall()]

    def get_professional_names(self):
        return [pro[0] for pro in self.cursor.execute('SELECT name_pro FROM professional').fetchall()]

    def add_schedule(self, id_user, id_pro, available_data):
        
        self.cursor.execute('''
            INSERT OR FAIL INTO schedule (id_user, id_pro, available_data)
            VALUES (?, ?, ?)
        ''', (id_user, id_pro, available_data))

        self.conn.commit()

    def create_schedule(self):
        user_name = self.combobox_user_name.get()
        professional_name = self.combobox_professional_name.get()
        date_str = self.entry_date.get()

        if not user_name or not professional_name or not date_str:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            
            id_user = self.cursor.execute('SELECT id FROM users WHERE name=?', (user_name,)).fetchone()
            if not id_user:
                messagebox.showerror("Error", f"User with name {user_name} not found.")
                return

            
            id_pro = self.cursor.execute('SELECT id_pro FROM professional WHERE name_pro=?', (professional_name,)).fetchone()
            if not id_pro:
                messagebox.showerror("Error", f"Professional with name {professional_name} not found.")
                return

            self.add_schedule(id_user[0], id_pro[0], date_str)
            messagebox.showinfo("Schedule Created", "Schedule created successfully!")
            
            self.show_info_on_treeview()



    def show_info_on_treeview(self):
        
        self.schelude_treeview.delete(*self.schelude_treeview.get_children())

        
        scheludes_data = self.cursor.execute('''
            SELECT users.name, professional.name_pro, schedule.available_data, users.status
            FROM schedule
            JOIN users ON schedule.id_user = users.id
            JOIN professional ON schedule.id_pro = professional.id_pro
        ''').fetchall()

        
        for schelude in scheludes_data:
            user_name, professional_name, available_data, status = schelude
            status_label = "Active" if status == 1 else "Inactive"
            self.schelude_treeview.insert('', 'end', values=(user_name, professional_name, available_data, status_label))
            
    def update_user_status(self):
        
        selected_item = self.schelude_treeview.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a schedule to update the status.")
            return

        
        selected_values = self.schelude_treeview.item(selected_item, 'values')
        user_name = selected_values[0]  # Assuming user name is the first column

        
        current_status = self.cursor.execute('SELECT status FROM users WHERE name=?', (user_name,)).fetchone()

        if not current_status:
            messagebox.showerror("Error", f"User with name {user_name} not found.")
            return

        
        new_status = 2 if current_status[0] == 1 else 1

        
        self.cursor.execute('UPDATE users SET status=? WHERE name=?', (new_status, user_name))
        self.conn.commit()

        
        self.show_info_on_treeview()
        messagebox.showinfo("Status Updated", f"Status of user {user_name} updated to {new_status}")
        
    def delete_schedule(self):
        
        selected_item = self.schelude_treeview.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a schedule to delete.")
            return

        
        selected_values = self.schelude_treeview.item(selected_item, 'values')
        user_name = selected_values[0]  # Assuming user name is the first column
        professional_name = selected_values[1]  # Assuming professional name is the second column
        available_data = selected_values[2]  # Assuming available data is the third column

        
        id_user = self.cursor.execute('SELECT id FROM users WHERE name=?', (user_name,)).fetchone()
        if not id_user:
            messagebox.showerror("Error", f"User with name {user_name} not found.")
            return

        
        id_pro = self.cursor.execute('SELECT id_pro FROM professional WHERE name_pro=?', (professional_name,)).fetchone()
        if not id_pro:
            messagebox.showerror("Error", f"Professional with name {professional_name} not found.")
            return

        
        self.cursor.execute('DELETE FROM schedule WHERE id_user=? AND id_pro=? AND available_data=?',
                            (id_user[0], id_pro[0], available_data))
        self.conn.commit()

        
        self.show_info_on_treeview()
        messagebox.showinfo("Schedule Deleted", f"Schedule for user {user_name} and professional {professional_name} deleted.")