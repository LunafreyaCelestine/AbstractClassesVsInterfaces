from abc import ABC, abstractmethod


class Person(ABC):


    """ 
    If you have concrete methods, functions, or class attributes add a constructor
    A constructor is not necessarily needed if there are no concrete members defined
    and the parent class is ABC 
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this is and example of an abstract method
    @abstractmethod
    def say_hello(self):
        """Abstract method to greet."""
        pass

    @abstractmethod
    def get_details(self):
        """Abstract method to return details about the person."""
        pass

    # This is an example of a concrete method    
    def celebrate_birthday(self):
        """Concrete method that subclasses inherit."""
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

# The following would raise a TypeError because you cannot directly instantiate an abstract class:
# person = Person("Generic Person", 30)

class Employee(Person):
    
    # because we defined a constructor in Person, we need to call super()__init__()
    def __init__(self, name, age, job_title):
        super().__init__(name, age) # relevant arguments are passed to parent constructor, often time **kwargs is used here
        self.job_title = job_title

    def say_hello(self):
        return f"Hi, I'm {self.name}!"

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Title: {self.title}"



