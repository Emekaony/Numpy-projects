class Human:
    def __init__(self, name, age, coordinates):
        self.name = name
        self.age = age
        self.coordinates = coordinates

    def __str__(self):
        return str(self.coordinates)

    def sayHello(self):
        print(f"Hello there, {self.name}")

    def move(self, direction):
        self.coordinates["x_coord"] += direction["x"]
        self.coordinates["y_coord"] += direction["y"]
        return self.coordinates


Emeka = Human("Nnaemeka", 20, {"x_coord": 33, "y_coord": -99})
print(Emeka)

direction = {
    "x": 44,
    "y": 32
}
