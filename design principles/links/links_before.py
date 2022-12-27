# TOPIC : Program to an Interface, not an Implementation
class Company:
    def __init__(self) -> None:
        pass
    
    def createSoftware(self) -> None:
        d = Designer()
        d.designArchitecture()
        p = Programmer()
        p.writeCode()
        t = Tester()
        t.testSoftware()


class Designer():
    def __init__(self) -> None:
        pass
    
    def designArchitecture(self) -> None:
        print("Designer is designing an applications.")
    
class Programmer():
    def __init__(self) -> None:
        pass

    def writeCode(self) -> None:
        print("Programmer is writing an applications.")


class Tester():
    def __init__(self) -> None:
        pass

    def testSoftware(self) -> None:
        print("Tester is testing application for bugs.")
    



c = Company()
c.createSoftware()