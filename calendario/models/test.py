import sqlite3
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Listbox
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import ttk 
from datetime import datetime
from datetime import timedelta
from database.db import *




conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()



def add_user(name, phone, mail, adress, status):
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT OR FAIL INTO users (name, phone, mail, adress, register_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, phone, mail, adress, register_date, status))

    
    conn.commit()
    update_combobox_users()


def register_user():
    name = entry_name.get()
    phone = entry_phone.get()
    mail = entry_mail.get()
    adress = entry_adress.get()
    status = 1
    
    if not name or not mail or not adress or not phone:
        messagebox.showerror("Erro", "Para ter uma experiência completa, precisamos que você informe todos os dados do formulário.")
    
    else:
        add_user(name, phone, mail, adress, status)
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    


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
    
    if not name_pro or not phone_pro:
        messagebox.showerror("Erro", "Para ter uma experiência completa, precisamos que você informe todos os dados do formulário.")
    
    else:
        add_pro(name_pro, phone_pro)
        messagebox.showinfo("Cadastro", "Profissional cadastrado com sucesso!")

#
def update_user_status():
    selected_user = combo_user.get()
    new_status = combo_status.get()

    if not selected_user:
        messagebox.showwarning("Aviso", "Selecione um id de usuário antes de atualizar o status.")
        return

    try:
        if new_status == "Inativo":
            cursor.execute('UPDATE users SET status = "2" WHERE id = ?', (selected_user,))
            conn.commit()
            messagebox.showinfo("Atualização de Status", "Status do usuário atualizado para Inativo.")
            if cursor.rowcount > 0:
                print("Update successful")
            else:
                print('UPDATE users SET status = 2 WHERE id = ?', (selected_user,))
                print("No rows were updated. The specified id may not exist.")
    
        elif new_status == "Ativo":
            cursor.execute('UPDATE users SET status = "1" WHERE id = ?', (selected_user))
            conn.commit()
            messagebox.showinfo("Atualização de Status", "Status do usuário atualizado para Ativo.")
        else:
            messagebox.showwarning("Aviso", "Selecione 'Inativo' ou 'Ativo' para atualizar o status do usuário.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar o status: {e}")

    update_combobox_users()
    
    update_schelude_list()


