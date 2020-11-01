import random as rnd
from math import *

class DRange(object):
    """
    Класс описывает непрерывный интервал вещественных чисел [a;b], используемый как ген в хромосоме,
    а так же инструменты для кроссовера, мутации, интерполяции значений в интервале
    """
    diap = 0.4
    def __init__(self, a, b, name='drange'):
        """
        a    левая (или правая) граница интервала гена
        b    правая(или левая)  граница интервала гена
        name имя гена
        """
        self.a = min(a, b)
        self.b = max(a, b)
        self.name = name

        
    def get_rnd_value(self):
        """
        функция генерации случайного значения в интервале
        """
        return rnd.uniform(self.a, self.b)
        
        
    def __repr__(self):
        return f"DRange({self.a}, {self.b}, name='{self.name}')"


    def validate_value(self, value):
        if value > self.b:
            return self.b
        elif value < self.a:
            return self.a
        return value


    def cross(self, x1, x2):
        """
        Кроссовер двух генов (с использованием нормального распределения)
        
        x1     значение гена первого родителя
        x2     значение гена второго родителя
        
        return значение гена потомка
        """
        return rnd.uniform(x1, x2)

    def mutate(self, mu):
        """
        Мутация гена (с использованием нормального распределения)
        
        mu     значение гена до мутации
        
        return значение гена после мутации
        """
        x1 = mu - (self.b - self.a)*self.diap*0.5
        x2 = mu + (self.b - self.a)*self.diap*0.5
        x1 = self.validate_value(x1)
        x2 = self.validate_value(x2)
        return rnd.uniform(x1, x2)

class ChromoController(object):
    """
    Класс описывает хромосому постоянной структуры
    а так же инструменты для кроссовера, мутации, интерполяции хромосом
    """

    def __init__(self, ranges):
        """
        ranges      список описаний генов (гены должны иметь разные имена!!!)
        constraints список функций для определения пригодности хромосомы, функции вида
                    f(chr) -> float, где chr - хромосома (создается функциями get_chromo, cross, mutate, interp, 
                    find_zero_golden_method). Если возврацаемое значение >= 0, то хромосома приемлимая
        """
        self.ranges_dict = {r.name: r for r in ranges}
        self.ranges_list = [r for r in ranges]

    def __repr__(self):
        return f"ChromoController({repr(self.ranges_list)},constraints = {repr(self.constraints)})"

    def __getitem__(self, key):
        if key in self.ranges_dict:
            return self.ranges_dict[key]
        return self.ranges_list[key]

    def get_chromo(self):
        """
        метод получения новой хромосомы со случайными значениями генов
        """
        ch = {}
        for k in self.ranges_dict:
            ch[k] = self[k].get_rnd_value()
#         ch = {key: self[key].get_rnd_value() for key in self.ranges_dict}
        return ch

    def cross(self, chromo1, chromo2):
        """
        метод проведения кроссовера двух хромосом
        
        chromo1, chromo2  хромосомы родителей
        
        return            хромосома-потомок
        """
        child = {}
        for k in self.ranges_dict:
            child[k] = self[k].cross(chromo1[k], chromo2[k])
#         child = {key: self[key].cross(chromo1[key], chromo2[key]) for key in self}
        return child

    def mutate(self, chromo, keys):
        """
        метод проведения мутации хромосомы 
        
        chromo  хромосома-родитель
        keys    имена мутирующих генов
        
        return  хромосома-мутант
        """
        mutant = dict(chromo)
        mutant.pop('fitness', None)
        for key in keys:
            mutant[key] = self[key].mutate(mutant[key])
        return mutant