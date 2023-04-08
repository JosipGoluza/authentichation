import bcrypt

from typing import TextIO
from getpass import getpass

from utf8_operations import encodeUTF8


def add_command(username: str, file: TextIO):
    change_pass_flag = False
    hashed_password: bytes = bytes()

    password = getpass("Password: ")
    repeat_password = getpass("Repeat password: ")
    if password == repeat_password:
        print("User " + username + " successfuly added.")

        password_bytes = encodeUTF8(password)
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password_bytes, salt)
    else:
        print("User add failed. Password mismatch.")
        quit()

    file.write(username + " " + change_pass_flag.__str__() + " " + hashed_password.__str__() + "\n")
