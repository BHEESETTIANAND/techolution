class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, user_id):
        new_user = User(name, user_id)
        self.users.append(new_user)

    def list_users(self):
        if not self.users:
            print("No users available.")
            return
        for user in self.users:
            print(user)

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
