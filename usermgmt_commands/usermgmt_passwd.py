from getpass import getpass

from custom_operations import hash_password, write_file, remove_line


def passwd_command(username: str):
    with open('passwords.txt', 'r+') as file:
        for line in file:
            lineList = line.split()
            if lineList[0] == username:
                password = getpass("Password: ")
                repeat_password = getpass("Repeat password: ")

                if password == repeat_password:
                    all_lines = remove_line(file, line)

                    new_password = hash_password(password)
                    new_user = lineList[0]
                    new_flag = lineList[1]
                    all_lines.append(new_user + " " + new_flag + " " + new_password + "\n")

                    write_file(file, all_lines)

                    print("Password change successful.")
                    file.close()
                    quit()
                else:
                    print("Password change failed. Password mismatch.")
                    file.close()
                    quit()
        print("Username does not exist")
        file.close()
