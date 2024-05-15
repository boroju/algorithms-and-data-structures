from abc import ABC, abstractmethod


# Class: A blueprint for creating objects that defines attributes and methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Object: An instance of a class.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Attribute: A variable associated with a class or object.
print(person1.name)  # Output: Alice


# Inheritance: A mechanism where a new class inherits properties and behaviors from an existing class.
class Student(Person):
    def __init__(self, name, age, student_id, university):
        super().__init__(name, age)
        self.student_id = student_id
        self.university = university

    # Redefining get_name method for Student
    def get_name(self):
        return self.name


# Encapsulation: The bundling of data (attributes) and methods that operate on the data (methods)
# into a single unit (class), and controlling access to the data through methods.
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


# Polymorphism: The ability of objects of different classes to be treated as objects of a common superclass.
def display_info(person):
    # Using directly the name attribute
    print("Name:", person.name)
    print("Age:", person.age)


student = Student("Charlie", 20, "S12345", "XYZ University")
display_info(student)


# Abstraction: Hiding the complex implementation details and showing only the essential features of an object.

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Car is being driven")


# Overloading: Defining multiple methods with the same name but different parameters or types.

# In Python, method overloading (having multiple methods with the same name but different parameters)
# is not directly supported like in some other languages such as Java or C++.
# However, you can achieve similar functionality by using default parameter values.
# Here's how you can define and use the MathOperations class with "overloaded" add methods:

class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


# Instantiate MathOperations
math_ops = MathOperations()

# Use the overloaded add method
result1 = math_ops.add(2, 3)
result2 = math_ops.add(2, 3, 4)

print("Result 1:", result1)  # Output: 5
print("Result 2:", result2)  # Output: 9


# Constructor and Destructor: Special methods in Python. Constructor is used to initialize an object,
# and Destructor is used to perform cleanup activities before an object is destroyed.

class MyClass:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")
