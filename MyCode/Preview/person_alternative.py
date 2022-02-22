"""
Альтернативная реализация классов Person и Manager с данными, методами
и с перегрузкой операторов (не используется в объектах, предусматривающих
возможность сохранения)
"""
class Person:
    """
    универсальное представление человека: данные + логика
    """
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, persent):
        self.pay *= (1.0 + persent)
    def __str__(self):
        return ('<%s => %s, %s, %s>' % (self.__class__.__name__, self.name, self.job, self.pay))

class Manager(Person):
    """
    класс со специализированным методом giveRaise,
    наследующий обобщенные методы lastName и __str__
    """
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, persent, bonus=0.1):
        Person.giveRaise(self, persent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 44)
    sue = Person('Sue Jons', 47, 40000, 'hardware')
    tom = Manager(name = 'Tom Doe', age = 50, pay = 50000)
    print(sue, sue.pay, sue.lastName())
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
