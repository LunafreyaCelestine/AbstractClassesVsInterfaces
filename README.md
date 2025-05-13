# AbstractClassesVsInterfaces


## A quick and dirty example of abstract classes and interfaces in python

### Key Points

### Abstract Classes
- Abstract classes typically follow the naming convention of "AbstractPerson" or "AbstractSomeClass"
- Cannot be instantiated
- Can have concrete attributes and methods
- Use the @abstractmethod decorator to annotate abstract methods
- Can be subclassed
- Can have constructors in python, but not good practice
- Define an abstract blueprint for other, child classes that doesn't get directly isntantiated
- Reference python's ABC module in the python docs for more info

### Interfaces
- Interfaces typically follow the naming convetion of "CameraI" or "CameraInterface"
- If a class uses an interface, it is called "Class X implements the Y interface"
- Python uses ABC for defining interfaces which leads to confusion between the two
- You can declare abstract methods that are then defined in the implementing class
- Do not define concrete methods in an interface, python allows it but many languages don't
- Interface describe behavior




