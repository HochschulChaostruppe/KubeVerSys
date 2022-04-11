import sys
import os

class Grade(object):

    def __init__(self, name: str, ects: int, grade: float):
        self.name = name
        self.ects = ects
        self.grade = grade
        self.__weighted = None

    def __repr__(self) -> str:
        return self.__name__

    def __str__(self) -> str:
        return f'{self.name}: {self.ects} | {self.grade}'

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def ects(self) -> int:
        return self.__ects

    @ects.setter
    def ects(self, ects) -> None:
        if ects < 1:
            raise ValueError('ECTS cannot be zero or negative!')
        self.__weighted = None
        self.__ects = ects
        
    @property
    def grade(self) -> float:
        return self.__grade

    @grade.setter
    def grade(self, grade) -> None:
        if grade < 1.0 or grade > 5.0:
            raise ValueError('Grade must be between 1.0 and 5.0!')
        self.__weighted = None
        self.__grade = grade

    @property
    def weighted(self) -> float:
        if self.__weighted is None:
            self.__weighted = self.__ects * self.__grade
        return self.__weighted

def mean(grades: list[Grade]) -> float:
    weighted_sum = sum([x.weighted for x in grades])
    ects_sum = sum([x.ects for x in grades])
    return weighted_sum / ects_sum

def main():
    grades = [
        Grade('Einführung in die Informatik / Digitaltechnik', 7, 2.4),
        Grade('Einführung in die Programmierung', 4, 4.0),
        Grade('Lineare Algebra', 5, 1.4),
        Grade('Physik', 3, 1.3),
        Grade('Projektarbeit I', 5, 2.2),
        Grade('Algorithmen & Datenstrukturen / Automaten & Sprachen', 5, 2.9),
        Grade('Analysis', 5, 1.0),
        Grade('Betriebssysteme', 3, 2.2),
        Grade('Elektrotechnik', 6, 2.5),
        Grade('Objektorientierte Programmierung', 5, 1.0),
        Grade('Projektarbeit II', 5, 1.8), 
        Grade('Betriebssystemverwaltung', 3, 1.5),
        Grade('Elektronik', 5, 3.2),
        Grade('Projektarbeit III', 5, 1.7),
        Grade('Rechnernetze', 4, 3.8),
        Grade('Statistik / Optimierung', 5, 1.2),
        Grade('Datenbanken', 9, 2.2),
        Grade('Englisch', 3, 1.1),
        Grade('Praxisprüfung I', 5, 3.4),
        Grade('Signale & Systeme', 5, 1.2),
        Grade('Spezielle Themen I', 4, 1.7),
        Grade('Systementwicklung', 7, 3.3),
        Grade('Spezielle Themen II', 4, 2.7),
        Grade('Systemprogrammierung', 2, 1.7),
        Grade('Technische Informatik', 6, 1.7)
        ]
    print(mean(grades))

if __name__ == '__main__':
    main()