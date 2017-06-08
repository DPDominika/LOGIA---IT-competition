#zad 4, etap 1/15
#http://logia.oeiizk.waw.pl/nowa/page.php?sr=logia15/1etap

def bieg(tempo):

    """ Parametrem funkcji jest liczba naturalna, nie zawierająca
        w swym zapisie zer, z zakresu od 11 do 2147483647"""

    tempo2 = str(tempo)
    wynik = 0
    n = 0
    for i in range(len(tempo2)-1):
        n-=1
        if tempo2[n-1] == tempo2[n]:
            wynik += 1
    return wynik


        
