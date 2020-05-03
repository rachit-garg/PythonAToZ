from database_connection import DatabaseConnection

def create_table():
   # connection = sqlite3.connect('data.db')
   with DatabaseConnection('data.db') as connection:
       cursor = connection.cursor()
       cursor.execute('CREATE TABLE IF NOT books(name text primary key, author text, read integer)')


def add_book(name,author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        #cursor.execute(f'INSERT INTO books VALUES("{name}","{author}",0)')
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))



def read_data():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books =[{'name': row[0],'author' : row[1], 'read' : row[2]} for row in cursor.fetchall()] #[(name,author,read),(name,author,read)
    return books

print(read_data())