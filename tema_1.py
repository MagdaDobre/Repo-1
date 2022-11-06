# exercitiul 1:
# o variabila este o eticheta pusa unei cutii ce contine mai multe valori/lucruri/informatii

# -----------------------------------------------------------------------------------------
# exercitiul 2: declararea si initializare unei variabile
# string
#nume = 'Magda'
#print(nume)
# int
#varsta = 33
#print(varsta)
# float
#venit = 3500.5
#print(venit)
# bool
#angajata = False
#print(angajata)

#prezentare = f'Buna! Numele meu este {nume}, am varsta de {varsta} ani. Teoretic, venit meu este de {venit} lei, desi statusul de angajare este {angajata}.'
#print(prezentare)

# ------------------------------------------------------------------------------------------
# exercitiul 3 - functia type
#print(type(nume))
#print(type(varsta))
#print(type(venit))
#print(type(angajata))


# -----------------------------------------------------------------------------------------
# exercitiul 4 - functia round
#venit = round(venit)
#print(f'Noul venit este {venit}')
#print(type(venit))

# ----------------------------------------------------------------------------------------
# exercitiul 5
#print(f'Numele meu este {nume}')
#print(f'Am varsta de {varsta} ani.')
#print(f'Venitul actual este de {venit} lei.')
#print(f'Propozitia sunt angajata la momentul actual este {angajata}.')

# ----------------------------------------------------------------------------------------
# exercitiul 6
# nume = input('Va rugam adaugati numele dvs: ')
# prenume = input('Va rugam adaugati prenumele dvs: ')
# print(f'Numele complet are ' + str(len(nume) + len(prenume)) + ' caractere.')

# ----------------------------------------------------------------------------------------
# exercitiul 7
# lungime = int(input('Valoare lungime:'))
# latime = int(input('Valoare latime:'))
# aria = lungime * latime
# print(f'Aria dreptunghiului este {aria}')

# -----------------------------------------------------------------------------------------
# exercitiul 8
# enunt = 'Coral is either the stupidest animal or the smartest rock'
# print(enunt.count(' the ')) - aici am pus spatiu inainte si dupa cuvant (the) pentru a nu il pune la calcul si pe the din either

# -----------------------------------------------------------------------------------------
# exercitiul 9
# print(enunt.replace(' the ',' THE ')) - la fel ca mai sus

# ------------------------------------------------------------------------------------------
# exercitiul 10

# assert enunt.isdigit() == False
# print('Nu exista numere in enunt')
# assert enunt.isdigit() == True
# print('Avem numere in variabila enunt')

# -------------------------------------------------------------------------------------------

# exercitii optionale
#  exercitiul 1
# string_impar = input('String impar:')

# metoda 1
# print(string_impar[2])

# metoda 2
# mijloc = int(len(string_impar)/2)
# print(string_impar[mijloc])

# exercitiul 2
# exemplu = 'babababab'
#
# assert exemplu == exemplu[::-1]
# print('Acest string este un palindrom')

# exercitiul 3
# nume, prenume = input('Adauga nume si prenume:').split()
# print(nume)
# print(prenume)

# exercitiul 4
# nume_prenume = input('Adauga nume si prenume:')
# primul_caracter = nume_prenume[0]
# print(primul_caracter)
# capital_primul_caracter = primul_caracter.upper()
# print(capital_primul_caracter)
# capitalizam_primul_caracter = nume_prenume[0] + nume_prenume[1:-1].replace(primul_caracter,capital_primul_caracter) + nume_prenume[-1]
# print(capitalizam_primul_caracter)

# exercitiul 5
user = input('Enter user:')
parola = input('Enter password:')
l_parola = str(len(parola))
print(f'Parola pentru user {user} este {parola} si are {l_parola} caractere')















