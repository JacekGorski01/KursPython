def menu_builder(file_list,line):
    '''It is for building menu from external text file.
    You can either create mnu from single text file (each line of menu has to be single line in file)
    or you can grab firs commented-out line contains menu string from collection of files.

    This is for purpose of "multitool" script. Point line in a file you want to add to menu.
    String slicing has been done due to my own text formating in a file

    Parameters:
    file_list (str) - file list to read
    line (int) - int(1) to print first line from selected files or int(line) to print out menu from whole text file.

    Return:
    None

    Action:
    Print string
    '''
    print("*** W I E L O   N A R Z Ę D Ź *** by JACEK VER 1.0\n")
    #otwieram w pętli pliki z listy
    for i, file in enumerate(file_list):
        with open(file, "r") as file:
            #otwarty plik cztam linia po linii do linii podanej w parametrze funkcji.
            # Nie chciałem czytać całego pliku i wybierać linii zwłaszcza, że ta była jest w mioch plikach na początku
            if range(line) == range(1):
                for j in range(line):
                    content = file.readline()
                    print(f"({i+1}) {content[1:]}") #wycinam "#"

            else:
                for j in range(line):
                    line_content = file.readline()
                    print(f"({j + 1}) {line_content}")
    print("(R) Wylosuj za mnie\n\n(Q) Wyjdź z WIELO NARZĘDZIA")


