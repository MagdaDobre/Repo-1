# exercitiu 1
# Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
import random

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']


for i in range(0, len(masini)):
    print(f'Mașina mea preferata este {masini[i]}')

print(f'--------------------------------------')

for i in masini:
    print(f'Mașina mea preferata este {i}')
print(f'--------------------------------------')

i = 0
while i < len(masini):
    print(f'Mașina mea preferata este {masini[i]}')
    i +=1
print("am iesit din while")
print(f'--------------------------------------')

# exercitiul 2
# Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,exceptând primul și ultimul.
# În else:
# - Printează lista.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']


for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# exercitiu 3.
# Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
#
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']


for i in masini:
    if i == 'Mercedes':
        print('am găsit mașina dorită de dvs')
        break
    else:
        print(f'Am găsit mașina {i}. Mai căutam')

# exercitiul 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# - Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {i}')

print('-------------------------------------------')

# exercitiul 5. Modernizează parcul de mașini:

# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini_vechi= []
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for masina in masini:
    print(masina)
    if masina == 'Trabant' or masina == 'Lăstun' in masini:
        masini_vechi.append(masina)
        print(masini_vechi)

masini[masini.index("Trabant")] = "Tesla"
masini[masini.index("Lăstun")] = "Tesla"

print(f'Modele vechi:{masini_vechi} ')
print(f'Modele noi: {masini}')


print('-------------------------------------------')
# exercitiul 6
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# ● Iterează prin listă.


pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

buget = 15000


for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Acestea sunt masinile care se incadreaza in buget {masina}')

for masina, pret in pret_masini.items():
    print(f'Masina {masina} are pretul de {pret} euro')

print('-------------------------------------------')

# exercitiul 7
# Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitie_3 = 0

for numar in numere:
    if numar == 3:
        aparitie_3 = aparitie_3 + 1
print(f'De {aparitie_3} ori apare numarul 3 in lista data')

print('-------------------------------------------')

# exercitiul 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

suma = 0

for numar in numere:
    suma += numar
print(suma)

print('-------------------------------------------')

# exercitiul 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
cel_mai_mare_numar = numere[0]

for numar in numere:
    if numar > cel_mai_mare_numar:
        cel_mai_mare_numar = numar
print(f'Acesta este cel mai mare numar din lista: {cel_mai_mare_numar}')

print('-------------------------------------------')

# exercitiul 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_noua = []

for numar in numere:
    if numar > 0:
        numar = 0 - numar
    lista_noua.append(numar)

print(f'Noua lista este {lista_noua}')

print('-------------------------------------------')

# exercitii optionale

#  exercitiul 1
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)

print(f'Acestea sunt numerele pare: {numere_pare}')
print(f'Acestea sunt numerele impare: {numere_impare}')
print(f'Acestea sunt numerele pozitive: {numere_pozitive}')
print(f'Acestea sunt numerele negative: {numere_negative}')

print('-------------------------------------------')

# exercitiul 2
# Aceeași listă:
# Ordonează crescător lista fară să folosești sort.

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range (len(alte_numere)):
    for j in range (i + 1,len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]

print(f'Lista sortata este: {alte_numere}')

print('-------------------------------------------')

# exercitiul 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!

import random

numar_secret = random.randrange(1,31)
numar_ghicit = None

while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Va rugam introduceti un nr:'))
    if numar_secret > numar_ghicit:
        print(f'Numarul secret {numar_secret} este mai mare decat cel introdus {numar_ghicit}')
    elif numar_secret < numar_ghicit:
        print(f'Numarul secret {numar_secret} este mai mic decat cel introdus {numar_ghicit}')
else:
        print('Felicitări! Ai ghicit!')

print('-------------------------------------------')

# exercitiul 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333

numar = int(input('Alege un numar:'))

for i in range(numar+1):
    for j in range(i):
        print(i, end='')
    print()

print('-------------------------------------------')

# exercitiu 5
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')
