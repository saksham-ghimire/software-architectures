# TOPIC : Program to an Interface, not an Implementation
import abc

class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_work():
        pass

class Company:
    def __init__(self) -> None:
        pass
    
    def createSoftware(self, e:list[Employee]) -> None:
        for i in e:
            i.do_work()


class Designer(Employee):
    def __init__(self) -> None:
        pass
    
    def do_work(self) -> None:
        print("Designer is designing an applications.")
    
class Programmer(Employee):
    def __init__(self) -> None:
        pass

    def do_work(self) -> None:
        print("Programmer is writing an applications.")


class Tester(Employee):
    def __init__(self) -> None:
        pass

    def do_work(self) -> None:
        print("Tester is testing application for bugs.")
    




c = Company()
c.createSoftware([Designer(),Programmer(),Tester()])