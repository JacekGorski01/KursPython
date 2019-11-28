class A():
    def __init__(self):
        A.litera = "A"

class B(A):
    # def __init__(self):
    #     B.litera = "B"
    pass

class C(A):
    def __init__(self):
        C.litera = "C"


class D(B, C):
    pass


litera = D()
print(D.litera)
