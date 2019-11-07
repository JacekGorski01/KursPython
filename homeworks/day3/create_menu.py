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
    #otwieram w pętli pliki z listy
    for i, file in enumerate(file_list):
        with open(file, "r") as file:
            #otwarty plik cztam linia po linii do linii podanej w parametrze funkcji.
            # Nie chciałem czytać całego pliku i wybierać linii zwłaszcza, że ta była jest w mioch plikach na początku
            for j in range(line):
                line_content = file.readline()
            if j == line-1: #czytam linie aż znajduje wskazaną w zminnej żeby ją wydrukować
                end = len(line_content) - 9
                text = (line_content[13:(end)]) #odcinam znaki z kodu (od printa)
                print(f"({i + 1}) {text}.") #i+1 żeby odpowiednio ponumerować menu
                continue

    print("(R) Wylosuj za mnie\n(Q) Wyjdź z WIELO NARZĘDZIA")


