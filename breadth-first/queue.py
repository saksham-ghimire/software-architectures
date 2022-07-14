# simple queue implementation
class Queue:
    def __init__(self) -> None:
        self.Elements = []
    def insertToQueue(self,value) -> None:
        self.Elements.extend(value)
    def popLeft(self) -> any:
        return self.Elements.pop(0) 
    def getAllElements(self) -> list:
        return self.Elements