from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

# ConcreteObserver
class TextObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(self.name + ": " + state)

# Subject
class TextSubject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, state):
        for observer in self.observers:
            observer.update(state)

# ConcreteSubject
class TextEdit(TextSubject):
    def __init__(self):
        super().__init__()
        self.text = ""

    # SetState(State)
    def set_text(self, text):
        self.text = text
        self.notify(text)

    def get_text(self):
        return self.text

# Client
observer1 = TextObserver("Observer 1")
observer2 = TextObserver("Observer 2")

textEdit = TextEdit()
textEdit.attach(observer1)
textEdit.attach(observer2)

textEdit.set_text("text text")


# Output:
# Observer #1: test text
# Observer #2: test text
