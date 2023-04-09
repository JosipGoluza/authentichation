from getpass import getpass

from custom_operations import encodeUTF8, hash_password, write_line, check_existing_user


def add_command(username: str):
    with open('passwords.txt', 'a+') as file:
        check_existing_user(file, username)

        change_pass_flag = "0"
        hashed_password: bytes = bytes()

        password = getpass("Password: ")
        repeat_password = getpass("Repeat password: ")
        if password == repeat_password:
            if len(password) < 8:
                print("Password too short. Minimum 8 characters.")
                quit()
            print("User " + username + " successfuly added.")

            hashed_password: str = hash_password(password)
        else:
            print("User add failed. Password mismatch.")
            quit()

        write_line(username, change_pass_flag, hashed_password, file)
        file.close()
