def multiplylist(liste):
    total = 1.0
    try:
        for item in liste:
            total *= float(item)
        return total
    except:
        return None
