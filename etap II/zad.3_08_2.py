#zad.3 etap2/08
#http://logia.oeiizk.waw.pl/nowa/page.php?sr=logia08/2etap

def MAXX(słowo):
    """gdzie :słowo jest dowolnym niepustym słowem składającym się jedynie
    z małych liter alfabetu łacińskiego. Wynikiem funkcji jest najdłuższe
    podsłowo (fragment słowa - ciąg kolejnych znaków), które rozpoczyna się
    i kończy się tym samym znakiem. Jeśli w danym słowie jest wiele takich
    najdłuższych podsłów, to wynikiem jest dowolne z nich."""

    pocz = {}
    kon = {}
    final = []
   

    for i in range(len(słowo)):
        if słowo[i] not in pocz:
            pocz[słowo[i]] = i

    for i in range((len(słowo)-1), -1, -1):
        if słowo[i] not in kon:
            kon[słowo[i]] = i

    for key in pocz:
        final.append(słowo[pocz.get(key):(kon.get(key)+1)])
    return max(final, key=len)
   
        


        


   
