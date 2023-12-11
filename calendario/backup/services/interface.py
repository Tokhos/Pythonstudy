import tkinter
from tkinter import Button
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Tk
import sqlite3

from models.data import Data
from database.db import *

class Interface:
    def __init__(self):
        
        root = Tk()
        root.title("Sistema de Agendamento")

        root.mainloop()
            
        label_name = Label(root, text="Nome:")
        label_phone = Label(root, text="Telefone:")
        label_mail = Label(root, text="E-mail:")
        label_adress = Label(root, text="Endereço:")

        entry_name = Entry(root)
        entry_phone = Entry(root)
        entry_mail = Entry(root)
        entry_adress = Entry(root)
        
        label_name_pro = Label(root, text="Nome Profissional:")
        label_phone_pro = Label(root, text="Telefone Profissional:")

        entry_name_pro = Entry(root)
        entry_phone_pro = Entry(root)

        button_register_pro = Button(root, text="Cadastrar Profissional", command=register_pro)
        
        

        button_register_user = Button(root, text="Cadastrar Usuário", command=register_user)   
        
        label_users = Label(root, text="Usuários:")
        label_professional = Label(root, text="Profissionais:")

        combo_user = ttk.Combobox(root, state="readonly")
        combo_pro = ttk.Combobox(root, state="readonly")

        button_create_schelude = Button(root, text="Criar Agendamento", command=create_schelude)


        label_schelude = Label(root, text="Agendamentos:")
        listbox_schelude = Listbox(root, selectmode="single")

        button_cancel_schelude = Button(root, text="Cancelar Agendamento", command=cancel_schelude_tk) 

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
        scrollbar_schelude.grid(row=12, column=2, padx=5, pady=5, sticky="ns")

        listbox_schelude = Listbox(
            root, selectmode="single", yscrollcommand=scrollbar_schelude.set
        )
        listbox_schelude.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

        scrollbar_schelude.config(command=listbox_schelude.yview)

        button_cancel_schelude = Button(
            root, text="Cancelar Agendamento", command=cancel_schelude_tk
        )
        button_cancel_schelude.grid(row=13, column=0, pady=5)

        update_combobox_users()
        update_combobox_pro()
        update_schelude_list()
        
        root.mainloop()

        conn.close()
