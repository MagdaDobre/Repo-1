# exercitiu 1

def suma_2nr(numar,numar2):
    print(f'Suma este {numar + numar2}')

# exercitiu 2
def t_f(numar):
    if numar % 2 == 0:
        print(True)
    else:
        print(False)

# exercitiu 3
def total_nume():
    nume_complet = input('Numele complet este:')
    nume_complet = len(nume_complet)
    print(f'Numarul total de caractere este {nume_complet}')

    # def total_caractere(nume, prenume1, prenume2):                # rezolvarea data de ea, cred ca iese fara spatiu la numaratoare
    #     return len(nume + prenume1 + prenume2)
    #
    # print(total_caractere('Popescu', 'George', 'Dan'))
    # print(total_caractere('Ionescu', 'Daniela', 'Andreea'))

# exercitiu 4

def aria_dreptunghi():
    lungime = int(input('Adaugati lungimea:'))
    latime = int(input('Adaugati latimea:'))
    aria = lungime * latime
    print(f'Aria dreptunghiului este {aria}')

#  exercitiu 5
def aria_cerc():
    pi = 3.14
    raza = float(input('Adaugati raza:'))
    aria = pi*raza*raza
    print(f'Aria cercului este {aria}')

#  exercitiu 6
def caracter_existent():
    exemplu = input('Adaugati textul:')
    caracter_de_verificat = input("Adaugati caracterul de verificat:")
    if caracter_de_verificat in exemplu:
        print(True)
    else:
        print(False)

# exercitiu 7
def nr_caractere():
    text = 'AlabalaPorToCalA'
    caracter_lowercase = 0
    caracter_uppercase = 0
    for caracter in text:
        if caracter.islower():
            caracter_lowercase += 1

        else:
            caracter_uppercase +=1

    print(f'Nr de caractere lower case este {caracter_lowercase}')
    print(f'Nr de caractere upper case este {caracter_uppercase}')

# exercitiu 8
def lista_totala():
    lista = [2,5,3,69,-5,9,-12]
    lista_nr_poz = []
    for numere in lista:
        if numere >= 0:
            lista_nr_poz.append(numere)
    print(f"Acestea sunt numerele pozitive: {lista_nr_poz}")

