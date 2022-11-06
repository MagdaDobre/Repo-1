# exercitiul 1
# Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă.
# Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări.
# Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.

lista_muzicala = ['do','re','mi','fa','sol','la','si','do']
print(lista_muzicala)
lista_muzicala = lista_muzicala[::-1]
print(lista_muzicala)
lista_muzicala.reverse()
print(lista_muzicala)

# exercitiul 2
# De câte ori apare ‘do’?

print(lista_muzicala.count('do'))

# exercitiul 3
# Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]

lista_1.extend(lista_2)
print(lista_1)

# exercitiul 4
# ● Sortează și afișează lista generată la exercițiul anterior.
# ● Sterge numărul 0 folosind o funcție.
# ● Afișeaza iar lista.

lista_1.sort()
print(lista_1)

lista_1.remove(0)
print(lista_1)

# *exercitiul 5
# Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.

if len(lista_1) <= 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# exercitiul 6
# Folosește o funcție care să șteargă lista de la exercițiul 3.

lista_1.clear()
print(lista_1)

# exercitiul 7

if len(lista_1) <= 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# exercitiul 8
# Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

print(dict1.keys())

# exercitiul 9
# Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie

print(f'Ana a luat nota ' + str(dict1['Ana']))
print(f'Gigel a luat nota ' + str(dict1['Gigel']))
print(f'Dorel a luat nota ' + str(dict1['Dorel']))

# exercitiul 10
# Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare

dict1.update({'Dorel': '6'})
print(dict1)

dict1['Dorel'] = 6
print(dict1)

print(dict1['Dorel'])

# exercitiul 11
# Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi

dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)


print('*------------------------------')
#  exercitiul 12
# Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt


zile_sapt.add('luni')
print(zile_sapt)

# exercitiul 13
# Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.


if weekend == weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămâna.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# exercitiul 14
# Afișează diferențele dintre aceste 2 seturi.

print(zile_sapt.difference(weekend))

# exercitiul 15
# Afișază intersecția elementelor din aceste 2 seturi.

print(zile_sapt.intersection(weekend))

# exercitiul optional
# Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferiteb
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
# Google search hint
# “how to check if item îs în list python”



jucatori = ['Ionel', 'Gigel', 'Vasile','Mircea','Sebi']
schimbari_max = 3
schimbari_efectuate = 0

jucator_de_schimbat = input('Adaugati jucatorul care trebuie schimbat :').capitalize()



if jucator_de_schimbat in jucatori and schimbari_efectuate <= schimbari_max:
    print('Se poate face schimbarea')

    jucatori.remove(jucator_de_schimbat)
    print(jucatori)

    jucatori.append(input('Jucatorul nou este:').capitalize())
    print(jucatori)

    schimbari_efectuate +=1

    print('A intrat jucatorul ' + jucatori[-1] + ' , a iesit jucatorul ' + jucator_de_schimbat + ', mai ai ' + str(schimbari_max - schimbari_efectuate) + ' schimbari la dispozitie.')

else:
    print('Nu se poate efectua schimbarea, deoarece jucatorul ' + jucator_de_schimbat + ' nu este in teren.')

