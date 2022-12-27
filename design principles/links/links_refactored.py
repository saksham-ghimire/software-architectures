# TOPIC : Program to an Interface, not an Implementation
import abc

class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_work():
        pass

class Company(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def get_employee() -> list[Employee]:
        pass
    
    def createSoftware(self) -> None:
        employees = self.get_employee()
        for i in employees:
            i.do_work()


class GameDevCompany(Company):
    def get_employee(self) -> list[Employee]:
        return [Designer(),Programmer(),Tester()]

class OutSourcingCompany(Company):
    def get_employee(self) -> list[Employee]:
        return [Programmer(),Designer(),Tester()]


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
    




c = OutSourcingCompany()
c.createSoftware()
GameDevCompany()