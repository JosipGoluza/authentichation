from typing import TextIO
from getpass import getpass


def add_command(username: str, file: TextIO):
    change_pass_flag = False

    password = getpass("Password: ")
    repeat_password = getpass("Repeat password: ")
    if password == repeat_password:
        print("User " + username + " successfuly added.")
    else:
        print("User add failed. Password mismatch.")
        quit()

    file.write(username + " " + change_pass_flag.__str__() + " " + password + "\n")
