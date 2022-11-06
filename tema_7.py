
# exercitiu 2.
# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print('Cel mai probabil am colturi')

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        print(f'Aria patratului este {self.__latura * self.__latura}')


    @property
    def latura(self):
        return self.latura

    @latura.getter
    def latura(self):
        print(f"Getter: Latura are lungimea de {self.__latura}")
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f"Setter: Am updatat lungimea cu {latura}")
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f"Deleter: Am sters lungimea laturii.")
        self.__latura = None



class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        print(f'Aria cercului este {self.__raza * self.__raza * self.PI}')

    @property
    def raza(self):
        return self.raza

    @raza.getter
    def raza(self):
        print(f"Getter: Raza este {self.__raza}")
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f"Setter: Am updatat raza cu {raza}")
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f"Deleter: Am sters raza.")
        self.__raza = None

    def descrie(self):
        print('Eu nu am colturi')


patrat_test = Patrat(5)
patrat_test.descrie()

patrat_test.aria()

patrat_test.latura
patrat_test.latura = 7
patrat_test.latura
del patrat_test.latura
patrat_test.latura

print('----------------------')
cerc_test = Cerc(5)

cerc_test.descrie()

cerc_test.aria()

cerc_test.raza
cerc_test.raza = 7
cerc_test.raza
del cerc_test.raza
cerc_test.raza







