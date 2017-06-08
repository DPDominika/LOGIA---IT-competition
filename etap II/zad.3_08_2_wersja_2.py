#zad.3 etap2/08
#http://logia.oeiizk.waw.pl/nowa/page.php?sr=logia08/2etap

def MAXX(słowo):
    """gdzie :słowo jest dowolnym niepustym słowem składającym się jedynie
    z małych liter alfabetu łacińskiego. Wynikiem funkcji jest najdłuższe
    podsłowo (fragment słowa - ciąg kolejnych znaków), które rozpoczyna się
    i kończy się tym samym znakiem. Jeśli w danym słowie jest wiele takich
    najdłuższych podsłów, to wynikiem jest dowolne z nich."""

    podsł = []
    dł = []
    n = 0

    while n <= len(słowo)-1:
        n+=1
        for i in range(len(słowo)):
            if (słowo[i:(i+n)])[0] == (słowo[i:(i+n)])[-1]:
                podsł.append(słowo[i:(i+n)])
        
    for j in range(len(podsł)):             
        dł.append(len(podsł[j])) 

    return podsł[(dł.index(max(dł)))] 


        
