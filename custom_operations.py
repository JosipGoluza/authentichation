from typing import TextIO, List

import bcrypt


def encodeUTF8(data: str):
    return bytes(data, 'utf-8')


def write_line(username: str, change_pass_flag: str, hashed_password: str, file):
    file.write(username + " " + change_pass_flag.__str__() + " " + hashed_password.__str__() + "\n")


def hash_password(password: str):
    password_bytes = encodeUTF8(password)
    salt = bcrypt.gensalt()

    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)

    return hashed_password_bytes.decode('utf-8')


def write_file(file: TextIO, all_lines: list):
    file.seek(0)
    file.truncate()
    for line in all_lines:
        file.write(line)


def remove_line(file, username):
    username_bytes = encodeUTF8(username)
    file.seek(0)
    all_lines: List[str] = file.readlines()
    for all_line in all_lines:
        all_line_list = all_line.split()
        if bcrypt.checkpw(username_bytes, all_line_list[0].encode('utf-8')):
            all_lines.remove(all_line)
    return all_lines


def check_existing_user(file, username: str):
    file.seek(0)
    file_lines: List[str] = file.readlines()
    username_bytes = encodeUTF8(username)
    for line in file_lines:
        line_list = line.split()
        if bcrypt.checkpw(username_bytes, line_list[0].encode('utf-8')):
            print("User already exists.")
            quit()
