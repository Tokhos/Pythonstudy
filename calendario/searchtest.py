import sqlite3
import tkinter as tk

def search():
    search_term = entry_search.get()
    # Connect to SQLite database
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    # Execute SQL query to search for the term
    c.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + search_term + '%',))
    # Fetch results
    results = c.fetchall()
    conn.close()
    # Display results in the text widget
    text_widget.delete(1.0, tk.END)  # Clear previous results
    for result in results:
        text_widget.insert(tk.END, str(result) + '\n')

# Create main window
root = tk.Tk()
root.title("SQLite Search")

# Create search entry and button
entry_search = tk.Entry(root)
entry_search.pack()
button_search = tk.Button(root, text="Search", command=search)
button_search.pack()

# Create text widget to display results
text_widget = tk.Text(root)
text_widget.pack()

root.mainloop()
