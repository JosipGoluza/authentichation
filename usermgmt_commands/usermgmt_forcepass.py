import bcrypt

from custom_operations import remove_line, write_file


def forcepass_command(username: str):
    with open('passwords.txt', 'r+') as file:
        for line in file:
            lineList = line.split()
            if bcrypt.checkpw(username.encode('utf-8'), lineList[0].encode('utf-8')):
                all_lines = remove_line(file, username)

                new_user = lineList[0]
                new_flag = "1"
                new_password = lineList[2]
                all_lines.append(new_user + " " + new_flag + " " + new_password + "\n")

                write_file(file, all_lines)

                print("User will be requested to change password on next login.")
                file.close()
                quit()
        print("Username does not exist")
        file.close()
