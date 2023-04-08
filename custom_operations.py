from typing import TextIO

import bcrypt


def decodeUTF8(data: bytes):
    return data.decode('utf-8')


def encodeUTF8(data: str):
    return bytes(data, 'utf-8')


def write_line(username: str, change_pass_flag: str, hashed_password: str, file):
    file.write(username + " " + change_pass_flag.__str__() + " " + hashed_password.__str__() + "\n")


def hash_password(password: str):
    password_bytes = encodeUTF8(password)
    salt = bcrypt.gensalt()

    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)

    return decodeUTF8(hashed_password_bytes)


def write_file(file: TextIO, all_lines: list):
    file.seek(0)
    file.truncate()
    for line in all_lines:
        file.write(line)


def remove_line(file, line):
    file.seek(0)
    all_lines = file.readlines()
    for all_line in all_lines:
        if all_line == line:
            all_lines.remove(all_line)
    return all_lines
