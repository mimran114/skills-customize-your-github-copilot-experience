from typing import List

class Animal:
    def __init__(self, name: str, age: int, species: str):
        self.name = name
        self.age = age
        self.species = species

    def speak(self) -> str:
        return "..."

    def __repr__(self) -> str:
        return f"{self.species}({self.name}, {self.age})"


class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Dog")

    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Cat")

    def speak(self) -> str:
        return "Meow!"


class Shelter:
    def __init__(self):
        self.animals: List[Animal] = []

    def admit_animal(self, animal: Animal) -> str:
        self.animals.append(animal)
        return f"Admitted {animal.name} the {animal.species}."

    def adopt_animal(self, name: str) -> str:
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                return f"{name} has been adopted!"
        return f"No animal named {name} found."

    def list_animals(self) -> List[str]:
        return [animal.name for animal in self.animals]


class Caretaker:
    def __init__(self, name: str, shelter: Shelter):
        self.name = name
        self.shelter = shelter

    def care_for(self, animal: Animal) -> str:
        return f"{self.name} is caring for {animal.name}."


if __name__ == "__main__":
    shelter = Shelter()
    rover = Dog("Rover", 4)
    whiskers = Cat("Whiskers", 2)

    print(shelter.admit_animal(rover))
    print(shelter.admit_animal(whiskers))

    caretaker = Caretaker("Jordan", shelter)
    print(caretaker.care_for(rover))

    print("Current animals:", shelter.list_animals())
    print(shelter.adopt_animal("Rover"))
    print("Current animals:", shelter.list_animals())
