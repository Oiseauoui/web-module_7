import sqlite3
from pprint import pprint

from create_table import create_tables  # Check if it's create_table or create_tables
from insert import seed_data


if __name__ == '__main__':
    try:
        connect = sqlite3.connect('hw_module_7')
        cur = connect.cursor()

        create_tables()
        seed_data(connect, cur)

        connect.commit()
    except sqlite3.Error as error:
        pprint(error)
    finally:
        connect.close()
