from custom_operations import remove_line, write_file


def forcepass_command(username: str):
    with open('passwords.txt', 'r+') as file:
        for line in file:
            lineList = line.split()
            if lineList[0] == username:
                all_lines = remove_line(file, username)

                new_user = lineList[0]
                lineList[1] = "1" if lineList[1] == "0" else "0"
                new_flag = lineList[1]
                new_password = lineList[2]
                all_lines.append(new_user + " " + new_flag + " " + new_password + "\n")

                write_file(file, all_lines)

                print("User will be requested to change password on next login.")