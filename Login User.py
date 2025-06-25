class UserSystem:
    def start(self): 
        self.users = {}

    def create_user(self):
        name = input("Enter your name: ")
        user_id = input("Create a user ID: ")
        if user_id in self.users:
            print("This ID is already taken.")
            return
        password = input("Create a password: ")
        self.users[user_id] = {'name': name, 'password': password}
        print("User registered successfully!")

    def login_user(self):
        user_id = input("Enter your user ID: ")
        password = input("Enter your password: ")
        if user_id in self.users and self.users[user_id]['password'] == password:
            print("Welcome,", self.users[user_id]['name'])
        else:
            print("Login failed. ID or password is incorrect.")

def begin_program():
    system = UserSystem()
    system.start()

    while True:
        print("\n1. Register User")
        print("2. Login User")
        print("3. Exit Program")
        option = input("Choose an option: ")

        if option == '1':
            system.create_user()
        elif option == '2':
            system.login_user()
        elif option == '3':
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

begin_program()