def CelToFah(lampotila):
    fah = lampotila * 1,8 + 32
    return fah

def CelToKel(lampotila):
    kel = lampotila + 273,15
    return kel

def KelToFah(lampotila):
    fah = lampotila * 1,8 - 459,67
    return fah

def KelToCel(lampotila):
    cel = lampotila - 273,15
    return cel

def FahToKel(lampotila):
    kel = (lampotila + 459,67) / 1,8 
    return kel

def FahToCel(lampotila):
    cel = (lampotila - 32) / 1,8
    return cel

versio = 1.0