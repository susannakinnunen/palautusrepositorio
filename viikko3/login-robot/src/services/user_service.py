from entities.user import User
        
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if re.match("^[a-z]{3,}", username):
            pass  
        else:
            raise UserInputError("Username must contain at least 3 characters. Accepted characters are letters from a to z.")
            
        if re.search("[0-9@#$%^&+=?]", password) and len(password) >= 8:
            pass
        else:
            raise UserInputError("Passwords must contain at least 8 characters and must not only contain letters.")