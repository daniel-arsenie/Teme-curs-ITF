from abc import abstractmethod, ABC


# De raspuns la intrebarile:
# 1. Ce inseamna if __name__ == "__main__" scris intr - un fisier python?
# Raspuns: pastreaza o bucata de cod pentru a fi rulat
# doar atunci cand programul este rulat ca script

# 2. Cum instalam un pachet extern python?
# Raspuns:mergem in bara de jos in Pycharm la Python Packages,
# cautam packetul care ne itereseaza(ex: Selenium)
# si click pe Install Package de langa Version


# 3. Ce este dataclass in python?
# Raspuns: "dataclass" este un modul care poate fi importat
# pentru a genera "metode speciale"(__init__() si __repr__())
# intr-o clasa definita de noi.


# 4. Ce este functia hash?
# Raspuns: "hash" este o functie in Python care returneaza valoarea unui obiect.
# hash are ca valoare de baza un integer.
# Obiectele schimbate folosind hash() nu ma pot reveni la valoarea de dinainte de hash().
# int_val = 4      -> hash(int_val) va fi tot 4
# flt_val = 24.56  -> hash(flt_val) va fi 1291272085159665688


# 5. Cum pot face codul de mai jos sa functioneze corect?

# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def __eq__(self, other):
#         return isinstance(other, Person) and self.age == other.age and self.name == other.name
#
#
# s = set()
# p = Person(29, "Adrian")
# s.add(p)

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    # __eq__ folosim doar daca vrem sa comparam 2 obiecte
    # def __eq__(self, other):
    #     return isinstance(other, Person) and self.age == other.age and self.name == other.name

    def __str__(self):  # str- creem un string atunci cand creem un obiect si dam print la obiect
        return f'Person: {self.name}, Age: {self.age}'

    def __repr__(self):  # folosit pentru printarea colectiilor de obiecte, liste
        # ca sa facem lista din obiectele noastre
        return str(self)


p = Person(29, "Adrian")
# p2 = Person(18, 'Stefan')

s = set()
s.add(p)
# s.add(p2)

print(s)


# 2. Rezolv?? exerci??iul dup?? ce ai urcat proiectul (tot ce am facut p??n?? acum
# ??mpreun??).
# ABSTRACTION
# Clasa abstract?? FormaGeometrica
# Con??ine un field PI=3.14
# Con??ine o metod?? abstract?? aria (op??ional)
# Con??ine o metod?? a clasei descrie() - aceasta printeaz?? pe ecran ???Cel mai
# probabil am colturi???

class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi.')


# INHERITANCE
# Clasa P??trat - mo??tene??te FormaGeometrica
# constructor pentru latur??

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        print('Setting as property:')
        return self.__latura

    @latura.getter
    def latura(self):
        print('Getting value:')
        return self.__latura

    @latura.setter
    def latura(self, noua_latura):
        print('Settin new value to "latura":')
        self.__latura = noua_latura

    @latura.deleter
    def latura(self):
        print('Deleting value')
        self.__latura = None

    def aria(self):
        return f'Aria patratului este: {self.__latura ** 2}'


# ENCAPSULATION
# latura este proprietate privat??
# Implementeaz?? getter, setter, deleter pentru latur??
# Implementeaz?? metoda cerut?? de interfa???? (op??ional, doar dac?? ai ales s??
# implementezi metoda abstract?? aria)

# Clasa Cerc - mo??tene??te FormaGeometrica
# constructor pentru raz??
# raza este proprietate privat??
# Implementeaz?? getter, setter, deleter pentru raz??
# Implementeaz?? metoda cerut?? de interfa???? - ??n calcul folose??te field PI
# mostenit din clasa p??rinte (op??ional, doar dac?? ai ales s?? implementezi metoda
# abstract?? aria)

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        print('Setting as property:')
        return self.__raza

    @raza.getter
    def raza(self):
        print('Getting value:')
        return self.__raza

    @raza.setter
    def raza(self, noua_raza):
        print('Settin new value to "raza":')
        self.__raza = noua_raza

    @raza.deleter
    def raza(self):
        print('Deleting value')
        self.__raza = None

    def aria(self):
        print(f'Aria este: {self.pi * (self.__raza ** 2)}')

    def descrie(self):
        print('Eu nu am colturi.')


# POLYMORPHISM
# Define??te o nou?? metod?? descrie - printeaz?? ???Eu nu am colturi???
# Creeaz?? un obiect de tip P??trat ??i joac??-te cu metodele lui
# Creeaz?? un obiect de tip Cerc ??i joac??-te cu metodele lui
# 3. Actualizeaz?? proiectul pe github facand un push la noul cod
# ??n Folderul de teme ajunge s?? pui doar linkul cu proiectul t??u public
# Curs git/github
# https://bit.ly/3yfFvqL - VIDEO 4

p1 = Patrat(25)
p2 = Patrat(10)

print(p1.latura)
print(p2.latura)

p1.latura = 16
print(p1.latura)
p2.latura = 8
print(p2.latura)

# del p1.latura
# print(p1.latura)
# del p2.latura
# print(p1.latura)

print(p1.aria())
print(p2.aria())

p1.descrie()
p2.descrie()

print(50 * "#")

########################################

c1 = Cerc(10)
c2 = Cerc(15)

print(c1.raza)
print(c2.raza)

c1.raza = 12
print(c1.raza)
c2.raza = 21
print(c2.raza)

# del c1.raza
# print(c1.raza)
# del c2.raza
# print(c2.raza)

c1.aria()
c2.aria()

c1.descrie()
c2.descrie()
