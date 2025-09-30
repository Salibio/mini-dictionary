DROP TABLE IF EXISTS words;
CREATE TABLE words (
    id INTEGER PRIMARY KEY,
    word TEXT NOT NULL UNIQUE
);

DROP TABLE IF EXISTS definitions;
CREATE TABLE definitions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    definition TEXT NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words(id)
);

DROP TABLE IF EXISTS synonyms;
CREATE TABLE synonyms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    synonym_id INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words(id),
    FOREIGN KEY (synonym_id) REFERENCES words(id)
);

DROP TABLE IF EXISTS antonyms;
CREATE TABLE antonyms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id INTEGER NOT NULL,
    antonym_id INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words(id),
    FOREIGN KEY (antonym_id) REFERENCES words(id)
);


