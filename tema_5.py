from tema_5_utile import suma_2nr, t_f, total_nume, aria_dreptunghi,aria_cerc,caracter_existent,nr_caractere,lista_totala, doua_nr,ex_zece,luna_an, calculator,CountFrequency,val_max, nr_suma, double_list, reducere_pret, datetime, date_tine_Ch,zile_ramase_Craciun

# exercitiu 1 : 1.Funcție care să calculeze și să returneze suma a două numere

suma_2nr(2,1)

# exercitiu 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

t_f(27)

# exercitiu 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

total_nume()

# exercitiu 4. Funcție care returnează aria dreptunghiului
aria_dreptunghi()

# exercitiu 5. Funcție care returnează aria cercului
aria_cerc()

# exercitiu 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
caracter_existent()

# exercitiu 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

nr_caractere()

# exercitiu 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
lista_totala()

# exercitiu 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

doua_nr(3,3)

# exercitiu 10.Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

ex_zece()

# exercitii Optionale
# ex 1 opt. Funcție care primește o lună din an și returnează câte zile are acea luna

luna_an('Februarie')

# ex 2 opt
# Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

calculator(10,2)

# ex 3 opt
# Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

CountFrequency()

# ex 4 opt. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

val_max(6,2,3)

# ex 5 opt. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

nr_suma(5)

# ex opt bonus 1. Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

double_list()

# ex opt bonus 2. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.

reducere_pret()

# ex opt bonus 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
datetime()
date_tine_Ch()

# ex opt bonus 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
zile_ramase_Craciun()