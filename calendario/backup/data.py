from tkinter import ttk 
from tkinter import Label
from tkinter import Entry
from tkinter import Tk


from tkinter import Button
from tkinter import Listbox


from datetime import datetime
from datetime import timedelta


class Data:
    def __init__(self):
        self.data = []


def add_user(name, phone, mail, adress):
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT OR FAIL INTO users (name, phone, mail, adress, register_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, phone, mail, adress, register_date))
    conn.commit()
    update_combobox_users()



def register_user():
    name = entry_name.get()
    phone = entry_phone.get()
    mail = entry_mail.get()
    adress = entry_adress.get()

    add_user(name, phone, mail, adress)
    messagebox.showinfo("cadastro", "Usuário cadastrado com sucesso!")



def add_pro(name_pro, phone_pro):
    cursor.execute('''
        INSERT OR FAIL INTO professional (name_pro, phone_pro)
        VALUES (?, ?)
    ''', (name_pro, phone_pro))
    conn.commit()
    update_combobox_pro()



def register_pro():
    name_pro = entry_name_pro.get()
    phone_pro = entry_phone_pro.get()

    add_pro(name_pro, phone_pro)
    messagebox.showinfo("Cadastro", "Profissional cadastrado com sucesso!")





def schelude(id_user, id_pro, days_foward=3):
    available_data = (datetime.now() + timedelta(days=days_foward)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT OR FAIL INTO schelude (id_user, id_pro, available_data)
        VALUES (?, ?, ?)
    ''', (id_user, id_pro, available_data))
    conn.commit()
    update_schelude_list()




def visualize_users():
    cursor.execute('SELECT id, name FROM users')
    users = cursor.fetchall()
    return users





def visualize_pro():
    cursor.execute('SELECT id_pro, name_pro FROM professional')
    profissionais = cursor.fetchall()
    return profissionais





def visualize_schelude(id_pro):
    cursor.execute('''
        SELECT id_schelude, id_user, available_data
        FROM schelude
        WHERE id_pro = ?
    ''', (id_pro,))
    schelude = cursor.fetchall()
    return schelude



listbox_schelude = Listbox(root, selectmode="single")

def schelude_time(id_schelude):
   
    pass

def cancel_schelude(id_schelude):
    cursor.execute('DELETE FROM schelude WHERE id_schelude = ?', (id_schelude,))
    conn.commit()
    update_schelude_list()


combo_user = ttk.Combobox(root, state="readonly")
combo_pro = ttk.Combobox(root, state="readonly")

def create_schelude():
    id_user = combo_user.get()
    id_pro = combo_pro.get()

    if not id_user or not id_pro:
        messagebox.showwarning("Aviso", "Selecione um usuário e um profissional antes de criar um agendamento.")
        return

    schelude(id_user, id_pro)
    messagebox.showinfo("Agendamento", "Agendamento criado com sucesso!")





def cancel_schelude_tk():
    selected_schelude = listbox_schelude.curselection()

    if not selected_schelude:
        messagebox.showwarning("Aviso", "Selecione um agendamento antes de cancelar.")
        return

    id_schelude = listbox_schelude.get(selected_schelude[0]).split()[0]
    cancel_schelude(id_schelude)
    messagebox.showinfo("Cancelamento", "Agendamento cancelado com sucesso!")






def update_combobox_users():
    combo_user['values'] = visualize_users()
    

def update_combobox_pro():
    combo_pro['values'] = visualize_pro()





def update_schelude_list():
    listbox_schelude.delete(0, 'end')




    id_pro = combo_pro.get()
    schelude_pro = visualize_schelude(id_pro)


    

    for schelude in schelude_pro:
        date_defined = datetime.strptime(schelude[2], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
        listbox_schelude.insert('end', f"{schelude[0]} - Usuário: {schelude[1]}, Data: {date_defined}")