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

connection = sqlite3.connect("conversion/dictionary.db")
