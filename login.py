import os
import sys
from getpass import getpass

import bcrypt

from custom_operations import remove_line, hash_password, write_file, encodeUTF8

if not os.path.isfile("passwords.txt"):
    file1 = open("passwords.txt", "w")
    file1.close()

username = sys.argv[1]

with open("passwords.txt", "r+") as file:
    lines = file.readlines()
    for line in lines:
        lineList = line.split()
        if bcrypt.checkpw(username.encode('utf-8'), lineList[0].encode('utf-8')):
            if lineList[1] == "0":
                hashed_password = lineList[2].encode('utf-8')
                # encoding user password
                password = getpass("Password: ")
                passwordBytes = password.encode('utf-8')

                # checking password
                if bcrypt.checkpw(passwordBytes, hashed_password):
                    print("Login successful")
                else:
                    print("Wrong password")

            elif lineList[1] == "1":
                hashed_password = lineList[2].encode('utf-8')
                # encoding user password
                password = getpass("Password: ")
                userBytes = password.encode('utf-8')

                # checking password
                if bcrypt.checkpw(userBytes, hashed_password):
                    new_password = getpass("New password: ")
                    repeat_new_password = getpass("Repeat new password: ")
                    if new_password == repeat_new_password:
                        all_lines = remove_line(file, username)

                        new_user = bcrypt.hashpw(encodeUTF8(username), bcrypt.gensalt()).decode('utf-8')
                        new_flag = "0"
                        new_password_hashed = hash_password(new_password)
                        all_lines.append(new_user + " " + new_flag + " " + new_password_hashed + "\n")

                        write_file(file, all_lines)
                else:
                    print("Username or password incorrect.")
            else:
                print("Wrong flag")
            quit()
    print("Username does not exist")
    file.close()
