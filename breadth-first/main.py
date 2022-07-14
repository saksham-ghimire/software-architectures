from queue import Queue

def main():
    # Initialize a queue
    q = Queue()
    # hold name of already searched personnel
    searched = []

    # The dataset to search on 
    graph = {}
    graph["you"] = ["bob", "alice" , "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    # The person to find
    name = "thom"

    q.insertToQueue(graph["you"])
    while q.getAllElements():
        person = q.popLeft()
        if person not in searched:
            if person == name:
                print(f"{person} found.")
                return
            else:
                q.insertToQueue(graph[person])
                searched.append(person)
    
    print(f"Person {name} not found")

if __name__ == "__main__":
    main()