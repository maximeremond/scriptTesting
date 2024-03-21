def divideList(liste):
    try:
        liste = [float(item) for item in liste]
    except:
        return None
    return None if (len(liste) != 2 or 0 in liste) else (liste[0]/liste[1])
