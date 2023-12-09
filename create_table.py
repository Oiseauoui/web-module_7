import sqlite3


def create_tables():
    connect = sqlite3.connect('hw_module_7')
    cur = connect.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS disciplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            teacher_id INTEGER,
            group_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        );
    ''')

    # Create 'groups' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    ''')
    # Create 'students' table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups (id)
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            discipline_id INTEGER,
            student_id INTEGER,
            grade INTEGER,
            date_of DATE,
            FOREIGN KEY (discipline_id) REFERENCES disciplines (id),
            FOREIGN KEY (student_id) REFERENCES students (id)
        );
    ''')
    #
    # connect.commit()
    # connect.close()
