def FtoC(f):
    '''Transforms Fahrenheitas to Celcius
    Arguments:
    f (int) - number of Fahrenheit`s degrees

    Return:
    c (int) - number of Celcius degrees
    '''
    c = (f - 32) / (9 / 5)
    c = ("%.2f" % c)

    return c

def KtoC(k):
    '''Transforms Kelvins to Celcius
      Arguments:
      k (int) - number of Kelivin`s degrees

      Return:
      c (int) - number of Celcius degrees
      '''

    c = ("%.2f" % (k - 273.15))


    return c