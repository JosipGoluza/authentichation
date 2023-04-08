import os.path
import sys

from usermgmt_commands.usermgmt_add import add_command
from usermgmt_commands.usermgmt_del import del_command
from usermgmt_commands.usermgmt_forcepass import forcepass_command
from usermgmt_commands.usermgmt_passwd import passwd_command

command = sys.argv[1]
argument = sys.argv[2]

if not os.path.isfile("passwords.txt"):
    file1 = open("passwords.txt", "w")
    file1.close()

with open('passwords.txt', 'a+') as file:
    if command == "add":
        add_command(argument, file)

    elif command == "passwd":
        passwd_command(argument)

    elif command == "forcepass":
        forcepass_command(argument)

    elif command == "del":
        del_command(argument)

    else:
        print("Wrong command")

file.close()
