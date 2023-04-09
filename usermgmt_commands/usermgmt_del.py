from custom_operations import remove_line, write_file


def del_command(username: str):
    with open('passwords.txt', 'r+') as file:
        for line in file:
            lineList = line.split()
            if lineList[0] == username:
                all_lines = remove_line(file, username)
                write_file(file, all_lines)
                print("User deleted.")
                file.close()
                quit()
        print("Username does not exist")
        file.close()
