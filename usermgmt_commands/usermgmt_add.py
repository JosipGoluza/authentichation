from getpass import getpass

import bcrypt

from custom_operations import encodeUTF8, hash_password, write_line


def add_command(username: str):
    with open('passwords.txt', 'a+') as file:
        change_pass_flag = "0"
        hashed_password: bytes = bytes()

        password = getpass("Password: ")
        repeat_password = getpass("Repeat password: ")
        if password == repeat_password:
            print("User " + username + " successfuly added.")

            hashed_password: str = hash_password(password)
        else:
            print("User add failed. Password mismatch.")
            quit()

        write_line(username, change_pass_flag, hashed_password, file)
        file.close()
