def menu_builder(file_list,line):
    '''Show selected line without reading all lines in file

    This is form purpose of "multitool" script. Point line in a file you want to add to menu.
    String slicing has been done due to my own text formating in a file

    Parameters:
    file_list (str) - file list to read
    line (int) - line from file above you want to print (BY DEFALLT line = 3)

    Return:
    None

    Action:
    Print string
    '''
    print("*** W I E L O   N A R Z Ę D Ź *** by JACEK VER 1.0\n")
    for i, file in enumerate(file_list):
        with open(file, "r") as file:

            for j in range(line):
                line_content = file.readline()
            if j == line-1:
                end = len(line_content) - 9
                text = (line_content[13:(end)])
                print(f"({i + 1}) {text}.")
                continue

    print("(R) Wylosuj za mnie\n(Q) Wyjdź z WIELO NARZĘDZIA")


