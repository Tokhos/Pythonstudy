import sqlite3
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Listbox
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import ttk 
from datetime import datetime, timedelta


conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()


cursor.execute('''
      CREATE TABLE IF NOT EXISTS users(
         id_user INTEGER PRIMARY KEY AUTOINCREMENT
     )
 ''')

cursor.execute('''
      CREATE TABLE IF NOT EXISTS professional_id(
         id_professional INTEGER PRIMARY KEY AUTOINCREMENT
     )
 ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT,
        endereco TEXT,
        data_cadastro TEXT,
        FOREIGN KEY (id) REFERENCES users (id_user)       
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS profissionais (
        id_profissional INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_profissional TEXT NOT NULL,
        phone_profissional TEXT,
        FOREIGN KEY (id_professional) REFERENCES professional_id (id_professional)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_profissional INTEGER,
        data_disponivel TEXT,
        FOREIGN KEY (id_usuario) REFERENCES usuarios (id),
        FOREIGN KEY (id_profissional) REFERENCES profissionais (id_profissional)
    )
''')
conn.commit()


def adicionar_usuario(nome, telefone, email, endereco):
    data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO usuarios (nome, telefone, email, endereco, data_cadastro)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, telefone, email, endereco, data_cadastro))
    conn.commit()
    atualizar_combobox_usuarios()

def adicionar_profissional(nome_profissional, phone_profissional):
    cursor.execute('''
        INSERT INTO profissionais (nome_profissional, phone_profissional)
        VALUES (?, ?)
    ''', (nome_profissional, phone_profissional))
    conn.commit()
    atualizar_combobox_profissionais()

