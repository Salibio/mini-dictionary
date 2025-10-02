"""
1. Get the word’s ID

SELECT id
FROM words
WHERE word = 'your_keyword';


2. Get definitions

SELECT definition
FROM definitions
WHERE word_id = (SELECT id FROM words WHERE word = 'your_keyword');


3. Get synonyms

SELECT w2.word AS synonym
FROM words w1
JOIN synonyms s ON w1.id = s.word_id
JOIN words w2 ON s.synonym_id = w2.id
WHERE w1.word = 'your_keyword';


4. Get antonyms

SELECT w2.word AS antonym
FROM words w1
JOIN antonyms a ON w1.id = a.word_id
JOIN words w2 ON a.antonym_id = w2.id
WHERE w1.word = 'your_keyword';
"""

import sqlite3
import tkinter as tk
from tkinter import scrolledtext

# Connect to your SQLite database
connection = sqlite3.connect("conversion/dictionary.db")
cursor = connection.cursor()

# Function to search word
def search_word():
    word = search_entry.get().strip().lower()
    text_area.delete("1.0", tk.END)  # Clear previous results

    # 1. Get the word ID
    cursor.execute("SELECT id FROM words WHERE word = ?", (word,))
    result = cursor.fetchone()

    if not result:
        text_area.insert(tk.END, f"'{word}' not found in dictionary.")
        return

    word_id = result[0]

    # 2. Get definitions
    cursor.execute("SELECT definition FROM definitions WHERE word_id = ?", (word_id,))
    definitions = [row[0] for row in cursor.fetchall()]

    # 3. Get synonyms
    cursor.execute("""
        SELECT w2.word
        FROM words w1
        JOIN synonyms s ON w1.id = s.word_id
        JOIN words w2 ON s.synonym_id = w2.id
        WHERE w1.word = ?
    """, (word,))
    synonyms = [row[0] for row in cursor.fetchall()]

    # 4. Get antonyms
    cursor.execute("""
        SELECT w2.word
        FROM words w1
        JOIN antonyms a ON w1.id = a.word_id
        JOIN words w2 ON a.antonym_id = w2.id
        WHERE w1.word = ?
    """, (word,))
    antonyms = [row[0] for row in cursor.fetchall()]

    # Build result text
    result_text = f"{word.capitalize()}:\n\n"

    if definitions:
        result_text += "Definitions:\n"
        for d in definitions:
            result_text += f" - {d}\n"
        result_text += "\n"

    if synonyms:
        result_text += "Synonyms:\n"
        result_text += ", ".join(synonyms) + "\n\n"

    if antonyms:
        result_text += "Antonyms:\n"
        result_text += ", ".join(antonyms) + "\n\n"

    text_area.insert(tk.END, result_text)

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Mini Dictionary")
root.geometry("600x500")

# Top frame for search
top_frame = tk.Frame(root)
top_frame.pack(fill="x", padx=5, pady=5)

# Search bar
tk.Label(top_frame, text="Search Word:").pack(side="left")
search_entry = tk.Entry(top_frame, width=40)
search_entry.pack(side="left", padx=5)

# Search button
search_button = tk.Button(top_frame, text="Search", command=search_word)
search_button.pack(side="left")

# Enter key also triggers search
root.bind('<Return>', lambda event: search_word())

# Text area
text_area = scrolledtext.ScrolledText(root, wrap="word", width=80, height=25)
text_area.pack(fill="both", expand=True, padx=5, pady=5)

# Status bar
status_bar = tk.Label(root, text="Type a word and press Enter or Search.", anchor="w")
status_bar.pack(side="bottom", fill="x")

# Run the app
root.mainloop()

# Close database when app exits
connection.close()
