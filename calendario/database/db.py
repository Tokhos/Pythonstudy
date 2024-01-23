import sqlite3


conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS user_base(
         id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
     )
 ''')

cursor.execute('''
      CREATE TABLE IF NOT EXISTS professional_id(
         id_pro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
     )
 ''')


#cursor.execute('''
#     CREATE TABLE IF NOT EXISTS status(
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         user_status INTEGER
#         FOREIGN KEY (id) REFERENCES user_base (id_user)
#     )
# ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE,
        mail TEXT NOT NULL UNIQUE,
        adress TEXT NOT NULL,
        register_date TEXT NOT NULL,
        status NUMBER NOT NULL,
        FOREIGN KEY (id) REFERENCES user_base (id_user)
               
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS professional (
        id_pro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name_pro TEXT NOT NULL,
        phone_pro TEXT NOT NULL UNIQUE,
        FOREIGN KEY (id_pro) REFERENCES professional_id (id_pro)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id_schedule INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_user INTEGER NOT NULL,
        id_pro INTEGER,
        available_data TEXT,
        FOREIGN KEY (id_user) REFERENCES user_base (id_user),
        FOREIGN KEY (id_pro) REFERENCES professional_id (id_pro)
    )
''')