def schelude(id_user, id_pro, days_foward=3):
    available_data = (datetime.now() + timedelta(days=days_foward)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT OR FAIL INTO schelude (id_user, id_pro, available_data)
        VALUES (?, ?, ?)
    ''', (id_user, id_pro, available_data))
    conn.commit()
    update_schelude_list()

def visualize_users():
    cursor.execute('SELECT id FROM users')
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

def schelude_time(id_schelude):
   
    pass

def cancel_schelude(id_schelude):
    cursor.execute('DELETE FROM schelude WHERE id_schelude = ?', (id_schelude,))
    conn.commit()
    update_schelude_list()



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
   
    

#base tkinter

root = Tk()
root.title("Sistema de Agendamento")

#label superior
label_name = Label(root, text="Nome:")
label_phone = Label(root, text="Telefone:")
label_mail = Label(root, text="E-mail:")
label_adress = Label(root, text="Endereço:")


#campo de registro
entry_name = Entry(root)
entry_phone = Entry(root)
entry_mail = Entry(root)
entry_adress = Entry(root)


#confirmação de registro
button_register_user = Button(root, text="Cadastrar Usuário", command= register_user)


#label inferior(profissional)
label_name_pro = Label(root, text="Nome Profissional:")
label_phone_pro = Label(root, text="Telefone Profissional:")

#campo de cadastro de profissional
entry_name_pro = Entry(root)
entry_phone_pro = Entry(root)

#confirmação de registro profissional
button_register_pro = Button(root, text="Cadastrar Profissional", command= register_pro)


#botão de confirmação de agendamento
button_create_schelude = Button(root, text="Criar Agendamento", command= create_schelude)

#visualização de lista de agendamentos
label_schelude = Label(root, text="Agendamentos:")
listbox_schelude = Listbox(root, selectmode="single")

label_username = Label(root, text="Usuários:")
listbox_username= Listbox(root, selectmode="single")

#cancelamento de agendamento
button_cancel_schelude = Button(root, text="Cancelar Agendamento", command= cancel_schelude_tk)


#visualização de usuarios e profissionais
label_users = Label(root, text="ID do Usuário:")
label_professional = Label(root, text="Profissionais:")
label_status= Label(root, text="Status")

#combinação de usuarios e profissionais
combo_user = ttk.Combobox(root, state="readonly")
combo_pro = ttk.Combobox(root, state="readonly")


#exibir lista de usuários
def userexib():
    cursor.execute(f"SELECT id, name FROM users")
    users = cursor.fetchall()

    tree = ttk.Treeview(root)
    tree["columns"] = tuple(range(len(users[0])))
    tree.heading('#1', text=f"id")
    tree.heading('#2', text=f"name")
    
    for line in users:
        tree.insert("", "end", values=line)

    scrollbar_tree = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.grid(row=12, column=2, sticky="s")
    scrollbar_tree.grid(row=12, column=3, sticky="s")

    for i in range(len(users[0])):
        tree.column(i, stretch=False)
        tree.column(i, minwidth=30)
    
    tree.bind("<Configure>", lambda e: tree.item(tree.focus(), tags=("ttk",)))

    


#posicionamentos
label_status.grid(row=8, column=2, padx=5, pady=5, sticky="w")

combo_status = ttk.Combobox(root, values=["Ativo", "Inativo"], state="readonly")
combo_status.set("Ativo")
combo_status.grid(row=9, column=2, padx=5, pady=5)

button_update_status = Button(root, text="Atualizar Status", command=update_user_status)
button_update_status.grid(row=10, column=2, pady=10)

button_update_username = Button(root, text="Exibir Usuários", command= userexib)
button_update_username.grid (row=12, column=3, pady=10)

#####
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_mail.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_adress.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_phone.grid(row=1, column=1, padx=5, pady=5, sticky="w")
entry_mail.grid(row=2, column=1, padx=5, pady=5, sticky="w")
entry_adress.grid(row=3, column=1, padx=5, pady=5, sticky="w")

button_register_user.grid(row=4, column=0, columnspan=2, pady=10)

label_name_pro.grid(row=5, column=0, padx=5, pady=5, sticky="e")
label_phone_pro.grid(row=6, column=0, padx=5, pady=5, sticky="e")

entry_name_pro.grid(row=5, column=1, padx=5, pady=5, sticky="w")
entry_phone_pro.grid(row=6, column=1, padx=5, pady=5, sticky="w")

button_register_pro.grid(row=7, column=0, columnspan=2, pady=10)

label_users.grid(row=8, column=0, padx=5, pady=5, sticky="e")
label_professional.grid(row=8, column=1, padx=5, pady=5, sticky="w")

combo_user.grid(row=9, column=0, padx=5, pady=5)
combo_pro.grid(row=9, column=1, padx=5, pady=5)

button_create_schelude.grid(row=10, column=0, columnspan=2, pady=10)

label_schelude.grid(row=11, column=0, padx=5, pady=5, sticky="w")
listbox_schelude.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

button_cancel_schelude.grid(row=13, column=0, pady=5)


scrollbar_schelude = Scrollbar(root)
scrollbar_schelude.grid(row=11, column=1, padx=5, pady=5, sticky="ns")


listbox_schelude = Listbox(root, selectmode="single", yscrollcommand=scrollbar_schelude.set)
listbox_schelude.grid(row=12, column=0, columnspan=2, padx=5, pady=5)


scrollbar_schelude.config(command=listbox_schelude.yview)

button_cancel_schelude = Button(root, text="Cancelar Agendamento", command=cancel_schelude_tk)
button_cancel_schelude.grid(row=13, column=0, pady=5)

update_combobox_users()
update_combobox_pro()
update_schelude_list()



root.mainloop()


conn.close()
