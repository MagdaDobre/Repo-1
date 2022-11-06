# exercitiu 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
import self as self


class circle:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')

    def aria(self):
        return self.raza * self.raza * 3.14

    def diametru(self):
        return self.raza + self.raza

    def circumferinta(self):
        return (self.raza + self.raza) * 3.14


circle1 = circle(5,'alb')
print(circle1)
circle1.descrie_cerc()

circle1.aria()
print(circle1.aria())
circle1.diametru()
print(circle1.diametru())
circle1.circumferinta()
print(circle1.circumferinta())


# exercitiu 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class dreptunghi:

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}.')

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


dreptunghi1 = dreptunghi(4,5,'verde')
print(dreptunghi1)
dreptunghi1.descrie()

dreptunghi1.aria()
print(dreptunghi1.aria())
dreptunghi1.perimetrul()
print(dreptunghi1.perimetrul())

dreptunghi1.schimba_culoarea('albastru')
dreptunghi1.descrie()


# exercitiu 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Angajatul se numeste {self.nume} {self.prenume} si are salariul de {self.salariu} de lei.')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu = self.salariu + (self.salariu * procent / 100)


angajat1 = angajat('andrei', 'vlad', 500)
print(angajat1)
angajat1.descrie()

angajat1.nume_complet()
print(angajat1.nume_complet())

angajat1.salariu_lunar()
print(angajat1.salariu_lunar())

angajat1.salariu_anual()
print(angajat1.salariu_anual())

angajat1.marire_salariu(50)
angajat1.descrie()

# exercitiu 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self,suma):
        if suma > self.sold:
            print(f'Suma solicitata depaseste soldul actual in valoare de {self.sold} lei.')
        else:
            self.sold = self.sold - suma
            print(f'Ati retras suma de {suma} lei. Soldul actual este de {self.sold} lei.')

    def creditare_cont(self, suma):
        self.sold = self.sold + suma
        print(f'Ati alimentat contul cu suma de {suma} lei. Soldul actual este de {self.sold} lei.')

cont1 = cont('ro12bcr','andrei', 100)
print(cont1)
cont1.afisare_sold()

cont1.debitare_cont(150)
cont1.afisare_sold()

cont1.creditare_cont(500)
cont1.afisare_sold()


# exercitiu opt 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class factura:
    serie = 'AV00001'
    numar = None
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        print(f'Cantitatea actuala este {self.cantitate} buc.')

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        print(f'Pretul actual este {self.pret_buc} lei/buc.')

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume
        print(f'Numele actual al produsului este {self.nume_produs}.')

    def genereaza_factura(self):
        from datetime import datetime
        from tabulate import tabulate

        print(f'Factura seria {self.serie} numar {self.numar}')
        print(f'Data: {datetime.today()}')

        table = [['Produs', 'Cantitate','Pret bucata','Total'], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc]]
        print(tabulate(table))


factura1 = factura(12, 'tv', 2, 200)
print(factura1)


factura1.schimba_cantitatea(5)
factura1.schimba_pretul(50)
factura1.schimba_nume_produs('laptop')
factura1.genereaza_factura()

# exercitiu opt 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False

# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class masina:
    marca = 'Opel'
    model = ['Astra', 'J', 'H']
    viteza_maxima = 0
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'Alb', 'Verde', 'Albastru', 'Rosu', 'Negru'}
    inmatriculata = False

    def __init__(self,model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Masina marca {self.marca},model {self.model}, culoarea {self.culoare}, viteza actuala: {self.viteza_actuala} km/h si viteza maxima {self.viteza_maxima} km/h, inmatriculata {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
        else:
            print(f'Culoare indisponibila. Alegeti din variantele date: {self.culori_disponibile}')

    def accelereaza(self, viteza):
        if viteza <=0:
            print('Nu se poate accelera, viteza nu este pozitiva')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala = viteza

    def franeaza(self):
        if self.viteza_actuala > 0:
            self.viteza_actuala = 0
            print(f"Masina a ajuns la {self.viteza_actuala} km.")
        else:
            print("Nu putem frana pentru ca viteza este deja 0 km.")


masina1 = masina('Astra', 220)
masina1.descrie()

masina1.inmatriculare()
masina1.descrie()

masina1.vopseste('Rosu')
print(masina1.culoare)

masina1.accelereaza(90)
print(masina1.viteza_actuala)
masina1.descrie()

masina1.franeaza()
masina1.franeaza()


# exercitiu opt 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class TodoList:
    to_do = {}

    def adauga_task(self, nume, descriere):
        self.to_do[nume] = descriere

    def finalizeaza_task(self,nume):
        self.to_do.pop(nume)

    def afiseaza_todo_list(self):
        print(self.to_do.keys())

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.to_do:
            print(f'Detaliile suplimentare ale taskului {nume_task} sunt {self.to_do.values()}')
        else:
            task_nou = input('Acest task nu este in lista. Doriti adaugarea acestui nou task? [da/nu]:').lower()
            if task_nou == 'nu':
                print('Task-ul nu a fost adaugat.')
            else:
                descriere_task_nou = input('Va rugam sa adaugati descrierea taskului nou: ')
                self.adauga_task(nume_task, descriere_task_nou)


TodoList_test = TodoList()
print(TodoList_test)
TodoList_test.adauga_task('mail', 'raspuns mail')
TodoList_test.adauga_task('call', 'apelare clienti')
print(TodoList_test.to_do)
TodoList_test.finalizeaza_task('call')
print(TodoList_test.to_do)
TodoList_test.afiseaza_todo_list()
TodoList_test.afiseaza_detalii_suplimentare('apel')
print(TodoList_test.to_do)