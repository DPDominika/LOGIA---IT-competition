#zad.3 etap2/09
#http://logia.oeiizk.waw.pl/nowa/page.php?sr=logia09/2etap

def ICP(x):

    """ICP :x, której daną :x jest niepuste słowo złożone wyłącznie z cyfr
(maksymalnie 100 cyfr), a wynikiem wartość logiczna prawda,
gdy iloczyn cyfr danej :x jest liczbą pierwszą, a fałsz,
gdy iloczyn cyfr danej :x nie jest liczbą pierwszą."""

    wynik = 1
    pierwsza = 0
    licznik = 0

    for i in x:
        wynik *= int(i)

    for m in range(2, 101):
        if wynik % m == 0:
            pierwsza += 1
        else:
            licznik += 1
            
    return pierwsza == 1
    return pierwsza > 1


        
