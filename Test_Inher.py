class Animal:
    def __init__(self):
        self.colors = 2
        self.bool = True

    def breath(self):
        print("inhales/exhales")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Underwater")

    def swim(self):
        print("can swim")


nemo = Fish()
nemo.breath()
nemo.swim()
print(nemo.colors)
