def addlist(liste):
    somme = 0
    try:
        for item in liste:
            somme += float(item)
        return somme
    except:
        return None
