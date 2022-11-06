# exercitiul 1
#  cum functioneaza un if else - daca conditia care urmeaza cuvantul cheie if este evaluata ca True, se va executa codul.Daca conditia este False, se poate adauga, optional, else.

#  exercitiul 2
x = 3
y = 3
z = 3

print(type(x))
if x >= 0 and type(x) == int:
    print(' x este numar natural')
else:
    print('x nu este numar natural')

# exercitiul 3
if x >=1:
    print('x este numar pozitiv')
elif x<0:
    print('x este numar negativ')
else:
    print('x este numar neutru')

# exercitiu 4
if x >= -2 and x <=13:
    print('x este intre range-ul afisat')
else:
    print(' x nu este in range-ul solicitat')

# exercitiu 5

if x - y < 5:
    print('statementul este valid')

exercitiul 6
if not(x >= 5 and x <=27):
    print(' x nu este intre 5 si 27')

# exercitiul 7
print(type(x))
print(type(y))

if x == y:
    print("x si y sunt egale")
elif x >y:
    print('x mai mare ca y')
else:
    print('y mai mare ca x')

# exercitiul 8

if x == y == z:
    print('Triunghiul este echilateral')
elif (x == y and x != z) or (x == z and x != y):
    print("Triunghiul este isoscel")
else:
    print('Triunghiul este oarecare')

# exercitiul 9
litera = input('Adauga o litera: ')

if litera in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
    print('litera este o vocala')
else:
    print('litera nu este o vocala')

# exercitiul 10

nota = int(input('Adaugati nota: '))

if nota > 9:
    print('Calificativul obtinut este A')
elif nota > 8:
    print('Calificativul obtinut este B')
elif nota > 7:
    print('Calificativul obtinut este C')
elif nota > 6:
    print('Calificativul obtinut este D')
elif nota > 4:
    print('Calificativul obtinut este E')
elif nota <= 4 and nota >= 1:
    print('Calificativul obtinut este F')
else:
    print('Nota introdusa nu este valida')

# ---------------------------------------------------------------------------------------

# exercitiile optionale
# exercitiul 1

x = 70
y = 50
z = 60

if len(str(x)) >= 4:
    print('X are minim 4 cifre')

# exercitiul 2
if len(str(x)) == 6:
     print('X are exact 6 cifre')

# exercitiul 3

if x % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

#  exercitiul 4

if x > y and x > z:
    print(' x este cel mai mare')
elif y > x and y > z:
    print('y este cel mai mare')
else:
    print('z este cel mai mare')

# exercitiul 5

if x + y + z == 180 and x!= 0 and y != 0 and z != 0:
    print('This triangle is valid')
else:
    print('This triangle is invalid')

# exercitiul 6

string = 'Coral is either the stupidest animal or the smartest rock'
nr_caracter = int(input('introduceti nr: '))
print(string[:-nr_caracter])

# exercitiul 7
string = 'Coral is either the stupidest animal or the smartest rock'
string_nou = (string[0:5] + string[-5:])
print(string_nou)

# exercitiul 8
string = 'Coral is either the stupidest animal or the smartest rock'
index_de_start = string.index('rock')
print(index_de_start)
print(string[0:index_de_start])

# exercitiul 9
denumire = input('Introdu valoarea:')
assert denumire[0].lower() == denumire[-1].lower()
print('Primul si ultimul caracter sunt la fel')

# exercitiul 10
string_numeric = '0123456789'

print(f'Numerele pare sunt: {string_numeric[0:-1:2]}')
print(f'Numerele impare sunt: {string_numeric[1::2]}')

# exercitiul 11 BONUS

import random
dice_roll = random.randrange(1,7)
numar_utilizator = int(input('Ce numar credeti ca a picat: '))

if numar_utilizator <= 0 or numar_utilizator > 6:
    print('Numar invalid. Va rugam sa alegeti din intervalul 1 - 6 ')
elif numar_utilizator < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_utilizator} dar a fost {dice_roll}')
elif numar_utilizator > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_utilizator} dar a fost {dice_roll}')
else:
    print(f'Ai ghicit.Felicitari! Ai ales {numar_utilizator} si zarul a fost {dice_roll}')