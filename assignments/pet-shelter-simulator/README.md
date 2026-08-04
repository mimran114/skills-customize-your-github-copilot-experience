# 📘 Assignment: Pet Shelter Simulator

## 🎯 Objective

Practice object-oriented design by building a pet shelter simulator with classes, inheritance, and interactions between animals and caretakers.

## 📝 Tasks

### 🛠️ Define the Animal Class Hierarchy

#### Description
Create a base `Animal` class and subclasses for different animal types such as `Dog` and `Cat`.

#### Requirements
Completed program should:

- Define an `Animal` class with attributes for `name`, `age`, and `species`.
- Add a method `speak()` to return a sound specific to the animal.
- Create at least two subclasses that override `speak()`.
- Instantiate each subclass and demonstrate the method output.

### 🛠️ Build the Shelter Manager

#### Description
Create a `Shelter` class that stores animals and manages admissions and adoptions.

#### Requirements
Completed program should:

- Define a `Shelter` class with a list of animals.
- Add methods to `admit_animal(animal)` and `adopt_animal(name)`.
- Return a message when an animal is admitted or adopted.
- Remove adopted animals from the shelter list.

### 🛠️ Add Caretaker Interaction and Reporting

#### Description
Implement a `Caretaker` class that can care for animals and report shelter status.

#### Requirements
Completed program should:

- Define a `Caretaker` class with a name and assigned shelter.
- Add a method `care_for(animal)` that returns a care action message.
- Add a method `list_animals()` on the shelter to show current resident names.
- Demonstrate admitting animals, caring for them, and processing an adoption.
