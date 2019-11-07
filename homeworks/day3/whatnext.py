def start_other_module(filename):

    '''Start any other module after finishing this sub-programme

    Parameters:
    filname (string): name of module to import

    Action:
    importing module to the ongoing script

    '''
    what_next = input(f'\nJeśli chcesz wykonać inny program ({filename}) wybierz "T", jeśli chcesz zakończyć - dowolny klawisz.')
    if what_next == "T":
        __import__(filename)
    else:
        print("Do zobaczenia!")
        exit(0)


