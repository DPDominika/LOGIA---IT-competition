#zad.2 2etap/12
#http://logia.oeiizk.waw.pl/nowa/page.php?sr=logia12/2etap

def IleCyfr(liczba, podstawa):

    """IleCyfr :liczba :podstawa, której wynikiem jest liczba cyfr liczby
podanej jako pierwszy parametr w układzie o podstawie podanej jako drugi
parametr. Parametr :liczba jest nieujemną liczbą całkowitą zapisaną w układzie
dziesiętnym nie większą niż 1020, parametr :podstawa jest liczbą całkowitą
większą od 1 i mniejszą niż 17."""

    wynik = ""
    wynik_2 = ""
    zbior = zbior = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while liczba != 0:
        for k in zbior.keys():
            if liczba % podstawa == k:
                wynik += zbior.get(k)
        liczba //= podstawa
    return len(wynik)

#poniżej kod, który również wypisuje liczbę po przeliczeniu z systemu
#dziesiątkowego na wybrany
    #w = len(wynik)-1
    #for i in range(len(wynik)):
        #wynik_2 += wynik[w]
        #w-=1
    #return wynik_2, len(wynik)
  



   