# exercitiu 9
def doua_nr(x, y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif x < y:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale.')

# exercitiu 10
def ex_zece():
    nr = 4
    set = {4, 7, 12}
    if nr not in set:
        set.add(nr)
        print('am adaugat numărul nou în set')
        return True
    else:
        print('nu am adaugat numărul în set. Acesta există deja')
        return False

# ex 1 opt

def luna_an(luna):
    lunile_anului = {
        'Ianuarie': 31,
        'Februarie': 28,
        'Martie': 31,
        'Aprilie': 30
    }

    if luna in lunile_anului.keys():
        print(f'In luna {luna} sunt {lunile_anului[luna]} zile.')

    # if luna in lunile_anului:                 # solutie data de ea
    #     return lunile_anului.get(luna)
    #
    # print(calendar('June'))
    # print(calendar('January'))
    # print(calendar('February'))


# ex 2 optional

def calculator(x, y):
    def suma(x, y):
        return x + y
    def scadere (x,y):
        return x - y
    def inmultire(x,y):
        return x * y
    def impartire (x,y):
        return x / y

    a = suma(x, y)
    b = scadere(x, y)
    c = inmultire(x, y)
    d = impartire(x, y)
    print("Suma:", a)
    print("Diferenta:", b)
    print("Inmultirea:", c)
    print("Impartirea:", d)
    return a, b, c, d

    # def calculator(x, y):             # solutie data de ea
    #     a = x + y
    #     b = x - y
    #     c = x * y
    #     d = x / y
    #     return a, b, c, d
    #
    # a, b, c, d = calculator(3, 2)
    #
    # print("Suma: ", a)
    # print("Diferenta: ", b)
    # print("Inmultirea: ", c)
    # print("Impartirea: ", d)


# a, b, c, d = calculator(10, 2)

# ex 3 optional

# def lista_dict():
#     lista_exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
#     dict = {
#         '0': 0,
#         '1': 0,
#         '2': 0,
#         '3': 0,
#         '4': 0,
#         '5': 0,
#         '6': 0,
#         '7': 0,
#         '8': 0,
#         '9': 0
#     }

def CountFrequency():
    my_list = [1,1,3,4,5,6,5,2,1]
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d" % (key, value))

    # def count(lista):                     # solutie data de ea
    #     cnt = {
    #         0: 0,
    #         1: 0,
    #         2: 0,
    #         3: 0,
    #         4: 0,
    #         5: 0,
    #         6: 0,
    #         7: 0,
    #         8: 0,
    #         9: 0
    #     }
    #     for i in cnt.keys():
    #         for j in lista:
    #             if i == j:
    #                 cnt[i] = cnt[i] + 1
    #     return cnt
    #
    # lista1 = [1, 1, 2, 7, 7, 7]
    #
    # print(count(lista1))


#  ex 4 opt


def val_max(nr1, nr2, nr3):
    maxim = 0

    if nr1 > nr2 and nr1 > nr3:
        maxim = int(nr1)
    elif nr2 > nr1 and nr2 > nr3:
        maxim = int(nr2)
    else:
        maxim = int(nr3)

    print(f'Valoarea maxima este {maxim}')

    # def maxim(a, b, c):                       # solutie data de ea
    #     if a == b and b == c:
    #         max = a
    #     elif a >= b and a >= c:
    #         max = a
    #     elif b >= a and b >= c:
    #         max = b
    #     else:
    #         max = c
    #     return max
    #
    # print(maxim(5, 7, 2))  # returneaza 7
    # print(maxim(7, 6, 2))  # returneaza 7
    # print(maxim(5, 6, 7))  # returneaza 7
    # print(maxim(4, 4, 4))  # returneaza 4
    # print(maxim(4, 3, 3))  # returneaza 4
    # print(maxim(3, 4, 3))  # returneaza 4
    # print(maxim(3, 3, 4))  # returneaza 4

# ex 5 opt

def nr_suma(nr):
    suma = sum(range(0,nr+1))
    print(suma)

    # def suma_num(a):                  # solutie data de ea
    #     suma = 0
    #     for i in range(0, a + 1):
    #         suma = suma + i
    #     return suma
    #
    # print(suma_num(3))  # returneaza 6

# ex opt bonus 1

def double_list():
    list1 = [1, 1, 2, 3, 4, 6, 9]
    list2 = [2, 2, 3, 4, 5, 7, 8]
    result = {}

    result = [i for i in list1 if i in list2]
    print(f"The common elements in the two lists are: {result}")

    # def common_nr(l1, l2):                #solutie data de ea
    #     set1 = set(l1)
    #     set2 = set(l2)
    #     return set1.intersection(set2)
    #
    # list1 = [1, 1, 2, 3]
    # list2 = [2, 2, 3, 4]
    #
    # print(common_nr(list1, list2))


# ex opt bonus 2
def reducere_pret():
    pret_produs = 100
    reducere = 10
    pret_final = 0



    if reducere > 0 and reducere <= 110:
        pret_final = pret_produs - pret_produs * reducere / 100
    print(f'Pretul final al produsului este: {pret_final} lei')

    # def reducere_preturi(price, sale):                # solutie data de ea
    #     if sale > 100 or sale < 0:
    #         return 'reducere invalida'
    #     new_price = price - (sale / 100) * price
    #     return new_price
    #
    # print(reducere_preturi(100, 10))  # 90
    # print(reducere_preturi(100, -1))  # no
    # print(reducere_preturi(100, 101))  # no

# ex opt bonus 3
def datetime():
    from datetime import datetime


    now = datetime.now()
    print('Current DateTime:', now)

def date_tine_Ch():
    from datetime import datetime
    import pytz

    datetime_China = datetime.now(pytz.timezone('Asia/Kolkata'))
    print('China:',  datetime_China.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

# ex opt bonus 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)


def zile_ramase_Craciun():
    import datetime

    today = datetime.date.today()
    future = datetime.date(2022,12,25)
    diff = future - today
    print(f'Zile ramase pana la Craciun :{diff.days} zile')