def agendar(id_usuario, id_profissional, dias_para_frente=3):
    data_disponivel = (datetime.now() + timedelta(days=dias_para_frente)).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO agendamentos (id_usuario, id_profissional, data_disponivel)
        VALUES (?, ?, ?)
    ''', (id_usuario, id_profissional, data_disponivel))
    conn.commit()
    atualizar_lista_agendamentos()

def visualizar_usuarios():
    cursor.execute('SELECT id, nome FROM usuarios')
    usuarios = cursor.fetchall()
    return usuarios

def visualizar_profissionais():
    cursor.execute('SELECT id_profissional, nome_profissional FROM profissionais')
    profissionais = cursor.fetchall()
    return profissionais

def visualizar_agendamentos(id_profissional):
    cursor.execute('''
        SELECT id_agendamento, id_usuario, data_disponivel
        FROM agendamentos
        WHERE id_profissional = ?
    ''', (id_profissional,))
    agendamentos = cursor.fetchall()
    return agendamentos

def agendar_horario(id_agendamento):
    # Adicione lógica específica, se necessário
    pass

def cancelar_agendamento(id_agendamento):
    cursor.execute('DELETE FROM agendamentos WHERE id_agendamento = ?', (id_agendamento,))
    conn.commit()
    atualizar_lista_agendamentos()

# Funções Tkinter
def cadastrar_usuario():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    endereco = entry_endereco.get()

    adicionar_usuario(nome, telefone, email, endereco)
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

def cadastrar_profissional():
    nome_profissional = entry_nome_profissional.get()
    phone_profissional = entry_phone_profissional.get()

    adicionar_profissional(nome_profissional, phone_profissional)
    messagebox.showinfo("Cadastro", "Profissional cadastrado com sucesso!")

def criar_agendamento():
    id_usuario = combo_usuarios.get()
    id_profissional = combo_profissionais.get()

    if not id_usuario or not id_profissional:
        messagebox.showwarning("Aviso", "Selecione um usuário e um profissional antes de criar um agendamento.")
        return

    agendar(id_usuario, id_profissional)
    messagebox.showinfo("Agendamento", "Agendamento criado com sucesso!")

def cancelar_agendamento_tk():
    selected_agendamento = listbox_agendamentos.curselection()

    if not selected_agendamento:
        messagebox.showwarning("Aviso", "Selecione um agendamento antes de cancelar.")
        return

    id_agendamento = listbox_agendamentos.get(selected_agendamento[0]).split()[0]
    cancelar_agendamento(id_agendamento)
    messagebox.showinfo("Cancelamento", "Agendamento cancelado com sucesso!")


def atualizar_combobox_usuarios():
    combo_usuarios['values'] = visualizar_usuarios()

def atualizar_combobox_profissionais():
    combo_profissionais['values'] = visualizar_profissionais()

def atualizar_lista_agendamentos():
    listbox_agendamentos.delete(0, 'end')

    id_profissional = combo_profissionais.get()  # Substitua pelo ID do profissional logado
    agendamentos_profissional = visualizar_agendamentos(id_profissional)

    for agendamento in agendamentos_profissional:
        data_formatada = datetime.strptime(agendamento[2], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
        listbox_agendamentos.insert('end', f"{agendamento[0]} - Usuário: {agendamento[1]}, Data: {data_formatada}")


root = Tk()
root.title("Sistema de Agendamento")


label_nome = Label(root, text="Nome:")
label_telefone = Label(root, text="Telefone:")
label_email = Label(root, text="E-mail:")
label_endereco = Label(root, text="Endereço:")

entry_nome = Entry(root)
entry_telefone = Entry(root)
entry_email = Entry(root)
entry_endereco = Entry(root)

button_cadastrar_usuario = Button(root, text="Cadastrar Usuário", command=cadastrar_usuario)


label_nome_profissional = Label(root, text="Nome Profissional:")
label_phone_profissional = Label(root, text="Telefone Profissional:")

entry_nome_profissional = Entry(root)
entry_phone_profissional = Entry(root)

button_cadastrar_profissional = Button(root, text="Cadastrar Profissional", command=cadastrar_profissional)


label_usuarios = Label(root, text="Usuários:")
label_profissionais = Label(root, text="Profissionais:")

combo_usuarios = ttk.Combobox(root, state="readonly")
combo_profissionais = ttk.Combobox(root, state="readonly")

button_criar_agendamento = Button(root, text="Criar Agendamento", command=criar_agendamento)


label_agendamentos = Label(root, text="Agendamentos:")
listbox_agendamentos = Listbox(root, selectmode="single")

button_cancelar_agendamento = Button(root, text="Cancelar Agendamento", command=cancelar_agendamento_tk)


label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_telefone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_email.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_endereco.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_telefone.grid(row=1, column=1, padx=5, pady=5, sticky="w")
entry_email.grid(row=2, column=1, padx=5, pady=5, sticky="w")
entry_endereco.grid(row=3, column=1, padx=5, pady=5, sticky="w")

button_cadastrar_usuario.grid(row=4, column=0, columnspan=2, pady=10)

label_nome_profissional.grid(row=5, column=0, padx=5, pady=5, sticky="e")
label_phone_profissional.grid(row=6, column=0, padx=5, pady=5, sticky="e")

entry_nome_profissional.grid(row=5, column=1, padx=5, pady=5, sticky="w")
entry_phone_profissional.grid(row=6, column=1, padx=5, pady=5, sticky="w")

button_cadastrar_profissional.grid(row=7, column=0, columnspan=2, pady=10)

label_usuarios.grid(row=8, column=0, padx=5, pady=5, sticky="e")
label_profissionais.grid(row=8, column=1, padx=5, pady=5, sticky="w")

combo_usuarios.grid(row=9, column=0, padx=5, pady=5)
combo_profissionais.grid(row=9, column=1, padx=5, pady=5)

button_criar_agendamento.grid(row=10, column=0, columnspan=2, pady=10)

label_agendamentos.grid(row=11, column=0, padx=5, pady=5, sticky="w")
listbox_agendamentos.grid(row=12, column=0, columnspan=2, padx=5, pady=5)

button_cancelar_agendamento.grid(row=13, column=0, pady=5)


scrollbar_agendamentos = Scrollbar(root)
scrollbar_agendamentos.grid(row=12, column=2, padx=5, pady=5, sticky="ns")

listbox_agendamentos = Listbox(root, selectmode="single", yscrollcommand=scrollbar_agendamentos.set)
listbox_agendamentos.grid(row=12, column=0, columnspan=2, padx=5, pady=5)


scrollbar_agendamentos.config(command=listbox_agendamentos.yview)

button_cancelar_agendamento = Button(root, text="Cancelar Agendamento", command=cancelar_agendamento_tk)
button_cancelar_agendamento.grid(row=13, column=0, pady=5)


atualizar_combobox_usuarios()
atualizar_combobox_profissionais()
atualizar_lista_agendamentos()


root.mainloop()


conn.close()

