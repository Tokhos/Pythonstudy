import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Application")

        self.home_frame = tk.Frame(root)
        self.client_frame = tk.Frame(root)
        self.professional_frame = tk.Frame(root)
        self.schelude_frame = tk.Frame(root)

        self.entry_name = tk.Entry(self.client_frame)
        self.entry_phone = tk.Entry(self.client_frame)
        self.entry_mail = tk.Entry(self.client_frame)
        self.entry_adress = tk.Entry(self.client_frame)

        self.entry_name_pro = tk.Entry(self.professional_frame)
        self.entry_phone_pro = tk.Entry(self.professional_frame)

        self.user_name_combobox = ttk.Combobox(self.schelude_frame, state="readonly")
        self.professional_name_combobox = ttk.Combobox(self.schelude_frame, state="readonly")

        self.schelude_datetime_picker = ttk.Entry(self.schelude_frame)
        
        self.schelude_treeview = ttk.Treeview(self.schelude_frame, columns=('User', 'Professional', 'Available Date'), show='headings')
        self.schelude_treeview.heading('User', text='User')
        self.schelude_treeview.heading('Professional', text='Professional')
        self.schelude_treeview.heading('Available Date', text='Available Date')
        self.schelude_treeview.pack(pady=10)
        
        delete_schelude_button = tk.Button(self.schelude_frame, text="Delete Schelude", command=self.delete_schelude)
        delete_schelude_button.pack(side=tk.LEFT, pady=10, padx=5)

        self.create_home_frame()
        self.create_client_frame()
        self.create_professional_frame()
        self.create_schelude_frame()

        self.show_frame(self.home_frame)

    def create_home_frame(self):
        client_button = tk.Button(self.home_frame, text="Client", command=lambda: self.show_frame(self.client_frame), width=15, height=2)
        client_button.pack(pady=10)

        professional_button = tk.Button(self.home_frame, text="Professional", command=lambda: self.show_frame(self.professional_frame), width=15, height=2)
        professional_button.pack(pady=10)

        schelude_button = tk.Button(self.home_frame, text="Schelude", command=lambda: self.show_frame(self.schelude_frame), width=15, height=2)
        schelude_button.pack(pady=10)

    def create_client_frame(self):
        label_name = tk.Label(self.client_frame, text="Name:")
        label_name.pack(pady=5, padx=10, anchor="w")
        self.entry_name.pack(pady=5)

        label_phone = tk.Label(self.client_frame, text="Phone:")
        label_phone.pack(pady=5, padx=10, anchor="w")
        self.entry_phone.pack(pady=5)

        label_mail = tk.Label(self.client_frame, text="Email:")
        label_mail.pack(pady=5, padx=10, anchor="w")
        self.entry_mail.pack(pady=5)

        label_adress = tk.Label(self.client_frame, text="Address:")
        label_adress.pack(pady=5, padx=10, anchor="w")
        self.entry_adress.pack(pady=5)

        register_button = tk.Button(self.client_frame, text="Register User", command=self.register_user)
        register_button.pack(side=tk.LEFT, pady=10, padx=5)

        back_button = tk.Button(self.client_frame, text="Back to Home", command=lambda: self.show_frame(self.home_frame))
        back_button.pack(side=tk.LEFT, pady=10, padx=5)

    def create_professional_frame(self):
        label_name_pro = tk.Label(self.professional_frame, text="Name:")
        label_name_pro.pack(pady=5, padx=10, anchor="w")
        self.entry_name_pro.pack(pady=5)

        label_phone_pro = tk.Label(self.professional_frame, text="Phone:")
        label_phone_pro.pack(pady=5, padx=10, anchor="w")
        self.entry_phone_pro.pack(pady=5)

        register_button_pro = tk.Button(self.professional_frame, text="Register Professional", command=self.register_pro)
        register_button_pro.pack(side=tk.LEFT, pady=10, padx=5)

        back_button_pro = tk.Button(self.professional_frame, text="Back to Home", command=lambda: self.show_frame(self.home_frame))
        back_button_pro.pack(side=tk.LEFT, pady=10, padx=5)

    def create_schelude_frame(self):
        label_user_name = tk.Label(self.schelude_frame, text="Select User Name:")
        label_user_name.pack(pady=5, padx=10, anchor="w")
        self.user_name_combobox.pack(pady=5)

        label_professional_name = tk.Label(self.schelude_frame, text="Select Professional Name:")
        label_professional_name.pack(pady=5, padx=10, anchor="w")
        self.professional_name_combobox.pack(pady=5)

        label_schelude_datetime = tk.Label(self.schelude_frame, text="Select Date and Time (YYYY-MM-DD HH:MM:SS):")
        label_schelude_datetime.pack(pady=5, padx=10, anchor="w")
        self.schelude_datetime_picker.pack(pady=5)

        create_schelude_button = tk.Button(self.schelude_frame, text="Create Schelude", command=self.create_schelude)
        create_schelude_button.pack(side=tk.LEFT, pady=10, padx=5)

        back_button = tk.Button(self.schelude_frame, text="Back to Home", command=lambda: self.show_frame(self.home_frame))
        back_button.pack(side=tk.TOP, anchor=tk.NE, pady=10, padx=10)
        
        view_scheludes_button = tk.Button(self.schelude_frame, text="View Scheludes", command=self.view_scheludes)
        view_scheludes_button.pack(side=tk.LEFT, pady=10, padx=5)
        

        self.update_combobox_options()

    def view_scheludes(self):
        self.schelude_treeview.delete(*self.schelude_treeview.get_children())
        scheludes_data = cursor.execute('''
            SELECT users.name, professional.name_pro, schelude.available_data
            FROM schelude
            JOIN users ON schelude.id_user = users.id
            JOIN professional ON schelude.id_pro = professional.id_pro
        ''').fetchall()

        for schelude in scheludes_data:
            self.schelude_treeview.insert('', 'end', values=schelude)
            
    def delete_schelude(self):
        # Get the selected schelude from the Treeview
        selected_item = self.schelude_treeview.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a schelude to delete.")
            return

        # Extract values from the selected item
        selected_values = self.schelude_treeview.item(selected_item, 'values')
        if not selected_values:
            messagebox.showerror("Error", "Failed to get values from the selected schelude.")
            return

        # Unpack the tuple of values
        user_name, professional_name, available_data = selected_values

        # Fetch the schelude ID based on user name, professional name, and available_data
        schelude_id = cursor.execute('''
            SELECT schelude.id_schelude
            FROM schelude
            JOIN users ON schelude.id_user = users.id
            JOIN professional ON schelude.id_pro = professional.id_pro
            WHERE users.name=? AND professional.name_pro=? AND schelude.available_data=?
        ''', (user_name, professional_name, available_data)).fetchone()

        if schelude_id:
            # Delete the schelude from the database
            cursor.execute('DELETE FROM schelude WHERE id_schelude=?', (schelude_id[0],))
            conn.commit()

            # Remove the schelude from the Treeview
            self.schelude_treeview.delete(selected_item)
            messagebox.showinfo("Success", "Schelude deleted successfully.")
        else:
            messagebox.showerror("Error", "Failed to delete the selected schelude.")


    def show_frame(self, frame):
        self.home_frame.pack_forget()
        self.client_frame.pack_forget()
        self.professional_frame.pack_forget()
        self.schelude_frame.pack_forget()

        frame.pack(expand=True, fill="both", padx=10, pady=10)

    def add_user(self, name, phone, mail, adress, status):
        existing_users = cursor.execute('SELECT name, phone FROM users WHERE name=? OR phone=?', (name, phone)).fetchall()
        if existing_users:
            return False
        else:
            register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                INSERT OR FAIL INTO users (name, phone, mail, adress, register_date, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, phone, mail, adress, register_date, status))
        
            conn.commit()
            self.update_combobox_users()
            return True

    def register_user(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        mail = self.entry_mail.get()
        adress = self.entry_adress.get()
        status = 1
    
        if not name or not mail or not adress or not phone:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            success = self.add_user(name, phone, mail, adress, status)
            if success:
                messagebox.showinfo("Cadastro", "User registered successfully!")

    def add_pro(self, name_pro, phone_pro):
        existing_professionals = cursor.execute('SELECT name_pro, phone_pro FROM professional WHERE name_pro=? OR phone_pro=?', (name_pro, phone_pro)).fetchall()
        if existing_professionals:
            return False
        else:
            cursor.execute('''
                INSERT OR FAIL INTO professional (name_pro, phone_pro)
                VALUES (?, ?)
            ''', (name_pro, phone_pro))
            conn.commit()
            self.update_combobox_pro()
            return True

    def register_pro(self):
        name_pro = self.entry_name_pro.get()
        phone_pro = self.entry_phone_pro.get()
    
        if not name_pro or not phone_pro:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            success = self.add_pro(name_pro, phone_pro)
            if success:
                messagebox.showinfo("Cadastro", "Professional registered successfully!")

    def create_schelude(self):
        id_user = self.get_user_id()
        id_pro = self.get_pro_id()
        schelude_datetime_str = self.schelude_datetime_picker.get()

        try:
            schelude_datetime = datetime.strptime(schelude_datetime_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            messagebox.showerror("Error", "Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS.")
            return

        existing_scheludes = cursor.execute('SELECT * FROM schelude WHERE id_user=? AND id_pro=? AND available_data=?', (id_user, id_pro, schelude_datetime_str)).fetchall()
        if existing_scheludes:
            messagebox.showerror("Error", "The selected date and time are already scheluded. Please choose another.")
        else:
            cursor.execute('''
                INSERT INTO schelude (id_user, id_pro, available_data)
                VALUES (?, ?, ?)
            ''', (id_user, id_pro, schelude_datetime_str))
            conn.commit()
            messagebox.showinfo("Success", "Schelude created successfully!")

    def get_user_id(self):
        selected_user_name = self.user_name_combobox.get()
        id_user = cursor.execute('SELECT id FROM users WHERE name=?', (selected_user_name,)).fetchone()
        return id_user[0] if id_user else None

    def get_pro_id(self):
        selected_pro_name = self.professional_name_combobox.get()
        id_pro = cursor.execute('SELECT id_pro FROM professional WHERE name_pro=?', (selected_pro_name,)).fetchone()
        return id_pro[0] if id_pro else None

    def update_combobox_users(self):
        user_names = [row[0] for row in cursor.execute('SELECT name FROM users').fetchall()]
        self.user_name_combobox['values'] = user_names

    def update_combobox_pro(self):
        professional_names = [row[0] for row in cursor.execute('SELECT name_pro FROM professional').fetchall()]
        self.professional_name_combobox['values'] = professional_names

    def update_combobox_options(self):
        self.update_combobox_users()
        self.update_combobox_pro()

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.geometry("500x400")
    root.mainloop()
