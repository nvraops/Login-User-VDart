import sqlite3

class UserManager:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.create_db()

    def create_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name TEXT, userid TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()

    def register(self):
        name = input("Enter your name: ")
        userid = input("Enter user ID: ")
        password = input("Enter password: ")
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, userid, password))
            conn.commit()
            print("Registration successful!")
        except sqlite3.IntegrityError:
            print("User ID already exists.")
        conn.close()

    def login(self):
        userid = input("Enter user ID: ")
        password = input("Enter password: ")
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE userid=? AND password=?", (userid, password))
        if c.fetchone():
            print("Login successful!")
        else:
            print("Invalid credentials.")
        conn.close()

def main():
    manager = UserManager()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            manager.register()
        elif choice == '2':
            manager.login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()