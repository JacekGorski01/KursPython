from whatnext import start_other_module

print("\n*** To jest program do rysowania prostokąta o zadanych wymiarach ***\n")

w=int(input("Podaj szerokość prostokąta: "))
h=int(input("Podaj wysokość prostokąta: "))

def print_top_bottom(w):
    '''Print the top and bottom line of square, which is w-long

    Parameters:
    w (int): weight of bottom/top line

    Action:
    Drawing a line

    Returns:
    None
    '''
    print("+" + (w - 2) * "-" + "+")

print_top_bottom(w)


while h > 2:
    print("|" + (w-2) * " " + "|")
    h-=1

print_top_bottom(w)


start_other_module("multitool")